from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id= models.BigAutoField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=255)
    blog_created = models.DateField(auto_now_add=True)
    blog_edited = models.DateField(auto_now=True)
    blog_pic = models.ImageField(upload_to='blog_pic', null=True)