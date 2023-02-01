from django.db import models

# Create your models here.

class DataBase(models.Model):
    Image = models.FileField(upload_to='Input/data')
    Number = models.TextField(max_length=50)
    status = models.TextField(max_length= 50)


class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()