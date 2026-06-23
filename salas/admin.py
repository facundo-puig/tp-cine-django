from django.contrib import admin
from .models import Sala, Asiento

# Register your models here.

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre', 'tipo', 'capacidad')
    list_filter = ('tipo',)