from django.contrib import admin
from .models import Post, PostText

# Register your models here.
admin.site.register(Post)
admin.site.register(PostText)
