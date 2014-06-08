from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
   url(r'^$', views.PostList.as_view(), name='post-list'),
   url(r'^(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post-detail'),
   url(r'^(?P<pk>\d+)/edit/$', views.PostUpdate.as_view(), name='post-update'),
   url(r'^new/$', views.PostCreate.as_view(), name='post-create'),
)
