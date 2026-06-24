from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'genero', 'duracion', 'sinopsis', 'imagen', 'trailer_url', 'en_cartelera', 'fecha_estreno', 'formatos')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'genero': forms.Select(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'duracion': forms.NumberInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'sinopsis': forms.Textarea(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'rows': 4}),
            'trailer_url': forms.URLInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'fecha_estreno': forms.DateInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'type': 'date'}),
            'formatos': forms.CheckboxSelectMultiple(attrs={'class': 'text-texto'}),
        }