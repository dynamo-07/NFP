from django import forms
from .models import *

class contact(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class feed(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'

class food(forms.ModelForm):
    class Meta:
        model = foodbook
        fields = '__all__'