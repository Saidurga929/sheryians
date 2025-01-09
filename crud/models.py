from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=30)
    Phone=models.IntegerField()
    Date_And_Time=models.DateTimeField(auto_now_add=True)