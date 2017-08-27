from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson


def index(request):
    context = {'courses': Course.objects.all()}

    return render(request, 'index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course__id__contains=course_id)
    context = {'course': course, 'lessons': lessons}

    return render(request, 'courses/detail.html', context)

