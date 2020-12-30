from django.urls import path
from .views import (home,galeria,listado_peliculas,
                    nueva_pelicula,modificar_pelicula,
                    eliminar_pelicula,registro_usuario,
                    cambio_contraseña, detalle_peliculas
                    )

urlpatterns = [
    path('',home, name="home" ),
    path('galeria/',galeria, name="galeria"),
    path('listado-peliculas/', listado_peliculas, name = "listado_peliculas"),
    path('nueva-pelicula/', nueva_pelicula, name = "nueva_pelicula"),
    path('modificar-pelicula/<id>/', modificar_pelicula, name = "modificar_pelicula"),
    path('eliminar-pelicula/<id>/', eliminar_pelicula, name = "eliminar_pelicula"),
    path('registro/', registro_usuario, name = "registro_usuario"),
    path('cambio-password/', cambio_contraseña, name = "cambio_contraseña"),
    path('detalle-peliculas/',detalle_peliculas, name = "detalle_peliculas"),
]