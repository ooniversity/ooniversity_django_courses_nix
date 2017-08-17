"""Quadrantic URLs"""

from django.conf.urls import url
from . import views

# app_name = 'quadratic'
urlpatterns = [
    url(r'^results', views.ResultsView.as_view(), name='results'),
]
