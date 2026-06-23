from django.contrib import admin
from django.contrib import admin
from .models import Funcion

# Register your models here.

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'sala', 'formato', 'fecha', 'hora', 'precio')
    list_filter = ('fecha', 'pelicula')