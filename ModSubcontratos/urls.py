from .views import *
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(SubContratos.as_view()), name="subcontratos"),
    path("GuardarSubontrato/", login_required(GuardarSubcontrato.as_view()), name="guardarSubcontrato"),
]




