from django.conf.urls import url
from courses.views import CourseDetailView

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', CourseDetailView.as_view(), name='detail'),
]
