from django.db import models
from title.models import Title
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):

    baseUser = models.ForeignKey(User)
    baseTitle = models.ForeignKey(Title)

    baseText = models.TextField(max_length=100)

    baseCreatedAt = models.DateTimeField(auto_now_add=True)
    baseUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baseText

class BaseText(models.Model):

    baseTextBase = models.ForeignKey(Base)

    baseTextText = models.TextField(max_length=200)

    # stashImage = models.ImageField(null=True, blank=True, width_field="stashWidth", height_field="stashHeight")
    # stashWidth = models.IntegerField(default=0)
    # stashHeight = models.IntegerField(default=0)

    baseTextCreatedAt = models.DateTimeField(auto_now_add=True)
    baseTextUpdatedAt = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.baseTextText
