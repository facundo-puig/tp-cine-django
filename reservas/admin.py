from django.contrib import admin
from .models import Reserva, ReservaProducto

# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'funcion', 'cantidad_entradas', 'estado', 'fecha_creacion')
    list_filter = ('estado',)