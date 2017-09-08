from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.list_view, name='index'),
    url(r'^course_id/(?P<course_id>\d+)?$', views.list_view, name='course_students'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail')
]
