"""Subcontratos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from Usuarios.views import Login, ResetPass, ManageUser
from .views import Index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Login/", Login.as_view(), name="login"),
<<<<<<< HEAD
    path("Restablecer/", ResetPass.as_view(), name="restablecer"),
    path("GestionUsuarios/", ManageUser.as_view(), name="manageuser"),
=======
    path("RestablecerContraseña/", ResetPass.as_view(), name="restablecer"),
>>>>>>> 86c5c242259ccbc3ba016a53caaedd57ef3e5f78
    path("Logout/", LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path("", Index.as_view(), name="index"),
    path("Usuarios/", include("Usuarios.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
"""
Como funcionan las urls, el primer parametro que es el string es como se debe escribir en el navegador
para los que tiene  include se debe poner el nombre de la url y luego se pone el del archivo que incluye 
"""