from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import FrontPage


urlpatterns = patterns('',

    url(r'',
        include(
            'pages.urls',
            namespace='pages',
            app_name='pages'
        )
    ),

    url(r'^$', FrontPage.as_view()),

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
