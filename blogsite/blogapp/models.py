
from pydoc import render_doc
from django.db import models

from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser 

# # Create your models here.

# class BlogUser(AbstractUser):
#     profile_pic = models.ImageField(upload_to='media/profile_pic',null=True,blank=True) 


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=300) 
    desc = models.TextField() 
    create_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    image = models.ImageField(upload_to='media/blog_image',blank=True,null=True) 

    def __str__(self):
        return self.title[:30] 
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True) 
    bio = models.TextField(null=True,blank=True) 
    profile_pic = models.ImageField(upload_to='media/profile_pic') 

    def __str__(self):
        return self.user.username 
