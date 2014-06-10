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


class PostCreate(CreateView):
    model = blog_models.Post
    template_name = 'console/post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('console:blog')


class PostUpdate(UpdateView):
    model = blog_models.Post
    template_name = 'console/post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('console:blog')


class PostPublish(View):

    def dispatch(self, *args, **kwargs):
        pass


