from django.shortcuts import render

from .models import Course


def detail(request, course_id):
    course = Course.objects.get(id=course_id)

    return render(request, 'courses/detail.html', {'course': course})