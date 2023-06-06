from django import forms
from .models import IPCR_Form_model, IPCR_Remarks

class IPCR_Form(forms.ModelForm):
    class Meta:
        model = IPCR_Form_model
        fields = '__all__'

class IPCR_Remarks_Form(forms.ModelForm):
    class Meta:
        model = IPCR_Remarks
        fields = '__all__'
        exclude = ['author', 'reviewer', 'IPCR_Submitted']