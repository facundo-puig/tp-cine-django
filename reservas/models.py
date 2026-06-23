from django.db import models
from django.conf import settings
from funciones.models import Funcion
from candy.models import Producto

# Create your models here.

class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservas')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='reservas')
    cantidad_entradas = models.PositiveIntegerField(default=1)
    productos = models.ManyToManyField(Producto, through='ReservaProducto', blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.funcion}'
    
    def total(self):
        total_entradas = self.funcion.precio * self.cantidad_entradas
        total_candy = sum(rp.producto.precio * rp.cantidad for rp in self.reservaproducto_set.all())
        return total_entradas + total_candy
    
class ReservaProducto(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.producto} x{self.cantidad}'