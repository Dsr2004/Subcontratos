import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from .models import *
from .forms import SubcontratoForm

# Create your views here.
class SubContratos(View):
    template_name = "crearSubcontratos.html"
    
    def get(self, request, *args, **kwargs):
        ultimo_id = Subcontrato.objects.last()
        if ultimo_id:ultimo_id+=1
        else:ultimo_id=1
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
        if request.POST.get("impo")=="si":
            file = request.FILES["excelItems"]
            if file:
                df = pd.read_excel(file)
                print(df)
        form = self.form_class(request.POST)
        if form.is_valid():
            print("yes")
            return HttpResponse(request.POST)
        else:
            return JsonResponse({"errores":form.errors}, status=400) 
        