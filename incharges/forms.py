# incharges/forms.py

from django import forms
from .models import Incharge

class InchargeForm(forms.ModelForm):
    class Meta:
        model = Incharge
        fields = ['name', 'contact', 'email', 'assigned_bus']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'assigned_bus': forms.Select(attrs={'class': 'form-control'}),
        }
