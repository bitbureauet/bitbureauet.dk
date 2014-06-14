from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, TemplateView, ListView,
    View
)

from blog import models as blog_models


class Dashboard(TemplateView):
    template_name = 'console/dashboard.html'


class BlogDashboard(ListView):
    queryset = blog_models.Post.objects.all()
    template_name = 'console/blog_dashboard.html'
    context_object_name = 'posts'


class BlogPostMixin:
    model = blog_models.Post
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('console:blog')


class PostCreate(BlogPostMixin, CreateView):
    template_name = 'console/post_form.html'


class PostUpdate(BlogPostMixin, UpdateView):
    template_name = 'console/post_form.html'


class PostPublish(View):

    def dispatch(self, *args, **kwargs):
        pass


