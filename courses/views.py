# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Course
from .forms import CourseModelForm, LessonModelForm

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
            messages.success(request, 'Course ' + course.name + ' has been successfully added.')
            return redirect('index')
    else:
        form = CourseModelForm
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
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
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course ' + course.name + ' has been deleted.')
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonModelForm(request.POST, initial={'course': course.id})
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson ' + lesson.subject + ' has been successfully added.')
            return redirect('courses:detail', pk=course.id)
    else:
        form = LessonModelForm(initial={'course': course.id})
    return render(request, 'add_lesson.html', {'form': form})
