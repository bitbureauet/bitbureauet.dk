from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
    '',

    # Blog posts
    url(r'^blog/$', views.BlogDashboard.as_view(), name='blog'),
    url(r'^blog/new/$', views.PostCreate.as_view(), name='post-create'),
    url(r'^blog/(?P<slug>[\w-]+)/edit/$', views.PostUpdate.as_view(), name='post-update'),

    # Flatpages
    url(r'^pages/new/$', views.PageCreate.as_view(), name='page-create'),
    url(r'^pages/(?P<slug>[\w-]+)/edit/$', views.PageUpdate.as_view(), name='page-update'),
    url(r'^pages/$', views.PagesDashboard.as_view(), name='pages'),

    # Admin dashboard
    url(r'$', views.Dashboard.as_view(), name='dashboard'),
)