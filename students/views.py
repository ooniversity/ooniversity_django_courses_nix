from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.utils import datastructures

from .models import Student

def list_view(request):
    students = None
    try:
        coourse_id = request.GET['course_id']
        students = Student.objects.filter(courses = coourse_id)
        print(coourse_id)
    except datastructures.MultiValueDictKeyError:
        students = Student.objects.all()
    
    return render(request, 'students/list.html', {'students' : students})

def detail(request, pk):
    try:
        student = Student.objects.get(id = pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound()
    
    print(pk)
    return render(request, 'students/detail.html', {'student' : student})
