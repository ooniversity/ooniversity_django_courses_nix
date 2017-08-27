# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseNotFound
from coaches.models import Coach

def detail(request, pk):
    try:
        coach = Coach.objects.get(id=pk)
        coach_courses = coach.coach_courses.all()
        assis_courses = coach.assistant_courses.all()
    except Coach.DoesNotExist:
        return HttpResponseNotFound()
    
    context = {
        'coach': coach,
        'coach_courses': coach_courses,
        'assis_courses': assis_courses,
    }
    return render(request, 'coaches/detail.html', context)
