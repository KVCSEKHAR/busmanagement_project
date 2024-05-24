# staff/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Staff
from .forms import StaffForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Profile 




def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members})

def staff_detail(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/staff_detail.html', {'staff_member': staff_member})

@login_required
def staff_create(request):
    
    if not request.user.profile.user_type in ['staff', 'admin']:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('/staff')  # Redirect to a relevant page
    
    
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member created successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/staff_form.html', {'form': form})

@login_required
def staff_update(request, pk):
    if not request.user.profile.user_type in ['staff', 'admin']:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('/staff')  # Redirect to a relevant page
    
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff_member)
    return render(request, 'staff/staff_form.html', {'form': form})

@login_required
def staff_delete(request, pk):
    if not request.user.profile.user_type in ['staff', 'admin']:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('/staff')  # Redirect to a relevant page
    
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff_member.delete()
        return redirect('staff_list')
    return render(request, 'staff/staff_confirm_delete.html', {'staff_member': staff_member})
