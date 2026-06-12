from django.shortcuts import render, get_object_or_404
from .models import Pelicula

# Create your views here.

def home(request):
    peliculas = Pelicula.objects.filter(en_cartelera=True)
    return render(request, 'home.html', {'peliculas': peliculas})

def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})

