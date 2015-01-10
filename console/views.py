from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, UpdateView, TemplateView, ListView,
    View)

from blog import models as blog_models
from pages import models as page_models

from core import models as core_models
from core import mixins


class Dashboard(mixins.LoginRequiredMixin, TemplateView):
    template_name = 'console/dashboard.html'


class BlogDashboard(mixins.LoginRequiredMixin, ListView):
    queryset = blog_models.Post.objects.all()
    template_name = 'console/blog_dashboard.html'
    context_object_name = 'posts'


class BlogPostEditMixin:
    model = blog_models.Post
    context_object_name = 'post'
    template_name = 'console/post_form.html'

    def get_success_url(self):
        return reverse('console:blog')

    def form_valid(self, form):
        form.save()
        form.instance.edited_by.add(self.request.user)

        return super().form_valid(form)


class PostCreate(mixins.LoginRequiredMixin, BlogPostEditMixin, CreateView):
    pass


class PostUpdate(mixins.LoginRequiredMixin, BlogPostEditMixin, UpdateView):
    pass


class PagesDashboard(mixins.LoginRequiredMixin, ListView):
    queryset = page_models.Page.objects.all()
    template_name = 'console/pages_dashboard.html'
    context_object_name = 'pages'


class PageEditMixin:
    model = page_models.Page
    context_object_name = 'page'
    template_name = 'console/page_form.html'

    def get_success_url(self):
        return reverse('console:pages')


class PageCreate(mixins.LoginRequiredMixin, PageEditMixin, CreateView):
    pass


class PageUpdate(mixins.LoginRequiredMixin, PageEditMixin, UpdateView):
    pass


class PhoneNumbersList(ListView):
    queryset = core_models.Profile.objects.filter(
        phone_number__isnull=False).order_by('user__username')
    template_name = 'console/phonenumber_dashboard.html'
    context_object_name = 'profiles'


class PhoneNumbersActivate(View):

    def dispatch(self, request, *args, number, **kwargs):
        self.number = number
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        profile = core_models.Profile.objects.get(phone_number=self.number)
        profile.put_on_call()
        return redirect('console:phone-numbers')

