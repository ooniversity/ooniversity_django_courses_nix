from django.conf.urls import url
from courses import views as courses_views


app_name = 'courses'
urlpatterns = [
    url(r'^courses/(?P<pk>[0-9]+)/', courses_views.courses, name='courses'),
]
