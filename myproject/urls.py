from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # polls app
    url(r'^polls/', include('polls.urls', namespace="polls")),

    # Admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin app
    url(r'^admin/', include(admin.site.urls)),
)
