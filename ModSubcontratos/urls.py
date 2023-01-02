from .views import *
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("BusquedaInfoSubcontrato/", login_required(BusquedaInfoSubcontrato.as_view()), name="busquedaInfoSubcontrato"),
    path("CrearSubcontrato/", login_required(SubContratos.as_view()), name="subcontratos"),
    path("GuardarSubontrato/", login_required(GuardarSubcontrato.as_view()), name="guardarSubcontrato"),
    path("", login_required(ListarSubcontratos.as_view()), name="listsubcontratos"),
    path("VerSubcontrato/<int:pk>", login_required(VerSubcontrato.as_view()), name="verSubcontrato"),
    path("ModificarSubcontrato/<int:pk>", login_required(ModificarSubcontrato.as_view()), name="modificarSubcontrato"),
    path("VerSeguimientoActa/<int:pk>", login_required(VerSeguimientoActa.as_view()), name="verSeguimientoActa"),
    path("cargarExcelSubcontratos/", login_required(excelSubcontratos.as_view()), name="excelSubcontratos"),
]




