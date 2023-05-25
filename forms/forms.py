from django import forms
from .models import IPCR_Form_model

class IPCR_Form(forms.ModelForm):
    class Meta:
        model = IPCR_Form_model
        fields = '__all__'
