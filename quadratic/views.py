# -*- coding: utf-8 -*-
from django.shortcuts import render
import math
from .forms import QuadraticForm


def calc_descr(a, b, c):
    descr = b ** 2 - 4 * a * c
    result = ''

    if descr > 0:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        result = 'Квадратное уравнение имеет два действительных корня: ' \
                            'x1 = {0:.1f}, x2 = {1:.1f}'.format(round(x1, 1), round(x2, 1))
    elif descr == 0:
        x1 = -(b / 2 * a)
        result = 'Дискриминант равен нулю, квадратное уравнение имеет один ' \
                            'действительный корень: x1 = x2 = {0:.1f}'.format(round(x1, 1))
    else:
        result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

    return descr, result

# Create your views here.
def quadratic_results(request):

    a = None
    b = None
    c = None

    context = {}

    if 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)
            context['D_var'], context['D_info'] = calc_descr(form.cleaned_data['a'],
                                                            form.cleaned_data['b'],
                                                            form.cleaned_data['c'])
    else:
        form = QuadraticForm()

    context['form'] = form

    return render(request, 'quadratic/results.html', context)