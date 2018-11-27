from django import forms
from general_sam.models import Aptitud_Matricula

class Edita_Aptitud_Form(forms.ModelForm):

    class Meta:
        model = Aptitud_Matricula
        exclude = ['estudiante', 'periodo_lectivo']

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