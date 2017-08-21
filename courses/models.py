from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject


class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
