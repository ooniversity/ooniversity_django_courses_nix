from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.utils import datastructures

from .models import Student


def list_view(request):
    try:
        students = Student.objects.filter(courses=request.GET['course_id'])
    except:
        students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'student_detail.html', {'student': student})