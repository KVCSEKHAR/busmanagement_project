# incharges/forms.py

from django import forms
from .models import Incharge

class InchargeForm(forms.ModelForm):
    class Meta:
        model = Incharge
        fields = ['name', 'contact', 'email', 'assigned_bus']
