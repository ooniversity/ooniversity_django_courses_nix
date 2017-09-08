from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    form_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

