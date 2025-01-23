from django.db import models

# Create your models here.

class Courses(models.Model):
    name=models.CharField(max_length=100)
    lang=models.CharField(max_length=50)
    price=models.FloatField()
    image=models.ImageField(upload_to='images')


class Enquiry(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    date=models.DateTimeField()
