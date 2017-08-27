from django.db import models
from coaches.models import Coach
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

