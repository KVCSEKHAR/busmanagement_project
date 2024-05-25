# routes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Route
from .forms import RouteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def route_list(request):
    routes = Route.objects.all()
    return render(request, 'routes/route_list.html', {'routes': routes})

def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'routes/route_detail.html', {'route': route})

@login_required
def route_create(request):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/incharges')  # Redirect to a relevant page
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm()
    return render(request, 'routes/route_form.html', {'form': form})

@login_required
def route_update(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/incharges')  # Redirect to a relevant page
    route = get_object_or_404(Route, pk=pk)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'routes/route_form.html', {'form': form})

@login_required
def route_delete(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/incharges')  # Redirect to a relevant page
    route = get_object_or_404(Route, pk=pk)
    if request.method == 'POST':
        route.delete()
        return redirect('route_list')
    return render(request, 'routes/route_confirm_delete.html', {'route': route})

