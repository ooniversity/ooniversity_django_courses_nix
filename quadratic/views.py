"""Quadratic View"""

import math
from django.shortcuts import render
from django.views import generic

ERROR_UNDEFINED = 'коэффициент не определен'
ERROR_DIGIT = 'коэффициент не целое число'
ERROR_A_ZERO = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
ERROR_D_NEGATIVE = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений'


class ResultsView(generic.TemplateView):
    """Quadratic Results View"""
    template_name = 'quadratic/results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)

        # items = dict(self.request.GET.items())
        items = {
            'a': self.request.GET.get('a', ''),
            'b': self.request.GET.get('b', ''),
            'c': self.request.GET.get('c', ''),
        }

        context.update({
            'items': items,
            'errors': {},
            'd': None,
            'x1': None,
            'x2': None
        })

        errors = self.validate(**items)
        if errors:
            result = {'errors': errors}
        else:
            result = self.calculate(**items)

        context.update(result)
        return context

    def validate(self, **kwargs):
        """Validate Input Data"""
        result = {}

        for key, value in kwargs.items():
            if value == '':
                result[key] = ERROR_UNDEFINED
                continue

            if not self._is_digit(value):
                result[key] = ERROR_DIGIT
                continue

            if key == 'a' and value == '0':
                result[key] = ERROR_A_ZERO
                continue
        return result

    @classmethod
    def calculate(cls, **kwargs):
        """Calculate X1 and X2"""
        a = int(kwargs.get('a'))
        b = int(kwargs['b'])
        c = int(kwargs['c'])
        result = {}

        d = b**2 - 4 * a * c
        result.update({'d': d})
        if d < 0:
            result.update({'errors': {'d': ERROR_D_NEGATIVE}})
            return result

        x1 = round((-b + math.sqrt(d)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(d)) / (2 * a), 2)
        result.update({'x1': x1, 'x2': x2})
        return result


    @classmethod
    def _is_digit(cls, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()
