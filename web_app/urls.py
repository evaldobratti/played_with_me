from django.conf.urls import patterns, url

from web_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('^matches/(?P<match_id>\d+)/$', views.match_detail, name='match_details'),
    url('^players/(?P<player_id>\d+)/$', views.player_detail, name='player_details'),
    url('^friends/(?P<players>(\d+/){2,})$', views.friends_detail, name='friends_detail'),

)