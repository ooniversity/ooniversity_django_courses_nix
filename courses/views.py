from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lesson
from django.contrib import messages
from .forms import CourseModelForm, LessonModelForm


# Create your views here.
def list_view(request):
    courses_list = Course.objects.all()

    return render(request, 'index.html',
                  {'courses_list': courses_list})


def detail(request, course_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    lessons_list = Lesson.objects.filter(course = course_obj)
    #print(course_obj.coach.description)
    return render(request, 'courses/detail.html',
                  {'lessons_list': lessons_list,
                   'course_obj': course_obj})


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Course ' + instance.name + ' has been successfully added.')
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html',
                  {'form': form})


def edit(request, course_id):
    course = Course.objects.get(id = course_id)

    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('/courses/edit/'+course_id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html',
                  {'form': form})


def remove(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course ' + course.name + ' has been deleted.')
        return redirect('/')

    return render(request, 'courses/remove.html',
                  {'course': course})


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Lesson ' + instance.subject + ' has been successfully added.')
            return redirect('/courses/' + course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html',
                  {'form': form})