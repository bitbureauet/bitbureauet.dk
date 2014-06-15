from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import FrontPage, CallEndpoint


urlpatterns = patterns(
    '',

    url(r'^$', FrontPage.as_view()),

    url(
        regex=r'^accounts/',
        view=include('allauth.urls')
    ),

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

    url(r'^call/', CallEndpoint.as_view()),

    url(r'^django_admin/', include(admin.site.urls)),

    url(r'',
        include(
            'pages.urls',
            namespace='pages',
            app_name='pages'
        )
    ),
)
