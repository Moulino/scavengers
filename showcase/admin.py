from django.contrib import admin
from django.utils.html import format_html
from .models import Evenement, Biere, PointDeVente

@admin.register(Biere)
class BiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'degre', 'volume', 'est_disponible')
    list_filter = ('est_disponible', 'type')
    search_fields = ('nom', 'description')
    ordering = ('ordre_affichage',)

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'lieu', 'est_actif')
    list_filter = ('est_actif', 'date')
    search_fields = ('titre', 'lieu', 'description')
    date_hierarchy = 'date'

@admin.register(PointDeVente)
class PointDeVenteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'ville', 'actif')
    list_filter = ('type', 'actif', 'ville')
    search_fields = ('nom', 'ville', 'adresse')
    ordering = ('ordre', 'nom')
    list_editable = ('actif',)
