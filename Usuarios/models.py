from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group


class UsuarioManager(BaseUserManager):
    def create_user(self,usuario,nombres,apellidos,correo,cedula,password=None):
        if  not correo:
            raise ValueError('El usuario debe tener un correo electronico!')
        usuario = self.model(
            usuario=usuario, 
            nombres = nombres, 
            apellidos = apellidos, 
            correo = self.normalize_email(correo),
            cedula = cedula,
            )
        usuario.set_password(password)
        usuario.save()
        return usuario


    def create_superuser(self,usuario,nombres,apellidos,correo,cedula,password=None):
        if  not correo:
            raise ValueError('El usuario debe tener un correo electronico!')
        usuario = self.model(
            usuario=usuario, 
            nombres = nombres, 
            apellidos = apellidos,
            correo = self.normalize_email(correo),
            cedula = cedula,

            )
        usuario.set_password(password)
        usuario.administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    id = models.AutoField(unique=True, primary_key=True, auto_created=True)
    usuario = models.CharField("Nombre de Usuario", unique=True, max_length=50)
    nombres  = models.CharField("Nombres", blank=False, null=False, max_length=50)
    apellidos = models.CharField("Apellidos", blank=False, null=False, max_length=25)
    correo = models.EmailField('Correo Electrónico', unique=True)
    cedula = models.CharField('Cedula', unique=True, max_length=15, null=False, blank=False)
    estado = models.BooleanField("Estado del usuario", default=True)
    rol = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="rol", null=True, blank=True)
    administrador = models.BooleanField(default=False)
    objects = UsuarioManager()


    USERNAME_FIELD='usuario' 
    REQUIRED_FIELDS=["nombres", "apellidos","correo","cedula"]

    class Meta:
        db_table = "usuarios"

    def __str__(self):
        return '{}'.format(self.nombres.capitalize()+' '+self.apellidos.lower())

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.administrador



#modelos temporales luego se van a borrar

class Nomina(models.Model):
    razon_social = models.CharField(max_length=90,null=True, blank=True)
    cargo = models.CharField(max_length=90,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.razon_social+ " "+ self.cargo
    class Meta:
        db_table = "nominas"

class Centro_Operacion(models.Model):
    id_proyecto = models.CharField(max_length=15)
    nombre_proyecto = models.CharField(max_length=90,null=True, blank=True)

    def __str__(self):
        return self.nombre_proyecto
    class Meta:
        db_table = "centros_de_operaciones"
    

class Compania(models.Model):
    compania = models.CharField(max_length=90,null=True, blank=True)

    def __str__(self):
        return self.compania
    class Meta:
        db_table = "companias"
    
class Item(models.Model):
    pass
    
class Proveedor(models.Model):
    nit = models.CharField(max_length=50,null=True, blank=True)
    razon_social = models.CharField(max_length=150,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.razon_social
    class Meta:
        db_table = "proovedores"
    