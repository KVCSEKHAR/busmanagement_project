from django import forms
from .models import Buses

class BusForm(forms.ModelForm):
    class Meta:
        model = Buses
        fields = [
            'bus_no', 'bus_reg_no', 'bus_route', 'bus_driver_name', 
            'bus_driver_contact', 'bus_incharge_name', 'bus_incharge_contact', 
            'bus_model', 'bus_sitting_capacity'
        ]
        widgets = {
            'bus_no': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_reg_no': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_route': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_driver_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_incharge_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_incharge_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_model': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_sitting_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
