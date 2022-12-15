from .views import *
from django.urls import path, include

urlpatterns = [
    path("", SubContratos.as_view(), name="subcontratos"),
    path("GuardarSubontrato/", GuardarSubcontrato.as_view(), name="guardarSubcontrato"),
]




