from django.shortcuts import render
from .models import Event, Beer
from django.utils import timezone

def index(request):
    upcoming_events = Event.objects.filter(
        is_active=True,
        date__gte=timezone.now()
    ).order_by('date')[:3]
    
    beers = Beer.objects.filter(is_available=True)
    
    context = {
        'upcoming_events': upcoming_events,
        'beers': beers,
    }
    return render(request, 'showcase/index.html', context)
