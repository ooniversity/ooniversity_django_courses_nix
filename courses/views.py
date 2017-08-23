from django.shortcuts import render
from courses.models import Course, Lesson


def courses(request, pk):
    course = Course.objects.get(id=pk)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lesson_list': lessons})


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'course_list': courses})
