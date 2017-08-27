from django.shortcuts import render, get_object_or_404
from .models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    c_courses = Course.objects.filter(coach__id=coach_id)
    a_courses = Course.objects.filter(assistant__id=coach_id)
    # c_courses = list(i.name for i in coach_courses)
    # a_courses = list(i.name for i in assistant_courses)
    context = {'coach': coach, 'c_courses': c_courses, 'a_courses': a_courses}

    return render(request, 'coaches/detail.html', context)
