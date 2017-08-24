from django.shortcuts import render
from students.models import Student


def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses=request.GET['course_id'])
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'list_view': students})


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})
