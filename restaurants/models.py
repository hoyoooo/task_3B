from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 120)
    describtion = models.TextField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    logo = models.ImageField(null = True, blank = True)

class Item(models.Model):
    name = models.CharField(max_length = 120)
    price= models.DecimalField()
    describtion = models.TextField()
    


    def __str__(self):
        return self.name