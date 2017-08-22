from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__():
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
    course = 
    order = models.PositiveIntegerField()
    
    def __str__():
        return self.subject
