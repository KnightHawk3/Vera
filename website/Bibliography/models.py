from django.db import models
from biblio.webquery import isbndb
from bs4 import BeautifulSoup

# TODO Make this seperate
ISBNDB_KEY = 'N2B2IQ8H'
query = isbndb.IsbndbQuery(ISBNDB_KEY)


class Bibliography(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

    def __unicode__(self):
        return self.owner


class Entry(models.Model):
    bib = models.ForeignKey(Bibliography)
    isbn = models.CharField(default=0)
    detailsHTML = query.query_service("isbn", isbn, '')
    details = BeautifulSoup(detailsHTML)
    title = details.title.string
    author = details.authorstext.string

    def __unicode__(self):
        return self.isbn
