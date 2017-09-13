from django.shortcuts import get_object_or_404, get_list_or_404, render
from students.models import Students


# Create your views here.
def students(request):
    students = get_list_or_404(Students)
    return render(request, 'students/list_view.html', {'students': students})


def student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    return render(request, 'students/detail.html', {'student': student})
