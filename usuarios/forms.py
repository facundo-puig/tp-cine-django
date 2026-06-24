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