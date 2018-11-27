#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import uuid
from django.db import models
from usuarios_sam.models import CustomUser

from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator
#from .validators import validate_file_extension
from django.core.exceptions import ValidationError



    
    
class Invoices(models.Model):
    id_invoice = models.AutoField(primary_key = True)
    name = models.CharField(max_length =25,null=False,blank=False)
    surname = models.CharField(max_length =25,null=False,blank=False)
    identity_card = models.CharField(max_length =13,null=False,blank=False)
    address = models.CharField(max_length =80,null=False,blank=False)
    phone_regex = RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone = models.CharField(max_length = 9, validators=[phone_regex], verbose_name = u"Teléfono de Domicilio",null=False,blank=False)
    cell_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell = models.CharField(max_length = 10, validators = [cell_regex] , verbose_name = u"Teléfono Celular",null=False,blank=False)
    email=models.EmailField(max_length = 254,null=False,blank=False)
    id_students = models.CharField(max_length =254)
    date_update=models.DateField( null=True, blank=True)
   
    def __unicode__(self):
        return str(self.id_invoice)

class Relation(models.Model):
    identity=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email_s=models.CharField(max_length =254)
    email_r=models.CharField(max_length =254)
    
    def __unicode__(self):
        return str(self.identity)