from django.contrib import admin
from info.models import Userprofile, Bridge, Userreaction, Baseprofile, Stashprofile, Postprofile
from info.models import Commentbaseprofile, Commentstashprofile, Commentpostprofile, BaseFlow, BaseProCon, BaseReaction, StashFlow, StashProCon, StashReaction, PostFlow, PostReaction
from info.models import CommentBaseFlow, CommentBaseReaction, CommentStashFlow, CommentStashReaction, CommentPostFlow, CommentPostReaction
# Register your models here.

admin.site.register(Userprofile)
admin.site.register(Bridge)
admin.site.register(Userreaction)

admin.site.register(Baseprofile)
admin.site.register(BaseFlow)
admin.site.register(BaseProCon)
admin.site.register(BaseReaction)

admin.site.register(Stashprofile)
admin.site.register(StashFlow)
admin.site.register(StashProCon)
admin.site.register(StashReaction)

admin.site.register(Postprofile)
admin.site.register(PostFlow)
admin.site.register(PostReaction)

admin.site.register(Commentbaseprofile)
admin.site.register(CommentBaseFlow)
admin.site.register(CommentBaseReaction)

admin.site.register(Commentstashprofile)
admin.site.register(CommentStashFlow)
admin.site.register(CommentStashReaction)

admin.site.register(Commentpostprofile)
admin.site.register(CommentPostFlow)
admin.site.register(CommentPostReaction)



