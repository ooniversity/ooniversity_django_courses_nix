from django.conf.urls import url
from students.views import StudentDetailView, StudentsIndexView

app_name = 'students'
urlpatterns = [
    url(r'^$', StudentsIndexView.as_view(), name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', StudentDetailView.as_view(), name='detail'),
]
