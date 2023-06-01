from django import forms
from .models import user_post

class user_post_forms(forms.ModelForm):
    class Meta:
        model = user_post
        fields = '__all__'
        exclude = ['author', 'date_posted', 'department']