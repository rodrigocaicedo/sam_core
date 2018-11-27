from django import forms
from capellania_sam.models import InformeGeneral, InformeRemision, InformeNovedades, InformeSeguimiento, ControlDeFormulario

class InformeGeneralForm(forms.ModelForm):

    class Meta:
        model = InformeGeneral
        exclude = []

#class ItemForm_Check(forms.ModelForm):
#    class Meta:
#        model = Pedido_Item
#        #fields = ['profesor','item','cantidad','presentacion','detalle','descripcion_uso','materia']
#        exclude=('profesor','fecha','materia','descripcion_uso',)


#class AprobacionForm(forms.Form):
#    class Meta:
#        model = Aprobacion_Item

#class ValoracionForm(forms.ModelForm):
#    class Meta:
#        model = Valoracion_Item
#        fieds = ["item", "proveedor", "valor"]
