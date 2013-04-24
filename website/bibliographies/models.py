import datetime
from django.db import models
from django.utils import timezone

class Bibliography(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_date < now

    was_created_recently.admin_order_field = 'create_date'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    bibliography = models.ForeignKey(Bibliography)
    title = models.CharField(max_length=100)
    datePublished = models.DateTimeField('date published')
    author = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title
