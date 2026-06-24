from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Pelicula
from .forms import PeliculaForm
from promociones.models import Promocion


# Listado de películas
def home(request):
    peliculas = Pelicula.objects.filter(en_cartelera=True)

    hoy = date.today()
    promociones_carousel = Promocion.objects.filter(
        activa=True,
        fecha_inicio__lte=hoy,
        fecha_fin__gte=hoy,
    ).exclude(imagen='')

    return render(request, 'home.html', {
        'peliculas': peliculas,
        'promociones_carousel': promociones_carousel,
    })

# Detalle de película
def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})

# Crear película
@permission_required('peliculas.add_pelicula')
def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/form.html', {'form': form, 'titulo': 'Agregar película'})

# Editar película
@permission_required('peliculas.change_pelicula')
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('detalle_pelicula', pk=pelicula.pk)
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/form.html', {'form': form, 'titulo': 'Editar película'})

# Borrar película
@permission_required('peliculas.delete_pelicula')
def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('home')
    return render(request, 'peliculas/confirmar_eliminar.html', {'pelicula': pelicula})