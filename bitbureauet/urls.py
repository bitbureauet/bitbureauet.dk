from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    url(r'^blog/',
        include(
            'blog.urls',
            namespace='blog',
            app_name='blog'
        )
    ),

    url(r'^console/',
        include(
            'console.urls',
            namespace='console',
            app_name='console'
        )
    ),

    url(r'^django_admin/', include(admin.site.urls)),
)