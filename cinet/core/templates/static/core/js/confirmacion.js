function confirmarEliminacion(id){
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podras deshacer esta accion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!'
      }).then((result) => {
        if (result.value) {
          //redirigir al usuario a la ruta de eliminar
            window.location.href = "/eliminar-pelicula/"+id+"/";
        }
      })
}