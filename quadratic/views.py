# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import QuadraticForm

def quadratic_results(request):
    discriminant = result = False
    form = QuadraticForm()
    if 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        form = QuadraticForm(request.GET)

    if form.is_valid():
        data = form.cleaned_data
        discriminant = data['b'] ** 2 - 4 * data['a'] * data['c']
        result = get_result(data['a'], data['b'], data['c'], discriminant)

    return render(request, "quadratic/results.html", {'form': form, 'discriminant': discriminant, 'result': result})

def get_result(a, b, c, discriminant):
    if discriminant == 0:
        x = x = (-b + discriminant ** (1 / 2.0)) / 2 * a
        return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
    elif discriminant < 0:
        return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        x1 = (-b + discriminant ** (1 / 2.0)) / 2 * a
        x2 = (-b - discriminant ** (1/2.0)) / 2 * a
        return 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)


