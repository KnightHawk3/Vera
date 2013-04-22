from django.contrib import admin
from bibliographies.models import Entry, Bibliography


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1


class BibliographyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
    ]
    inlines = [EntryInline]
    list_display = ('name', 'create_date', 'was_created_recently')
    list_filter = ['create_date']
    search_fields = ['title']
    date_hierarchy = 'create_date'

admin.site.register(Bibliography, BibliographyAdmin)
