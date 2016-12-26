from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, readyness, liveness

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health/ready$', readyness),
    url(r'^health/live$', liveness),
    url(r'^health$', readyness),
    url(r'^admin/', include(admin.site.urls)),
]
