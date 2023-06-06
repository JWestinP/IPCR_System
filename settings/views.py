from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def settings(request):
    user = request.user

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        # Update more user information fields as needed
        user.save()
        messages.success(request, 'Your information has been updated successfully.')

    context = {'user': user}
    return render(request, 'settings/settings.html', context)