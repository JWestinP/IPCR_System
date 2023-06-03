from django.shortcuts import render
from .forms import user_post_forms
from .models import user_post
from datetime import date, datetime
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.decorators import allowed_users

# Create your views here.
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def member_notification(request):
    current_user = request.user
    user_groups = current_user.groups.values_list('name', flat=True)
    specific_group = 'Superadmin'
    recent_notifications = user_post.objects.filter(
        Q(author__groups__name__in=user_groups) | Q(author=current_user) | Q(author__groups__name=specific_group)
    ).order_by('-date_posted').distinct()[:5]

    current_date = datetime.now().date()
    firstmidterm_deadline = datetime.strptime("2023-10-30", "%Y-%m-%d").date()
    firstfinalterm_deadline = datetime.strptime("2024-02-03", "%Y-%m-%d").date()
    secondmidterm_deadline = datetime.strptime("2024-04-10", "%Y-%m-%d").date()
    secondfinalterm_deadline = datetime.strptime("2023-06-16", "%Y-%m-%d").date()

    if current_date <= secondfinalterm_deadline:
        deadline_date = datetime.strptime("2023-06-16", "%Y-%m-%d").date()

    elif current_date <= firstmidterm_deadline:
        deadline_date = datetime.strptime("2023-10-30", "%Y-%m-%d").date()

    elif current_date <= firstfinalterm_deadline:
        deadline_date = datetime.strptime("2024-02-03", "%Y-%m-%d").date()

    elif current_date <= secondmidterm_deadline:
        deadline_date = datetime.strptime("2024-04-10", "%Y-%m-%d").date()

    days_until_deadline = (deadline_date - current_date).days

    return render(request, 'notification/member_notification.html', {'recent_notifications': recent_notifications, 'deadline_date': deadline_date, 'current_date': current_date, 'days_until_deadline': days_until_deadline})

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Admin_Dean', 'Admin_Director', 'Superadmin'])
def admin_superadmin_notification(request): 
    recent_notifications = user_post.objects.order_by('-date_posted')[:10]
    
    current_date = datetime.now().date()
    firstmidterm_deadline = datetime.strptime("2023-10-30", "%Y-%m-%d").date()
    firstfinalterm_deadline = datetime.strptime("2024-02-03", "%Y-%m-%d").date()
    secondmidterm_deadline = datetime.strptime("2024-04-10", "%Y-%m-%d").date()
    secondfinalterm_deadline = datetime.strptime("2023-06-16", "%Y-%m-%d").date()
    
    if current_date <= secondfinalterm_deadline:
        deadline_date = datetime.strptime("2023-06-16", "%Y-%m-%d").date()
        
    elif current_date <= firstmidterm_deadline:
        deadline_date = datetime.strptime("2023-10-30", "%Y-%m-%d").date()
        
    elif current_date <= firstfinalterm_deadline:
        deadline_date = datetime.strptime("2024-02-03", "%Y-%m-%d").date()
        
    elif current_date <= secondmidterm_deadline:
        deadline_date = datetime.strptime("2024-04-10", "%Y-%m-%d").date()
        
    days_until_deadline = (deadline_date - current_date).days
    
    return render(request, 'notification/admin_superadmin_notification.html', {'recent_notifications': recent_notifications, 'deadline_date' : deadline_date, 'current_date' : current_date,
                                                                               'days_until_deadline': days_until_deadline})


def create_notification(request):
    forms = user_post_forms()
    
    if request.method == 'POST':
        current_user = request.user
        forms = user_post_forms(request.POST)
        group_names = [group.name for group in current_user.groups.all()]
        forms.instance.department = ', '.join(group_names)
        forms.instance.author = current_user
        forms.instance.date_posted = datetime.now().date()
        if forms.is_valid():
            model_instance = forms.save(commit=False)
            model_instance.save()
            messages.success(request, "Your new post has been created.")
            # Redirect to a success page or perform any other desired action
    
    return render(request, 'notification/create_post.html', {'forms': forms})
