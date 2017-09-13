from django.db import models
from courses.models import Course


class Students(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.surname + ' ' + self.name

    @property
    def full_name(self):
        return self.surname + ' ' + self.name
