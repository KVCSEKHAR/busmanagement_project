from django.contrib import admin
from buses.models import Buses
from drivers.models import  Driver 
from incharges.models import Incharge 
from students.models import Student 
from routes.models import Route
from staff.models import Staff

admin.site.register(Buses)
admin.site.register(Driver)
admin.site.register(Incharge)
admin.site.register(Route)
admin.site.register(Staff)
admin.site.register(Student)




