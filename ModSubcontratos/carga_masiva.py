import pandas as pd
import os
from .models import Nomina ,Centro_Operacion ,Compania ,Proveedor
from django.conf import settings
from django.shortcuts import redirect

BASE_DIR = settings.BASE_DIR


def cargar_Nomina():
    Nomina.objects.all().delete()
    Nomina.objects.raw('TRUNCATE nominas RESTART IDENTITY')
    excel = os.path.join(BASE_DIR, "EXCELS/nomina(1).xlsx")
    df = pd.read_excel(excel)
    
    for index, row in df.iterrows():
        nomina, creado = Nomina.objects.get_or_create(
            razon_social = row["razon_social"],
            cargo = row["cargo"],
            email = row["mail"]
        )
    print("Terminado la carga masiva de la nomina")
        
def cargar_Centro_Operacion():
    Centro_Operacion.objects.all().delete()
    Centro_Operacion.objects.raw('TRUNCATE centros_de_operaciones RESTART IDENTITY')
    excel = os.path.join(BASE_DIR, "EXCELS/centros de operaciones.xlsx")
    df = pd.read_excel(excel)
    
    for index, row in df.iterrows():
        centro, creado = Centro_Operacion.objects.get_or_create(
            id_proyecto = row["IdProyecto"],
            nombre_proyecto = row["NombreProyecto"],
        )
    print("Terminado la carga masiva de los centros de operaciones")
        
def cargar_compania():
    Compania.objects.all().delete()
    Compania.objects.raw('TRUNCATE companias RESTART IDENTITY')
    excel = os.path.join(BASE_DIR, "EXCELS/compañias.xlsx")
    df = pd.read_excel(excel)
    
    for index, row in df.iterrows():
        compañia, creado = Compania.objects.get_or_create(
            compania = row["COMPAÑÍA"],
        )
    print("Terminado la carga masiva de las compañias")
        

def cargar_proveedores():
    Proveedor.objects.all().delete()
    Proveedor.objects.raw('TRUNCATE proveedores RESTART IDENTITY')
    excel = os.path.join(BASE_DIR, "EXCELS/provs.xlsx")
    df = pd.read_excel(excel)
    
    for index, row in df.iterrows():
        proveedor, creado = Proveedor.objects.get_or_create(
            nit = row["f200_nit"],
            razon_social = row["razon_social"],
            email = row["f202_email"]
        )
    print("Terminado la carga masiva de los proveedores")



def carga_masiva(request):
    cargar_Nomina()
    cargar_Centro_Operacion()
    cargar_compania()
    cargar_proveedores()
    return redirect("manageuser")