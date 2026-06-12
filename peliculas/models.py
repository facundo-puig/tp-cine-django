from django.db import models

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

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50, choices=GENEROS)
    duracion = models.PositiveIntegerField(help_text='Duración en minutos')
    sinopsis = models.TextField()
    imagen = models.ImageField(upload_to='peliculas/')
    trailer_url = models.URLField(blank=True)
    en_cartelera = models.BooleanField(default=True)
    fecha_estreno = models.DateField()

    def __str__(self):
        return self.titulo