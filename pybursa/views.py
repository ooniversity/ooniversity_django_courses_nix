from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course

def index(request):
    course_list = Course.objects.all()
    return render(request, 'templates/index.html', {'courses': course_list})
def contact(request):
    return render(request, 'templates/contact.html')

def student_list(request):
    return render(request, 'templates/student_list.html')

def student_detail(request):
    return render(request, 'templates/student_detail.html')
