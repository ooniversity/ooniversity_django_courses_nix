from django.conf.urls import url

from coaches.views import CoachDetailView

app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', CoachDetailView.as_view(), name='detail'),
]
