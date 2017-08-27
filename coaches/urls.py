from django.conf.urls import url
from coaches import views as coaches_views


app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', coaches_views.detail, name='detail'),
]
