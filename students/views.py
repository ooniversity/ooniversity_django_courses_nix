from django.shortcuts import render, get_object_or_404
from .models import Student


# Create your views here.
def detail(request, student_id):
    student_obj = get_object_or_404(Student, pk=student_id)

    return render(request, 'students/detail.html',
                  {'student_obj': student_obj})


def list_view(request):
    #student_list = Student.objects.all()

    if 'course_id' in request.GET:
        student_list = Student.objects.filter(courses__id=request.GET['course_id'])
    else:
        student_list = Student.objects.all()

    #print(student_list[0].courses.all())
    return render(request, 'students/list.html',
                  {'student_list': student_list})