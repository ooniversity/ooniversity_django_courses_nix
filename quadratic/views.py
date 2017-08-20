from django.http import HttpResponse, QueryDict
from django.shortcuts import render
import cmath

def results(request):
    query_items = {}
    query_items['a'] = request.GET['a']
    query_items['b'] = request.GET['b']
    query_items['c'] = request.GET['c']

    def sanitizer(query_items):
        sanitized_items = {}
        is_valid = False
        error_messages = {
        'zero_first':'коэффициент при первом слагаемом уравнения не может быть равным нулю',
        'is_undefind':'коэффициент не определен',
        'is_not_int':'коэффициент не целое число'
        }
        
        for key, value in query_items.items():
            if not value:
                sanitized_items[key] = error_messages['is_undefind']
            else:
                try:
                    i = int(value)
                    if i == 0 and key == 'a':
                        sanitized_items[key] = error_messages['zero_first']
                    else:
                        sanitized_items[key] = i
                except ValueError as e:  
                    sanitized_items[key] = error_messages['is_not_int']
        return sanitized_items
   
    def equationSolver(values):
        a = values['a']
        b = values['b']
        c = values['c']
        discr = b**2 - 4 * a * c;
        if discr > 0:
            import math
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            result = {'discr': discr, 'x1': x1, 'x2': x1} 
        elif discr == 0:
            x1 = -b / (2 * a)
            result =  {'discr': discr, 'x1': x1} 
        else:
            result = {'discr': discr} 
        return result
    
    params = sanitizer(query_items)

    if all(isinstance(value, int) for value in params.values()):
        result = equationSolver(params)
    else:
        for k, v in query_items.items():
            if isinstance(params[k], str):
                params[k] = {'value': v, 'error': params[k]}
            else:
                params[k] = {'value': v, 'error': ''}
      
        result = None
   

    return render(request, 'quadratic/results.html', {
        'request': query_items,
        'response': params,
        'result': result})
