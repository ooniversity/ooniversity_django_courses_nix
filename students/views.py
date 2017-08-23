from django.shortcuts import render
from students.models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'student_list': students})


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})
