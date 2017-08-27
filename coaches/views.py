from django.shortcuts import render
from django.http import HttpResponseNotFound
from coaches.models import Coach


def detail(request, coach_id):
    try:
        coach = Coach.objects.get(id=coach_id)
        coach_courses = coach.coach_courses.all()
        coach_assistant = coach.assistant_courses.all()
    except Coach.DoesNotExist:
        return HttpResponseNotFound()

    context = {
        'coach': coach,
        'coach_courses': coach_courses,
        'coach_assistant': coach_assistant,
    }
    return render(request, 'coach_detail.html', context)