from django.shortcuts import get_list_or_404, render
from courses.models import Course, Lesson

# Create your views here.
def course_item(request, course_id):
    course = get_list_or_404(Lesson.objects.order_by('order'), course_id=course_id)
    return  render(request, 'courses/detail.html', {'course': course})