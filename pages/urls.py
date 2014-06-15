from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', views.PageDetail.as_view(), name='page-detail'),
)
