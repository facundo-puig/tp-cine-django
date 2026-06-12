from django.contrib import admin
from .models import Pelicula

# Register your models here.

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'duracion', 'fecha_estreno', 'en_cartelera')
    list_filter = ('genero', 'en_cartelera')
    search_fields = ('titulo',)
    list_editable = ('en_cartelera',)