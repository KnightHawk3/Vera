from django.contrib import admin
from Bibliography.models import Bibliography, Entry


class EntriesInLine(admin.StackedInline):
    model = Entry
    extra = 3


class BibAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['owner']}),
    ]
    inlines = [EntriesInLine]

admin.site.register(Bibliography, BibAdmin)
