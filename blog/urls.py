from django.conf.urls import url, include
from django.contrib import admin
import blog
from blog import views

urlpatterns = [
    url(r'^$', blog.views.home, name='home'),
    url(r'^about/', blog.views.about, name='about'),
    url(r'^contact/', blog.views.contact, name='contact'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', blog.views.show_article, name='article'),
]
