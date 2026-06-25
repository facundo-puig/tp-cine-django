from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from funciones.models import Funcion
from candy.models import Producto
from salas.models import Asiento
from usuarios.forms import PagoForm
from .models import Reserva, ReservaProducto
import json
from promociones.models import Promocion
from datetime import date

@login_required
def seleccionar_asientos(request, funcion_pk):
    funcion = get_object_or_404(Funcion, pk=funcion_pk)
    asientos = funcion.sala.asientos.all()
    
    # Asientos ya reservados para esta función
    asientos_ocupados = Asiento.objects.filter(
        reserva__funcion=funcion,
        reserva__estado__in=['pendiente', 'confirmada']
    ).values_list('pk', flat=True)

    return render(request, 'reservas/seleccionar_asientos.html', {
        'funcion': funcion,
        'asientos': asientos,
        'asientos_ocupados': list(asientos_ocupados),
    })

@login_required
def seleccionar_candy(request):
    if request.method != 'POST':
        return redirect('home')

    funcion_id = request.POST.get('funcion_id')
    asientos_ids = request.POST.getlist('asientos')

    if not asientos_ids:
        return redirect('home')

    request.session['funcion_id'] = funcion_id
    request.session['asientos_ids'] = asientos_ids

    productos = Producto.objects.filter(en_stock=True).order_by('categoria')
    precios_json = json.dumps({str(p.pk): p.precio for p in productos})

    return render(request, 'reservas/seleccionar_candy.html', {
        'productos': productos,
        'funcion_id': funcion_id,
        'asientos_ids': asientos_ids,
        'precios_json': precios_json,
    })

@login_required
def confirmar_reserva(request):
    if request.method != 'POST':
        return redirect('home')

    funcion_id = request.POST.get('funcion_id')
    asientos_ids = request.POST.getlist('asientos')
    funcion = get_object_or_404(Funcion, pk=funcion_id)
    asientos = Asiento.objects.filter(pk__in=asientos_ids)

    productos_seleccionados = []
    for producto in Producto.objects.filter(en_stock=True):
        cantidad = int(request.POST.get(f'producto_{producto.pk}', 0))
        if cantidad > 0:
            productos_seleccionados.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': producto.precio * cantidad,
            })

    # Buscar promoción activa para la fecha de la función
    hoy = date.today()
    promocion = Promocion.objects.filter(
        activa=True,
        fecha_inicio__lte=hoy,
        fecha_fin__gte=hoy,
    ).first()

    total_entradas = funcion.precio * len(asientos_ids)

    # Aplicar descuento solo a entradas
    descuento_entradas = 0
    total_entradas_con_descuento = total_entradas
    if promocion:
        descuento_entradas = (total_entradas * promocion.descuento) // 100
        total_entradas_con_descuento = total_entradas - descuento_entradas

    total_candy = sum(p['subtotal'] for p in productos_seleccionados)
    total = total_entradas_con_descuento + total_candy

    pago_form = PagoForm(request.POST if request.POST.get('confirmar') else None)

    if request.POST.get('confirmar'):
        if pago_form.is_valid():
            reserva = Reserva.objects.create(
                usuario=request.user,
                funcion=funcion,
                cantidad_entradas=len(asientos_ids),
                estado='confirmada',
            )
            reserva.asientos.set(asientos)
            for item in productos_seleccionados:
                ReservaProducto.objects.create(
                    reserva=reserva,
                    producto=item['producto'],
                    cantidad=item['cantidad'],
                )
            return redirect('mis_reservas')

    return render(request, 'reservas/confirmar_reserva.html', {
        'funcion': funcion,
        'asientos': asientos,
        'productos_seleccionados': productos_seleccionados,
        'total_entradas': total_entradas,
        'descuento_entradas': descuento_entradas,
        'total_entradas_con_descuento': total_entradas_con_descuento,
        'total_candy': total_candy,
        'total': total,
        'promocion': promocion,
        'asientos_ids': asientos_ids,
        'funcion_id': funcion_id,
        'pago_form': pago_form or PagoForm(),
    })

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})