from django.conf.urls import patterns, url

from web_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('^matches/(?P<match_id>\d+)/$', views.match_details, name='match_details'),
    url('^players/(?P<player_id>\d+)/$', views.match_details, name='match_details')
)