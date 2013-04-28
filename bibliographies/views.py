from django.shortcuts import render
from django.http import HttpResponseRedirect
from bibliographies.forms import BibliographyForm
from django.contrib.auth import logout


def add_bibliography(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    print request.user
    if request.method == 'POST':  # If the form has been submitted...
        form = BibliographyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # TODO: Have this redirect to a sucess page
            bibliography = form.save(commit=False)
            # Here is where I can set logging
            bibliography.save()
            if request.user.is_authenticated():
                return HttpResponseRedirect('/')  # Redirect after POST
            else:
                return HttpResponseRedirect('/add')

    else:
        # If they didn't fill out a form display the form
        form = BibliographyForm()

    return render(request, 'bibliographies/add.html', {
        'form': form,
    })

def login_or_logout(request):
    if not request.user.is_authenticated():
        return render(request, 'bibliographies/login.html')
    else:
        logout(request)
        return HttpResponseRedirect('/')
