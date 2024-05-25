from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Driver
from .forms import DriverForm


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})


def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})

@login_required
def driver_create(request):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/drivers')  # Redirect to a relevant page
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'drivers/driver_form.html', {'form': form})

@login_required
def driver_update(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/drivers')  # Redirect to a relevant page
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_detail', pk=pk)
    else:
        form = DriverForm(instance=driver)
    return render(request, 'drivers/driver_form.html', {'form': form})

@login_required
def driver_delete(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/drivers')  # Redirect to a relevant page
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    return render(request, 'drivers/driver_confirm_delete.html', {'driver': driver})
