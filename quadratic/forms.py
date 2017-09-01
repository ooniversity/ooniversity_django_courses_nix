from django import forms
from django.core.validators import RegexValidator
from django.forms import ValidationError

# alphanumeric = RegexValidator(r'^-?[0-9]*$', 'коэффициент не целое число')
# clean_a = RegexValidator(r'^[^0]+$', 'коэффициент при первом слагаемом уравнения не может быть равным нулю')


class QuadraticForm(forms.Form):
    a = forms.IntegerField(
        label='коэффициент a',
    )
    b = forms.IntegerField(
        label='коэффициент b',
    )
    c = forms.IntegerField(
        label='коэффициент c',
    )

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

        return a

