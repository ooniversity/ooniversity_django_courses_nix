import math
from django.shortcuts import render
from .forms import QuadraticForm


def quadratic_results(request):
    context = {}
    if request.method == 'POST':
        form = QuadraticForm(request.POST)
        if form.is_valid():
            context['result'] = solve_quadratic(form.cleaned_data)
    else:
        form = QuadraticForm()

    context['form'] = form
    return render(request, 'quadratic/results.html', context)


def solve_quadratic(data):
    discriminant = data['b'] ** 2 - 4 * data['a'] * data['c']
    result = {'D': discriminant}

    if discriminant >= 0:
        result['x1'] = round((-data['b'] + math.sqrt(discriminant)) / (2 * data['a']), 2)
        result['x2'] = round((-data['b'] - math.sqrt(discriminant)) / (2 * data['a']), 2)

    return result
