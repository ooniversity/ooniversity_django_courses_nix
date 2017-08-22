from django.shortcuts import render
from courses.models import Course, Lesson, Student


def index(request):
    courses = Course.objects.all()
    return render(request, 'pybursa/index.html', {'course_list': courses})


def contact(request):
    return render(request, 'pybursa/contact.html')


def student_list(request):
    return render(request, 'pybursa/student_list.html')


def student_detail(request):
    return render(request, 'pybursa/student_detail.html')

