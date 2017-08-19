from django.shortcuts import render

def quadratic_results(request):
    not_digit_message = 'коэффициент не целое число'
    not_defined_message = 'коэффициент не определен'
    first_arg_zero = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    a_m = ''
    b_m = ''
    c_m = ''
    print(request.GET['a'])
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    
    if a == '':
        a_m = not_defined_message
    elif a == '0':
        a_m = first_arg_zero
    else:
        try:
            a = int(a)
        except ValueError:
            a_m = not_digit_message
    
    if b == '':
        b_m = not_defined_message
    else:
        try:
            b = int(b)
        except ValueError:
            b_m = not_digit_message
    
    if c == '':
        c_m = not_defined_message
    else:
        try:
            c = int(c)
        except ValueError:
            c_m = not_digit_message
    
    d = ''
    d_m = ''
    result = ''
    if a_m == '' and b_m == '' and c_m == '':
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
    
    context = {
        'a' : a,
        'a_m' : a_m,
        'b' : b,
        'b_m' : b_m,
        'c' : c,
        'c_m' : c_m,
        'd' : d,
        'd_m' : d_m,
        'r_m' : result
    }
    
    return render(request, 'quadratic/results.html', context)

