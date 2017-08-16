"""Polls Views"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic


def index(request):
    """Polls Vote"""
    return render(request, 'pybursa/index.html')

def contact(request):
    """Contact Page"""
    return render(request, 'pybursa/contact.html')

def student_list(request):
    """Student List Page"""
    return render(request, 'pybursa/student_list.html')

def student_detail(request, pk):
    """Student Detail Page"""
    return render(request, 'pybursa/student_detail.html')
