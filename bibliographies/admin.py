from django.contrib import admin
from bibliographies.models import Entry, Bibliography


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1


class BibliographyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [EntryInline]
    list_display = ('name', 'was_created_recently')
    search_fields = ['title']

admin.site.register(Bibliography, BibliographyAdmin)
