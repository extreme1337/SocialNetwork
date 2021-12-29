from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, UserProfile

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)