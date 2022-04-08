from .models import Info
from django import forms

class InfoForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = Info
        fields = ('__all__')