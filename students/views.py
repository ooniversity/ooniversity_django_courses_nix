from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student

import logging
logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    ordering = ['-id']

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = Student.objects.filter(courses__id=course_id)
        return qs

#some comment edited
class StudentDetailView(DetailView):
    model = Student

    logger.debug('Students detail view has been debugged!')
    logger.warning('Logger of students detail view warns you!')
    logger.info('Logger of students detail view informs you!')
    logger.error('Students detail view went wrong!')


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
