from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Promocion
from .forms import PromocionForm

# Create your views here.

# Listado de promociones
def listado_promociones(request):
    promociones = Promocion.objects.filter(activa=True)
    return render(request, 'promociones/listado.html', {'promociones': promociones})

# Detalle de promoción
def detalle_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    return render(request, 'promociones/detalle.html', {'promocion': promocion})

# Crear promoción
@permission_required('promociones.add_promocion')
def crear_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listado_promociones')
    else:
        form = PromocionForm()
    return render(request, 'promociones/form.html', {'form': form, 'titulo': 'Agregar promoción'})

# Editar promoción
@permission_required('promociones.change_promocion')
def editar_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('detalle_promocion', pk=promocion.pk)
    else:
        form = PromocionForm(instance=promocion)
    return render(request, 'promociones/form.html', {'form': form, 'titulo': 'Editar promoción'})

# Eliminar promoción
@permission_required('promociones.delete_promocion')
def eliminar_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    if request.method == 'POST':
        promocion.delete()
        return redirect('listado_promociones')
    return render(request, 'promociones/confirmar_eliminar.html', {'promocion': promocion})