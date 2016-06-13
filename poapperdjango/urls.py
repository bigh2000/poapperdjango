"""poapperdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.show_main'),
    url(r'^(?P<pk>\d+)/$', 'main.views.post_detail'),
    url(r'^(?P<pk>\d+)/comments/new/$', 'main.views.comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'main.views.comment_edit'),
    url(r'^info/$', 'info.views.show_main'),
    url(r'^info/(?P<pk>\d+)/$', 'info.views.post_detail'),
    url(r'^qna/$', 'qna.views.show_main'),
    url(r'^qna/(?P<pk>\d+)/$', 'qna.views.post_detail'),
    url(r'^scratch/$', 'scratch.views.show_main'),
    url(r'^scratch/(?P<pk>\d+)/$', 'scratch.views.post_detail'),
]
