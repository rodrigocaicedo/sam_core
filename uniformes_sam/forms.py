from django import forms
from django.db import models
from uniformes_sam.models import Lista_Estudiantes,Lista_Representante,Estudiantes_Representante,Uniformes,Cab_Proforma,Det_Proforma

class CabProformanewform(forms.ModelForm):

    class Meta:
        model = Cab_Proforma
        fields = ['id_rep','fecha','telefono','celular','total']
   
