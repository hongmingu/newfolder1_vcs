from django.contrib import admin
from info.models import Userprofile, Bridge, Userreaction, Baseprofile, Stashprofile, Postprofile, Commentbaseprofile, Commentstashprofile, Commentpostprofile, BaseFlow, BaseProCon, StashFlow, StashProCon, PostFlow, CommentBaseFlow, CommentStashFlow, CommentPostFlow
# Register your models here.

admin.site.register(Userprofile)
admin.site.register(Bridge)
admin.site.register(Userreaction)

admin.site.register(Baseprofile)
admin.site.register(BaseFlow)
admin.site.register(BaseProCon)

admin.site.register(Stashprofile)
admin.site.register(StashFlow)
admin.site.register(StashProCon)

admin.site.register(Postprofile)
admin.site.register(PostFlow)

admin.site.register(Commentbaseprofile)
admin.site.register(CommentBaseFlow)

admin.site.register(Commentstashprofile)
admin.site.register(CommentStashFlow)

admin.site.register(Commentpostprofile)
admin.site.register(CommentPostFlow)



