from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('xivinsight.core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
