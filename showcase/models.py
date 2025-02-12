from django.db import models
from django.utils import timezone

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateField()
    lieu = models.CharField(max_length=200)
    description = models.TextField()
    lien_info = models.URLField(blank=True, null=True, verbose_name="Lien pour plus d'informations")
    afficher_lien = models.BooleanField(default=True, verbose_name="Afficher le lien 'Plus d'informations'")
    est_actif = models.BooleanField(default=True)

    class Meta:
        ordering = ['date']
        verbose_name = "Événement"
        verbose_name_plural = "Événements"

    def __str__(self):
        return f"{self.titre} - {self.date.strftime('%d/%m/%Y')}"

class Biere(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    histoire = models.TextField(help_text="L'histoire derrière cette bière")
    type = models.CharField(max_length=100)
    degre = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Degré d'alcool")
    ibu = models.IntegerField(verbose_name="IBU (International Bitterness Units)", help_text="Indice d'amertume")
    volume = models.IntegerField(help_text="Volume en cl")
    est_disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='bieres/')
    ordre_affichage = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre_affichage']
        verbose_name = "Bière"
        verbose_name_plural = "Bières"

    def __str__(self):
        return f"{self.nom} - {self.type}"

class PointDeVente(models.Model):
    TYPE_CHOICES = [
        ('BAR', 'Bar'),
        ('CAVE', 'Cave à bières'),
        ('SHOP', 'Boutique'),
        ('AUTRE', 'Autre'),
    ]
    
    nom = models.CharField(max_length=100, verbose_name="Nom de l'établissement")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='BAR')
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=100)
    horaires = models.TextField(blank=True, null=True, help_text="Horaires d'ouverture")
    lien = models.URLField(blank=True, null=True, verbose_name="Lien vers le site web")
    actif = models.BooleanField(default=True)
    ordre = models.IntegerField(default=0, help_text="Ordre d'affichage")
    
    class Meta:
        verbose_name = "Point de vente"
        verbose_name_plural = "Points de vente"
        ordering = ['ordre', 'nom']
    
    def __str__(self):
        return f"{self.nom} ({self.ville})"
