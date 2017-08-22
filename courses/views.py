from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course, Lesson


# Create your views here.
def list_view(request):
    courses_list = Course.objects.all()

    return render(request, 'courses/list.html',
                  {'courses_list': courses_list})


def detail(request, course_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    lessons_list = Lesson.objects.filter(course = course_obj)

    return render(request, 'courses/detail.html',
                  {'lessons_list': lessons_list,
                   'course_obj': course_obj})
