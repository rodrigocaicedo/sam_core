#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from general_sam.models import *


# Register your models here.
admin.site.register(Periodo_Lectivo)
admin.site.register(Seccion)
admin.site.register(Nivel)
admin.site.register(Clase)
admin.site.register(Matricula)
admin.site.register(Estado_Matricula)
admin.site.register(Homeroom_Registry)
admin.site.register(Aptitud_Matricula)
admin.site.register(Grupo)
admin.site.register(Matricula_Grupo)
admin.site.register(Area_Academica)
admin.site.register(Materia_Escolar)
admin.site.register(Materia_Grupo)
admin.site.register(Asignacion_Profesores)


