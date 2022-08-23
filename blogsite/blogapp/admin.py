from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Post,Profile
# Register your models here.

# def UserModel(UserAdmin):
#     list_display = ['username',]

# admin.site.register(BlogUser,UserModel) 
admin.site.register(Post) 
admin.site.register(Profile)  

