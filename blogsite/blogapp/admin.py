from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Post,BlogUser


admin.site.register(BlogUser) 
admin.site.register(Post) 


