from django.shortcuts import render
from django.http import HttpResponseNotFound
from courses.models import Course
from coaches.models import Coach


def detail(request, pk):
    try:
        coach = Coach.objects.get(id=pk)
    except Coach.DoesNotExist:
        return HttpResponseNotFound()

    courses_coach = Course.objects.filter(coach=coach)
    courses_assistant = Course.objects.filter(assistant=coach)
    return render(request, 'coaches/detail.html', {
        'coach': coach,
        'courses_coach': courses_coach,
        'courses_assistant': courses_assistant
    })
