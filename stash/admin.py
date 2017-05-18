from django.contrib import admin
from stash.models import Stash, StashImage, StashUrl
# Register your models here.

admin.site.register(Stash)
admin.site.register(StashImage)
admin.site.register(StashUrl)