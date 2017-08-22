from django.conf.urls import url

from . import views


app_name = 'courses'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
]