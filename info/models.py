from django.db import models
from django.contrib.auth.models import User
from title.models import Title
from base.models import Base
from stash.models import Stash
from post.models import Post
from comment.models import Comment
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    userprofileCalledName = models.TextField(max_length=30)
    userprofileImage = models.ImageField(blank=True)
    userprofileDescription = models.TextField(max_length=100)
    userprofileCreatedAt = models.DateTimeField(auto_now_add=True)
    userprofileUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'UserProfile : %s, Updated at : %s' % (self.user.username, self.userprofileUpdatedAt)

@receiver(post_save, sender=User)
def createUserprofile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)
@receiver(post_save, sender=User)
def saveUserprofile(sender, instance, **kwargs):
    instance.userprofile.save()
################################################################################################
class Baseprofile(models.Model):
    base = models.OneToOneField(Base, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    basePro = models.PositiveIntegerField(default=0)
    baseCon = models.PositiveIntegerField(default=0)
    baseStage = models.PositiveIntegerField(default=0)
    baseBlinded = models.SmallIntegerField(default=1)

    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Base)
def createBaseprofile(sender, instance, created, **kwargs):
    if created:
        Baseprofile.objects.create(base=instance)

@receiver(post_save, sender=Base)
def saveBaseprofile(sender, instance, **kwargs):
    instance.baseprofile.save()

################################################################################################

class Stashprofile(models.Model):
    stash = models.OneToOneField(Stash, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    stashPro = models.PositiveIntegerField(default=0)
    stashCon = models.PositiveIntegerField(default=0)
    stashStage = models.PositiveIntegerField(default=0)
    stashBlinded = models.SmallIntegerField(default=1)

    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Stash)
def createStashprofile(sender, instance, created, **kwargs):
    if created:
        Stashprofile.objects.create(stash=instance)

@receiver(post_save, sender=Stash)
def saveStashprofile(sender, instance, **kwargs):
    instance.stashprofile.save()

################################################################################################

class Postprofile(models.Model):
    post = models.OneToOneField(Post, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Post)
def createPostprofile(sender, instance, created, **kwargs):
    if created:
        Postprofile.objects.create(post=instance)

@receiver(post_save, sender=Post)
def savePostprofile(sender, instance, **kwargs):
    instance.postprofile.save()



################################################################################################

class Commentprofile(models.Model):
    comment = models.OneToOneField(Comment, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Comment)
def createCommentprofile(sender, instance, created, **kwargs):
    if created:
        Commentprofile.objects.create(comment=instance)

@receiver(post_save, sender=Comment)
def saveBaseprofile(sender, instance, **kwargs):
    instance.commentprofile.save()

#####################################################################################

class Bridge(models.Model):
    bridgingUserProfile = models.ForeignKey(Userprofile, related_name='bridgingUserProfile')
    bridgedUserProfile = models.ForeignKey(Userprofile, related_name='bridgedUserProfile')
    bridgeCreatedAt = models.DateTimeField(auto_now_add=True)
    bridgeUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'bridging : %s, bridged : %s, UpdatedAt : %s, Created At : %s' % (self.bridgingUserProfile, self.bridgedUserProfile, self.bridgeCreatedAt, self.bridgeUpdatedAt)

    class Meta:
        unique_together = (('bridgingUserProfile', 'bridgedUserProfile'),)

########################################################################################

class BaseFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedBaseProfile = models.ForeignKey(Baseprofile)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Base info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedBaseProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedBaseProfile'),)

class BaseProCon(models.Model):
    userProfile = models.ForeignKey(Userprofile)
    proBaseProfile = models.ForeignKey(Stashprofile, related_name='proBase')
    conBaseProfile = models.ForeignKey(Stashprofile, related_name='conBase')

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Base Pro or Con // User : %s, proBase : %s, conBase : %s, UpdatedAt : %s, CreatedAt : %s' % (self.userProfile, self.proBaseProfile, self.conBaseProfile, self.CreatedAt, self.UpdatedAt)

    class Meta:
        unique_together = (('userProfile', 'proBaseProfile'), ('userProfile', 'conBaseProfile'),)


########################################################################################

class StashFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedStashProfile = models.ForeignKey(Stashprofile)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Stash info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedStashProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedStashProfile'),)

class StashProCon(models.Model):
    userProfile = models.ForeignKey(Userprofile)
    proStashProfile = models.ForeignKey(Stashprofile, related_name='proStash')
    conStashProfile = models.ForeignKey(Stashprofile, related_name='conStash')

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Stash Pro or Con // User : %s, proStash : %s, conStash : %s, UpdatedAt : %s, CreatedAt : %s' % (self.userProfile, self.proStashProfile, self.conStashProfile, self.CreatedAt, self.UpdatedAt)

    class Meta:
        unique_together = (('userProfile', 'proStashProfile'), ('userProfile', 'conStashProfile'),)


########################################################################################

class PostFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedPostProfile = models.ForeignKey(Postprofile)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Post info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedPostProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedPostProfile'),)

########################################################################################

class CommentFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedCommentProfile = models.ForeignKey(Commentprofile)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Comment info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedCommentProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedCommentProfile'),)



#######################################################################################

'''
class Contentsprofile(models.Model):
    title = models.OneToOneField(Title, null=True, blank=True)
    basic = models.OneToOneField(Base, null=True, blank=True)
    stash = models.OneToOneField(Stash, null=True, blank=True)
    post = models.OneToOneField(Post, null=True, blank=True)
    comment = models.OneToOneField(Comment, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    postprofileCreatedAt = models.DateTimeField(auto_now_add=True)
    postprofileUpdatedAt = models.DateTimeField(auto_now=True)
    #Do something to connect Post1 or Post2

@receiver(post_save, sender=Title)
def createContentprofileForTitle(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(title=instance)
@receiver(post_save, sender=Title)
def saveContentsprofileForTitle(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Base)
def createContentsprofileForBasic(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(basic=instance)
@receiver(post_save, sender=Base)
def saveContentsprofileForBasic(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Stash)
def createContentsprofileForStash(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(stash=instance)
@receiver(post_save, sender=Stash)
def saveContentsprofileForStash(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Post)
def createContentsprofileForPost(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(post=instance)
@receiver(post_save, sender=Post)
def saveContentsprofileForPost(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Comment)
def createContentsprofileForComment(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(comment=instance)
@receiver(post_save, sender=Comment)
def saveContentsprofileForComment(sender, instance, **kwargs):
    instance.contentsprofile.save()
'''
#######################################################################################################################
'''
class Flow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedContentsProfile = models.ForeignKey(Contentsprofile)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedContentProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedContentsProfile'),)
'''