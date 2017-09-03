# -*- coding: utf-8 -*-
from django.db import models

from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length = 45)
    surname = models.CharField(max_length = 45)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length = 45)
    address = models.CharField(max_length = 200)
    skype = models.CharField(max_length = 64)
    courses = models.ManyToManyField(Course, help_text='FAQ help you')
 
    def full_name(self):
        return self.name + ' ' + self.surname
