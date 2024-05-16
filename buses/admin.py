from django.contrib import admin
from .models import Buses
from drivers.models import Driver
from students.models import Student
from routes.models import Route
# Register your models here.
admin.site.register(Buses)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Student)



