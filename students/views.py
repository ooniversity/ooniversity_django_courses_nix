from django.shortcuts import render
from django.http import HttpResponseNotFound
from students.models import Student


def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses=request.GET['course_id'])
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'list_view': students})


def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'students/detail.html', {'student': student})
