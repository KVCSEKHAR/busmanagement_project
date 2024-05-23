from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import BusForm

from . models import Buses

def bus_list(request):
    buses = Buses.objects.all()
    return render(request, 'buses/bus_list.html', {'buses': buses})

def bus_details(request, bus_no):
    bus = get_object_or_404(Buses, bus_no=bus_no)
    return render(request, 'bus_details.html', {'bus': bus})

def bus_create(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'buses/bus_form.html', {'form': form})

def bus_update(request, pk):
    bus = get_object_or_404(Buses, pk=pk)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm(instance=bus)
    return render(request, 'buses/bus_form.html', {'form': form})

def bus_delete(request, pk):
    bus = get_object_or_404(Buses, pk=pk)
    if request.method == 'POST':
        bus.delete()
        return redirect('bus_list')
    return render(request, 'buses/bus_confirm_delete.html', {'bus': bus})