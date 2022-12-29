from django.conf import settings
import json
from datetime import datetime
from Subcontratos.correo import enviarCorreo
from ModSubcontratos.models import Subcontrato
from Usuarios.models import Usuario

def schedule_api():
    subcontratos = Subcontrato.objects.filter(estado="1").filter(proximo_envio_correo=datetime.now())
    if subcontratos:
        for subcontrato in subcontratos:
            contexto = {"nombrePersona": subcontrato.elaborador, "titulo": subcontrato.get_seguimiento_acta_display(), "id":subcontrato.consecutivo, "fecha_creacion": subcontrato.fecha_creacion}
            enviarCorreo("Recordatorio de realización de acta", "CorreosSubcontratos/RecordatorioActaBase.html", contexto, ["davitdy2015@gmail.com"])
            print("correo enviado")
                
    # enviarCorreo("Envio de correo cada minuto - EDEMSA", "CorreosSubcontratos/correoPrueba.html",{"p1":"prueba"},["davitdy2015@gmail.com"])
            # print("enviado")
    
    
    
""""
subcontratos = Subcontrato.objects.filter(estado="1").filter(proximo_envio_correo=datetime.now())
    if subcontratos:
        for subcontrato in subcontratos:
            for tipo_validador in subcontrato.validadores:
                validadores = Usuario.objects.filter(rol__name="Validador").filter(tipo_validador=tipo_validador)
                for validador in validadores:
                    contexto = {"nombrePersona": validador, "titulo": subcontrato.get_seguimiento_acta_display(), "id":subcontrato.consecutivo, "fecha_creacion": subcontrato.fecha_creacion}
                    enviarCorreo("Recordatorio de realización de acta", "CorreosSubcontratos/RecordatorioActaBase.html", contexto, ["davitdy2015@gmail.com", "juanma28o123@gmail.com"])
                    print("correo enviado")

"""