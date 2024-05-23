# drivers/forms.py
from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'contact', 'license_number', 'address', 'bus_assigned']
