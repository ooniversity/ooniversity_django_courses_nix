from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentModelForm


# Create your views here.
def detail(request, student_id):
    student_obj = get_object_or_404(Student, pk=student_id)

    return render(request, 'students/detail.html',
                  {'student_obj': student_obj})


def list_view(request):
    #student_list = Student.objects.all()

    if 'course_id' in request.GET:
        student_list = Student.objects.filter(courses__id=request.GET['course_id'])
    else:
        student_list = Student.objects.all()

    #print(student_list[0].courses.all())
    return render(request, 'students/list.html',
                  {'student_list': student_list})


def add(request):

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            fullname = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
            messages.success(request, 'Student ' + fullname + ' has been successfully added.')
            return redirect('/students/')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html',
                  {'form': form})


def edit(request, student_id):
    student = Student.objects.get(id = student_id)

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('/students/')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html',
                  {'form': form})


def remove(request, student_id):
    student = Student.objects.get(id = student_id)
    full_name = student.name + ' ' + student.surname

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on ' + full_name + ' has been successfully deleted.')
        return redirect('/students/')

    return render(request, 'students/remove.html',
                  {'full_name': full_name})