from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'pythonthrone/index.html'
    context_object_name = 'index_page'

class ContactView(TemplateView):
    template_name = 'pythonthrone/contact.html'
    context_object_name = 'contact_page'

class StudentListView(TemplateView):
    template_name = 'pythonthrone/student_list.html'
    context_object_name = 'student_list_page'

class StudentDetailView(TemplateView):
    template_name = 'pythonthrone/student_detail.html'
    context_object_name = 'student_detail'
