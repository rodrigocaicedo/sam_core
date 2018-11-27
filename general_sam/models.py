#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import string
from datetime import date

from django.db import models, IntegrityError

from django.core.exceptions import ValidationError

from usuarios_sam.models import Students, People, Teacher, Student, Relative, Student_Relative

from usuarios_sam.authhelper import get_token_from_shared_secret

from usuarios_sam.outlookservice import get_groups, create_group, user_to_group, check_member




"""el model periodo lectivo define la unidad de funcionamiento del colegio, al año lectivo.
Por esto, su definicion es bastante simple."""



class Periodo_Lectivo(models.Model):
    inicio = models.DateField(null=False, blank=False, unique = True)
    fin = models.DateField(null=False, blank=False, unique = True)
    actual = models.BooleanField(default = False)


    def __unicode__(self):
        return "{0}-{1}".format(self.inicio.strftime("%Y"), self.fin.strftime("%Y"))

class Seccion(models.Model):
	nombre = models.CharField(max_length = 50, blank = False, null = False)
	activo = models.BooleanField(blank = False, null = False, default = True)

	def __unicode__(self):
		return self.nombre



class Nivel(models.Model):
	seccion = models.ForeignKey(Seccion, blank = True, null = True)
	nombre = models.CharField(max_length = 50, blank = False, null = False, unique = True)
	nombre_ministerio = models.CharField(max_length = 50, blank = False, null = False)
	nombre_aplicaciones = models.CharField(max_length = 50, blank = False, null = False)
	activo = models.BooleanField(blank = False, null = False, default = False)

	def __unicode__(self):
		return self.nombre


class Clase(models.Model):
	periodo_lectivo = models.ForeignKey(Periodo_Lectivo)
	nivel = models.ForeignKey(Nivel)
	paralelo = models.CharField(max_length = 3, blank = False, null = False)
	capacidad = models.IntegerField(default=25)

	class Meta:
		unique_together = ("periodo_lectivo", "nivel","paralelo")

	def __unicode__(self):
		return "{0} {1} - {2}".format(self.nivel, self.paralelo, self.periodo_lectivo)



class Homeroom_Registry(models.Model):
	clase = models.ForeignKey(Clase)
	homeroom = models.ForeignKey(Teacher)
	inicio = models.DateField()
	fin = models.DateField(blank = True, null = True)


	def __unicode___(self):
		return "{0} - {1}".format(self.clase, self.homeroom.id_teachers.get_full_name())

class Aptitud_Matricula(models.Model):
	estudiante = models.ForeignKey(Student)
	nivel = models.ForeignKey(Nivel)
	periodo_lectivo = models.ForeignKey(Periodo_Lectivo)
	observaciones = models.TextField(blank = True, null = True)
	tipo = models.CharField(max_length = 1, choices = ((u"A", u"Antiguo"), (u"N", u"Nuevo")))
	fecha = models.DateField(auto_now_add = True)
	matriculado = models.BooleanField(default = False)
	resuelto = models.DateField(blank = True, null = True)

	class Meta:
		unique_together = ("periodo_lectivo", "estudiante", "nivel")

	def __unicode__(self):
		return "{0} - {1}".format(self.estudiante.user.get_legal_name(), self.periodo_lectivo)


class Matricula(models.Model):
	estudiante = models.ForeignKey(Student)
	clase = models.ForeignKey(Clase)
	tipo = models.CharField(max_length = 2, choices = ((u"OR", u"Ordinaria"), (u"EX", u"Extraordinaria"), (u"PA", u"Pase de Año")))
	fecha = models.DateField(auto_now_add = True)

	class Meta:
		unique_together = ("clase", "estudiante")

	def __unicode__(self):
		return "{0} - {1}".format(self.estudiante.user.get_legal_name(), self.clase)


class Estado_Matricula(models.Model):
	"""
	Tabla para registrar y consultar el último estado (activo o inactivo) de una matrícula.
	"""
	matricula = models.ForeignKey(Matricula)
	matricula_activa = models.BooleanField()
	observaciones = models.CharField(max_length = 400, blank = True)
	inicio = models.DateField(auto_now_add = True)
	fin = models.DateField(blank = True, null = True)


class Grupo(models.Model):

	#USO INTERNO: Modelo que define los diferentes grupos en la escuela en cada año lectivo. Inicialmente, todas la clases tienen un grupo, pero este objeto también se define en casos de clases cque se dividan, etc.
	nombre = models.CharField(max_length = 100)
	periodo_lectivo = models.ForeignKey(Periodo_Lectivo)
	activo = models.BooleanField(default = False)
	o365_id = models.CharField(max_length = 150, blank = True)

	class Meta:
		unique_together = ("nombre", "periodo_lectivo")

	def __unicode__(self):
		return "{0} {1}".format(self.periodo_lectivo, self.nombre)

	def save(self, *args, **kwargs):
		nombre = "Estudiantes de {0}".format(self.nombre)
		self.o365_id = ""
		grupos = get_groups(nombre)
		for x in grupos["value"]:
			if x["displayName"] == nombre:
				self.o365_id = x["id"]
		if not self.o365_id or self.o365_id == "":
			#nick = nick.decode("utf-8")
			nick = nombre
			nick = nick.replace(" de ", ".")
			nick = "".join((nick).split())
			nick = nick.lower()
			grupo = create_group(nombre, nick)
			self.o365_id = grupo["id"]
		super(Grupo,self).save(*args,**kwargs)



class Matricula_Grupo(models.Model):

	#USO INTERNO: Registro de los estudiantes en los grupos que les correspondan. Estos registros pueden ser dinámicos, según la necesidad de existencia de los grupos.
	matricula = models.ForeignKey(Matricula)
	grupo = models.ForeignKey(Grupo)
	inicio = models.DateField(auto_now_add = True)
	fin = models.DateField(blank = True, null = True)

	class Meta:
		unique_together = ("matricula", "grupo", "inicio", "fin")

	def __unicode__(self):
		return "{0} {1}".format(self.matricula.estudiante, self.grupo)


	def save(self, *args, **kwargs):

		if Matricula_Grupo.objects.filter(matricula = self.matricula, grupo = self.grupo, fin = None).exclude(pk = self.pk).exists():
			raise IntegrityError("Existe un registro vigente en este grupo.")


		if check_member(self.matricula.estudiante.user.email, self.grupo.o365_id) == False:
			user_to_group(self.matricula.estudiante.user.email, self.grupo.o365_id)


		super(Matricula_Grupo,self).save(*args,**kwargs)
            

class Area_Academica(models.Model):

	#USO INTERNO: Modelo que define las direferentes áreas académicas a las que las Materias pueden responder.
	nombre = models.CharField(max_length = 150, blank = False, null = False, unique=True)

	def __unicode__(self):
		return self.nombre


class Materia_Escolar(models.Model):

	#USO INTERNO: Modelo que define las materias que se imparten realmente en la escuela, más allá de las definiciones legales: malla curricular, quimestres, parciales, etc.
	area_academica = models.ForeignKey(Area_Academica, blank = True, null = True)
	nombre = models.CharField(max_length = 50, blank = False, null = False, unique = True)
	activo = models.BooleanField(blank = False, null = False, default = False)




	def __unicode__(self):
		return self.nombre




class Materia_Grupo(models.Model):

	#USO INTERNO: Modelo para el registro de los objetos "Materia_Escolar" que se imparten a los diferentes grupos, más allá de las definiciones legales.
	grupo = models.ForeignKey(Grupo)
	materia = models.ForeignKey(Materia_Escolar)
	inicio = models.DateField(null = False, blank = False)
	fin = models.DateField(blank = True, null = True)

	def __unicode__(self):
		return "{0}-{1}".format(self.materia.nombre, self.grupo.nombre)


	def save(self, *args, **kwargs):

		if Materia_Grupo.objects.filter(materia = self.materia, grupo = self.grupo, fin = None).exclude(pk = self.pk).exists():
			raise IntegrityError("Existe un registro vigente en este grupo.")

		super(Materia_Grupo,self).save(*args,**kwargs)




class Asignacion_Profesores(models.Model):

	#USO INTERNO: Registro de profesores responsables de los objetos "Materia_Grupo"
	profesor = models.ForeignKey(Teacher)
	actividad = models.ForeignKey(Materia_Grupo)
	inicio = models.DateField(null = False, blank = False)
	fin = models.DateField(blank = True, null = True)

	def __unicode__(self):
		return "{0}-{1}".format(self.actividad, self.profesor.id_teachers.get_full_name())
   