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

    def get_queryset(self):
        queryset = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            queryset = Student.objects.filter(courses__id=course_id)
        return queryset


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Student {} {} has been successfully added.'.format(self.object.name, self.object.surname)
        )

        return response


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
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
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request,
            'Student {} {} has been successfully deleted.'.format(self.object.name, self.object.surname)
        )

        return response

