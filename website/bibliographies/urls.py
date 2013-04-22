from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone
from bibliographies.models import Bibliography

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Bibliography.objects.filter(create_date__lte=timezone.now) \
                .order_by('-create_date')[:5],
            context_object_name='latest_bibliography_list',
            template_name='bibliographies/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            queryset=Bibliography.objects.filter(create_date__lte=timezone.now),
            model=Bibliography,
            template_name='bibliographies/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Bibliography,
            template_name='bibliographies/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'bibliographies.views.vote', name='vote'),
)
