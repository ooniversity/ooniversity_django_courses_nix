
from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='polls_index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='polls_detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='polls_results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='polls_vote'),
]
