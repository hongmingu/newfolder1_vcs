from django.db import models
from django.contrib.auth.models import User
from title.models import Title
from base.models import Base
from stash.models import Stash
from post.models import Post
# Create your models here.

class CommentBase(models.Model):

    commentBase = models.ForeignKey(Base, blank=True, null=True)
    commentUser = models.ForeignKey(User)

    commentText = models.TextField(max_length=200)

    commentCreatedAt = models.DateTimeField(auto_now_add=True)
    commentUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentText

class CommentBaseText(models.Model):

    commentBaseTextCommentBase = models.ForeignKey(CommentBase)
    commentBaseTextCommentText = models.TextField(max_length=200)

    commentBaseTextCreatedAt = models.DateTimeField(auto_now_add=True)
    commentBaseTextUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentBaseTextCommentText

class CommentStash(models.Model):

    commentStash = models.ForeignKey(Stash, blank=True, null=True)
    commentUser = models.ForeignKey(User)

    commentText = models.TextField(max_length=200)

    commentCreatedAt = models.DateTimeField(auto_now_add=True)
    commentUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentText


class CommentStashText(models.Model):

    commentStashTextCommentStash = models.ForeignKey(CommentStash)
    commentStashTextCommentText = models.TextField(max_length=200)

    commentStashTextCreatedAt = models.DateTimeField(auto_now_add=True)
    commentStashTextUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentStashTextCommentText

class CommentPost(models.Model):

    commentPost = models.ForeignKey(Post, blank=True, null=True)
    commentUser = models.ForeignKey(User)

    commentText = models.TextField(max_length=200)

    commentCreatedAt = models.DateTimeField(auto_now_add=True)
    commentUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentText


class CommentPostText(models.Model):

    commentPostTextCommentStash = models.ForeignKey(CommentPost)
    commentPostTextCommentText = models.TextField(max_length=200)

    commentPostTextCreatedAt = models.DateTimeField(auto_now_add=True)
    commentPostTextUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentPostTextCommentText
