from django.shortcuts import render

def quadratic_results(request):

    qe = QuadraticEquation(request.GET['a'], request.GET['b'], request.GET['c'])
    descr = False
    result = False

    if qe.is_valid:
        qe.calc_descr()
        d = qe.get_descr()
        result = qe.get_result()

    return render(request, "results.html",
                  {'a': qe.get_a(),'b': qe.get_b(), 'c': qe.get_c(), 'd': descr, 'result': result})


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.is_valid = True
        self.a = self.set_input(a, True)
        self.b = self.set_input(b)
        self.c = self.set_input(c)
        self.d = False

    def set_input(self, value, is_first=False):
        error = False
        if value == '':
            self.is_valid = False
            error = 'коэффициент не определен'
        else:
            try:
                value = int(value)
                if is_first is True and value == 0:
                    self.is_valid = False
                    error = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            except ValueError:
                self.is_valid = False
                error = 'коэффициент не целое число'
        return {'value': value, 'error': error}

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_descr(self):
        return self.d

    def get_result(self):
        if self.get_descr() == 0:
            x = self.calc_root()
            return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
        elif self.get_descr() < 0:
            return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        else:
            x1 = self.calc_root()
            x2 = self.calc_root(2)
            return 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)

    def calc_descr(self):
        self.d = self.b['value'] ** 2 - 4 * self.a['value'] * self.c['value']

    def calc_root(self, order=1):
        if order == 1:
            x = (-self.b['value'] + self.d ** (1 / 2.0)) / 2 * self.a['value']
        else:
            x = (-self.b['value'] - self.d ** (1/2.0)) / 2 * self.a['value']
        return x
