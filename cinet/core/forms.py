from django import forms
from django.forms import ModelForm
from .models import Pelicula
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm

class PeliculaForm(ModelForm):

    class Meta:
        model = Pelicula
        fields = ['nombre','duracion','anio','genero'] 

class CustomUserForm(UserCreationForm):
    pass


