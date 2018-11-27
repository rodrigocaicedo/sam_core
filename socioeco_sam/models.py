# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import uuid

from django.db import models
from django.core.validators import RegexValidator

from django_countries.fields import CountryField

from general_sam.models import Clase




# Create your models here.

class Evaluacion_Socioeco(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	requerido = models.BooleanField(default = False)
	solicitante = models.CharField(max_length = 200)
	email = models.EmailField()
	inicio = models.DateField(auto_now_add = True)
	enviado = models.DateField(blank=True, null=True)
	resuelto = models.BooleanField(default = False)
	motivo_solicitud = models.TextField(null = True, blank=True, default = "")
	capacidad_pago = models.IntegerField(default = 0)
	familia = models.CharField(max_length = 200)

	class Meta:
		unique_together = ("email","resuelto")

	def __unicode__(self):
		return u"{} {}".format(self.solicitante,self.email)


class Aceptacion(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	aceptacion = models.BooleanField(default = False)



class Representante(models.Model):
	PADRE = "PADRE"
	MADRE = "MADRE"
	ABUELO = "ABUELO"
	ABUELA = "ABUELA"
	TIO = "TIO"
	TIA = "TIA"
	OTRO = "OTRO"
	RELACION_CHOICES = (
		(PADRE, "Padre"),
		(MADRE, "Madre"),
		(ABUELO, "Abuelo"),
		(ABUELA, "Abuela"),
		(TIO, "Tío"),
		(TIA, "Tía"),
		(OTRO, "Otro"),
		)

	evaluacion_socioeco = models.ForeignKey("Evaluacion_Socioeco")
	relacion = models.CharField(max_length = 6, choices = RELACION_CHOICES)
	nombres = models.CharField(max_length = 200)
	apellido_paterno = models.CharField(max_length = 200)
	apellido_materno = models.CharField(max_length = 200)
	numero_id = models.CharField(max_length = 20)

	CASADO = "CASADO"
	SOLTERO = "SOLTERO"
	VIUDO = "VIUDO"
	DIVORCIADO = "DIVORCIADO"
	ESTADO_CIVIL_CHOICES = (
		(CASADO, "Casado"),
		(SOLTERO, "Soltero"),
		(VIUDO, "Viudo"),
		(DIVORCIADO, "Divorciado"),
		(OTRO, "Otro"),
		)
	
	estado_civil = models.CharField(max_length = 10, choices = ESTADO_CIVIL_CHOICES)
	fecha_nacimiento = models.DateField()
	pais_nacimiento = CountryField(default = "EC")
	ciudad_nacimiento = models.CharField(max_length = 20)
	
	BASICA = "BASICA"
	BACHILLERATO = "BACHILLERATO"
	TERCER_NIVEL = "TERCER NIVEL"
	CUARTO_NIVEL = "CUARTO NIVEL"
	NIVEL_ESTUDIOS_CHOICES = (
		(BASICA, "Básica"),
		(BACHILLERATO, "Bachillerato"),
		(TERCER_NIVEL, "Tercer Nivel"),
		(CUARTO_NIVEL, "Cuarto Nivel"),
		)

	nivel_estudios = models.CharField(max_length = 15, choices = NIVEL_ESTUDIOS_CHOICES)
	titulo = models.CharField(max_length = 30, blank = True)
	telefono_fijo_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
	telefono_casa = models.CharField(max_length = 9, validators=[telefono_fijo_regex], verbose_name = u"Teléfono del Domicilio")
	telefono_celular_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
	telefono_celular = models.CharField(max_length = 10, validators = [telefono_celular_regex] , verbose_name = u"Teléfono Celular")
    
	MOVISTAR = "MOVISTAR"
	CLARO = "CLARO"
	CNT = "CNT"
	OTRA = "OTRA"
	OPERADORA_CHOICES = (
    	(MOVISTAR, "Movistar"),
    	(CLARO, "Claro"),
    	(CNT, "Cnt"),
	(OTRA, "Otra"),
    	)

	operadora_celular = models.CharField(max_length = 8, choices = OPERADORA_CHOICES)
	numero_hijos = models.IntegerField()
	lugar_trabajo = models.CharField(max_length = 50)
	cargo = models.CharField(max_length = 50)
	tiempo_trabajo = models.IntegerField()
	direccion_trabajo = models.CharField(max_length = 250)
	telefono_trabajo = models.CharField(max_length = 9, validators=[telefono_fijo_regex], verbose_name = u"Teléfono del Trabajo")
	correo_personal = models.EmailField()
	correo_trabajo = models.EmailField()

	class Meta:
		unique_together = ("evaluacion_socioeco","nombres","apellido_paterno", "apellido_materno", "numero_id")

	def __unicode__(self):
		return u"{} {}".format(self.nombres,self.apellido_paterno)


class Estudiante(models.Model):
	evaluacion_socioeco = models.ForeignKey("Evaluacion_Socioeco")
	nombres = models.CharField(max_length = 200)
	apellido_paterno = models.CharField(max_length = 200)
	apellido_materno = models.CharField(max_length = 200)
	numero_id = models.CharField(max_length = 20)
	
	MASCULINO = "MASCULINO"
	FEMENINO = "FEMENINO"

	GENERO_CHOICES = (
		(MASCULINO,"Masculino"),
		(FEMENINO,"Femenino"),
		)


	genero = models.CharField(max_length = 15, choices = GENERO_CHOICES)
	fecha_nacimiento = models.DateField()
	pais_nacimiento = CountryField(default = "EC")
	ciudad_nacimiento = models.CharField(max_length = 20)
	nivel = models.ForeignKey(Clase)

	class Meta:
		unique_together = ("evaluacion_socioeco","nombres","apellido_paterno", "apellido_materno", "numero_id")

	def __unicode__(self):
		return u"{} {}".format(self.nombres,self.apellido_paterno)


class Domicilio(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	pais_residencia = CountryField()
	provincia_residencia = models.CharField(max_length = 20)
	ciudad_residencia = models.CharField(max_length = 20)
	parroquia_residencia = models.CharField(max_length = 20)
	
	URBANO = "URBANO"
	URBANO_MARGINAL = "URBANO-MARGINAL"
	RURAL = "RURAL"

	TIPO_PARROQUIA_CHOICES = (
		(URBANO,"Urbano"),
		(URBANO_MARGINAL, "Urbano-marginal"),
		(RURAL,"Rural"),
		)

	tipo_parroquia = models.CharField(max_length = 20, choices = TIPO_PARROQUIA_CHOICES, default = "")
	barrio = models.CharField(max_length = 20)

	NORTE = "NORTE"
	CENTRO = "CENTRO"
	SUR = "SUR"
	VALLES = "VALLES"
	SUBURBIO = "SUBURBIO"
	ZONA_RURAL = "ZONA RURAL"

	ZONA_CHOICES = (
		(NORTE, "Norte"),
		(CENTRO, "Centro"),
		(SUR, "Sur"),
		(VALLES, "Valles"),
		(SUBURBIO, "Suburbio"),
		(ZONA_RURAL, "Zona Rural"),
		)


	zona = models.CharField(max_length = 15, choices = ZONA_CHOICES, default = "")
	direccion_principal = models.CharField(max_length = 30)
	direccion_secundaria = models.CharField(max_length = 30)
	direccion_numero = models.CharField(max_length = 20)

	telefono_fijo_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
	telefono_casa = models.CharField(max_length = 9, validators=[telefono_fijo_regex], verbose_name = u"Teléfono del Domicilio")	


class Integrante_Familia(models.Model):
	evaluacion_socioeco = models.ForeignKey("Evaluacion_Socioeco")
	nombres_completos = models.CharField(max_length = 50)
	fecha_nacimiento = models.DateField()
	numero_id = models.CharField(max_length = 20)

	CASADO = "CASADO"
	SOLTERO = "SOLTERO"
	VIUDO = "VIUDO"
	DIVORCIADO = "DIVORCIADO"
	OTRO = "OTRO"
	ESTADO_CIVIL_CHOICES = (
		(CASADO, "Casado"),
		(SOLTERO, "Soltero"),
		(VIUDO, "Viudo"),
		(DIVORCIADO, "Divorciado"),
		(OTRO, "Otro"),
		)
	estado_civil = models.CharField(max_length = 10, choices = ESTADO_CIVIL_CHOICES, default= "")
	parentesco = models.CharField(max_length = 20)
	INICIAL = "INICIAL"
	BASICA = "BASICA"
	BACHILLERATO = "BACHILLERATO"
	TERCER_NIVEL = "TERCER NIVEL"
	CUARTO_NIVEL = "CUARTO NIVEL"
	NIVEL_ESTUDIOS_CHOICES = (
		(INICIAL, "Inicial"),
		(BASICA, "Básica"),
		(BACHILLERATO, "Bachillerato"),
		(TERCER_NIVEL, "Tercer Nivel"),
		(CUARTO_NIVEL, "Cuarto Nivel"),
		)

	nivel_estudios = models.CharField(max_length = 15, choices = NIVEL_ESTUDIOS_CHOICES, default = "")
	titulo = models.CharField(max_length = 50, blank = True)
	actividad = models.CharField(max_length = 50)
	enfermedad_cronica = models.CharField(max_length = 50, blank = True)
	discapacidad = models.CharField(max_length = 50, blank = True)
	validado = models.BooleanField(default = False)

	class Meta:
		unique_together = ("evaluacion_socioeco","nombres_completos", "numero_id")

	def __unicode__(self):
		return u"{}".format(self.nombres_completos)


class Situacion_Habitacional(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	
	PROPIA = "PROPIA"
	ARRENDADA = "ARRENDADA"
	CEDIDA_TRABAJO = "TRABAJO"
	CEDIDA_FAMILIAR = "FAMILIAR"
	OTRA = "OTRA"

	POSESION_VIVIENDA_CHOICES = (
		(PROPIA, "Propia"),
		(ARRENDADA, "Arrendada"),
		(CEDIDA_TRABAJO, "Cedida por el trabajo"),
		(CEDIDA_FAMILIAR, "Cedida por algún familiar"),
		(OTRA, "otra"),
		)

	posesion_vivienda = models.CharField(max_length = 20, choices = POSESION_VIVIENDA_CHOICES, default = "")
	tipo_vivienda = models.CharField(max_length = 40)

	CONCRETO = "CONCRETO"
	ADOBE = "ADOBE"
	MADERA = "MADERA"
	ESTRUCTURA_VIVIENDA_CHOICES = (
		(CONCRETO, "Concreto"),
		(ADOBE, "Adobe"),
		(MADERA, "Madera"),
		)
	
	estructura_vivienda = models.CharField(max_length = 10, choices = ESTRUCTURA_VIVIENDA_CHOICES, default = "")
	agua_potable = models.BooleanField()
	alcantarillado = models.BooleanField()
	electricidad = models.BooleanField()
	telefono_fijo = models.BooleanField()
	internet = models.BooleanField()
	tv_cable = models.BooleanField()

	def __unicode__(self):
		return u"{}".format(self.evaluacion_socioeco)


class Responsable_Gastos(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	responsable_gastos = models.CharField(max_length = 100)
	

class Propiedades(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	cantidad_inmuebles = models.IntegerField()
	valor_inmuebles = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2)
	cantidad_vehiculos = models.IntegerField()
	valor_vehiculos = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2)

	def __unicode__(self):
		return u"{}".format(self.evaluacion_socioeco)	


class Ingresos(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	dependencias = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	negocios = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	inversiones = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	arriendos = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	otros = models.CharField(max_length = 120, blank = True)
	otros_ingreso = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0, blank = True)

	def __unicode__(self):
		return u"{}".format(self.evaluacion_socioeco)	


class Gastos(models.Model):
	evaluacion_socioeco = models.OneToOneField("Evaluacion_Socioeco")
	gastos_vivienda = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	gastos_alimentacion = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	gastos_educacion = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	gastos_transporte = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	gastos_salud = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	gastos_vestimenta = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0)
	gastos_otros = models.IntegerField(default = 0)#DecimalField(max_digits=8, decimal_places =2, default = 0, blank = True)

	def __unicode__(self):
		return u"{}".format(self.evaluacion_socioeco)	
