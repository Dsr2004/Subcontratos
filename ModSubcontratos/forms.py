from django import forms
from .models import Subcontrato

class SubcontratoForm(forms.ModelForm):
    class Meta:
        model = Subcontrato
        fields = "__all__"
        widgets = {
            "tipo_contrato": forms.Select(attrs={"class":"form-select","autocomplete":"off","onchange":"getComboA(this)"}),
            "elaborador": forms.Select(attrs={"class":"form-control","id":"elaborador","style":"width: 100%;","autocomplete":"off"}),
            "proyecto": forms.Select(attrs={"class":"form-control", "id":"proyecto","autocomplete":"off"}),
            "proveedor": forms.Select(attrs={"class":"form-control","id":"proveedor", "autocomplete":"off"}),
            "tipo_orden": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "numero_orden": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "tarifa_iva": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "porcentaje_administracion": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "porcentaje_imprevistos": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "porcentaje_utilidad": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "seguimiento_acta": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "fecha_inicio_contrato": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "fecha_vencimiento_contrato": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "director_obra": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "gestor_contrato": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "correo_notificacion_proveedor": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "validadores": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "polizas": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "contrato": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "polizas_garantias": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "acta_inicio": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "modificaciones_contractuales": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "acta_recibo_final": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "acta_liquidacion": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
           
        
        }