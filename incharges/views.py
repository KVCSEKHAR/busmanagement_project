# incharges/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Incharge
from .forms import InchargeForm

def incharge_list(request):
    incharges = Incharge.objects.all()
    return render(request, 'incharges/incharge_list.html', {'incharges': incharges})

def incharge_details(request, pk):
    incharge = get_object_or_404(Incharge, pk=pk)
    return render(request, 'incharges/incharge_details.html', {'incharge': incharge})

def incharge_create(request):
    if request.method == 'POST':
        form = InchargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incharge_list')
    else:
        form = InchargeForm()
    return render(request, 'incharges/incharge_form.html', {'form': form})

def incharge_update(request, pk):
    incharge = get_object_or_404(Incharge, pk=pk)
    if request.method == 'POST':
        form = InchargeForm(request.POST, instance=incharge)
        if form.is_valid():
            form.save()
            return redirect('incharge_list')
    else:
        form = InchargeForm(instance=incharge)
    return render(request, 'incharges/incharge_form.html', {'form': form})

def incharge_delete(request, pk):
    incharge = get_object_or_404(Incharge, pk=pk)
    if request.method == 'POST':
        incharge.delete()
        return redirect('incharge_list')
    return render(request, 'incharges/incharge_confirm_delete.html', {'incharge': incharge})
