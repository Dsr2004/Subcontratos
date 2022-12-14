from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required



urlpatterns = [
      path("ListarUsuarios/", login_required(ListarUsuarios.as_view()), name="manageuser"),
      path("CrearUsuario/", login_required(CrearUsuario.as_view()), name="crearUsuario"),
      path("ModificarUsuario/<int:pk>", login_required(ModificarUsuario.as_view()), name="modificarUsuario"),
      path("ModificarEstadoUsuario/", login_required(ModificarEstadoUsuario.as_view()), name="modificarEstadoUsuario"),
      path("CambiarContrasena/", login_required(CambiarContrasena.as_view()), name="cambiarContrasena"),

      path("MiCuenta/<int:pk>", login_required(MiCuenta.as_view()), name="miCuenta"),
]