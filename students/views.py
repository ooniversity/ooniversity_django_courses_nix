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
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        if 'course_id' in self.request.GET:
            context['course_id'] = self.request.GET['course_id']
        
        return context

    def get_queryset(self):
        if 'course_id' in self.request.GET:
            queryset = self.model._default_manager.filter(courses = self.request.GET['course_id'])
        else:
            queryset = self.model._default_manager.all()

        return queryset


class StudentDetailView(DetailView):
    model = Student


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
