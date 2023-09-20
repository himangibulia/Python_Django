from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import cv

# for resume
class cv_form(forms.ModelForm):
    class Meta:
        model=cv
        fields=('__all__')
        exclude=('user',)
        
         