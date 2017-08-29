from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from .forms import StudentModelForm

from .models import Student


def list_view(request):
    try:
        students = Student.objects.filter(courses=request.GET['course_id'])
    except:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student ' + student.name + ' ' + student.surname + ' has been successfully added.')
            return redirect('students:list_view')
    else:
        form = StudentModelForm
    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def delete(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on ' + student.name + ' ' + student.surname + ' has been successfully deleted.')
        return redirect('students:list_view')
    return render(request, 'students/delete.html', {'student': student})

def detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'students/detail.html', {'student': student})