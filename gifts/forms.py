from django import forms
from .models import Birthday

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['age', 'creator', 'img', 'description']
