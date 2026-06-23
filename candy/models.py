from django.db import models

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = [
        ('pochoclos', 'Pochoclos'),
        ('bebidas', 'Bebidas'),
        ('combos', 'Combos'),
        ('golosinas', 'Golosinas'),
        ('otros', 'Otros'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='candy/', blank=True)
    en_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre