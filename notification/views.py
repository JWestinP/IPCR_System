from django.shortcuts import render

# Create your views here.

def member_notification (request):
    return render(request, ('notification/member_notification.html'))

def admin_notification (request):
    return render(request, ('notification/admin_notification.html'))