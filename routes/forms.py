# routes/forms.py
from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_name', 'start_location', 'end_location', 'route_number', 'active']
