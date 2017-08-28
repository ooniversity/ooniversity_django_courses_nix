from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def get_serial_number(self):
        return self.id

    def get_name_surname(self):
        return self.name + ' ' + self.surname
    get_name_surname.short_description = 'Full name'

