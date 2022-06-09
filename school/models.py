from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    courseTitle = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    courseDate = models.DateField
    courseTime = models.TimeField()
    roomNumber = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.courseTitle

    class Meta:
        db_table='course'
        verbose_name_plural='courses'

class Assignment(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    assignmentName = models.CharField(max_length=255)
    dueDate = models.DateField()
    assignmentDetails = models.TextField()
    

    def __str__(self):
        return self.assignmentName

    class Meta:
        db_table='assignment'
        verbose_name_plural='assignments'