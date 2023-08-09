from django.db import models

# Create your models here.

class form(models.Model):
    Blog=models.CharField(max_length=50)
    Contant=models.CharField(max_length=500)
    Create=models.DateTimeField(max_length=100)
    Update=models.DateTimeField(max_length=100)