from django.shortcuts import render,get_object_or_404

from . models import Student
# Create your views here.


def student_details(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    return render(request, 'student_details.html', {'student': student})
    
