from django.db import models

# Create your models here.
class Course(models.Model):
    idcourse = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    hour = models.IntegerField()
    credits = models.IntegerField()
    state = models.BooleanField()

# Create your models here.
class Career(models.Model):
    idcareer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    shortname = models.CharField(max_length=100)
    image = models.CharField(max_length=10)
    state = models.BooleanField()
