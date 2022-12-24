from .views import *
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("CrearSubcontrato/", login_required(SubContratos.as_view()), name="subcontratos"),
    path("GuardarSubontrato/", login_required(GuardarSubcontrato.as_view()), name="guardarSubcontrato"),
    path("", login_required(ListarSubcontratos.as_view()), name="listsubcontratos"),
    path("VerSubcontrato/<int:pk>", login_required(VerSubcontrato.as_view()), name="verSubcontrato"),
    path("ModificarSubcontrato/", login_required(ModificarSubcontrato.as_view()), name="modificarSubcontrato"),
    
]




