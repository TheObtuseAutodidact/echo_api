from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<echo>(.*)+)/$', views.post, name='post')
    # url(r'^$', views.detail, name='detail'),
]
