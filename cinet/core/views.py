from django.shortcuts import render , redirect
from .models import Pelicula
from .forms import PeliculaForm , CustomUserForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def galeria(request):
    return render(request,'core/galeria.html')

def listado_peliculas(request):
    peliculas = Pelicula.objects.all()
    data = {
        'Peliculas' : peliculas
    }
    return render(request,'core/listado_peliculas.html', data)

@login_required
def nueva_pelicula(request):
    data = {
        'form' : PeliculaForm()
    }

    if request.method == 'POST':
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente!"
    return render(request,'core/nueva_pelicula.html', data)

def modificar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id = id)
    data = {
        'form' : PeliculaForm(instance=pelicula)
    }

    if request.method == 'POST':
        formulario = PeliculaForm(data = request.POST, instance= pelicula)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente!"
            data['form'] = formulario
    return render(request,'core/modificar_pelicula.html',data)

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id = id)
    pelicula.delete()

    return redirect(to="listado_peliculas")

def registro_usuario(request):
    data = {
        'form' : CustomUserForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigir al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect("home")

    return render(request,'registration/registrar.html',data)

def cambio_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to = "home" )
    else:
        form = PasswordChangeForm(user=request.user)

    data = {'form' : form }
    return render(request,'registration/cambio_password.html',data)


def detalle_peliculas(request):
    peliculas = Pelicula.objects.all()
    data = {
        'Peliculas' : peliculas
    }
    return render(request,'core/detalle_peliculas.html',data)