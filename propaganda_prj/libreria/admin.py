from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from .models import Autori, Editori, Generi, Libri


@admin.register(Libri)
class LibriAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'autore', 'editore', 'isbn', 'prezzo', 'disponibile', ]
    list_filter = ("autore", "editore", )
    search_fields = ("titolo", )

    
    actions = ["segna_come_indisponibile"]
    def segna_come_indisponibile(request, queryset):
        queryset.update(disponibile = False)
        


@admin.register(Editori)
class EditoriAdmin(admin.ModelAdmin):
    list_display = ['societa',]

    
admin.site.register(Autori)
admin.site.register(Generi)




