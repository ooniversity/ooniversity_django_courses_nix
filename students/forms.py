from django import forms
from .models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'skype': forms.TextInput(attrs={'class': 'form-control'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
