from django.conf.urls import include, url
from django.contrib import admin
import web_app


urlpatterns = [
    # Examples:
    # url(r'^$', 'played_with_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('web_app.urls', namespace='web_app')),
    url(r'^admin/', include(admin.site.urls)),
]