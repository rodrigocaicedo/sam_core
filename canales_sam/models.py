# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import Group


from usuarios_sam.models import CustomUser as User


class Registro_Temas(models.Model):
	usuario = models.ForeignKey(User)
	id_ticket = models.CharField(max_length = 10)
	correo_ticket = models.EmailField()


	def __unicode__(self):
		return self.usuario.get_full_name()

class Registro_Grupos(models.Model):
	grupo = models.ForeignKey(Group)
	id_ticket = models.CharField(max_length = 10)
	correo_ticket = models.EmailField()
	nombre = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombre
# Create your models here.
