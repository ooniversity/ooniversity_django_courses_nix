# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student

class StudentListView(ListView):
    model = Student
    paginate_by = 2

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
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student ' + self.object.name + ' ' + self.object.surname + ' has been successfully added.')
        return response

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Info on ' + self.object.name + ' ' + self.object.surname + ' has been successfully deleted.')
        return  response
