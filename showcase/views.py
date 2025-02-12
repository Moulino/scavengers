from django.shortcuts import render
from django.utils import timezone
from .models import Biere, Evenement, PointDeVente
from datetime import date

def index(request):
    evenements = Evenement.objects.filter(
        est_actif=True,
        date__gte=date.today()
    ).order_by('date')[:3]  # Limite aux 3 prochains événements
    
    bieres = Biere.objects.filter(est_disponible=True)
    
    points_vente = PointDeVente.objects.filter(actif=True)
    
    context = {
        'evenements': evenements,
        'bieres': bieres,
        'points_vente': points_vente,
    }
    return render(request, 'showcase/index.html', context)
