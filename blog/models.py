from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_id= models.BigAutoField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=255)
    blog_created = models.DateField(auto_now_add=True)
    blog_edited = models.DateField(auto_now=True)
    blog_pic = models.ImageField(upload_to='blog_pic', null=True)
    blog_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
<<<<<<< HEAD
=======

class Gallery(models.Model):
    galleryTitle = models.CharField(max_length=255)
    galleryPic = models.ImageField(upload_to='gallery')
    galleryTag = models.CharField(max_length=100)
    galleryUploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery')
    
>>>>>>> Reservation
