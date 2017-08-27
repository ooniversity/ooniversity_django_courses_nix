from django.shortcuts import render, get_object_or_404
from .models import Student
from courses.models import Course


def list_view(request):
    course_id = request.GET.get('course_id')
    course_name = ''
    if course_id:
        course = Course.objects.get(pk=course_id)
        course_name = course.name
        students = Student.objects.filter(courses__id__contains=course_id)
    else:
        students = Student.objects.all()
    context = {
        'course_name': course_name,
        'students': students
    }

    return render(request, 'students/list.html', context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}

    return render(request, 'students/detail.html', context)
