from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def member_home(request):
    current_user = request.user
    context = {
        'current_user' : current_user
    }
    return render(request, ('home/member_home.html'), context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Admin_Dean', 'Admin_Director'])
def admin_home(request):
    current_user = request.user
    context = {
        'current_user' : current_user
    }
    return render(request, ('home/admin_home.html'), context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Superadmin'])
def superadmin_home(request):
    current_user = request.user
    context = {
        'current_user' : current_user
    }
    return render(request, ('home/superadmin_home.html'), context)