from django.db import models

# Create your models here.
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
