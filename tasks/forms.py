from django import forms
from django.forms import ModelForm

from .models import *  


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'complete': forms.Textarea(attrs={'class': 'form-control'}),
        # }