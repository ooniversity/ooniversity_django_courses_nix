from django.conf.urls import url
from students.views import students, student

app_name = 'students'
urlpatterns = [
    url(r'^$', students, name='students'),
    url(r'^(?P<student_id>[0-9]+)/$', student, name='student'),
]
