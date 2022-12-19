import os
from django.db import models
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
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
    id_cia = models.CharField(max_length=250,null=True, blank=True)
    codigo = models.CharField(max_length=250,null=True, blank=True)
    referencia = models.CharField(max_length=250,null=True, blank=True)
    descripcion = models.CharField(max_length=250,null=True, blank=True)
    final = models.CharField(max_length=250,null=True, blank=True)
    
    def __str__(self):
        return self.final
    class Meta:
        db_table = "items"
    
class Proveedor(models.Model):
    nit = models.CharField(max_length=50,null=True, blank=True)
    razon_social = models.CharField(max_length=150,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.razon_social
    class Meta:
        db_table = "proovedores"
        

# FIN
TIPO_CONTRANTO =(
   ("1.1", "1.1 Contratos con IVA pleno suministros."),
   ("1.2", "1.2 Contratos con IVA pleno y algunos servicios."),
   ("2", "2. Contratos de servicios de obra civil."),
   ("3", "3. Contratos mixtos."),
  
)   
TIPO_ORDEN =(
   ("1", "OCS"),
   ("2", "OCM"),
  
)
SEGUIMIENTO_ACTAS = (
    ("1","Semanal"),
    ("2","Catorcenal"),
    ("3","Quincenal"),
    ("4","Mensual")
)
TIPO_POLIZA = (
    ("1","Cumplimiento"),
    ("2","Responsabilidad civil"),
    ("3","Todo riesgo"),
)
ASEGURADORAS = (
    ("1","SBS Seguros Colombia S.A"),
    ("2","BBVA Seguros"),
    ("3","CHUBB"),
    ("4","HDI Seguros S.A"),
    ("5","La Previsora"),
    ("6","BMI"),
    ("7","Suramericana S.A"),
    ("8","AXA Colpatria"),
    ("9","Berkley Seguros"),
    ("10","Confianza S.A"),
    ("11","Colmena Seguros"),
    ("12","Liberty Seguros"),
    ("13","Segurexpo"),
    ("14","Seguros del Estado"),
    ("15","Nacionar del seguros"),
    ("16","Zurich"),
    ("17","Aseguradora Solidaria"),
    ("18","Jmalucelli Travelers Seguros S.A"),
    ("19","Seguros Bolívar"),
    ("20","Seguros Mundial"),
    ("21","La Equidad Seguros"),
   
)

VALIDADORES = (
    ("Ambiental", "Ambiental"),
    ("Social", "Social"),
    ("RRHH", "RRHH"),
    ("Calidad", "Calidad"),
    ("SST", "SST"),
    ("P&C Planeación", "P&C Planeación"),
    ("P&C Costos", "P&C Costos"),
    ("Administrador", "Administrador"),
    ("Seguros", "Seguros"),
    
)
def extension(file):
        name, extension = os.path.splitext(file)
        return extension
    
def guardar_contrato(instance, filename):
    return  f"Subcontratos/{instance.proveedor.nit}-{instance.numero_orden}/contrato{extension(filename)}"
def guardar_polizas_garantias(instance, filename):
    return  f"Subcontratos/{instance.proveedor.nit}-{instance.numero_orden}/polizas_garantias{extension(filename)}"
def guardar_acta_inicio(instance, filename):
    return  f"Subcontratos/{instance.proveedor.nit}-{instance.numero_orden}/acta_inicio{extension(filename)}"
def guardar_modificaciones_contractuales(instance, filename):
    return  f"Subcontratos/{instance.proveedor.nit}-{instance.numero_orden}/modificaciones_contractuales{extension(filename)}"
def guardar_acta_recibo_final(instance, filename):
    return  f"Subcontratos/{instance.proveedor.nit}-{instance.numero_orden}/acta_recibo_final{extension(filename)}"
def guardar_acta_liquidacion(instance, filename):
    return  f"Subcontratos/{instance.proveedor.nit}-{instance.numero_orden}/acta_liquidacion{extension(filename)}"

def validar_extencion_archivo(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de archivo invalido, solo adjunte archivos .pdf, .jpg, jpeg, .png.')
   
class Poliza(models.Model):
    tipo_poliza = models.CharField(max_length=23)
    numero_poliza = models.CharField(max_length=100)
    aseguradora = models.CharField(max_length=34)
    fecha_vencimiento = models.DateField()
    
    class Meta:
        db_table = "polizas"
    
     
class Subcontrato(models.Model):
    tipo_contrato = models.CharField(max_length=5, choices=TIPO_CONTRANTO)
    elaborador = models.ForeignKey(Nomina, on_delete=models.SET_NULL, null=True)
    proyecto = models.ForeignKey(Centro_Operacion, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    compania = models.ForeignKey(Compania, on_delete=models.SET_NULL, null=True)
    tipo_orden = models.CharField(max_length=5, choices=TIPO_ORDEN)
    numero_orden = models.CharField(max_length=250)
    tarifa_iva = models.IntegerField(default=19)
    porcentaje_administracion = models.IntegerField(default=0) 
    porcentaje_imprevistos = models.IntegerField(default=0)
    porcentaje_utilidad = models.IntegerField(default=0)
    seguimiento_acta = models.CharField(max_length=5, choices=SEGUIMIENTO_ACTAS)
    fecha_inicio_contrato = models.DateField()
    fecha_vencimiento_contrato = models.DateField()
    director_obra = models.CharField(max_length=250)
    gestor_contrato = models.CharField(max_length=250)
    correo_notificacion_proveedor = models.EmailField()
    validadores = MultiSelectField(max_length=150, choices=VALIDADORES)
    polizas = models.ManyToManyField(Poliza)
    
    contrato = models.FileField(upload_to=guardar_contrato, validators = [validar_extencion_archivo])
    polizas_garantias = models.FileField(upload_to=guardar_polizas_garantias, validators = [validar_extencion_archivo])
    acta_inicio = models.FileField(upload_to=guardar_acta_inicio, validators = [validar_extencion_archivo])
    modificaciones_contractuales = models.FileField(upload_to=guardar_modificaciones_contractuales, validators = [validar_extencion_archivo])
    acta_recibo_final = models.FileField(upload_to=guardar_acta_recibo_final, validators = [validar_extencion_archivo])
    acta_liquidacion = models.FileField(upload_to=guardar_acta_liquidacion, validators = [validar_extencion_archivo])
    estado = models.CharField(max_length=250, default="En ejecución")

    class Meta:
        db_table = "subcontratos"
    

class Item_Subcontrato(models.Model):
        subcontrato = models.ForeignKey(Subcontrato, on_delete=models.CASCADE)
        item_codigo = models.ForeignKey(Item, on_delete=models.CASCADE)
        item_nombre = models.CharField(max_length=150)
        descripcion = models.TextField()
        unidad = models.CharField(max_length=150)
        cantidad = models.IntegerField()
        valor_unitario = models.IntegerField()
        
        class Meta:
            db_table = "items_subcontrato"
        
        @property
        def get_total(self):
            return str(self.cantidad*self.valor_unitario)
    