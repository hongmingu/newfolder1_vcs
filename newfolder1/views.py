from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from title.models import Title, TitleLength
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import HttpResponse, JsonResponse

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


def searched_list(request):
    # query = request.GET.get('q')
    # queryset_list = Title.objects.filter(titleText__contains='q')
    if request.method == 'GET':
        if request.is_ajax():
            q = request.GET['q']
            queryset_list = Title.objects.filter(titleText__contains=q)
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
            # queryset_list = {'hello' : word}
            posts = Title.objects.filter(titleText__contains=word).order_by('titlelength__titleLengthLength')
            queryset_list = {}

            for post in posts:
                queryset_list['name'] = post.titleText
                arr = []
                arr.append('arr1')
                arr.append('arr2')
                queryset_list['arrlist'] = arr
                queryset_list_1 = {}
                queryset_list_1['1'] = queryset_list
                queryset_list_1['2'] = queryset_list
            return JsonResponse(queryset_list_1)

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
