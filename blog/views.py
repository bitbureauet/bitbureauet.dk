# coding: utf-8

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models


class PostList(ListView):
    queryset = models.Post.objects.filter(published=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = models.Post.objects.all()[:5]
        return context
