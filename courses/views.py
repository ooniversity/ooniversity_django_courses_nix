from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
from .forms import CourseModelForm

def detail(request, pk):
    course = None
    
    try:
        course = Course.objects.get(id = pk)
    except:
        pass
    
    return render(request, 'courses/detail.html', {'course' : course})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course {!s} has been successfully added.'.format(course.name))
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk=course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course_name = course.name
        course.delete()
        messages.success(request, 'Course {!s} has been deleted.'.format(course_name))
        return redirect('/')
    return render(request, 'courses/remove.html', {'course': course})