from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import Usuario

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label = "Nombre de Usuario",
        widget = forms.TextInput(attrs={"autocomplete":"Vaca", "autofocus": "True","class":"form","id":"inputUsuario","placeholder":"Nombre de usuario", "required":"True"})
    )

    password  = forms.CharField(
        widget = forms.PasswordInput(attrs={"class":"form","placeholder":"Contraseña", "required":"True", "autocomplete":"false"})
    )