#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
#from django.contrib.flatpages.models import FlatPage

from .models import Ingresos, Gastos, Evaluacion_Socioeco, Representante, Estudiante, Domicilio, Integrante_Familia, Situacion_Habitacional, Responsable_Gastos, Propiedades



class EvaluacionForm(forms.ModelForm):

	class Meta:
		model = Evaluacion_Socioeco
		exclude = ["requerido", 'familia', 'inicio', 'resuelto', 'motivo_solicitud', 'capacidad_pago']


class FinalizarForm(forms.ModelForm):

	class Meta:
		model = Evaluacion_Socioeco
		exclude = ['requerido', 'familia', 'inicio', 'resuelto', 'solicitante', 'email']

class RepresentanteForm(forms.ModelForm):

	class Meta:
		model = Representante
		exclude = ['evaluacion_socioeco']


class EstudianteForm(forms.ModelForm):

	class Meta:
		model = Estudiante
		exclude = ['evaluacion_socioeco']

	def __init__(self, *args, **kwargs):
		super(EstudianteForm, self).__init__(*args, **kwargs)
		self.fields['nivel'].label_from_instance = lambda obj: "{0}{1}".format(obj.nivel, obj.paralelo)
		#self.fields['nivel'].label_from_instance = lambda obj: "Que bonito, no?"

class DomicilioForm(forms.ModelForm):

	class Meta:
		model = Domicilio
		exclude = ['evaluacion_socioeco']


class IntegranteForm(forms.ModelForm):
	class Meta:
		model = Integrante_Familia
		exclude = ['evaluacion_socioeco']


class HabitacionalForm(forms.ModelForm):
	class Meta:
		model = Situacion_Habitacional
		exclude = ['evaluacion_socioeco']


class ResponsableForm(forms.ModelForm):
	class Meta:
		model = Responsable_Gastos
		exclude = ['evaluacion_socioeco']

class PropiedadesForm(forms.ModelForm):
	class Meta:
		model = Propiedades
		exclude = ['evaluacion_socioeco']
		localized_fields = '__all__'

class IngresosForm(forms.ModelForm):
	class Meta:
		model = Ingresos
		exclude = ['evaluacion_socioeco']
		localized_fields = '__all__'

class GastosForm(forms.ModelForm):
	class Meta:
		model = Gastos
		exclude = ['evaluacion_socioeco']
		localized_fields = '__all__'