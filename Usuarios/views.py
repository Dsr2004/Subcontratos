from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
from .models import Usuario

class Login(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, self.template_name, {"form": self.form_class})
    
    def post(self, request, *args, **kwargs):
        context={}
        form = LoginForm(request,data=request.POST) #con esto se le pasan los datos al formulario, inserción
        context["form"]=form
        if form.is_valid():
            nombre = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre, password = contrasena)
            if usuario is not None:
                if usuario.estado == 1:
                    login(request, usuario)
                    if 'next' in request.GET:
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect("manageuser")
                else: 
                    context['error']="Este usuario se encuentra inhabilitado"
        else:
            try:
                Usuario.objects.get(usuario=form.cleaned_data.get('username'))
                context['error']="La contraseña es incorrecta"
            except:
                context['error']="El usuario ingresado no existe"
        return render(request, self.template_name, context)

def logout(request):
    logout(request)

class ResetPass(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Reset.html")

class ManageUser(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ManageUsers.html")
