from django.conf.urls import url

from . import views


app_name = 'courses'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^courses/add/$', views.add, name='add'),
    url(r'^courses/edit/(?P<course_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^courses/remove/(?P<course_id>[0-9]+)/$', views.remove, name='remove'),
    url(r'^courses/(?P<course_id>[0-9]+)/add_lesson$', views.add_lesson, name='add_lesson'),
]