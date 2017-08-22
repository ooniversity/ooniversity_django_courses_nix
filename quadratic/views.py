from django.shortcuts import render

def quadratic_results():
    a = set_operand(request.GET['a'], True)
    b = set_operand(request.GET['b'])
    c = set_operand(request.GET['c'])
    discriminant = results = is_valid = False
    if type(a) != str and type(b) != str and type(c) != str:
	    is_valid = True

    if is_valid:
        discriminant = b ** 2 - 4 * a * c
        result = get_result(a, b, c, discriminant)

    return render(request, "results.html", {'a': a,'b': b, 'c': c, 'discriminant': discriminant, 'result': result})

def set_operand(value, first=False):
    result = value
    if value == '':
    	result = 'коэффициент не определен'
    else:
        try:
            value = int(value)
            if first is True and value == 0:
                result = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        except ValueError:
            result = 'коэффициент не целое число'
    return result

def get_result(a, b, c, discriminant):
    if discriminant == 0:
        x = x = (-b + discriminant ** (1 / 2)) / 2 * a
        return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
    elif discriminant < 0:
        return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        x1 = x = (-b + discriminant ** (1 / 2)) / 2 * a
        x2 = (-b - discriminant ** (1/2)) / 2 * a
        return 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)


