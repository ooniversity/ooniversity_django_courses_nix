from django.shortcuts import render

from courses.models import Course

def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'students/student_list.html')

def student_detail(request):
    return render(request, 'students/detail.html')