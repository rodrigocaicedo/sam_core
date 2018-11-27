from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from usuarios_sam.models import CustomUser

class Profesor(models.Model):
    usuario = models.ForeignKey(CustomUser)
    
    def __unicode__(self):
        return self.usuario.get_full_name()
    
class Estudiante(models.Model):
    usuario = models.ForeignKey(CustomUser)
    
    def __unicode__(self):
        return self.usuario.get_full_name()
    

class Capellan(models.Model):
    usuario = models.ForeignKey(CustomUser)
    
    def __unicode__(self):
        return self.usuario.get_full_name()
    


class InformeRemision(models.Model):
    fecha = models.DateField(auto_now_add  = True)
    estudiante = models.ForeignKey(Estudiante)
    profesor = models.ForeignKey(Profesor)
    capellan = models.ForeignKey(Capellan)
    comportamientos =  models.TextField(blank = True)
    estrategias = models.TextField(blank = True)
    reunion_padres = models.BooleanField(default = False)
    fecha_reunion = models.DateField(blank = True)
    acuerdos_padres = models.TextField(blank = True)
    reunion_estudiante = models.BooleanField(blank = True)
    acuerdos_estudiante = models.TextField(blank = True)
    fortalezas_estudiante = models.TextField(blank = True)
    fecha_psicologia = models.DateField(blank = True)
    fecha_capelllania = models.DateField(blank = True)
    acuerdos = models.TextField(blank = True)
    constancia_psicologia = models.DateField(blank = True)
    constancia_capellania = models.DateField(blank=True)
   

class InformeNovedades(models.Model):
    fecha = models.DateField(auto_now_add = True)
    estudiante = models.ForeignKey(Estudiante)
    profesor = models.ForeignKey(Profesor)
    capellan = models.ForeignKey(Capellan)
    novedades =  models.TextField(blank = True)
    
    
class InformeSeguimiento(models.Model):
    fecha = models.DateField(auto_now_add  = True)
    estudiante = models.ForeignKey(Estudiante)
    profesor = models.ForeignKey(Profesor)
    capellan = models.ForeignKey(Capellan)
    aspectos_estudiante = models.TextField(blank = True)
    academicos_antes = models.TextField(blank = True)
    academicos_ahora = models.TextField(blank = True)
    actitud_antes = models.TextField(blank = True)
    actitud_ahora = models.TextField(blank = True)
    estrategias = models.TextField(blank = True)
    reunion_padres = models.BooleanField(default = False)
    fecha_reunion = models.DateField(blank = True)
    acuerdos_padres = models.TextField(blank = True)
    reunion_estudiante = models.BooleanField(blank = True)
    acuerdos_estudiante = models.TextField(blank = True)
    informacion_adicional = models.TextField(blank = True)
    pedidos_apoyo = models.TextField(blank = True)


class InformeGeneral(models.Model):
    fecha = models.DateField(auto_now_add  = True)
    estudiante = models.ForeignKey(Estudiante)
    profesor = models.ForeignKey(Profesor)
    capellan = models.ForeignKey(Capellan)
    fortalezas_actitud = models.TextField(blank = True)
    fortalezas_destrezas = models.TextField(blank = True)
    debilidades_actitud = models.TextField(blank = True)
    debilidades_destrezas = models.TextField(blank = True)
    estrategias = models.TextField(blank = True)
    reunion_padres = models.BooleanField(default = False)
    fecha_reunion = models.DateField(blank = True)
    acuerdos_padres = models.TextField(blank = True)
    reunion_estudiante = models.BooleanField(blank = True)
    acuerdos_estudiante = models.TextField(blank = True)
    informacion_adicional = models.TextField(blank = True)
    pedidos_apoyo = models.TextField(blank = True)

    
class ControlDeFormulario(models.Model):
    fecha_entrega = models.DateField(auto_now_add  = True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

