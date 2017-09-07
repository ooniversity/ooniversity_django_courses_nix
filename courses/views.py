from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course
from .forms import CourseModelForm, LessonModelForm

class CourseDetailView(DetailView):
    model = Course
    #context_object_name = 'course'
    template_name = 'courses/detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'

        return context

    def form_valid(self, form):
        self.object = form.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Course {!s} has been successfully added.'.format(self.object.name))

        return response


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')

        return response


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Course {!s} has been deleted.'.format(self.object.name))

        return response


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson {!s} has been successfully added.'.format(lesson.subject))
            return redirect('courses:detail', pk=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})