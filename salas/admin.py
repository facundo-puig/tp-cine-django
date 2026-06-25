from django.contrib import admin
from .models import Sala

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre', 'tipo', 'filas', 'columnas', 'capacidad')
    list_filter = ('tipo',)