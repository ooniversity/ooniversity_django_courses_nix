from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.utils import datastructures
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student
from .forms import StudentModelForm

class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        if 'course_id' in self.request.GET:
            queryset = self.model._default_manager.filter(courses = self.request.GET['course_id'])
        else:
            queryset = self.model._default_manager.all()

        return queryset


# def list_view(request):
#     students = None
#     try:
#         coourse_id = request.GET['course_id']
#         students = Student.objects.filter(courses = coourse_id)
#     except datastructures.MultiValueDictKeyError:
#         students = Student.objects.all()
#
#     return render(request, 'students/list.html', {'students' : students})

class StudentDetailView(DetailView):
    model = Student

# def detail(request, pk):
#     try:
#         student = Student.objects.get(id = pk)
#     except Student.DoesNotExist:
#         return HttpResponseNotFound()
#
#     return render(request, 'students/detail.html', {'student' : student})

class StudentCreateView(CreateView):
    model = Student
    fields = model.get_all_model_field_names(model)
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        self.object = form.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Student {!s} has been successfully added.'.format(self.object.full_name()))
        return response

# def add(request):
#     if request.method == 'POST':
#         form = StudentModelForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             messages.success(request, 'Student {!s} has been successfully added.'.format(instance.full_name()))
#             return redirect('students:list_view')
#     else:
#         form = StudentModelForm()
#
#     return render(request, 'students/add.html', {'form': form})

class StudentUpdateView(UpdateView):
    model = Student
    fields = model.get_all_model_field_names(model)
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

# def edit(request, pk):
#     student = Student.objects.get(id=pk)
#     if request.method == "POST":
#         form = StudentModelForm(request.POST, instance=student)
#         if form.is_valid():
#             student = form.save()
#             messages.success(request, 'Info on the student has been successfully changed.')
#             return redirect('students:edit', pk=student.id)
#     else:
#         form = StudentModelForm(instance=student)
#     return render(request, 'students/edit.html', {'form': form})

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on {!s} has been successfully deleted.'.format(self.object.full_name()))
        return response

# def remove(request, pk):
#     student = Student.objects.get(id=pk)
#     if request.method == "POST":
#         student_full_name = student.full_name()
#         student.delete()
#         messages.success(request, 'Info on {!s} has been successfully deleted.'.format(student_full_name))
#         return redirect('students:list_view')
#     return render(request, 'students/remove.html', {'student': student})