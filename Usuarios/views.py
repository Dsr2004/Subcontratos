from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Subcontratos.correo import enviarCorreo
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
    template_name = "Reset.html"
    def get(self, request, *args, **kwargs):
<<<<<<< HEAD
        return render(request, "Reset.html")

class ManageUser(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ManageUsers.html")
=======
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        correo = request.POST.get("correo")
        if not correo:
            messages.add_message(request, messages.ERROR, 'complete la información e intente nuevamente.')
            return render(request, self.template_name)
        try:
            usuario = Usuario.objects.get(email=correo)
        except:
            messages.add_message(request, messages.ERROR, 'No se encontró un usuario con este correo.')
            return render(request, self.template_name)
        password = Usuario.objects.make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
        usuario.set_password(password)
        usuario.save(update_fields=['password'])
        enviarCorreo("Recuperación Contraseña - EDEMSA", "Correos/restablecerContraseña.html",{"contraseña":password, "usuario":usuario.__str__()},["davitdy2015@gmail.com","juan.gaviria@lambdaanalytics.co"])
   

        messages.add_message(request, messages.INFO, 'Revise su correo electrónico.')
        return render(request, self.template_name)
    
def get(request):
    return render(request, "Correos/restablecerContraseña.html")
        
            
>>>>>>> 86c5c242259ccbc3ba016a53caaedd57ef3e5f78
