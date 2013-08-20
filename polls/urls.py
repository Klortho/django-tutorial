from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',

    # These use "generic views".  See
    # https://docs.djangoproject.com/en/1.3/topics/class-based-views/

    # Polls home
    url(r'^$', views.IndexView.as_view(), name='index'),

    # E.g.: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    # E.g.: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),

    # E.g.: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
