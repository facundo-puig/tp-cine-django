from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Pelicula(models.Model):
    GENEROS = [
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('animacion', 'Animación'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
    ]

    FORMATOS = [
        ('2d', '2D'),
        ('3d', '3D'),
        ('4d', '4D'),
        ('imax', 'IMAX'),
        ('dbox', 'D-BOX'),
    ]

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50, choices=GENEROS)
    duracion = models.PositiveIntegerField(help_text='Duración en minutos')
    sinopsis = models.TextField()
    imagen = models.ImageField(upload_to='peliculas/')
    trailer_url = models.URLField(blank=True)
    en_cartelera = models.BooleanField(default=True)
    fecha_estreno = models.DateField()
    formatos = MultiSelectField(choices=FORMATOS, blank=True)

    def __str__(self):
        return self.titulo