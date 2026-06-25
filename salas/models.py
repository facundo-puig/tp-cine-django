from django.db import models

class Sala(models.Model):
    TIPOS = [
        ('estandar', 'Estándar'),
        ('4d', '4D'),
        ('imax', 'IMAX'),
        ('dbox', 'D-BOX'),
        ('premium', 'Premium'),
    ]

    numero = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100, blank=True, help_text='Ej: Sala IMAX 1')
    tipo = models.CharField(max_length=50, choices=TIPOS, default='estandar')
    capacidad = models.PositiveIntegerField(editable=False, default=0)
    filas = models.PositiveIntegerField(default=5)
    columnas = models.PositiveIntegerField(default=10)

    def save(self, *args, **kwargs):
        self.capacidad = self.filas * self.columnas
        super().save(*args, **kwargs)
        if not self.asientos.exists():
            letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(self.filas):
                for numero in range(1, self.columnas + 1):
                    Asiento.objects.create(sala=self, fila=letras[i], numero=numero)

    def __str__(self):
        return f'Sala {self.numero} — {self.get_tipo_display()}'


class Asiento(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='asientos')
    fila = models.CharField(max_length=5, help_text='Ej: A, B, C')
    numero = models.PositiveIntegerField()

    class Meta:
        unique_together = ('sala', 'fila', 'numero')
        ordering = ['fila', 'numero']

    def __str__(self):
        return f'{self.sala} - {self.fila}{self.numero}'