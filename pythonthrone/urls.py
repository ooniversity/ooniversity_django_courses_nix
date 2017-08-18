from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^student_list/$', views.StudentListView.as_view(), name='student_list'),
    url(r'^student_detail/$', views.StudentDetailView.as_view(), name='student_detail'),
]
