from django.views import generic

from . import models


class PageList(generic.ListView):
    queryset = models.Page.objects.filter(published=True)
    template_name = 'pages/page_list.html'


class PageDetail(generic.DetailView):
    model = models.Page
    template_name = 'pages/page_detail.html'
