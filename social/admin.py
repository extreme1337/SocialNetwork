from django.contrib import admin
from django.contrib.auth.models import User

from .models import MessageModel, Post, Tag, ThreadModel, UserProfile, Comment, Notification

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(MessageModel)
admin.site.register(ThreadModel)
admin.site.register(Tag)