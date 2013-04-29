from django.conf.urls import patterns, url
from django.views.generic import DetailView, TemplateView
from bibliographies.models import Bibliography

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='bibliographies/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Bibliography,
            template_name='bibliographies/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Bibliography,
            template_name='bibliographies/results.html'),
        name='results'),
    url(r'^login/$', 'bibliographies.views.login_or_logout', name='login'),
    url(r'add/$', 'bibliographies.views.add_bibliography', name='add_bibliography'),
)
