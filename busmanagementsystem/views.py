from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from buses.models import Buses
from students.models import Student
from accounts.models import Profile




@login_required
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'index.html', {'user_type': user_profile.user_type})
    

def buses(request):
    bus = Buses.objects.all() 
    return render(request,"buses.html", {'bus' : bus})

def drivers(request):
    bus = Buses.objects.all() 
    return render(request,"drivers.html", {'bus' : bus})


def routes(request):
    bus = Buses.objects.all() 
    return render(request,"routes.html", {'bus' : bus})

def incharges(request):
    return render(request,"incharges.html")

def staff(request):
    return render(request,"staff.html")

def students(request):
    student = Student.objects.all()
    bus = Student.objects.all()
    return render(request,"students.html",{'student': student})




@login_required
def addbus(request):
    if request.method=='POST':
        bus_no = request.POST['bus_no']
        bus_reg_no = request.POST['bus_reg_no']
        bus_route = request.POST['bus_route']
        bus_driver_name = request.POST['bus_driver_name']
        bus_driver_contact = request.POST['bus_driver_contact']
        bus_incharge_name = request.POST['bus_incharge_name']
        bus_incharge_contact = request.POST['bus_incharge_contact']
        bus_model = request.POST['bus_model']
        bus_sitting_capacity = request.POST['bus_sitting_capacity']
        
        b=Buses(bus_no=bus_no,bus_reg_no=bus_reg_no,bus_route=bus_route,bus_driver_name=bus_driver_name,bus_driver_contact=bus_driver_contact,bus_incharge_name=bus_incharge_name,bus_incharge_contact=bus_incharge_contact,bus_model=bus_model,bus_sitting_capacity=bus_sitting_capacity)
        b.save()
    return render(request,"addbus.html")
