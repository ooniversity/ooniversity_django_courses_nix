from django.shortcuts import render

from .models import Course


def detail(request, course_id):
    course = Course.objects.get(id=course_id)

    return render(request, 'course_detail.html', {'course': course})