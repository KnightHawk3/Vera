from django.conf.urls import patterns, url

from Bibliography import views

urlpatterns = patterns('',
                       # ex: /Bibliography/
                       url(r'^$', views.index, name='index'),
                       # ex: /Bibliography/5/
                       url(r'^(?P<bib_id>\d+)/$', views.detail, name='detail'),
                       # ex: /Bibliography/5/results/
                       url(r'^(?P<bib_id>\d+)/results/$', views.results, name='results'),
                       # ex: /Bibliography/5/vote/
                       url(r'^(?P<bib_id>\d+)/vote/$', views.addingEntry, name='vote'),
                       )
