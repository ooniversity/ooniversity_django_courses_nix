from django.shortcuts import render
from courses.models import Course
from django.http import HttpResponse
from django.template import loader


def index(request):
    course_list = Course.objects.all()
    context = {'courses': course_list}
    return render(request, 'pybursa/index.html', context)


def contact(request):
    return render(request, 'pybursa/contact.html')


def student_list(request):
    return render(request, 'pybursa/student_list.html')


def student_detail(request):
    return render(request, 'pybursa/student_detail.html')
