import math
from django.views import generic


class ResultsView(generic.TemplateView):

    template_name = 'quadratic/results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        print(context)
        coefficients = {
            'a': kwargs.get('a', ''),
            'b': kwargs.get('b', ''),
            'c': kwargs.get('c', ''),
        }

        context.update({
            'coefficients': coefficients,
            'result': QuadraticCalculator.calculate(**kwargs)
        })
        return context


class QuadraticValidator():
    errors = {
        'undefined': 'коэффициент не определен',
        'not_digit': 'коэффициент не целое число',
        'empty_a': 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    }

    @classmethod
    def validate(cls, **kwargs):
        output = {}

        for key, value in kwargs:
            if value == '':
                output[key] = cls.errors['undefined']
                continue
            if not cls.__is_digit(value):
                output[key] = cls.errors['not_digit']
                continue
            if (key == 'a' and value == '') or 'a' not in kwargs.keys():
                output[key] = cls.errors['empty_a']

        return output

    @classmethod
    def __is_digit(cls, value):
        if value[0] in ['-', '+']:
            return value[1:].isdigit()
        else:
            return value.isdigit()


class QuadraticCalculator:

    negative_discriminant_error = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений'

    @classmethod
    def calculate(cls, **kwargs):
        result = {
            'discriminant': None,
            'errors': {},
            'roots': []
        }
        errors = QuadraticValidator.validate(**kwargs)
        return result
        if len(errors) > 0:
            result['error'] = errors
            return result

        a = int(kwargs['a'])
        b = int(kwargs['b'])
        c = int(kwargs['c'])

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            result['errors']['d'] = cls.negative_discriminant_error
            return result

        result['discriminant'] = discriminant

        root1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
        root2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
        result['roots'] = {'root1': root1, 'root2': root2}

        return result
