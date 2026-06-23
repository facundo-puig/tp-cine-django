from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'en_stock')
    list_filter = ('categoria', 'en_stock')
    list_editable = ('en_stock', 'precio')