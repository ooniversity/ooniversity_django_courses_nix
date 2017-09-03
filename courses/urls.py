from django.conf.urls import url

from . import views


app_name = 'courses'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^courses/add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^courses/edit/(?P<pk>[0-9]+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^courses/remove/(?P<pk>[0-9]+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^courses/(?P<course_id>[0-9]+)/add_lesson$', views.add_lesson, name='add_lesson'),
]