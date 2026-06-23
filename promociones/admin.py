from django.contrib import admin
from .models import Promocion

# Register your models here.

@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descuento', 'fecha_inicio', 'fecha_fin', 'activa')
    list_filter = ('activa',)
    list_editable = ('activa',)