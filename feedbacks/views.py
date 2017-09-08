# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail, mail_admins

class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(self.object.subject,
                    self.object.message)

        return response
