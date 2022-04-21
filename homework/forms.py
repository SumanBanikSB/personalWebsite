from .models import Homework
from django import forms

class homeworkForms(forms.ModelForm):
    class Meta:
        model = Homework
        fields  = ['student','topic','images']