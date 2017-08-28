from django.shortcuts import render
from django.views import generic
from .models import Student


class StudentsIndexView(generic.ListView):
    template_name = 'students/list_view.html'
    context_object_name = 'students'
    model = Student

    def get_queryset(self, **kwargs):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            return Student.objects.filter(courses=course_id)
        return Student.objects.all()


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'
