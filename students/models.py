from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from courses.models import Course


@python_2_unicode_compatible
class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    skype = models.CharField(max_length=50, null=True)
    courses = models.ManyToManyField(Course)

    def get_courses(self):
        courses = self.courses.all()
        names = list(i.name for i in courses)
        return names

    def __str__(self):
        return self.name + ' ' + self.surname

