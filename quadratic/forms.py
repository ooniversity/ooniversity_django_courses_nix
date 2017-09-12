from django import forms


errors = {
   'required': 'коэффициент не определен',
   'invalid': 'коэффициент не целое число',
}


class QuadraticForm(forms.Form):

    a = forms.IntegerField(widget=forms.TextInput, label='коэффициент a', error_messages=errors)
    b = forms.IntegerField(widget=forms.TextInput, label='коэффициент b', error_messages=errors)
    c = forms.IntegerField(widget=forms.TextInput, label='коэффициент c', error_messages=errors)

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')

        return a