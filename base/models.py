from django.db import models
from title.models import Title
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):

    baseUser = models.ForeignKey(User)
    baseTitle = models.ForeignKey(Title)
    baseSlug = models.SlugField(unique=True)

    baseText = models.TextField(max_length=100)

    baseCreatedAt = models.DateTimeField(auto_now_add=True)
    baseUpdatedAt = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.baseText
