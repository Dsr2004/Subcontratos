import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import View, ListView, CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from Subcontratos.correo import enviarCorreo
from .forms import LoginForm, UsuarioForm, CambiarContrasena
from .models import Usuario
from django.contrib.auth.models import  Group



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

class ResetPass(View):
    template_name = "restablecerContraseña.html"
    
    def get(self, request, *args, **kwargs):
        ctx = {"usuarios":Usuario.objects.all()}
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        correo = request.POST.get("correo")
        print(correo)
        if not correo:
            messages.add_message(request, messages.ERROR, 'complete la información e intente nuevamente.')
            return render(request, self.template_name)
        try:
            usuario = Usuario.objects.get(correo=correo)
        except:
            messages.add_message(request, messages.ERROR, 'No se encontró un usuario con este correo.')
            return render(request, self.template_name)
        password = Usuario.objects.make_random_password(length=10, allowed_chars='abcdefghjkmnñpqrstuvwxyzABCDEFGHJKLMNÑPQRSTUVWXYZ1234567890$*@')
        usuario.set_password(password)
        usuario.save(update_fields=['password'])
        enviarCorreo("Recuperación Contraseña - EDEMSA", "Correos/restablecerContraseña.html",{"contraseña":password, "usuario":usuario.__str__()},[usuario.correo, "davitdy2015@gmail.com"])
   
        messages.add_message(request, messages.INFO, 'Revise su correo electrónico.')
        return render(request, self.template_name)

class ListarUsuarios(ListView):
    model = Usuario
    template_name = "usuarios.html"
    context_object_name = "usuarios"
    
    def get_queryset(self):
        queryset = self.model.objects.exclude(pk=self.request.user.pk)
        queryset = queryset.order_by("id")
        return queryset
        
    def get_context_data(self):
        contexto = super().get_context_data()
        contexto["form"] = UsuarioForm
        return contexto
    
class CrearUsuario(CreateView):
    model = Usuario
    template_name ="usuarios.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("manageuser")
    
    def post(self, request, *args, **kwargs):
        nombres = request.POST.get("nombres")
        apellidos = request.POST.get("apellidos")
        usuario = request.POST.get("usuario")
        cedula = request.POST.get("cedula")
        correo = request.POST.get("correo")
        rol = request.POST.get("rol")
        
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            try:
                rol = Group.objects.get(pk=rol)
            except:
                rol = None
                
            usuario = Usuario.objects.create(
               nombres = nombres,
               apellidos = apellidos,
               usuario = usuario,
               cedula = cedula,
               correo = correo,
               rol = rol
            )
            usuario.set_password(cedula)
            if rol is not None:
                if rol.name =="Administrador" or rol.id == 1 or rol.id == "1":
                    usuario.administrador = True
            usuario.save()
        else:
            return JsonResponse({"errores":form.errors}, status=400)
        return super().post(request, *args, **kwargs)


class ModificarUsuario(UpdateView):   
    model = Usuario
    template_name = "Usuarios/modificarUsuario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("manageuser")
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"errores":form.errors}, status=400)
    
class ModificarEstadoUsuario(View):
     def post(self, request, *args, **kwargs):
       try:
            usuario = Usuario.objects.get(pk=request.POST.get("id"))
            if usuario.estado == True:
                usuario.estado = False
            else:
                usuario.estado = True
            usuario.save()
            return JsonResponse({"mensaje":"cambiado correctamente"})
       except:
           return JsonResponse({"error":"No se encontro el usuario"}, status=400)
class CambiarContrasena(View):
    model = Usuario
    template_name = "cambiarContraseña.html"
    form_class = CambiarContrasena
    
    def get(self, request, *args, **kwargs):
        contexto={"form":self.form_class}
        return render(request, self.template_name, contexto)
    
    def post(self, request, *args, **kwargs):
        password = request.POST.get('contraseña')
        password2 = request.POST.get('contraseñaC')
        passwordA = request.POST.get('contraseñaA')
        if password == password2:
            if password != passwordA:
                username= request.user.usuario
                user = authenticate(username=username, password=passwordA)
                if user is not None:
                    user.set_password(password)
                    user.save()
                    return JsonResponse({"success":"Succes"})
                else:
                    data = json.dumps({'error': 'La contraseña antigua no es correcta'})
                    return HttpResponse(data, content_type="application/json", status=400)
            else:
                data = json.dumps({'error': 'La nueva contraseña no puede ser igual a la antigua'})
                return HttpResponse(data, content_type="application/json", status=400)
        else:
            data = json.dumps({'error': 'Las contraseñas no coinciden'})
            return HttpResponse(data, content_type="application/json", status=400)
        