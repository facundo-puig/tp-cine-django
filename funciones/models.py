from django.db import models
from peliculas.models import Pelicula
from salas.models import Sala

# Create your models here.

class Funcion(models.Model):
    FORMATOS = [
        ('2d', '2D'),
        ('3d', '3D'),
        ('4d', '4D'),
        ('imax', 'IMAX'),
        ('dbox', 'D-BOX'),
    ]


    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='funciones')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='funciones')
    formato = models.CharField(max_length=10, choices=FORMATOS, default='2d')
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.pelicula} — {self.fecha} {self.hora}'

    class Meta:
        ordering = ['fecha', 'hora']