from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from title.models import Title, TitleLength
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json

def tutodetail(request, pk):

    if request.method == "POST":
        if request.is_ajax():
            matched_list = Title.objects.all()
            hello = list(matched_list.values('titleText'))
            good = request.user.pk

            context = {'posts' : matched_list,}

            dodo = {"user":good}
            return render(request, '_base.html', context)

    return JsonResponse({'hello' : 'baby'})
####################################################################################

def search(request):
    if request.method == 'GET':
        if request.is_ajax():
            q = request.GET['q']
            matched_list = Title.objects.all()
            hello = list(matched_list.values("pk", 'titleText'))
            context = {'posts' : matched_list,}
            return render(request, '_base.html', context)

            # return JsonResponse(hello, safe=False)

    return JsonResponse({'hello' : 'baby'})


####################################################################################

def searched_list(request):
    # query = request.GET.get('q')
    # queryset_list = Title.objects.filter(titleText__contains='q')
    if request.method == 'GET':
        if request.is_ajax():
            q = request.GET['q']
            matched_list = Title.objects.filter(titleText__contains=q)
            queryset_list = {}
            for title in matched_list :
                title.titleText

            return JsonResponse(queryset_list)

    if request.method == 'POST' and 'start_manifest' in request.POST:
        queryset_list = Title.objects.filter(titleText__contains='1')

    if request.method == 'POST' and 'close_manifest' in request.POST:
        queryset_list = Title.objects.filter(titleText__contains='2')

    context = {
        'title': queryset_list,
    }

    return render(request, 'searched_list.html', context)

def tutomainajax(request):
    if request.method == 'GET':
        if request.is_ajax():

            word = request.GET['word']
            word = word.replace(' ', '').lower()
            queryset_list = {'hello1' : 'world1', 'hello2' : 'world2', 'hello3' : ['world3', 'second_world3']}
            # posts = Title.objects.filter(titleText__contains=word).order_by('titlelength__titleLengthLength')
            # queryset_list = {}

            # for post in posts:
            #     queryset_list['name'] = post.titleText
                # arr = []
                # arr.append('arr1')
                # arr.append('arr2')
                # queryset_list['arrlist'] = arr
                # queryset_list_1 = {}
                # queryset_list_1['name1'] = queryset_list
                # queryset_list_1['name2'] = queryset_list
            return JsonResponse(queryset_list)

    return HttpResponse

######################################

def tutomainside(request):
    if request.method == 'POST':
        if request.is_ajax():

            posts = Title.objects.all()
            queryset_list = {'posts' : posts}
            return render(request, '_base.html', queryset_list)

    return HttpResponse

######################################
'''

'''

class AjaxListView(ListView):
    model = Title
    template_name = 'base.html'
    context_object_name = 'title_list'
    paginate_by = 2

    def get_template_names(self):
        if self.request.is_ajax():
            html = "<html><body>It is now</body></html>"
            return HttpResponse(html)


            # return ['_base.html']
        # return super(AjaxListView, self).get_template_names()
        return super(AjaxListView, self).get_template_names()

# post_list = AjaxListView.as_view(model=Title, template_name='base.html', context_object_name='title_list', paginate_by=2)
        # Create your views here.
'''
####################################################################################

def search(request):
    if request.method == 'GET':
        if request.is_ajax():
            q = request.GET['q']
            matched_list = Title.objects.order_by('titleUpdatedAt')
            # fordata = serializers.serialize('json', matched_list,)
            hello = list(matched_list.values('titleUpdatedAt'))
            keys = []
            druid = 0
            name = 'data '
            for index in range(len(hello)):
                # druid = druid + 1
                index = index + 1
                name = name + str(index)
                keys.append(name)
                name = 'data '

            dictionary = dict(zip(keys, hello))

            # serialized_q = json.dumps(list(matched_list.values()), cls=DjangoJSONEncoder)
            # queryset_list = {}
            # result = matched_list.values()  # return ValuesQuerySet object
            # for hello in result:
            #     queryset_list[hello] = result
            # list_result = [hello for hello in result] # converts ValuesQuerySet into Python list
            # number = 0
            # for title in matched_list :
            #     number += number
            #     queryset_list['title'] = title.titleText
            #     queryset_list['created'] = title.titleCreatedAt

            # queryset_list = {'hello1': 'world1', 'hello2': 'world2', 'hello3': ['world3', 'second_world3']}
            #

            return JsonResponse(hello, safe=False)

    return JsonResponse({'hello' : 'baby'})
'''