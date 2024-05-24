from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from buses.models import Buses
from drivers.models import Driver
from routes.models import Route
from incharges.models import Incharge
from staff.models import Staff
from students.models import Student


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Ensure profile does not already exist
            if not Profile.objects.filter(user=user).exists():
                profile = Profile.objects.create(
                    user=user,
                    user_type=form.cleaned_data['user_type']
                )
                profile.save()
            messages.success(request, 'Successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'Error in form submission.')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            profile = Profile.objects.get(user=user)
            if profile.user_type == 'admin':
                return redirect('admin')
            elif profile.user_type == 'driver':
                return redirect('driver')
            elif profile.user_type == 'incharge':
                return redirect('incharge')
            elif profile.user_type == 'student':
                return redirect('student')
            else:
                messages.error(request, 'User type is not recognized')
                return redirect('login')  # Redirect to appropriate dashboard based on user type
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect('/')

def admin(request):
    buscount = Buses.objects.count()
    drivercount = Driver.objects.count()
    routecount =  Route.objects.count()
    inchargecount = Incharge.objects.count()
    staffcount = Staff.objects.count()
    studentcount = Student.objects.count()
    return render(request, 'adminboard.html',{'buscount': buscount,'drivercount': drivercount, 'routecount': routecount, 'inchargecount': inchargecount, 'staffcount': staffcount, 'studentcount': studentcount})

def driver(request):
    return render(request, 'driverboard.html',{})

def incharge(request):
    return render(request, 'inchargeboard.html')

def student(request):
    return render(request, 'studentboard.html')