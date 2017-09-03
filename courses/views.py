from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def index(request):
    context = {'courses': Course.objects.all()}

    return render(request, 'index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course__id__contains=course_id)
    context = {'course': course, 'lessons': lessons}

    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        course = form.save()
        messages.success(request, 'Course ' + course.name + ' has been successfully added.')
        return redirect('/')
    else:
        form = CourseModelForm()

    context = {'form': form}

    return render(request, 'courses/add.html', context)


def edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        form.save()
        messages.success(request, 'The changes have been saved.')

        return redirect('courses:edit', course_id=course.id)

    form = CourseModelForm(instance=course)
    context = {'form': form}

    return render(request, 'courses/edit.html', context)


def remove(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course ' + course.name + ' has been deleted.')

        return redirect('/')

    context = {'course': course}

    return render(request, 'courses/remove.html', context)


def add_lesson(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        lesson = form.save()
        messages.success(request, 'Lesson ' + lesson.subject + ' has been successfully added.')
        return redirect('courses:detail', course_id=course.id)
    else:
        form = LessonModelForm(initial={'course': course})

    context = {'form': form}

    return render(request, 'courses/add_lesson.html', context)

