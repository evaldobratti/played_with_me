from django.conf.urls import patterns, url

from web_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('^match/(?P<match_id>\d+)/$', views.match_details, name='match_details')
)