from django.shortcuts import render
from .forms import QuadraticForm

def quadratic_results(request):
    context = {}
    if request.method == 'GET' and 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        form = QuadraticForm(request.GET)
        
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            d = b * b - 4 * a * c
            d_m = 'Дискриминант: {:d}'.format(d)
            if d > 0:
                x1 = (-b + pow(d, 0.5)) / 2 * a
                x2 = (-b - pow(d, 0.5)) / 2 * a
                result = 'Квадратное уравнение имеет два действительных корня: x1 = {:.1f}, x2 = {:.1f}'.format(x1, x2)
            elif d == 0:
                x1 = -b / 2 * a
                result = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {:.1f}'.format(x1)
            else:
                result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            context['d_m'] = d_m
            context['r_m'] = result
    else:
        form = QuadraticForm()

    context['form'] = form
    return render(request, 'quadratic/results.html', context)
