from django.shortcuts import render
from django.http import HttpResponseRedirect
from bibliographies.forms import BibliographyForm


def add_bibliography(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = BibliographyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # TODO: Have this redirect to a sucess page
            bibliography = form.save(commit=False)
            # Here is where I can set logging
            bibliography.save()
            return HttpResponseRedirect('/')  # Redirect after POST
    else:
        # If they didn't fill out a form display the form
        form = BibliographyForm()

    return render(request, 'bibliographies/add.html', {
        'form': form,
    })
