from django.shortcuts import render, redirect, get_object_or_404
from forms.forms import *
from forms.models import *
from django.contrib.auth.models import User, Group


# Create your views here.
def member_faculty_list(request):
    return render(request, ('faculty_list/member_faculty_list.html'))


def admin_faculty_list(request, user_id=None):
    current_user = request.user
    current_user_groups = current_user.groups.all()
    matching_users = User.objects.filter(groups__in=current_user_groups).exclude(id=current_user.id)
    
    selected_user = None
    
    if user_id is not None:
        selected_user = get_object_or_404(User, id=user_id)
        
    return render(request, 'faculty_list/admin_faculty_list.html', {'matching_users': matching_users, 'selected_user': selected_user})

def IPCR_Remarks_Create(request, user_id):
    selected_user = get_object_or_404(User, id=user_id)
    data = IPCR_Form_model_submitted.objects.filter(author=user_id).first()

    existing_instance = IPCR_Remarks.objects.filter(author=user_id).first()

    if request.method == 'POST':
        forms = IPCR_Remarks_Form(request.POST, instance=existing_instance)
        
        # Set the author field value in the form before checking its validity
        forms.instance.author = selected_user
        
        if forms.is_valid():
            model_instance = forms.save(commit=False)
            model_instance.save()
        else:
            print(forms.errors)  # Print form validation errors to the console
    else:
        forms = IPCR_Remarks_Form(instance=existing_instance)

    return render(request, 'faculty_list/IPCR_Remarks.html', {'selected_user': selected_user, 'data': data, 'forms': forms})