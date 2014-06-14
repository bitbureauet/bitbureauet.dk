from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, TemplateView, ListView,
    View
)
from django.contrib.flatpages.models import FlatPage

from blog import models as blog_models
from pages import models as page_models



class Dashboard(TemplateView):
    template_name = 'console/dashboard.html'


class BlogDashboard(ListView):
    queryset = blog_models.Post.objects.all()
    template_name = 'console/blog_dashboard.html'
    context_object_name = 'posts'


class BlogPostEditMixin:
    model = blog_models.Post
    context_object_name = 'post'
    template_name = 'console/post_form.html'

    def get_success_url(self):
        return reverse('console:blog')


class PostCreate(BlogPostEditMixin, CreateView):
    pass


class PostUpdate(BlogPostEditMixin, UpdateView):
    pass


class PagesDashboard(ListView):
    queryset = page_models.Page.objects.all()
    template_name = 'console/pages_dashboard.html'
    context_object_name = 'pages'


class PageEditMixin:
    model = page_models.Page
    context_object_name = 'page'
    template_name = 'console/page_form.html'

    def get_success_url(self):
        return reverse('console:pages')


class PageCreate(PageEditMixin, CreateView):
    pass


class PageUpdate(PageEditMixin, UpdateView):
    pass
