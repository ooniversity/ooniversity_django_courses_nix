from django.conf.urls import url
from courses import views as courses_views


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', courses_views.courses, name='courses'),
    url(r'^$', courses_views.index, name='index')
]
