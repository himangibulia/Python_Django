from django.db import models

# Create your models here.

class myprofile(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    roll_no=models.IntegerField()
    mobile_no=models.CharField(max_length=10)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=6)
    image=models.ImageField(upload_to='media')
    strem=models.CharField(max_length=50)
    description=models.CharField(max_length=400)