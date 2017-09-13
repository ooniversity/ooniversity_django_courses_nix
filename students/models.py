from django.db import models
from courses.models import Course


# Create your models here
class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name + ' ' + self.surname
