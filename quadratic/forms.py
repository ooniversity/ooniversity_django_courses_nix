from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(label='коэффициент a', max_length=10)
    b = forms.CharField(label='коэффициент b', max_length=10)
    c = forms.CharField(label='коэффициент c', max_length=10)

    def clean_a(self):
        a_data = self.cleaned_data['a']

        try:
            a_data = int(a_data)
        except ValueError:
            raise forms.ValidationError('коэффициент не целое число')

        if a_data == '0':
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

        return a_data

    def clean_b(self):
        b_data = self.cleaned_data['b']

        try:
            b_data = int(b_data)
        except ValueError:
            raise forms.ValidationError('коэффициент не целое число')

        return b_data

    def clean_c(self):
        c_data = self.cleaned_data['c']

        try:
            c_data = int(c_data)
        except ValueError:
            raise forms.ValidationError('коэффициент не целое число')

        return c_data