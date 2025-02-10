from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    date = models.DateTimeField(verbose_name="Date de l'événement")
    location = models.CharField(max_length=200, verbose_name="Lieu")
    description = models.TextField(verbose_name="Description")
    link = models.URLField(blank=True, verbose_name="Lien externe")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['date']

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d/%m/%Y')}"

    @property
    def is_past(self):
        return self.date < timezone.now()

class Beer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    subtitle = models.CharField(max_length=200, verbose_name="Sous-titre")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='beers/', verbose_name="Image")
    alcohol_content = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        verbose_name="Degré d'alcool"
    )
    volume = models.IntegerField(verbose_name="Volume (cl)")
    is_available = models.BooleanField(default=True, verbose_name="Disponible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bière"
        verbose_name_plural = "Bières"
        ordering = ['name']

    def __str__(self):
        return self.name
