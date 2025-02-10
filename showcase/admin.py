from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Beer

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_active', 'is_past', 'created_at')
    list_filter = ('is_active', 'date')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'
    ordering = ('-date',)
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('title', 'date', 'location', 'description')
        }),
        ('Options', {
            'fields': ('link', 'is_active'),
            'classes': ('collapse',)
        }),
    )

    def is_past(self, obj):
        return obj.is_past
    is_past.boolean = True
    is_past.short_description = "Événement passé"

@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_image', 'alcohol_content', 'volume', 'is_available')
    list_filter = ('is_available', 'alcohol_content')
    search_fields = ('name', 'description')
    ordering = ('name',)

    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'subtitle', 'description')
        }),
        ('Caractéristiques', {
            'fields': ('alcohol_content', 'volume', 'image')
        }),
        ('Options', {
            'fields': ('is_available',),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;" />',
                obj.image.url
            )
        return "Pas d'image"
    display_image.short_description = "Image"
