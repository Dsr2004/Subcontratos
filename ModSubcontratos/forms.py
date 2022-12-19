from django import forms
from .models import Subcontrato, Item_Subcontrato

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
            "seguimiento_acta": forms.Select(attrs={"class":"form-select"}),
            "fecha_inicio_contrato": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off"}),
            "fecha_vencimiento_contrato": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off"}),
            "director_obra": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "gestor_contrato": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "correo_notificacion_proveedor": forms.EmailInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "validadores": forms.SelectMultiple(attrs={"class":"form-select", "id":"validadores"}),
            "polizas": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}),
            "contrato": forms.FileInput(attrs={"class":"form-control form-control-sm", "autocomplete":"off"}),
            "polizas_garantias": forms.FileInput(attrs={"class":"form-control form-control-sm", "autocomplete":"off"}),
            "acta_inicio": forms.FileInput(attrs={"class":"form-control form-control-sm", "autocomplete":"off"}),
            "modificaciones_contractuales": forms.FileInput(attrs={"class":"form-control form-control-sm", "autocomplete":"off"}),
            "acta_recibo_final": forms.FileInput(attrs={"class":"form-control form-control-sm", "autocomplete":"off"}),
            "acta_liquidacion": forms.FileInput(attrs={"class":"form-control form-control-sm", "autocomplete":"off"}),
        }
    def __init__(self, *args, **kwargs):
        super(SubcontratoForm, self).__init__(*args, **kwargs)
        self.fields['contrato'].required = False
        self.fields['polizas_garantias'].required = False
        self.fields['acta_inicio'].required = False
        self.fields['modificaciones_contractuales'].required = False
        self.fields['acta_recibo_final'].required = False
        self.fields['acta_liquidacion'].required = False
        
        self.fields['estado'].required = False
        self.fields['tarifa_iva'].required = False
        self.fields['porcentaje_administracion'].required = False
        self.fields['porcentaje_imprevistos'].required = False
        self.fields['porcentaje_utilidad'].required = False
        self.fields['polizas'].required = False
        
        
class Item_SubcontratoForm(forms.ModelForm):
    class Meta:
        model = Item_Subcontrato
        fields = "__all__"