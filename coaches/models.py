from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.user.name
