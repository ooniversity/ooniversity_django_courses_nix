from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    skype = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)

    def get_full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    get_full_name.short_description = "Full Name"

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

