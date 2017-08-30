from django.contrib.auth.models import User
from django.db import models

from pybursa import settings

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gander = models.CharField(max_length=255, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.user.first_name

    def get_fool_name(self):
        return self.user.first_name + ' ' + self.user.last_name