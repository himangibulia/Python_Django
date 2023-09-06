from django.db import models

# Create your models here.

class student_detail(models.Model):
    username=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    pin_code=models.IntegerField(max_length=6)
    mobile_no=models.IntegerField(max_length= int|10)