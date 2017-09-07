from django.shortcuts import get_object_or_404, render
from . import models


def list_view(request, course_id = None):
    students = models.Students.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/list.html',context)


def detail(request, pk):
    student = get_object_or_404(models.Students, id=pk)
    context = {
        'student': student
    }

    return  render(request, 'students/detail.html', context)

