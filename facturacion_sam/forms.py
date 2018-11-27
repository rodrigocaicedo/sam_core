from django import forms
from django.db import models
from facturacion_sam.models import Invoices
from usuarios_sam.models import CustomUser

class Invoicesnewform(forms.ModelForm):

    class Meta:
        model = Invoices
        fields = ['name','surname','identity_card','address','phone','cell','email']
   