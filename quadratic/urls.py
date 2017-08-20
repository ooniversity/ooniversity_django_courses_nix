from django.conf.urls import url
from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^results/$',
        views.quadratic_results, name='results')
]
