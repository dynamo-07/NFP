from django import forms
from .models import *

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        exclude = ['user']

class feed(forms.ModelForm):
    class Meta:
        model = feedback
        exclude = ['user']

class food(forms.ModelForm):
    class Meta:
        model = foodbook
        exclude = ['user']