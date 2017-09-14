from django.shortcuts import get_object_or_404, get_list_or_404, render
from students.models import Students


# Create your views here.
def students(request):
    if 'course_id' in request.GET:
        students = get_list_or_404(Students, courses=request.GET['course_id'])
    else:
        students = get_list_or_404(Students)
    return render(request, 'students/list_view.html', {'students': students})


def student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    return render(request, 'students/detail.html', {'student': student})
