from django.shortcuts import render
from courses.models import Course, Lesson, Student


def index(request):
    courses = Course.objects.all()
    return render(request, 'pybursa/index.html', {'course_list': courses})


def contact(request):
    return render(request, 'pybursa/contact.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'student_list': students})


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})
