from django.shortcuts import render
import math


# Create your views here.
def quadratic_results(request):
    a = None
    b = None
    c = None

    context = {}

    if request.GET.get('a'):
        a = request.GET.get('a')
        try:
            a = int(request.GET.get('a'))
        except ValueError:
            context['a_err'] = 'коэффициент не целое число'

        if a == 0:
            context['a_err'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

        context['a_var'] = a
    else:
        context['a_err'] = 'коэффициент не определен'

    if request.GET.get('b'):
        b = request.GET.get('b')
        try:
            b = int(b)
        except ValueError:
            context['b_err'] = 'коэффициент не целое число'

        context['b_var'] = b
    else:
        context['b_err'] = 'коэффициент не определен'

    if request.GET.get('c'):
        c = request.GET.get('c')
        try:
            c = int(c)
        except ValueError:
            context['c_err'] = 'коэффициент не целое число'
        context['c_var'] = c
    else:
        context['c_err'] = 'коэффициент не определен'

    if 'a_err' not in context and 'b_err' not in context and 'c_err' not in context:
        descr = b**2 - 4 * a * c
        context['D_var'] = descr

        if descr > 0:
            x1 = (-b + math.sqrt(b**2 - 4* a * c)) / 2 * a
            x2 = (-b - math.sqrt(b**2 - 4* a * c)) / 2 * a
            context['D_info'] = 'Квадратное уравнение имеет два действительных корня: ' \
                                'x1 = {0:.1f}, x2 = {1:.1f}'.format(round(x1, 1), round(x2, 1))
        elif descr == 0:
            x1 = -(b / 2 * a)
            context['D_info'] = 'Дискриминант равен нулю, квадратное уравнение имеет один ' \
                                'действительный корень: x1 = x2 = {0:.1f}'.format(round(x1, 1))
        else:
            context['D_info'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

    return render(request, 'quadratic/results.html', context)