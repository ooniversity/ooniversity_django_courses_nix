from django.conf.urls import url
from students import views as students_views


app_name = 'students'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', students_views.student_detail, name='student_detail'),
    url(r'^$', students_views.student_list, name='student_list')
]
