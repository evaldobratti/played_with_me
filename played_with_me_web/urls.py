from django.conf.urls import patterns, url

from played_with_me_web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)