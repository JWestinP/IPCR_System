from django.shortcuts import render, get_object_or_404
from forms.forms import *
from forms.models import *
from django.contrib.auth.models import User, Group
from home.decorators import allowed_users
from django.db.models import Q
from django.contrib.auth import get_user_model
from datetime import date, datetime
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def member_faculty_list(request, user_id=None):
    current_user = request.user
    current_user_groups = current_user.groups.all()
    matching_users = User.objects.filter(groups__in=current_user_groups).exclude(id=current_user.id)
    
    selected_user = None
    
    query = request.GET.get('q')

    if user_id is not None:
        selected_user = get_object_or_404(User, id=user_id)
    
    if query:
        matching_users = matching_users.filter(
            Q(username__icontains=query) |  # Search by username (case-insensitive)
            Q(first_name__icontains=query) |  # Search by first name (case-insensitive)
            Q(last_name__icontains=query)  # Search by last name (case-insensitive)
        )
    
    return render(request, 'faculty_list/member_faculty_list.html', {'matching_users': matching_users, 'selected_user': selected_user})

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Admin_Dean', 'Admin_Director'])
def admin_faculty_list(request, user_id=None):
    current_user = request.user
    current_user_groups = current_user.groups.all()
    matching_users = User.objects.filter(groups__in=current_user_groups).exclude(id=current_user.id)
    
    selected_user = None
    
    query = request.GET.get('q')
    
    if user_id is not None:
        selected_user = get_object_or_404(User, id=user_id)
        
    if query:
        matching_users = matching_users.filter(
            Q(username__icontains=query) |  # Search by username (case-insensitive)
            Q(first_name__icontains=query) |  # Search by first name (case-insensitive)
            Q(last_name__icontains=query)  # Search by last name (case-insensitive)
        )
        
    user_group_names = current_user.groups.values_list('name', flat=True)

    return render(request, 'faculty_list/admin_faculty_list.html', {'matching_users': matching_users, 'selected_user': selected_user, 'current_user' : current_user, 'user_group_names': user_group_names})

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Superadmin'])
def superadmin_faculty_list(request,  group_id=None, user_id=None):
    groups = Group.objects.filter(name__icontains='faculty')
    selected_group = None
    users = None
    selected_user = None
    query = request.GET.get('q')

    if 'group_id' in request.GET:
        group_id = request.GET['group_id']
        if group_id:
            selected_group = get_object_or_404(Group, id=group_id)
            users = User.objects.filter(groups=selected_group)
        else:
            selected_group = None
            users = User.objects.all()

        if query:
            users = users.filter(
                Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
            
    elif user_id is not None:
        selected_user = get_object_or_404(User, id=user_id)


    return render(request, 'faculty_list/superadmin_faculty_list.html', {
        'groups': groups,
        'selected_group': selected_group,
        'users': users,
        'selected_user': selected_user,
        'query': query,
    })

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Admin_Dean'])
def IPCR_Remarks_Create(request, user_id):
    selected_user = get_object_or_404(User, id=user_id)
    data = IPCR_Form_model_submitted.objects.filter(author=user_id).first()

    existing_instance = IPCR_Remarks.objects.filter(author=user_id).first()

    if request.method == 'POST':
        forms = IPCR_Remarks_Form(request.POST, instance=existing_instance)
        
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        forms.instance.reviewer = f"{first_name} {last_name}"
        forms.instance.author = selected_user
        forms.instance.IPCR_Submitted = datetime.now().date()

        
        if forms.is_valid():
            model_instance = forms.save(commit=False)
            model_instance.save()

    else:
        forms = IPCR_Remarks_Form(instance=existing_instance)

    return render(request, 'faculty_list/IPCR_Remarks.html', {'selected_user': selected_user, 'data': data, 'forms': forms})

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Superadmin'])
def IPCR_Approval(request, user_id):
    selected_user = get_object_or_404(User, id=user_id)
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=user_id)
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author = user_id)
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=user_id)
    except IPCR_Rating.DoesNotExist:
        data3 = None
        
    if request.method == 'POST':
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        
        data.approver = f"{first_name} {last_name}"
        data.save()

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3,
        'selected_user': selected_user
    }

    return render(request, 'faculty_list/IPCR_Approve.html', context)
