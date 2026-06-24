from datetime import datetime
from peliculas.models import Pelicula

def year_context(request):
    return {'year': datetime.now().year}

def cine_context(request):
    return {
        'nombre_cine': 'Cinedev',
        'peliculas_cartelera': Pelicula.objects.filter(en_cartelera=True)[:5],
    }