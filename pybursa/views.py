from django.shortcuts import render
from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'pybursa/index.html', {'course_list': courses})


def contact(request):
    return render(request, 'pybursa/contact.html')
