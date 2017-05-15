from django.db import models
from title.models import Title
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Stash(models.Model):

    stashUser = models.ForeignKey(User)
    stashTitle = models.ForeignKey(Title)

    stashText = models.TextField(max_length=200)

    # stashImage = models.ImageField(null=True, blank=True, width_field="stashWidth", height_field="stashHeight")
    # stashWidth = models.IntegerField(default=0)
    # stashHeight = models.IntegerField(default=0)

    stashCreatedAt = models.DateTimeField(auto_now_add=True)
    stashUpdatedAt = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.stashText


    # stashPro = models.PositiveIntegerField(default=0)
    # stashCon = models.PositiveIntegerField(default=0)
    # stashStage = models.PositiveIntegerField(default=0)
    # stashBlinded = models.SmallIntegerField(default=1)


