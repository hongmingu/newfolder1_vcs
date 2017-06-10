from django.contrib import admin
from title.models import Title, TitleLength, TitleText
# Register your models here.

admin.site.register(Title)
admin.site.register(TitleLength)
admin.site.register(TitleText)