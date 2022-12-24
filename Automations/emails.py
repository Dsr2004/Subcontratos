from django.conf import settings
import json
from datetime import datetime
from Subcontratos.correo import enviarCorreo
from ModSubcontratos.models import Subcontrato

def schedule_api():
    subcontratos = Subcontrato.objects.filter(estado="1").filter(proximo_envio_correo=datetime.now())
    if subcontratos:
        for subcontrato in subcontratos:
            validadore = subcontrato.validadores
            #capturar usuarios que sean del mismo tipo de validador
            #enviar correos a esas personas 
        enviarCorreo("Envio de correo cada minuto - EDEMSA", "CorreosSubcontratos/correoPrueba.html",{"p1":"prueba"},["davitdy2015@gmail.com"])
    enviarCorreo("Envio de correo cada minuto - EDEMSA", "CorreosSubcontratos/correoPrueba.html",{"p1":"prueba"},["davitdy2015@gmail.com"])
    print("enviado")
     