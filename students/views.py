from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.utils import datastructures
from django.contrib import messages

from .models import Student
from .forms import StudentModelForm

def list_view(request):
    students = None
    try:
        coourse_id = request.GET['course_id']
        students = Student.objects.filter(courses = coourse_id)
    except datastructures.MultiValueDictKeyError:
        students = Student.objects.all()
    
    return render(request, 'students/list.html', {'students' : students})

def detail(request, pk):
    try:
        student = Student.objects.get(id = pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound()
    
    return render(request, 'students/detail.html', {'student' : student})

def add(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Student {!s} has been successfully added.'.format(instance.full_name()))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {'form': form})

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:edit', pk=student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student_full_name = student.full_name()
        student.delete()
        messages.success(request, 'Info on {!s} has been successfully deleted.'.format(student_full_name))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})