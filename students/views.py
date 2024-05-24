# students/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required

def student_create(request):
    if not request.user.profile.user_type in ['staff', 'admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/students')  # Redirect to a relevant page
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    if not request.user.profile.user_type in ['staff', 'admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/students')  # Redirect to a relevant page
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    if not request.user.profile.user_type in ['staff', 'admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('/students')  # Redirect to a relevant page
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
