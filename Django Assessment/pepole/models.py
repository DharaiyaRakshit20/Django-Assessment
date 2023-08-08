from django.db import models

# Create your models here.

class register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    address=models.TextField(max_length=200, default=True)
    propic=models.FileField(upload_to='media/',default='pepole.jpg')

class notc(models.Model):
    name=models.CharField(max_length=50)
    notice=models.CharField(max_length=500)
    date=models.DateField(max_length=50)

class S_watchmen(models.Model):
    w_propic=models.FileField(upload_to='watchmen/',default='pepole.jpg')
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    gat_no=models.CharField(max_length=10)
    mobile=models.CharField(max_length=12)

class Event(models.Model):
    E_images=models.FileField(upload_to="event/",default='pepole.jpg')
    E_name=models.CharField(max_length=100)
    E_date=models.DateField(max_length=10)
    E_time=models.TimeField(max_length=10)
    E_releted=models.CharField(max_length=500)