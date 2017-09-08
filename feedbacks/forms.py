from .models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'from_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'create_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
