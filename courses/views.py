from django.shortcuts import render
from courses.models import Course, Lesson, Student


def courses(request, pk):
    course = Course.objects.get(id=pk)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lesson_list': lessons})
