from django.conf.urls import patterns, include, url
from django.contrib import admin
from myproject import views
admin.autodiscover()

urlpatterns = patterns('',
    # home page
    url(r'^$', views.home, name='home'),

    # eutilities example
    url(r'^eutils/$', views.eutils, name='eutils'),

    # polls app
    url(r'^polls/', include('polls.urls', namespace="polls")),

    # Admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin app
    url(r'^admin/', include(admin.site.urls)),
)
