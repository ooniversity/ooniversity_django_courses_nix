from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentModelForm
from courses.models import Course
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id')
        course_name = ''
        page_title = 'Список студентов'
        if course_id:
            course = Course.objects.get(pk=course_id)
            course_name = course.name
            page_title = 'Студенты курса ' + course_name
        context['course_name'] = course_name
        context['page_title'] = page_title

        return context

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students = Student.objects.filter(courses__id__contains=course_id)
        else:
            students = Student.objects.all()

        return students


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    template_name = 'students/add.html'
    model = Student
    success_url = reverse_lazy('students:list')
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        messages.success(
            self.request,
            'Student {} {} has been successfully added.'.format(name, surname)
        )

        return response


class StudentUpdateView(UpdateView):
    template_name = 'students/edit.html'
    model = Student
    success_url = reverse_lazy('students:list')
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Info on the student has been successfully changed.'
        )

        return response


class StudentDeleteView(DeleteView):
    template_name = 'students/remove.html'
    model = Student
    success_url = reverse_lazy('students:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        name = self.object.name
        surname = self.object.surname
        messages.success(
            self.request,
            'Student {} {} has been successfully deleted.'.format(name, surname)
        )

        return response


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

