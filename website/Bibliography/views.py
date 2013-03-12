from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from Bibliography.models import Bibliography


def index(request):
    latest_bib_list = Bibliography.objects.all().order_by('-owner')[:5]
    context = {'latest_bib_list': latest_bib_list}
    return render(request, 'bibliography/index.html', context)


def detail(request, poll_id):
    try:
        bibliography = Bibliography.objects.get(pk=poll_id)
    except Bibliography.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': bibliography})


def results(request, bib_id):
    return HttpResponse("You're looking at the isbn of %s." % bib_id)


def addingEntry(request, bib_id):
    return HttpResponse("You're adding a isbn to %s." % bib_id)
