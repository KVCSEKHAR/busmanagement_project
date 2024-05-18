from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from . models import Buses

def bus_list(request):
    buses = Buses.objects.all()
    return render(request, 'buses.html', {'buses': buses})



def bus_details(request, bus_no):
    bus = get_object_or_404(Buses, bus_no=bus_no)
    return render(request, 'bus_details.html', {'bus': bus})
    