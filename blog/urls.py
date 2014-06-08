from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
   url(r'^$', views.PostList.as_view(), name='post-list'),
   url(r'^(?P<slug>[\w-]+)/$', views.PostDetail.as_view(), name='post-detail'),
)
