from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.PageList.as_view(), name='page-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.PageDetail.as_view(), name='page-detail'),
)
