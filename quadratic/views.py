from django.shortcuts import render
from .forms import QuadraticForm


def quadratic_results(request):
    d = False
    result = False
    form = QuadraticForm()
    if 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            d = get_d(data['a'], data['b'], data['c'])
            result = get_result(data['a'], data['b'], d)

    return render(request, "quadratic/results.html",
                  {'form': form, 'd': d, 'result': result})


def get_d(a, b, c):
    return b ** 2 - 4 * a * c


def calc_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d ** (1 / 2.0)) / 2 * a
    else:
        x = (-b - d ** (1 / 2.0)) / 2 * a
    return x


def get_result(a, b, d):
    if d == 0:
        x = calc_root(a, b, d)
        print(x)
        return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
    elif d < 0:
        return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        x1 = calc_root(a, b, d)
        x2 = calc_root(a, b, d, 2)
        return 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)
