from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
    id =models.IntegerField(primary_key=True)
class Student(models.Model):
    name = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
    id =models.IntegerField(primary_key=True)

# Create your models here.
