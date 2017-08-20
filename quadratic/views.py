from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .validator import is_valid, validate_a, validate


def quadratic_results(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    c = request.GET.get('c', '')
    data = {
        'a': a,
        'b': b,
        'c': c
    }
    if is_valid(a, b, c):
        data['result'] = {
            'desc': get_desc(a, b, c),
            'x1': get_x1(a, b, c),
            'x2': get_x2(a, b, c),
        }
    else:
        data['errors'] = {
            'a': validate_a(a),
            'b': validate(b),
            'c': validate(c)
        }

    return render(request, 'quadratic/results.html', {'data': data})


def get_desc(a, b, c):
    return int(b) ** 2 - 4 * int(a) * int(c)


def get_x1(a, b, c):
    x1 = (-int(b) + get_desc(a, b, c) ** (1 / 2.0)) / 2 * int(a)
    return x1


def get_x2(a, b, c):
    x2 = (-int(b) - get_desc(a, b, c) ** (1 / 2.0)) / 2 * int(a)
    return x2
