from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentModelForm
from courses.models import Course
from django.contrib import messages


def list_view(request):
    course_id = request.GET.get('course_id')
    course_name = ''
    if course_id:
        course = Course.objects.get(pk=course_id)
        course_name = course.name
        students = Student.objects.filter(courses__id__contains=course_id)
    else:
        students = Student.objects.all()
    context = {
        'course_name': course_name,
        'students': students
    }

    return render(request, 'students/list.html', context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}

    return render(request, 'students/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        student = form.save()
        messages.success(request, 'Student ' + student.get_full_name() + ' has been successfully added.')
        return redirect('/students/')
    else:
        form = StudentModelForm()

    context = {'form': form}

    return render(request, 'students/add.html', context)


def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        form.save()
        messages.success(request, 'Info on the student has been successfully changed.')

        return redirect('students:edit', student_id=student.id)

    form = StudentModelForm(instance=student)
    context = {'form': form}

    return render(request, 'students/edit.html', context)


def remove(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on ' + student.get_full_name() + ' has been successfully deleted.')

        return redirect('/students/')

    context = {'student': student}

    return render(request, 'students/remove.html', context)

