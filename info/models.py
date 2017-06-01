from django.db import models
from django.contrib.auth.models import User
from title.models import Title
from base.models import Base
from stash.models import Stash
from post.models import Post
from comment.models import CommentBase, CommentStash, CommentPost
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
class Userreaction(models.Model):
    userprofile = models.OneToOneField(Userprofile, primary_key=True)

    userReaction1 = models.PositiveSmallIntegerField(default=0)
    userReaction2 = models.PositiveSmallIntegerField(default=0)
    userReaction3 = models.PositiveSmallIntegerField(default=0)

    userreactionCreatedAt = models.DateTimeField(auto_now_add=True)
    userreactionUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'User : %s, Reaction1 : %s, Reaction2 : %s, Reaction3 : %s, Updated at : %s' % (self.userprofile.user.username, self.userReaction1 , self.userReaction2, self.userReaction3, self.userreactionUpdatedAt)

@receiver(post_save, sender=Userprofile)
def createUserreaction(sender, instance, created, **kwargs):
    if created:
        Userreaction.objects.create(userprofile=instance)

@receiver(post_save, sender=Userprofile)
def saveUserreactions(sender, instance, **kwargs):
    instance.userreaction.save()


################################################################################################
class Baseprofile(models.Model):
    base = models.OneToOneField(Base, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    basePro = models.PositiveIntegerField(default=0)
    baseCon = models.PositiveIntegerField(default=0)
    baseStage = models.PositiveIntegerField(default=0)
    baseBlinded = models.PositiveSmallIntegerField(default=1)

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
    stashBlinded = models.PositiveSmallIntegerField(default=1)

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

class Commentbaseprofile(models.Model):
    comment = models.OneToOneField(CommentBase, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=CommentBase)
def createCommentbaseprofile(sender, instance, created, **kwargs):
    if created:
        Commentbaseprofile.objects.create(comment=instance)

@receiver(post_save, sender=CommentBase)
def saveCommentBaseprofile(sender, instance, **kwargs):
    instance.commentbaseprofile.save()

################################################################################################

class Commentstashprofile(models.Model):
    comment = models.OneToOneField(CommentStash, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=CommentStash)
def createCommentprofile(sender, instance, created, **kwargs):
    if created:
        Commentstashprofile.objects.create(comment=instance)

@receiver(post_save, sender=CommentStash)
def saveCommentstashprofile(sender, instance, **kwargs):
    instance.commentstashprofile.save()

################################################################################################

class Commentpostprofile(models.Model):
    comment = models.OneToOneField(CommentPost, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    profileCreatedAt = models.DateTimeField(auto_now_add=True)
    profileUpdatedAt = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=CommentPost)
def createCommentpostprofile(sender, instance, created, **kwargs):
    if created:
        Commentpostprofile.objects.create(comment=instance)

@receiver(post_save, sender=CommentPost)
def saveCommentpostprofile(sender, instance, **kwargs):
    instance.commentpostprofile.save()

#####################################################################################

class Bridge(models.Model):
    bridgingUserProfile = models.ForeignKey(Userprofile, related_name='bridgingUserProfile')
    bridgedUserProfile = models.ForeignKey(Userprofile, related_name='bridgedUserProfile')

    bridgeState = models.PositiveSmallIntegerField(default=0)

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
    flowIsActive = models.PositiveSmallIntegerField(default=0)

    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Base info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedBaseProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedBaseProfile'),)

class BaseProCon(models.Model):
    userProfile = models.ForeignKey(Userprofile)
    RelatedBaseProfile = models.ForeignKey(Baseprofile, related_name='RelatedBase', null=True)

    ProConState = models.PositiveSmallIntegerField(default=0)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Base Pro or Con // User : %s, RelatedBase : %s, Pro or Con State : %s, UpdatedAt : %s, CreatedAt : %s' % (self.userProfile, self.RelatedBaseProfile, self.ProConState, self.UpdatedAt, self.CreatedAt)

    class Meta:
        unique_together = (('userProfile', 'RelatedBaseProfile'), )

class BaseReaction(models.Model):

    reactingUserProfile = models.ForeignKey(Userprofile)
    reactedBaseProfile = models.ForeignKey(Baseprofile, related_name='ReactedBase', null=True)

    reactionType = models.PositiveSmallIntegerField(default=0)

    reactionCreatedAt = models.DateTimeField(auto_now_add=True)
    reactionUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Base Reaction info // ReactingUser : %s, ReactedContent : %s, ReactionTupe : %s, UpdatedAt : %s, CreatedAt : %s' % (self.reactingUserProfile, self.reactedBaseProfile, self.reactionType, self.reactionUpdatedAt, self.reactionCreatedAt)

    class Meta:
        unique_together = (('reactingUserProfile', 'reactedBaseProfile'),)



########################################################################################

class StashFlow(models.Model):

    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedStashProfile = models.ForeignKey(Stashprofile)
    flowIsActive = models.PositiveSmallIntegerField(default=0)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Stash info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedStashProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedStashProfile'), )

class StashProCon(models.Model):
    userProfile = models.ForeignKey(Userprofile)
    RelatedStashProfile = models.ForeignKey(Stashprofile, related_name='RelatedStash', null=True)

    ProConState = models.PositiveSmallIntegerField(default=0)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Stash Pro or Con // User : %s, RelatedStash : %s, Pro or Con State : %s, UpdatedAt : %s, CreatedAt : %s' % (self.userProfile, self.RelatedStashProfile, self.ProConState, self.CreatedAt, self.UpdatedAt)

    class Meta:
        unique_together = (('userProfile', 'RelatedStashProfile'), )

class StashReaction(models.Model):
    reactingUserProfile = models.ForeignKey(Userprofile)
    reactedStashProfile = models.ForeignKey(Stashprofile, related_name='ReactedStash', null=True)

    reactionType = models.PositiveSmallIntegerField(default=0)

    reactionCreatedAt = models.DateTimeField(auto_now_add=True)
    reactionUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Stash Reaction info // ReactingUser : %s, ReactedContent : %s, ReactionTupe : %s, UpdatedAt : %s, CreatedAt : %s' % (
        self.reactingUserProfile, self.reactedStashProfile, self.reactionType, self.reactionUpdatedAt, self.reactionCreatedAt
        )

    class Meta:
        unique_together = (('reactingUserProfile', 'reactedStashProfile'),)

########################################################################################

class PostFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedPostProfile = models.ForeignKey(Postprofile)

    flowIsActive = models.PositiveSmallIntegerField(default=0)

    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Post info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedPostProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedPostProfile'),)

class PostReaction(models.Model):
    reactingUserProfile = models.ForeignKey(Userprofile)
    reactedPostProfile = models.ForeignKey(Postprofile, related_name='ReactedPost', null=True)

    reactionType = models.PositiveSmallIntegerField(default=0)

    reactionCreatedAt = models.DateTimeField(auto_now_add=True)
    reactionUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Post Reaction info // ReactingUser : %s, ReactedContent : %s, ReactionTupe : %s, UpdatedAt : %s, CreatedAt : %s' % (
            self.reactingUserProfile, self.reactedPostProfile, self.reactionType, self.reactionUpdatedAt,
            self.reactionCreatedAt
        )

    class Meta:
        unique_together = (('reactingUserProfile', 'reactedPostProfile'),)


########################################################################################

class CommentBaseFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedCommentProfile = models.ForeignKey(Commentbaseprofile)

    flowIsActive = models.PositiveSmallIntegerField(default=0)

    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'CommentBase info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedCommentProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedCommentProfile'),)

class CommentStashFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedCommentProfile = models.ForeignKey(Commentstashprofile)
    flowIsActive = models.PositiveSmallIntegerField(default=0)

    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'CommentStash info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedCommentProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedCommentProfile'),)

class CommentPostFlow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedCommentProfile = models.ForeignKey(Commentpostprofile)

    flowIsActive = models.PositiveSmallIntegerField(default=0)

    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'CommentPost info // flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedCommentProfile, self.flowCreatedAt, self.flowUpdatedAt)

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