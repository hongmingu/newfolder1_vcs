from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
from django.utils.text import slugify

class Title(models.Model):

    titleJudgingText = models.TextField(max_length=160, unique=True)
    titleText = models.TextField(max_length=160)

    titleCreatedAt = models.DateTimeField(auto_now_add=True)
    titleUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titleText

class TitleText(models.Model):

    titleTextTitle = models.ForeignKey(Title)
    titleTextText = models.TextField(max_length=160)

    titleTextCreatedAt = models.DateTimeField(auto_now_add=True)
    titleTextUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titleTextText

class TitleLength(models.Model):
    titleLengthTitle = models.ForeignKey(Title)
    titleLengthText = models.TextField(max_length=100)
    titleLengthLength = models.PositiveIntegerField(default=0)
    titleTextCreatedAt = models.DateTimeField(auto_now_add=True)
    titleTextUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titleLengthText



#
# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.satshTitle)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Title.objects.filter(slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = '%s-%s' % (slug, qs.first().id)
#         return create_slug()(instance, new_slug=new_slug)
#     return slug
#
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#         # slug = slugify(instance.stashTitle)
#         # exists = Stash.objects.filter(slug=slug).exists()
#         # if exists:
#         #     slug = '%s-%s' %(slug, instance.id)
#         # instance.slug = slug
#
# pre_save.connect(pre_save_post_receiver, sender=Title)

#
#
# @receiver(post_save, sender=Title)
# def create_contentrelationship(sender, instance, created, **kwargs):
#     if created:
#         ContentRelationship.objects.create(=instance)
#
# @receiver(post_save, sender=Title)
# def save_contentrelationship(sender, instance, **kwargs):
#     instance.contentrelationship.save()
