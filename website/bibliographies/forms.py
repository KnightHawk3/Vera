from django.forms import ModelForm
from bibliographies.models import Bibliography, Entry


class BibliographyForm(ModelForm):
    class Meta:
        model = Bibliography


class EntryForm(ModelForm):
    class Meta:
        model = Entry
