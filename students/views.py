from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentModelForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)

        if course_id:
            qs = qs.filter(courses__id=course_id)

        return qs


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm
    #fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        full_name = self.object.name + ' ' + self.object.surname
        messages.success(self.request, 'Student ' + full_name +  ' has been successfully added.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'

        return context


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm
    #fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'

        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm
    #fields = '__all__'

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        full_name = self.object.name + ' ' + self.object.surname
        messages.success(self.request, 'Info on ' + full_name + ' has been successfully deleted.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'

        return context