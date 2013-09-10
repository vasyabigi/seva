from django.conf.urls import patterns, include, url
from django.contrib import admin

from api import v1_api
from technologies.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url('^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
