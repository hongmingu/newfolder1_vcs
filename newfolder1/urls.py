"""newfolder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^title/', include('post.urls', namespace='title')),
    url(r'^base/', include('base.urls', namespace='base')),
    url(r'^stash/', include('stash.urls', namespace='stash')),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^comment/', include('comment.urls', namespace='comment')),
    url(r'^info/', include('info.urls', namespace='info')),
    # url(r'^$', TemplateView.as_view(template_name='base.html'))

    #############################################################################
    url(r'^$', views.AjaxListView.as_view(), name='for_base'),
    url(r'^searched_list/$', views.searched_list, name='searched_list'),
    url(r'^tutomain/$', TemplateView.as_view(template_name='tutobase.html')),
    url(r'^tutomain/ajax/$', views.tutomainajax, name='tutomainAjax'),
    url(r'^tutomain/ajax/side/$', views.tutomainside, name='tutomainAjaxSide'),
    url(r'^tutomain/detail/(?P<pk>\d+)/$', views.tutodetail, name="tutoDetail"),
    url(r'^tutomain/search/$', views.search, name="tutoSearch"),

    #############################################################################

]
