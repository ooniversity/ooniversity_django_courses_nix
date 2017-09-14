from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject