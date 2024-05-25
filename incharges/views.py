# incharges/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Incharge
from .forms import InchargeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def incharge_list(request):
    incharges = Incharge.objects.all()
    return render(request, 'incharges/incharge_list.html', {'incharges': incharges})

def incharge_details(request, pk):
    incharge = get_object_or_404(Incharge, pk=pk)
    return render(request, 'incharges/incharge_details.html', {'incharge': incharge})

@login_required
def incharge_create(request):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/incharges')  # Redirect to a relevant page
    if request.method == 'POST':
        form = InchargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incharge_list')
    else:
        form = InchargeForm()
    return render(request, 'incharges/incharge_form.html', {'form': form})

@login_required
def incharge_update(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/incharges')  # Redirect to a relevant page
    incharge = get_object_or_404(Incharge, pk=pk)
    if request.method == 'POST':
        form = InchargeForm(request.POST, instance=incharge)
        if form.is_valid():
            form.save()
            return redirect('incharge_list')
    else:
        form = InchargeForm(instance=incharge)
    return render(request, 'incharges/incharge_form.html', {'form': form})

@login_required
def incharge_delete(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/drivers')  # Redirect to a relevant page
    incharge = get_object_or_404(Incharge, pk=pk)
    if request.method == 'POST':
        incharge.delete()
        return redirect('incharge_list')
    return render(request, 'incharges/incharge_confirm_delete.html', {'incharge': incharge})
