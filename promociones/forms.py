from django import forms
from .models import Promocion

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ('titulo', 'descripcion', 'imagen', 'descuento', 'fecha_inicio', 'fecha_fin', 'activa')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'rows': 4}),
            'descuento': forms.NumberInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'type': 'date'}),
        }