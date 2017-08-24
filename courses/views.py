# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Course

def detail(request, pk):
    course = None
    
    try:
        course = Course.objects.get(id = pk)
    except:
        pass
    
    return render(request, 'courses/detail.html', {'course' : course})
