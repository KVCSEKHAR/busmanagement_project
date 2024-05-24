# routes/forms.py
from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_name', 'start_location', 'end_location', 'route_number', 'active']
        widgets = {
            'route_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter route name'}),
            'start_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter start location'}),
            'end_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter end location'}),
            'route_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter route number'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }