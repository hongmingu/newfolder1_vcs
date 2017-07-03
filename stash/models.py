from django.db import models
from title.models import Title
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class StashUrl(models.Model):

    stashUrlText = models.TextField(max_length=200)

    stashUrlCreatedAt = models.DateTimeField(auto_now_add=True)
    stashUrlUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stashUrlText

class Stash(models.Model):

    stashUser = models.ForeignKey(User)
    stashTitle = models.ForeignKey(Title)
    stashUrl = models.ForeignKey(StashUrl)

    stashText = models.TextField(max_length=200)

    stashCreatedAt = models.DateTimeField(auto_now_add=True)
    stashUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stashText

class StashVerbal(models.Model):
    stash = models.ForeignKey(Stash)
    stashVerbalUser = models.ForeignKey(User)

    stashVerbalText = models.TextField(max_length=200)

    stashCreatedAt = models.DateTimeField(auto_now_add=True)
    stashUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stashVerbalText


