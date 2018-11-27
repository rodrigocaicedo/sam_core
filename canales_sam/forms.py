#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from comunicaciones_sam.models import Comunicacion



class ComunicacionForm(forms.ModelForm):

	html = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs = {'theme':'advanced'}))

	class Meta:
		model = Comunicacion
		exclude = []


class TicketForm(forms.Form):
	tutor = forms.CharField(max_length = 150, label = "Nombre del representante")
	email = forms.EmailField(label = "Email del representante")
	student = forms.CharField(max_length = 150, label = "Nombre del estudiante")
	subject = forms.CharField(max_length = 200, label = "Asunto")
	message = forms.CharField(widget=forms.Textarea, label = "Mensaje")
	#grade = forms.CharField(max_length = 150, label = "Grado")



class TicketTemasForm(forms.Form):
	tutor = forms.CharField(max_length = 150, label = "Nombre del representante")
	email = forms.EmailField(label = "Email del representante")
	student = forms.CharField(max_length = 150, label = "Nombre del estudiante")
	subject = forms.CharField(max_length = 200, label = "Asunto")
	message = forms.CharField(widget=forms.Textarea, label = "Mensaje")
	grade = forms.CharField(max_length = 150, label = "Grado")