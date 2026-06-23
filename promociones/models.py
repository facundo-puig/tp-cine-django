from django.db import models

# Create your models here.

class Promocion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='promociones/', blank=True)
    descuento = models.PositiveIntegerField(help_text='Porcentaje de descuento, ej: 20')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
