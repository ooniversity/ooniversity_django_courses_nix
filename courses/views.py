from django.shortcuts import render, redirect, get_object_or_404,reverse
from .models import Course, Lesson
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def list_view(request):
    courses_list = Course.objects.all()

    return render(request, 'index.html',
                  {'courses_list': courses_list})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lessons_list = Lesson.objects.filter(course=self.object)
        context['lessons_list'] = lessons_list

        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('courses:list_view')
    form_class = CourseModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course ' + self.object.name + ' has been successfully added.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'

        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'

    def get_success_url(self):
        return reverse('courses:edit', args=(self.object.id,))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('courses:list_view')
    context_object_name = 'course_obj'

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Course ' + self.object.name + ' has been deleted.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Lesson ' + instance.subject + ' has been successfully added.')
            return redirect('courses:detail', course_id=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'add_lesson.html',
                  {'form': form})