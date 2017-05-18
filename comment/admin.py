from django.contrib import admin
from .models import CommentBase, CommentBaseText, CommentStash, CommentStashText, CommentPost, CommentPostText
# Register your models here.

admin.site.register(CommentBase)
admin.site.register(CommentBaseText)
admin.site.register(CommentStash)
admin.site.register(CommentStashText)
admin.site.register(CommentPost)
admin.site.register(CommentPostText)