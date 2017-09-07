from django.shortcuts import get_object_or_404, render
from . import models


def detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    context = {
        'course': course,
        'lessons': course.lesson_set.all()
    }

    return render(request, 'courses/detail.html', context)