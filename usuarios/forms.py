from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('email', 'telefono', 'fecha_nacimiento')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'email': forms.EmailInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'telefono': forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2'})

class PagoForm(forms.Form):
    titular = forms.CharField(
        label='Nombre del titular',
        widget=forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'placeholder': 'Nombre como figura en la tarjeta'})
    )
    numero = forms.CharField(
        max_length=16, min_length=16,
        label='Número de tarjeta',
        widget=forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'placeholder': '1234567890123456'})
    )
    vencimiento = forms.CharField(
        max_length=5,
        label='Vencimiento',
        widget=forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'placeholder': 'MM/AA'})
    )
    cvv = forms.CharField(
        max_length=4, min_length=3,
        label='CVV',
        widget=forms.TextInput(attrs={'class': 'w-full bg-background border border-borde text-texto rounded-lg px-4 py-2', 'placeholder': '123'})
    )