from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
from django.forms import modelform_factory

# Create your views here.

def IPCR_Form(request):
    IPCR_Form = modelform_factory(IPCR_Form_model, fields="__all__", exclude= ['author'])

    # Check if the user already has a saved instance of MyModel
    try:
        existing_instance = IPCR_Form_model.objects.get(author=request.user)
    except IPCR_Form_model.DoesNotExist:
        existing_instance = None

    if request.method == 'POST':
        forms = IPCR_Form(request.POST, instance=existing_instance)
        if forms.is_valid():
            model_instance = forms.save(commit=False)
            model_instance.author = request.user
            model_instance.save()
            return redirect('IPCR_Form')
    else:
        forms = IPCR_Form(instance=existing_instance)

    context = {
        'forms': forms
    }
    return render(request, 'forms/IPCRForm_Submit.html', context)
