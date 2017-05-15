from django.contrib import admin
from info.models import Userprofile, Bridge, Baseprofile, Stashprofile, Postprofile, Commentprofile, BaseFlow, BaseProCon, StashFlow, StashProCon, PostFlow, CommentFlow
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Bridge)
admin.site.register(Baseprofile)
admin.site.register(BaseFlow)
admin.site.register(BaseProCon)
admin.site.register(Stashprofile)
admin.site.register(StashFlow)
admin.site.register(StashProCon)
admin.site.register(Postprofile)
admin.site.register(PostFlow)
admin.site.register(Commentprofile)
admin.site.register(CommentFlow)


