from django.db import models
from django.conf import settings


# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.user.username