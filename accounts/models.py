from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    birthday = models.DateField()
    
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)