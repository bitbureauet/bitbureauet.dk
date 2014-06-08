from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
   url(r'^$', views.PostList.as_view(), name='post-list'),
   url(r'^new/$', views.PostCreate.as_view(), name='post-create'),
   url(r'^(?P<slug>[\w-]+)/$', views.PostDetail.as_view(), name='post-detail'),
   url(r'^(?P<slug>[\w-]+)/edit/$', views.PostUpdate.as_view(), name='post-update'),
)
