from django.conf.urls import include, url
from django.contrib import admin
import played_with_me_web


urlpatterns = [
    # Examples:
    # url(r'^$', 'played_with_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('played_with_me_web.urls', namespace='played_with_me')),
    url(r'^admin/', include(admin.site.urls)),
]
