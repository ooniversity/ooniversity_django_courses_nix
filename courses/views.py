from django.shortcuts import render
from django.views import generic
from .models import Course


class CourseIndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.all()


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'
