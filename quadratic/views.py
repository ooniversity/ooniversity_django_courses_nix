import math
from django.views import generic


def quadratic_results():
    return ResultsView.as_view()


class ResultsView(generic.TemplateView):

    template_name = 'quadratic/results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)

        coefficients = {
            'a': self.request.GET.get('a', ''),
            'b': self.request.GET.get('b', ''),
            'c': self.request.GET.get('c', ''),
        }

        context.update({
            'coefficients_names': ['a', 'b', 'c'],
            'coefficients': coefficients,
            'result': QuadraticCalculator.calculate(coefficients)
        })
        return context


class QuadraticValidator():
    errors = {
        'undefined': 'коэффициент не определен',
        'not_digit': 'коэффициент не целое число',
        'empty_a': 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    }

    @classmethod
    def validate(cls, kwargs):
        output = {}
        fields = ['a', 'b', 'c']
        for field in fields:
            value = kwargs.get(field, '')
            if value == '':
                output[field] = cls.errors['undefined']
                continue
            if not cls.__is_digit(value):
                output[field] = cls.errors['not_digit']
                continue
            if field == 'a' and value == '0':
                output[field] = cls.errors['empty_a']

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
    def calculate(cls, coefficients):

        result = {
            'discriminant': None,
            'errors': {},
            'roots': []
        }
        errors = QuadraticValidator.validate(coefficients)

        if len(errors) > 0:
            result['errors'] = errors
        else:
            a = int(coefficients['a'])
            b = int(coefficients['b'])
            c = int(coefficients['c'])

            discriminant = b ** 2 - 4 * a * c
            result['discriminant'] = discriminant

            if discriminant < 0:
                result['errors']['d'] = cls.negative_discriminant_error
            else:
                root1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
                root2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
                result['roots'] = {'root1': root1, 'root2': root2}

        return result
