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

class UsuarioForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Usuario
        fields = ['usuario','nombres','apellidos','correo','cedula',"rol", "tipo_validador"]
        widgets = {
            "usuario": forms.TextInput(attrs={"class":"form-control mb-3", "autocomplete":"off", "placeholder":"Ingrese el nombre de usuario"}),
            "nombres": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off", "placeholder":"Ingrese el nombre completo"}),
            "apellidos": forms.DateInput(attrs={"class":"form-control", "autocomplete":"off", "placeholder":"Ingrese los apellidos"}),
            "cedula": forms.TextInput(attrs={"class":"form-control mb-2", "autocomplete":"off", "placeholder":"Ingrese el número de documento"}),
            "correo": forms.EmailInput(attrs={"class":"form-control mb-2", "autocomplete":"off", "placeholder":"Ingrese el correo electrónico"}),
            "rol": forms.Select(attrs={"class":"form-select", "id":"rol_ti","autocomplete":"off", "onchange":"alert('Hola')"}),
            "tipo_validador":forms.Select(attrs={"class":"form-select", "autocomplete":"off"}),
            
        }
        
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['tipo_validador'].required = False
       
        
        
class CambiarContrasena(forms.ModelForm):
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(
        attrs={
            'id':"confpassword",
            'requerid':'requerid',
            'name':'passwordC',
            "class":"form-control",
            'placeholder':'Vuelve a escribir la contraseña'
        }
    ))
    passwordA = forms.CharField(label="Contraseña antigua",widget=forms.PasswordInput(
        attrs={
            'id':"newpassword",
            'requerid':'requerid',
            'name':'passwordA',
            "class":"form-control",
            'placeholder':'Ingrese la contraseña actual'
        }
    ))
    
    class Meta:
        model = Usuario
        
        fields=['password']
        widgets={
            'password': forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off",'id':"password",'requerid':'requerid','name':'password', 'placeholder': 'Ingrese la nueva contraseña'}),
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('passwordC')
        
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
