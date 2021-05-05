
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import *
from django import forms
class Taskform(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'

 