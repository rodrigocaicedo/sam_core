# -*- coding: UTF-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Lista_Estudiantes(models.Model):
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.nombres + " " + self.apellidos

class Lista_Representante(models.Model):
    nombres = models.CharField(max_length = 200, unique = True)

    def __unicode__(self):
        return self.nombres

class Estudiantes_Representante(models.Model):
    RELACION = (
        ('P', "Padre"),
        ('M', 'Madre'),
        ("T", "Tío / tía"),
        ("A", "Abuelo / abuela"),
        ("O", "Otro"),
    )
    estudiante = models.ForeignKey('Lista_Estudiantes')
    representante = models.ForeignKey('Lista_Representante')
    relacion = models.CharField(max_length = 1 , choices = RELACION)

    class Meta:
        unique_together = ("estudiante", "representante","relacion")

    def __unicode__(self):
        return self.representante.nombres + "--" +self.estudiante.nombres + " " + self.estudiante.apellidos 


class Uniformes(models.Model):
    id_uniformes = models.AutoField(primary_key = True)
    referencia=models.IntegerField(null = False,blank=False)
    descripcion= models.CharField(max_length = 200)
    color=models.CharField(max_length = 80)
    talla=models.CharField(max_length = 10)
    precio=models.IntegerField()
    
   
    
    def __unicode__(self):
        return self.descripcion
        
class Cab_Proforma (models.Model):
    id_rep=models.ForeignKey('Lista_Representante')
    fecha=models.DateField()
    telefono_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    telefono = models.CharField(max_length = 9, validators=[telefono_regex], verbose_name = u"Teléfono de Domicilio del Representante")
    celular_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    celular = models.CharField(max_length = 10, validators = [celular_regex] , verbose_name = u"Teléfono Celular del Representante")
    total=models.IntegerField()
    
    def __unicode__(self):
        return self.id_rep
        
        
class Det_Proforma(models.Model):
    id_cab=models.ForeignKey('Cab_Proforma')
    id_estudiante=models.ForeignKey('Lista_Estudiantes')
    referencia=models.IntegerField(null = True,blank=True)
    descripcion= models.CharField(max_length = 200)
    color=models.CharField(max_length = 80)
    talla=models.CharField(max_length = 10)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    subtotal=models.IntegerField()
    
    def __unicode__(self):
        return self.id_cab
    
 
    