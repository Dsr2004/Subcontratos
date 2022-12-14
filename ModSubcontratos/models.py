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
        return self.razon_social
    
    @property
    def get_name(self):
        return self.razon_social.capitalize()
    
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
        db_table = "proveedores"
        

# FIN
TIPO_CONTRATO =(
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
    ("19","Seguros Bol??var"),
    ("20","Seguros Mundial"),
    ("21","La Equidad Seguros"),
   
)

VALIDADORES = (
    ("Ambiental", "Ambiental"),
    ("Social", "Social"),
    ("RRHH", "RRHH"),
    ("Calidad", "Calidad"),
    ("SST", "SST"),
    ("P&C Planeaci??n", "P&C Planeaci??n"),
    ("P&C Costos", "P&C Costos"),
    ("Administrador", "Administrador"),
    ("Seguros", "Seguros"),
    
)

ESTADO_SUBCONTRATO = (
    ("1", "En ejecuci??n"),
    ("2", "No ejecutado"),
    ("3", "Suspendido"),
    ("4", "Liquidado"),
)
def extension(file):
        name, extension = os.path.splitext(file)
        return extension
    
def guardar_contrato(instance, filename):
    print("guado contrato y algo mas")
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
    aseguradora = models.CharField(max_length=34, choices=ASEGURADORAS)
    fecha_vencimiento = models.DateField()
    
    class Meta:
        db_table = "polizas"
        
    def __str__(self):
        if self.subcontrato_set.all():
            return f"Poliza del subcontrato {self.subcontrato_set.all()[0].pk}"
        else:
            return f"TIPO: {self.tipo_poliza} N??MERO: {self.numero_poliza} ASEGURADORA{self.get_aseguradora_display()} VENCIMIENTO:{self.fecha_vencimiento}"
    
     
class Subcontrato(models.Model):
    tipo_contrato = models.CharField(max_length=5, choices=TIPO_CONTRATO)
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
    impo = models.BooleanField()
    contrato = models.FileField(upload_to=guardar_contrato, validators = [validar_extencion_archivo])
    polizas_garantias = models.FileField(upload_to=guardar_polizas_garantias, validators = [validar_extencion_archivo])
    acta_inicio = models.FileField(upload_to=guardar_acta_inicio, validators = [validar_extencion_archivo])
    modificaciones_contractuales = models.FileField(upload_to=guardar_modificaciones_contractuales, validators = [validar_extencion_archivo])
    acta_recibo_final = models.FileField(upload_to=guardar_acta_recibo_final, validators = [validar_extencion_archivo])
    acta_liquidacion = models.FileField(upload_to=guardar_acta_liquidacion, validators = [validar_extencion_archivo])
    estado = models.CharField(max_length=30, choices=ESTADO_SUBCONTRATO, default="1")
    consecutivo = models.BigIntegerField(unique=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    proximo_envio_correo = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "subcontratos"
        
    def __str__(self):
        return f"Subcontrato {self.pk}"

    @property
    def CantidadPolizas(self):
        return self.polizas.all().count()
    
    @property 
    def get_subtotal(self):
        items = self.item_subcontrato_set.all()
        sub = sum([item.get_total for item in items])
        return sub
    
    @property
    def get_iva(self):
        iva = float("{:.5f}".format(self.get_subtotal*self.tarifa_iva/100))
        return iva    

    @property
    def get_porcentaje_administracion(self):
        porcentaje_administracion = float("{:.5f}".format(self.get_subtotal*self.porcentaje_administracion/100))
        return porcentaje_administracion

    @property
    def get_porcentaje_imprevistos(self):
        porcentaje_imprevistos = float("{:.5f}".format(self.get_subtotal*self.porcentaje_imprevistos/100))
        # print(porcentaje_imprevistos)
        return porcentaje_imprevistos

    @property
    def get_porcentaje_utilidad(self):
        porcentaje_utilidad = float("{:.5f}".format(self.get_subtotal*self.porcentaje_utilidad/100))
        # print(porcentaje_imprevistos)
        return porcentaje_utilidad

    @property
    def get_iva_utilidad(self):
        iva_utilidad = float("{:.5f}".format(self.get_porcentaje_utilidad*self.tarifa_iva/100))
        # print(porcentaje_imprevistos)
        return iva_utilidad

    @property
    def get_total(self):
        total = (self.get_subtotal+self.get_iva+self.get_porcentaje_administracion)
        return total

    
    
    

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
            
        def __str__(self):
            return f"Item del subcontrato {self.subcontrato.pk}"
        
        @property
        def get_total(self):
            return self.cantidad * self.valor_unitario
        
    

class SubCapitulo(models.Model):
    nombre = models.CharField(max_length=150)
    subitem = models.ManyToManyField(Item_Subcontrato)
    
    class Meta:
        db_table = "subcapitulos"
    
    
    def __str__(self):
        return self.nombre
    
    
ESTADOS_ACTAS=(
    ("1","Sin revisar"),
    ("2","Aprobado")
)
def guardar_listado_personal(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/listado_personal{extension(filename)}"
def guardar_seguridad_social(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/seguridad_social{extension(filename)}"
def guardar_otros_datos_adjuntos(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/otros_datos_adjuntos{extension(filename)}"
# -------------------------
def guardar_firma_Ambiental(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Ambiental{extension(filename)}"
def guardar_firma_Social(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Social{extension(filename)}"
def guardar_firma_RRHH(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_RRHH{extension(filename)}"
def guardar_firma_Calidad(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Calidad{extension(filename)}"
def guardar_firma_SST(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_SST{extension(filename)}"
def guardar_firma_Planeacion(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Planeacion{extension(filename)}"
def guardar_firma_Costos(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Costos{extension(filename)}"
def guardar_firma_Administrador(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Administrador{extension(filename)}"
def guardar_firma_Seguros(instance, filename):
    return  f"Subcontratos/Actas/{instance}-{instance.id}/firma_Seguros{extension(filename)}"

class Acta(models.Model):
    titulo = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices=ESTADOS_ACTAS)
    subcontrato = models.ForeignKey(Subcontrato, on_delete=models.CASCADE)
    listado_personal = models.FileField(upload_to=guardar_listado_personal, null=True, blank=True)
    seguridad_social = models.FileField(upload_to=guardar_seguridad_social, null=True, blank=True)
    otros_datos_adjuntos = models.FileField(upload_to=guardar_otros_datos_adjuntos, null=True, blank=True)
    #firmas
    firma_Ambiental = models.ImageField(upload_to=guardar_firma_Ambiental, null=True, blank=True)
    firma_Social = models.ImageField(upload_to=guardar_firma_Social, null=True, blank=True)
    firma_RRHH = models.ImageField(upload_to=guardar_firma_RRHH, null=True, blank=True)
    firma_Calidad = models.ImageField(upload_to=guardar_firma_Calidad, null=True, blank=True)
    firma_SST = models.ImageField(upload_to=guardar_firma_SST, null=True, blank=True)
    firma_Planeacion = models.ImageField(upload_to=guardar_firma_Planeacion, null=True, blank=True)
    firma_Costos = models.ImageField(upload_to=guardar_firma_Costos, null=True, blank=True)
    firma_Administrador = models.ImageField(upload_to=guardar_firma_Administrador, null=True, blank=True)
    firma_Seguros = models.ImageField(upload_to=guardar_firma_Seguros, null=True, blank=True)
    
    class Meta:
        db_table = "actas"

    def __str__(self):
        return self.titulo
    
    def get_nombre_listado_personal(self):
        if self.listado_personal:
            return os.path.basename(self.listado_personal.name)
        else:
            return "No existe el archivo"
    
    def get_nombre_seguridad_social(self):
        if self.seguridad_social:
            return os.path.basename(self.seguridad_social.name)
        else:
            return "No existe el archivo"

    
        
        
class Paquete_Trabajo(models.Model):
    paquete = models.CharField(max_length=200)
    
    def __str__(self):
        return self.paquete
    
    class Meta:
        db_table = "paquetes_de_trabajo"
        
        

class Seguimiento(models.Model):
    acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    item = models.ForeignKey(Item_Subcontrato, on_delete=models.CASCADE)
    paquete_trabajo = models.ForeignKey(Paquete_Trabajo, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{ self.acta.titulo} {self.item}"
    class Meta:
        db_table = "seguimiento_acta"
    
    @property
    def cantidad_por_ejecutar(self):
        return self.item.cantidad - self.cantidad
    
    @property
    def get_valor(self):
        return self.item.valor_unitario * self.cantidad

    