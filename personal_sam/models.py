#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.db import models
from usuarios_sam.models import CustomUser
import uuid
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

class Type_Permissions(models.Model):
    type=models.CharField(max_length=30,null=False,blank=False)
    discountable=models.BooleanField(default = False)

class Permissions(models.Model):
    date = models.DateField(_("Date"), default=date.today)
    applicant = models.CharField(max_length=100,null=False,blank=False)
    date_initial = models.DateField()
    date_end = models.DateField(null = True,blank=True)
    days=models.IntegerField(null=True,blank=True)
    hours=models.IntegerField(null=True,blank=True)
    reason=models.CharField(max_length=300,null=False,blank=False)
    id_type = models.ForeignKey('Type_Permissions')
 
    def __unicode__(self):
        return str(self.date) + " " + str(self.applicant)
        
class Delegated_Activities(models.Model):
    id_permissions = models.ForeignKey('Permissions')
    activity=models.CharField(max_length=300,null = True,blank=True)
    hour = models.TimeField(null = True,blank=True)
    responsable=models.CharField(max_length=100,null=False,blank=False)
    observations= models.CharField(max_length=300,null = True,blank=True)
    
    def __unicode__(self):
        return str(self.activity) + " " + str(self.responsable)
        
        
class State_Permissions(models.Model):
    state = models.CharField(max_length=20)
    date_initial = models.DateField()
    date_end = models.DateField(null=True,blank=True)
    user=models.CharField(max_length=20)
    observations = models.CharField(max_length=200,null = True)
    id_permissions  = models.ForeignKey('Permissions') 
    
    def __unicode__(self):
        return str(self.state) + " " + str(self.date_initial)
        