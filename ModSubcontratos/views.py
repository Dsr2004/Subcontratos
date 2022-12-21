import pandas as pd
from datetime import timedelta
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from django.db import transaction
from django.http import QueryDict
from .models import *
from .forms import SubcontratoForm, Item_SubcontratoForm

def validar_itemsSubcontrato(item):
    if not item["subcontrato"]:
        return {"subcontrato":"No hay un subcontrato en la lista."}
    
    if not item["item_codigo"]:
        return {"item_codigo":"No hay un codigo en la lista."}
    
    if not item["item_nombre"]:
        return {"item_nombre":"No hay un item en la lista."}
    
    if not item["descripcion"]:
        return {"descripcion":"No hay una descripción en la lista."}
    
    if not item["unidad"]:
        return {"unidad":"No hay un unidad en la lista."}
    
    if not item["cantidad"]:
        return {"cantidad":"No hay un cantidad en la lista."}
    
    if not item["valor_unitario"]:
        return {"valor_unitario":"No hay un valor unitario en la lista."}
    
    try:
        Item.objects.get(codigo=item["item_codigo"])
    except:
        return {"item_codigo":"No ay un item con este codigo {codigo}} en la base de datos".format(codigo=item['item_codigo'])}
    
    try:
        x = int(item["cantidad"])
    except:
        return {"cantidad":"Una cantidad no es un numero"}
    
    try:
       x = int(item["valor_unitario"])
    except:
        return {"valor_unitario":"Un valor unitario no es un numero"}
        
    return True
class SubContratos(View):
    template_name = "crearSubcontratos.html"
    # template_name = "subcontratos.html"
    
    def get(self, request, *args, **kwargs):
        ultimo_id = Subcontrato.objects.last()
        if ultimo_id:
            ultimo_id.pk+=1
            ultimo_id = ultimo_id.pk
        else:
            ultimo_id=1
        return render(request, self.template_name,{"ultimo_id":ultimo_id, "form":SubcontratoForm()})
    
    def post(self, request, *args, **kwargs):
        try:
            action = request.POST.get("action")
            tipo = request.POST.get("tipo")
            if tipo == "elaborador":
                if action == "autocompleteElaborador":
                    nomina = Nomina.objects.filter(razon_social__icontains=request.POST.get("term"))
                    nomina = nomina.values()
                    return JsonResponse(list(nomina), safe=False)
                elif action == "CargoElaborador":
                    elaborador = request.POST.get("elaborador")
                    elaborador = Nomina.objects.get(pk=elaborador)
                    return JsonResponse({"cargoElaborador":elaborador.cargo})
                
            elif tipo == "proyecto":
                if action == "autocompleteProyecto":
                    proyecto = Centro_Operacion.objects.filter(nombre_proyecto__icontains=request.POST.get("term"))
                    proyecto = proyecto.values()
                    return JsonResponse(list(proyecto), safe=False)
                elif action == "centroOperacionesProyecto":
                    proyecto = request.POST.get("proyecto")
                    proyecto = Centro_Operacion.objects.get(pk=proyecto)
                    return JsonResponse({"id":proyecto.id,"id_proyecto":proyecto.id_proyecto})
                elif action == "autocompleteCentroOperaciones":
                    nomina = Centro_Operacion.objects.filter(id_proyecto__icontains=request.POST.get("term"))
                    nomina = nomina.values()
                    return JsonResponse(list(nomina), safe=False)
                elif action == "proyectoCentroOperaciones":
                    centroOperacion = request.POST.get("centroOperacion")
                    centroOperacion = Centro_Operacion.objects.get(pk=centroOperacion)
                    return JsonResponse({"id":centroOperacion.id,"proyecto":centroOperacion.nombre_proyecto})
                
            elif tipo == "proveedor":
                if action == "autocompleteNit":
                    proveedores = Proveedor.objects.filter(nit__icontains=request.POST.get("term"))
                    proveedores = proveedores.values()
                    return JsonResponse(list(proveedores), safe=False)
                elif action == "autocompleteProveedor":
                    proveedores = Proveedor.objects.filter(razon_social__icontains=request.POST.get("term"))
                    proveedores = proveedores.values()
                    return JsonResponse(list(proveedores), safe=False)
                elif action == "proveedordelNIT":
                    proveedor = request.POST.get("nit")
                    print(proveedor)
                    proveedor = Proveedor.objects.get(pk=proveedor)
                    return JsonResponse({"id":proveedor.id,"proveedor":proveedor.razon_social})
                elif action == "NITdelProveedor":
                    proveedor = request.POST.get("proveedor")
                    proveedor = Proveedor.objects.get(pk=proveedor)
                    return JsonResponse({"id":proveedor.id,"nit":proveedor.nit})
            elif tipo == "compania":
                if action == "autocompleteCompania":
                    compania = Compania.objects.filter(compania__icontains=request.POST.get("term"))
                    compania = compania.values()
                    return JsonResponse(list(compania), safe=False)
            elif tipo == "item":
                if action == "autocompleteItem":
                    items = Item.objects.filter(codigo__icontains=request.POST.get("term"))
                    items = items.values()

                    return JsonResponse(list(items), safe=False)
                
                
        except Exception as e:
            print(str(e))
            return JsonResponse({"error":str(e)}, status = 400)

class GuardarSubcontrato(View):
    template_name = "crearSubcontratos.html"
    form_class = SubcontratoForm
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            if request.POST.get("impo")=="si":
                print(request.FILES)  
            try:
                with transaction.atomic():
                    subcontrato = form.save()
                    dias = 0
                    if subcontrato.seguimiento_acta == "1":
                        dias = 8
                    elif subcontrato.seguimiento_acta == "2":
                        dias = 14
                    elif subcontrato.seguimiento_acta == "3":
                        dias = 15
                    elif subcontrato.seguimiento_acta == "4":
                        dias = 30
                    else:
                        return JsonResponse({"errores":{"seguimiento_acta":["Seleccione una opcion valida."]}}, status=400)
        
                    subcontrato.proximo_envio_correo = subcontrato.fecha_creacion+timedelta(days=dias)
                    subcontrato.save()
                    print("el subcontratos es", subcontrato.pk)
                    if request.POST.get("impo")=="si":
                        file = request.FILES["excelItems"]
                        print("adfds", file)
                        if file:
                            df = pd.read_excel(file)
                            for index, row in df.iterrows():
                                data = {"subcontrato":subcontrato.pk,
                                        "item_codigo":row["Código ITEM"],
                                        "item_nombre":row["Item"],
                                        "descripcion":row["Descripción"],
                                        "unidad":row["Unidad"],
                                        "cantidad":row["Cantidad"],
                                        "valor_unitario":row["Valor Unitario"]}
                                if validar_itemsSubcontrato(data) == True:
                                    formItemSubcon = Item_Subcontrato.objects.create(subcontrato=subcontrato,
                                            item_codigo=Item.objects.get(codigo=row["Código ITEM"]),
                                            item_nombre=row["Item"],
                                            descripcion=row["Descripción"],
                                            unidad=row["Unidad"],
                                            cantidad=row["Cantidad"],
                                            valor_unitario=row["Valor Unitario"]
                                            )
                                else:
                                    print("validacionws: ",validar_itemsSubcontrato)
            except Exception as e:
                print("hubo un error ",e)
            return HttpResponse(request.POST)
        else:
            print(form.errors)
            return JsonResponse({"errores":form.errors}, status=400) 
        