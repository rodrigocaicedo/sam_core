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
from .validators import validate_file_extension
from django.core.exceptions import ValidationError


class Applications(models.Model):
    id_applications = models.AutoField(primary_key = True)
    nuevo = 'NEW'
    hermanos = 'OLD'
    type_student_choices = (
    (nuevo, 'Nuevo'),
    (hermanos, 'Con Hermanos'),
    )
    type_student = models.CharField(max_length=3,choices=type_student_choices,default=nuevo)
    date_application = models.DateTimeField(default = timezone.now)
    name_student = models.CharField(max_length = 25)
    surname_student = models.CharField(max_length = 25)
    female ='F'
    male='M'
    gender_student_choices=(
    (female, 'Femenino'),
    (male, 'Masculino'),
    )   
    gender_student = models.CharField(max_length = 1,choices=gender_student_choices,default=female)
    birth_date = models.DateField()
    birth_country = CountryField()
    country_home = CountryField()
    
    NIVELES = (
        (u'Inicial 1 (de 2 a 3 años)', u'Inicial 1 (de 2 a 3 años)'),
        (u'Inicial 2 (de 3 a 4 años)', u'Inicial 2 (de 3 a 4 años)'),
        (u'Inicial 2 (de 4 a 5 años) / Prekinder', u'Inicial 2 (de 4 a 5 años) / Prekinder'),
        (u'1ro de Básica / Kinder', u'1ro de Básica / Kinder'),
        (u'2do de Básica / 1st Grade', u'2do de Básica / 1st Grade'),
        (u'3ro de Básica / 2nd Grade', u'3ro de Básica / 2nd Grade'),
        (u'4to de Básica / 3rd Grade', u'4to de Básica / 3rd Grade'),
        (u'5to de Básica / 4th Grade', u'5to de Básica / 4th Grade'),
        (u'6to de Básica / 5th Grade', u'6to de Básica / 5th Grade'),
        (u'7mo de Básica / 6th Grade', u'7mo de Básica / 6th Grade'),
        (u'8vo de Básica / 7th Grade', u'8vo de Básica / 7th Grade'),
        (u'9no de Básica / 8th Grade', u'9no de Básica / 8th Grade'),
        (u'10mo de Básica / 9th Grade', u'10mo de Básica / 9th Grade'),
        (u'1ro de Bachillerato / 10th Grade', u'1ro de Bachillerato / 10th Grade'),
        (u'2do de Bachillerato / 11th Grade', u'2do de Bachillerato / 11th Grade'),
        (u'3ro de Bachillerato / 12th Grade', u'3ro de Bachillerato / 12th Grade'),    
        )
        
    applied_grade = models.CharField(max_length =50 , choices = NIVELES, verbose_name = u'Nivel al que aplica') 
    school_period = models.ForeignKey('PeriodSchool')  
    name_tutor = models.CharField(max_length = 25)
    surname_tutor = models.CharField(max_length = 25)
    mail_tutor = models.EmailField(max_length = 254)
   
    phone_tutor_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone_tutor = models.CharField(max_length = 9, validators=[phone_tutor_regex], verbose_name = u"Teléfono de Domicilio del Representante")
    cell_tutor_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell_tutor = models.CharField(max_length = 10, validators = [cell_tutor_regex] , verbose_name = u"Teléfono Celular del Representante")
    #phone_tutor = models.IntegerField(max_length = 9)
    #cell_tutor = models.IntegerField(max_length = 10)
    name_school = models.CharField(max_length = 25)
    address_school = models.CharField(max_length = 80)
    last_year = models.CharField(max_length = 9)
    special_observations=models.TextField(null=True,blank=True)
    bank_code = models.CharField(max_length = 6,null=True,blank=True)
    
    class Meta:
        unique_together = ("name_student", "surname_student","applied_grade","school_period")
   
        
    def __unicode__(self):
            return u"{} {}".format(self.name_student ,self.surname_student)
    


class Type_Tours(models.Model):
    id_typetour= models.AutoField(primary_key = True)
    name_tour = models.CharField(max_length = 25,null=True)
    date_tour = models.DateField(null=True)
    quota = models.IntegerField()
    state= models.BooleanField(default = False)
    
    def __unicode__(self):
        return u"{}".format(self.name_tour) 
   
   
class Tours(models.Model):
    id_tour = models.AutoField(primary_key = True)
    estado = models.BooleanField(default = True)
    id_typetour = models.ForeignKey('Type_Tours')
    id_applications = models.ForeignKey('Applications')   
    
    def __unicode__(self):
        return u"{}-{}".format (self.id_applications,  self.estado)
   

class Forms(models.Model):
    id_forms = models.AutoField(primary_key = True)
    id_applications = models.ForeignKey('Applications')
    identity_student = models.CharField(max_length =13,null = True,blank=True)
    code_student = models.UUIDField(default=uuid.uuid4, editable=False,null = True)
    name_student = models.CharField(max_length =25)
    surname_student = models.CharField(max_length =25)
    female ='F'
    male='M'
    gender_student_choices=(
        (female, 'Femenino'),
        (male, 'Masculino'),
        )
    gender_student = models.CharField(max_length = 1,choices=gender_student_choices,default=female,)
    birth_date = models.DateField()
    birth_country = CountryField()
    country_home = CountryField()
    address_student = models.CharField(max_length =80)
    NIVELES = (
        (u'Inicial 1 (de 2 a 3 años)', u'Inicial 1 (de 2 a 3 años)'),
        (u'Inicial 2 (de 3 a 4 años)', u'Inicial 2 (de 3 a 4 años)'),
        (u'Prebásica / Prekinder', u'Prebásica / Prekinder'),
        (u'1ero de Básica / Kinder', u'1ero de Básica / Kinder'),
        (u'2do de Básica / 1st Grade', u'2do de Básica / 1st Grade'),
        (u'3ro de Básica / 2nd Grade', u'3ro de Básica / 2nd Grade'),
        (u'4to de Básica / 3rd Grade', u'4to de Básica / 3rd Grade'),
        (u'5to de Básica / 4th Grade', u'5to de Básica / 4th Grade'),
        (u'6to de Básica / 5th Grade', u'6to de Básica / 5th Grade'),
        (u'7mo de Básica / 6th Grade', u'7mo de Básica / 6th Grade'),
        (u'8vo de Básica / 7th Grade', u'8vo de Básica / 7th Grade'),
        (u'9no de Básica / 8th Grade', u'9no de Básica / 8th Grade'),
        (u'10mo de Básica / 9th Grade', u'10mo de Básica / 9th Grade'),
        (u'1ro de Bachillerato / 10th Grade', u'1ro de Bachillerato / 10th Grade'),
        (u'2do de Bachillerato / 11th Grade', u'2do de Bachillerato / 11th Grade'),
        (u'3ro de Bachillerato / 12th Grade', u'3ro de Bachillerato / 12th Grade'),    
        )
        
    applied_grade = models.CharField(max_length =50 , choices = NIVELES, verbose_name = u'Nivel al que aplica') 
    medical_information = models.CharField(max_length =80)
    name_father = models.CharField(max_length =25)
    surname_father = models.CharField(max_length =25)
    identity_father = models.CharField(max_length =13)
    mail_father = models.EmailField(max_length =25)
    phone_father_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone_father = models.CharField(max_length = 9, validators=[phone_father_regex], verbose_name = u"Teléfono de Domicilio del Papá")
    cell_father_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell_father = models.CharField(max_length = 10, validators = [cell_father_regex] , verbose_name = u"Teléfono Celular del Papá")
    office_father_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    office_father = models.CharField(max_length = 9, validators=[office_father_regex], verbose_name = u"Teléfono de Oficina del Papá")
    name_mother = models.CharField(max_length =25)
    surname_mother = models.CharField(max_length =25)
    identity_mother = models.CharField(max_length =13)
    mail_mother = models.EmailField(max_length =25)
    phone_mother_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone_mother = models.CharField(max_length = 9, validators=[phone_mother_regex], verbose_name = u"Teléfono de Domicilio de la Mamá")
    cell_mother_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell_mother = models.CharField(max_length = 10, validators = [cell_mother_regex] , verbose_name = u"Teléfono Celular de la Mamá")
    office_mother_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    office_mother = models.CharField(max_length = 9, validators=[office_mother_regex], verbose_name = u"Teléfono de Oficina de la Mamá")
    name_tutor = models.CharField(max_length =25)
    surname_tutor = models.CharField(max_length =25)
    identity_tutor = models.CharField(max_length =13)
    mail_tutor = models.CharField(max_length =25)
    phone_tutor_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone_tutor = models.CharField(max_length = 9, validators=[phone_tutor_regex], verbose_name = u"Teléfono de Domicilio del Representante")
    cell_tutor_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell_tutor = models.CharField(max_length = 10, validators = [cell_tutor_regex] , verbose_name = u"Teléfono Celular del Representante")
    office_tutor_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    office_tutor = models.CharField(max_length = 9, validators=[office_tutor_regex], verbose_name = u"Teléfono de Oficina del Representante")
    address_tutor = models.CharField(max_length =80)
    date_form = models.DateTimeField(default = timezone.now)
     
    def __unicode__(self):
        return u"{}".format(self.name_student)



class Quotas(models.Model):
    id_quotas = models.AutoField(primary_key = True)
    grade = models.CharField(max_length =50)
    max_students = models.IntegerField()
    old_students = models.IntegerField()
    available_students = models.IntegerField()

    def __unicode__(self):
        return u"{}".format(self.id_quotas)
        
        
class Mails(models.Model):
    id_mails = models.AutoField(primary_key = True)
    title = models.CharField(max_length =50)
    sender = models.CharField(max_length =50)
    receiver = models.CharField(max_length =50)
    text = models.CharField(max_length =250,null = True)
    link = models.CharField(max_length =200,null = True,blank=True)
  
    def __unicode__(self):
        return u"{}".format(self.id_mails)

def validate_file_extension(value):   
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.bmp', '.gif', '.jpg', '.jpeg', '.tif', '.tiff', '.png', '.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'No se puede cargar el documento con esa extensión.')
        
class Documents_Type(models.Model):
    id_doctype = models.AutoField(primary_key = True)
    estado = models.BooleanField(default=True)
    grade = models.CharField(max_length =50)
    document = models.CharField(max_length =100)
 
    def __unicode__(self):
        return u"{}".format(self.document)
        
 

class Det_Documents(models.Model):
    id_detdoc= models.AutoField(primary_key = True)
    id_doctype = models.ForeignKey('Documents_Type')
    state=models.BooleanField(default=False)
    id_applications = models.ForeignKey('Applications')
    observations=models.CharField(max_length =80,null = True,blank=True)
    file = models.FileField(blank=False, null=False, upload_to="admisiones_sam/" , validators=[validate_file_extension])
    
  
    def __unicode__(self):
        return u"{}".format(self.id_detdoc)
  

class Type_Tests(models.Model):
    id_typetest= models.AutoField(primary_key = True)
    date_test = models.DateField(null = True)
    date_test_pre = models.DateField(null = True,blank = True)
    grade = models.CharField(max_length =50)
    time_test = models.TimeField(null = True)
    time_test_pre = models.TimeField(null = True,blank=True)
    teacher = models.CharField(max_length =50)
    type_test = models.CharField(max_length =50)
    state = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u"{}".format(self.type_test)


class Test(models.Model):
    id_test = models.AutoField(primary_key = True)
    opportunity = models.IntegerField()
    id_applications = models.ForeignKey('Applications')
    id_typetest = models.ForeignKey('Type_Tests')
    state=models.BooleanField(default=True)
  
    def __unicode__(self):
        return u"{}".format(self.id_test)
  
  
class State_Applications(models.Model):
    id_state = models.AutoField(primary_key = True)
    state = models.CharField(max_length=20)
    initial_date = models.DateTimeField(default = timezone.now,null=True)
    final_date = models.DateField(null=True,blank=True)
    observations = models.CharField(max_length=200,null = True)
    id_applications  = models.ForeignKey('Applications')
  
    def __unicode__(self):
        return u"{} {}".format(self.state, self.id_applications)
  
 
class Reports_Tests(models.Model):
    id_report = models.AutoField(primary_key = True)
    date_report = models.DateField(null = True)
    user = models.CharField(max_length =40)
    state = models.CharField(max_length =15)
    observations = models.TextField(null = True,blank=True)
    id_test  = models.ForeignKey('Test')
    id_applications  = models.ForeignKey('Applications')
    id_typetest  = models.ForeignKey('Type_Tests')
  
    def __unicode__(self):
        return u"{}".format(self.id_report)
        
class Det_Reports(models.Model):
    id_detreport = models.AutoField(primary_key = True)
    value = models.DecimalField(max_digits=5, decimal_places=2,null = True,blank=True)
    observations = models.TextField(null = True,blank=True)
    materia=models.CharField(max_length = 25,null=True,blank=True)
    id_report = models.ForeignKey('Reports_Tests')
    id_test = models.ForeignKey('Test')
    id_applications = models.ForeignKey('Applications')
    id_typetest = models.ForeignKey('Type_Tests')
  
    def __unicode__(self):
        return u"{}".format(self.id_detreport)
        
class Invoices(models.Model):
    id_invoice = models.AutoField(primary_key = True)
    name = models.CharField(max_length =25)
    surname = models.CharField(max_length =25)
    identity_card = models.CharField(max_length =13)
    address = models.CharField(max_length =80)
    phone_regex = RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone = models.CharField(max_length = 9, validators=[phone_regex], verbose_name = u"Teléfono de Domicilio")
    cell_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell = models.CharField(max_length = 10, validators = [cell_regex] , verbose_name = u"Teléfono Celular")
    id_applications = models.ForeignKey('Applications')
    mail=models.EmailField(max_length = 254)
  
    def __unicode__(self):
        return u"{}".format(self.id_invoice)


class PeriodSchool(models.Model):
    per_id = models.AutoField(primary_key = True)
    per_name = models.CharField(max_length =9)
    per_state=models.BooleanField(default=True)
    per_startdate = models.DateField()
    per_enddate = models.DateField()
    
    def __unicode__(self):
        return u"{}".format(self.per_name)
 
    class Meta:
        ordering = ["per_name"]

    def save(self, *args, **kwargs):
        self.per_name = "{0}-{1}".format(self.per_startdate.strftime("%Y"), self.per_enddate.strftime("%Y"))
        super(PeriodSchool, self).save(*args, **kwargs)

       

class AccountingDepartment (models.Model):
    id_accounting=models.AutoField(primary_key = True)
    state=models.BooleanField(default=True)
    observations=models.CharField(max_length =150)
    id_applications = models.ForeignKey('Applications')
    
    def __unicode__(self):
        return u"{}".format(self.id_accounting)

        
class AccountingDepartmentTest (models.Model):
    id_accountingtest=models.AutoField(primary_key = True)
    state=models.BooleanField(default=True)
    observations=models.CharField(max_length =150)
    id_applications = models.ForeignKey('Applications')
    
    def __unicode__(self):
        return u"{}".format(self.id_accountingtest) 

        
class AcademicSecretary (models.Model):
    id_secretary = models.AutoField(primary_key = True)
    state=models.CharField(max_length=2,blank = True, null = True)
    observations=models.CharField(max_length =150, blank = True, null = True)
    id_applications = models.ForeignKey('Applications')
    
    def __unicode__(self):
        return u"{}".format(self.id_secretary)
   
   
        
class Type_Grade(models.Model):
    id_typegrade=models.AutoField(primary_key = True)
    typegrade=models.CharField(max_length =100)
    typeschool=models.CharField(max_length =100)
    
    def __unicode__(self):
        return u"{}".format(self.id_typegrade)

    


class Countries(models.Model):
    country = CountryField()
    
    def __unicode__(self):
        return u"{}".format(self.country)