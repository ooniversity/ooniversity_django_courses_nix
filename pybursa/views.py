from django.shortcuts import render
from courses.models import Course


def index(request):
    course_list = Course.objects.all()
    context = {'courses': course_list}
    return render(request, 'pybursa/index.html', context)


def contact(request):
    return render(request, 'pybursa/contact.html')
