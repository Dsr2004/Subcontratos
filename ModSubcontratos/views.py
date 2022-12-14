import json
import pandas as pd
from datetime import timedelta
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import View, ListView, CreateView, UpdateView, TemplateView, DetailView
from django.http import QueryDict
from .models import *
from .forms import SubcontratoForm, Item_SubcontratoForm, PolizaForm

def validar_itemsSubcontrato(item ,tipo):
    if not item["subcontrato"]:
        raise Exception({"subcontrato":"No hay un subcontrato en la lista."})
    
    if not item["item_codigo"]:
        raise Exception({"item_codigo":"No hay un codigo en la lista."})
    
    if not item["item_nombre"]:
        raise Exception({"item_nombre":"No hay un item en la lista."})
    
    if not item["descripcion"]:
        raise Exception( {"descripcion":"No hay una descripción en la lista."})
    
    if not item["unidad"]:
        return Exception({"unidad":"No hay un unidad en la lista."})
    
    if not item["cantidad"]:
        raise Exception({"cantidad":"No hay un cantidad en la lista."})
    
    if not item["valor_unitario"]:
        raise Exception({"valor_unitario":"No hay un valor unitario en la lista."})
    
    try:
        if tipo == "excel":
            Item.objects.get(codigo=item["item_codigo"])
        elif tipo == "html":
            Item.objects.get(pk=item["item_codigo"])
    except:
        raise Exception({"item_codigo":"No hay un item con este codigo {codigo} en la base de datos".format(codigo=item['item_codigo'])})
    
    try:
        x = int(item["cantidad"])
    except:
        raise Exception({"cantidad":"Una cantidad no es un número"})
    
    try:
       x = int(item["valor_unitario"])
    except:
        raise Exception({"valor_unitario":"Un valor unitario no es un número"} )
    return True
class SubContratos(View):
    template_name = "crearSubcontratos.html"
    
    def get(self, request, *args, **kwargs):
        ultimo_id = Subcontrato.objects.last()
        if ultimo_id:
            consecutivo = ultimo_id.consecutivo+1
        else:
            consecutivo = 1

        return render(request, self.template_name,{"consecutivo":consecutivo, "form":SubcontratoForm(), "formPoliza":PolizaForm()})
    
class BusquedaInfoSubcontrato(View):
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
                    return JsonResponse({"id":proveedor.id,"proveedor":proveedor.razon_social,"email":proveedor.email})
                elif action == "NITdelProveedor":
                    proveedor = request.POST.get("proveedor")
                    proveedor = Proveedor.objects.get(pk=proveedor)
                    return JsonResponse({"id":proveedor.id,"nit":proveedor.nit,"email":proveedor.email})
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
            elif tipo == "acta":
                if action == "autocompleteItemActa":
                    sub = request.POST.get("subcontrato", None)
                    if sub is not None:
                        items = Item_Subcontrato.objects.filter(subcontrato=sub)
                        items = items.filter(item_nombre__icontains=request.POST.get("term"))
                        items = items.values()
                    else:
                        items = []
                    return JsonResponse(list(items), safe=False)
                elif action == "autocompleteDescripcionItem":
                    sub = request.POST.get("subcontrato", None)
                    if sub is not None:
                        items = Item_Subcontrato.objects.filter(subcontrato=sub)
                        items = items.filter(descripcion__icontains=request.POST.get("term"))
                        items = items.values()
                    else:
                        items = []
                    return JsonResponse(list(items), safe=False)
                elif action == "Itemdescripcion":
                    item = request.POST.get("item")
                    item = Item_Subcontrato.objects.get(pk=item)
                    return JsonResponse({"id":item.id,"item":item.item_nombre,"valor":item.valor_unitario, "unidad":item.unidad})
                
                elif action == "descripcionItem":
                    item = request.POST.get("item")
                    item = Item_Subcontrato.objects.get(pk=item)
                    return JsonResponse({"id":item.id,"descripcion":item.descripcion,"valor":item.valor_unitario, "unidad":item.unidad})
                
        except Exception as e:
            print(str(e))
            return JsonResponse({"error":str(e)}, status = 400)
        
class GuardarSubcontrato(View):
    template_name = "crearSubcontratos.html"
    form_class = SubcontratoForm
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    subcontrato = form.save()
                    polizas = json.loads(request.POST.get("listpolizas"))
                    for p in polizas:
                        poliza = Poliza.objects.create(
                            tipo_poliza = p["data"]["tipo"],
                            número_poliza = p["data"]["número"],
                            aseguradora = p["data"]["aseguradora"],
                            fecha_vencimiento = p["data"]["vencimiento"]
                        )
                        subcontrato.polizas.add(poliza)
                    
                    dias = 0
                    if subcontrato.seguimiento_acta == "1":
                        dias = 7
                    elif subcontrato.seguimiento_acta == "2":
                        dias = 14
                    elif subcontrato.seguimiento_acta == "3":
                        dias = 15
                    elif subcontrato.seguimiento_acta == "4":
                        dias = 30
                    else:
                        raise Exception("En el campo seguimiento acta, por favor seleccione una opción válida.")
                        # return JsonResponse({"errores":{"seguimiento_acta":["Seleccione una opcion valida."]}}, status=400)
                    subcontrato.proximo_envio_correo = subcontrato.fecha_creacion+timedelta(days=dias)
                    subcontrato.save()
                    print(subcontrato.proximo_envio_correo)
                    print("se genero el dia del correo")
                    if request.POST.get("impo")=="si":
                        print("sdsds")
                        file = request.FILES["excelItems"]
                        if file:
                            df = pd.read_excel(file)
                            for index, row in df.iterrows():
                                try:
                                    data = {"subcontrato":subcontrato.pk,
                                        "item_codigo":row["Código ITEM"],
                                        "item_nombre":row["Item"],
                                        "descripcion":row["Descripción"],
                                        "unidad":row["Unidad"],
                                        "cantidad":row["Cantidad"],
                                        "valor_unitario":row["Valor Unitario"]}
                                except Exception as e:
                                    raise Exception("El formato del Excel es incorrecto, por favor verifique la columna: ", str(e))
                                validacion = validar_itemsSubcontrato(data, "excel")
                                if validacion == True:
                                    formItemSubcon = Item_Subcontrato.objects.create(subcontrato=subcontrato,
                                            item_codigo=Item.objects.get(codigo=row["Código ITEM"]),
                                            item_nombre=row["Item"],
                                            descripcion=row["Descripción"],
                                            unidad=row["Unidad"],
                                            cantidad=row["Cantidad"],
                                            valor_unitario=row["Valor Unitario"]
                                            )
                                else:
                                    print("validaciones desde el excel: ",validacion)
                            subcontrato.impo = True
                            subcontrato.save()
                    elif request.POST.get("impo")=="no":
                        items = json.loads(request.POST.get("items"))
                        if items:
                            for i in items:
                                codigo = i["data"]["codigo"]
                                item = i["data"]["item"]
                                descripcion = i["data"]["descripcion"]
                                unidad = i["data"]["unidad"]
                                cantidad = i["data"]["cantidad"]
                                valorUnitario = i["data"]["valorUnitario"]
                                print(codigo,item,descripcion,unidad,cantidad,valorUnitario)
                                data = {"subcontrato":subcontrato.pk,
                                        "item_codigo":codigo,
                                        "item_nombre":item,
                                        "descripcion":descripcion,
                                        "unidad":unidad,
                                        "cantidad":cantidad,
                                        "valor_unitario":valorUnitario}
                                validacion = validar_itemsSubcontrato(data, "html")
                                if validacion == True:
                                    formItemSubcon = Item_Subcontrato.objects.create(
                                            subcontrato=subcontrato,
                                            item_codigo=Item.objects.get(pk=codigo),
                                            item_nombre=item,
                                            descripcion=descripcion,
                                            unidad=unidad,
                                            cantidad=cantidad,
                                            valor_unitario=valorUnitario
                                            )
                                    print(formItemSubcon)
                                else:
                                    print("validaciones desde html: ",validacion)
                            subcontrato.impo = False
                            subcontrato.save()
                        else:
                            raise Exception("ítems: Debe ingresar los ítems, esta sección es obligatoria.")
            except Exception as e:
                print("hubo un error al crear el subcontrato",str(e))
                return JsonResponse({"errores":str(e), "tipo":"general"}, status=400)
            print(reverse("listsubcontratos"))
            return JsonResponse({"mensaje":"Creado correctamente","path":reverse("listsubcontratos")}, status=200)
        else:
            print("error al validar el formulario", form.errors)
            return JsonResponse({"errores":form.errors}, status=400) 

class ListarSubcontratos(ListView):
    template_name = "listarSubcontratos.html"
    model = Subcontrato
    context_object_name = "subcontratos"
    

    # def get(self, request,*args, **kwargs):
    #     from datetime import datetime
    #     contexto = {"nombrePersona": "Juan Manuel gaviria", "P": "Prueba", "id":"15", "fecha_creacion": datetime.now().date()}
    #     from Subcontratos.correo import enviarCorreo
    #     enviarCorreo("Recordatorio de realización de acta", "CorreosSubcontratos/RecordatorioActaBase.html", contexto, ["davitdy2015@gmail.com", "juanma28o123@gmail.com"])
    #     return super().get(request,*args, **kwargs)


class VerSubcontrato(DetailView):
    model = Subcontrato
    template_name = "verSubcontrato.html"
    context_object_name = "subcontrato"
    
    def get_context_data(self, **kwargs):
        context = super(VerSubcontrato, self).get_context_data(**kwargs)
        context["items"] = self.get_object().item_subcontrato_set.all()
        return context

class ModificarSubcontrato(UpdateView):
    template_name = "modificarSubcontrato.html"
    model = Subcontrato
    form_class = SubcontratoForm
    success_url = reverse_lazy("listsubcontratos")
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        print("el form es valido")
        return JsonResponse({"mensaje":"Creado correctamente","path":reverse("verSubcontrato", kwargs={'pk':self.get_object().pk})}, status=200)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class VerSeguimientoActa(DetailView):
    model = Acta
    template_name = "Actas/verSeguimientoActa.html"
    context_object_name = "acta"

class excelSubcontratos(TemplateView):  
    def validar_ExcelSubcontrato(self, item ,tipo):
        if not item["item_codigo"]:
            return {"error":"No hay un codigo en la lista."}
        
        if not item["item_nombre"]:
            return {"error":"No hay un item en la lista."}
        
        if not item["descripcion"]:
            return {"error":"No hay una descripción en la lista."}
        
        if not item["unidad"]:
            return {"error":"No hay un unidad en la lista."}
        
        if not item["cantidad"]:
            return {"error":"No hay un cantidad en la lista."}
        
        if not item["valor_unitario"]:
            return {"error":"No hay un valor unitario en la lista."}
        
        try:
            if tipo == "excel":
                Item.objects.get(codigo=item["item_codigo"])
            elif tipo == "html":
                Item.objects.get(pk=item["item_codigo"])
        except:
            return {"error":"No hay un item con este codigo {codigo} en la base de datos".format(codigo=item['item_codigo'])}
        
        try:
            x = int(item["cantidad"])
        except:
            return {"error":"Una cantidad no es un número"}
        
        try:
            x = int(item["valor_unitario"])
        except:
            return {"error":"Un valor unitario no es un número"}
        return True
    
    def post(self, request, *args, **kwargs):
        file = request.FILES["excel"]
        if file:
            self._items = []
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                try:
                    data = {
                        # "subcontrato":,
                        "item_codigo":row["Código ITEM"],
                        "item_nombre":row["Item"],
                        "descripcion":row["Descripción"],
                        "unidad":row["Unidad"],
                        "cantidad":row['Cantidad'],
                        "valor_unitario":row["Valor Unitario"]}
                except Exception as e:
                    return JsonResponse({'error':f"El formato del Excel es incorrecto, por favor verifique la columna: {str(e)}"}, status=400)
                validacion = self.validar_ExcelSubcontrato(data, "excel")
                if validacion == True:
                    self._items.append(data)
                else:
                    return JsonResponse(validacion, status=400)
        else:
            return JsonResponse({'error':'no se cargo ningún archivo'}, status=400)
        return JsonResponse({request.POST.get('subCapitulo'):self._items})