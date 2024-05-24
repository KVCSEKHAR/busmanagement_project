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
            'bus_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bus Number'}),
            'bus_reg_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bus Registration Number'}),
            'bus_route': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Route Information'}),
            'bus_driver_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Driver Name'}),
            'bus_driver_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Driver Mobile Number'}),
            'bus_incharge_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter In-charge Name'}),
            'bus_incharge_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter In-charge Mobile Number'}),
            'bus_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bus Model Name'}),
            'bus_sitting_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bus Sitting Capacity Number'}),
        }
