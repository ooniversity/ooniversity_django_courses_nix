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

#def detail(request, student_id):
#    student_obj = get_object_or_404(Student, pk=student_id)
#
#    return render(request, 'students/detail.html',
#                  {'student_obj': student_obj})


class StudentsListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)

        if course_id:
            qs = qs.filter(courses__id=course_id)

        return qs

#def list_view(request):
#    #student_list = Student.objects.all()

#    if 'course_id' in request.GET:
#        student_list = Student.objects.filter(courses__id=request.GET['course_id'])
#    else:
#        student_list = Student.objects.all()

    #print(student_list[0].courses.all())
#    return render(request, 'students/list.html',
#                  {'student_list': student_list})

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        full_name = self.object.name + ' ' + self.object.surname
        messages.success(self.request, 'Student ' + full_name +  ' has been successfully added.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'

        return context

#def add(request):
#
#    if request.method == 'POST':
#        form = StudentModelForm(request.POST)
#        if form.is_valid():
#            instance = form.save()
#            fullname = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
#            messages.success(request, 'Student ' + fullname + ' has been successfully added.')
#            return redirect('/students/')
#    else:
#        form = StudentModelForm()
#    return render(request, 'students/add.html',
#                  {'form': form})

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'

        return context


#def edit(request, student_id):
#    student = Student.objects.get(id = student_id)
#
#    if request.method == 'POST':
#        form = StudentModelForm(request.POST, instance=student)
#        if form.is_valid():
#            student = form.save()
#            messages.success(request, 'Info on the student has been successfully changed.')
#            return redirect('/students/')
#    else:
#        form = StudentModelForm(instance=student)
#    return render(request, 'students/edit.html',
#                  {'form': form})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    fields = '__all__'

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        full_name = self.object.name + ' ' + self.object.surname
        messages.success(self.request, 'Info on ' + full_name + ' has been successfully deleted.')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'

        return context


#def remove(request, student_id):
#    student = Student.objects.get(id = student_id)
#    full_name = student.name + ' ' + student.surname
#
#    if request.method == 'POST':
#        student.delete()
#        messages.success(request, 'Info on ' + full_name + ' has been successfully deleted.')
#        return redirect('/students/')
#
#    return render(request, 'students/remove.html',
#                  {'full_name': full_name})