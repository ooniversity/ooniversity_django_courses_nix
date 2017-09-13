from django.db import models
from django.contrib.auth import get_user_model


class Coach(models.Model):
    user = models.OneToOneField(get_user_model())
    date_of_birth = models.DateField()
    gender = models.CharField(choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ), max_length=1)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.user.first_name

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
