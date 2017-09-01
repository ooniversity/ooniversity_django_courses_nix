from django import forms
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^-?[0-9]*$', 'коэффициент не целое число')
clean_a = RegexValidator(r'^[^0]+$', 'коэффициент при первом слагаемом уравнения не может быть равным нулю')


class QuadraticFrom(forms.Form):
    a = forms.CharField(
        max_length=10,
        label='коэффициент a',
        validators=[alphanumeric, clean_a]
    )
    b = forms.CharField(
        max_length=10,
        label='коэффициент b',
        validators=[alphanumeric]
    )
    c = forms.CharField(
        max_length=10,
        label='коэффициент c',
        validators=[alphanumeric]
    )

