#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from tinymce.widgets import TinyMCE

from comunicaciones_sam.models import Comunicacion, Adjunto

class ComunicacionForm(forms.ModelForm):

	html = forms.CharField(widget=TinyMCE(
		attrs={'style': 'width : 100%', 'rows':'20'}, 
		mce_attrs = {'theme':'advanced', 'theme_advanced_buttons1' : "bold,italic,underline,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,|,bullist,numlist,|,code", 'browser_spellcheck': 'true', 'language' : 'es'}
		))
	#html = forms.CharField(widget=TinyMCE(attrs={}, mce_attrs = {'theme':'advanced'}))
	#html = forms.CharField(widget=TinyMCE(attrs={'class': "col-md-12 col-sm-12 col-xs-12"}))

	class Meta:
		model = Comunicacion
		exclude = []


class AdjuntoForm(forms.ModelForm):

	class Meta:
		model = Adjunto
		widgets = {'attachment':forms.ClearableFileInput(attrs={"multiple":True})}
		exclude = ['attached_to']
        #widgets = {'attachment': forms.ClearableFileInput(attrs={'multiple': True, "print":True,}),}