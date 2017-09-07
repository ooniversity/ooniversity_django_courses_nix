
from django.conf.urls import url
from . import views


app_name = 'students'
urlpatterns = [
    url(r'^$', views.StudentListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/edit/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/remove/$', views.StudentDeleteView.as_view(), name='remove'),
]
