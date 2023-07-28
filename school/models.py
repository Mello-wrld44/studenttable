from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=200)
    Admission = models.CharField(max_length=200)
    Course = models.CharField(max_length=150)


    class Meta:
        db_table = "Student"