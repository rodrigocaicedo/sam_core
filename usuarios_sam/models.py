#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from django.db import models

from PIL import Image
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.http import urlquote
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self, first_name, father_last_name, mother_last_name, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        #photo_file = os.path.join("static/user/profile_photo", "default.jpg")
        photo_file = os.path.join("static/user/", "default.jpg")
        user = self.model(email=email, first_name = first_name, father_last_name = father_last_name, mother_last_name = mother_last_name, 
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, user_photo = photo_file, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, first_name, father_last_name, mother_last_name, email, password=None, **extra_fields):
        return self._create_user(first_name, father_last_name, mother_last_name, email, None ,False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user("", "", "", email, password, True, True,
                                 **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    identity_regex=RegexValidator(regex=r'^[a-zA-Z0-9_]+$', message= u"Ingrese solo numeros y letras." )
    identity = models.CharField(max_length = 20, validators=[identity_regex], verbose_name = u"Número de Identificación",null = True,blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    father_last_name = models.CharField(_('father last name'), max_length=30, blank=False)
    mother_last_name = models.CharField(_('mother last name'), max_length=30, blank=False)
    preferred_name = models.CharField(_('preferred name'), max_length = 30, blank = True)
    birthdate = models.DateField(_('birth date'), null=True, blank = True)
    female ='F'
    male='M'
    gender_choices=(
        (female, 'Femenino'),
        (male, 'Masculino'),
        )
    gender = models.CharField(max_length = 1,choices=gender_choices,default=female,)
    phone_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    phone = models.CharField(max_length = 9, blank = True, validators=[phone_regex], verbose_name = u"Teléfono del Domicilio")
    cell_regex = RegexValidator(regex=r'^0+\d{9}$', message= u"Ingrese su celular en el formato 0990909090.")
    cell = models.CharField(max_length = 10, blank = True, validators = [cell_regex] , verbose_name = u"Teléfono Celular")
    address = models.CharField(max_length =80, blank = True)
    birth_country = CountryField()
    country_home = CountryField()
    user_photo = models.ImageField(upload_to = "static/user/profile_photo/", default = "static/user/default.jpg")
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        #full_name = ""
        if self.mother_last_name == "":
            full_name = "{0} {1}".format(self.first_name, self.father_last_name)
        else:
            full_name = "{0} {1} {2}".format(self.first_name, self.father_last_name, self.mother_last_name)
        return full_name

    def get_legal_name(self):
        if self.mother_last_name == "":
            legal_name = "{0} {1}".format(self.father_last_name, self.first_name)
        else:
            legal_name = "{0} {1} {2}".format(self.father_last_name, self.mother_last_name, self.first_name)
        return legal_name

    def get_short_name(self):
        "Returns the short name for the user."
        if self.preferred_name == "":
            return self.first_name
        else:
            return self.preferred_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
"""
    def save(self, *args, **kwargs):
        if self.user_photo:
            image = Image.open(StringIO.StringIO(self.user_photo.read()))
            w, h = image.size
            if w > h:
                image = image.crop((w/2 - h/2 , 0, w/2 + h/2, h))
            else:
                image = image.crop((0, h/2 - w/2, w, h/2 + w/2))

            image = image.resize((600,600), Image.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.user_photo= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.get_full_name(), 'image/jpeg', output.len, None)
            self.user_photo = os.path.join("static/user/", "default.jpg")
        else:
            self.user_photo = os.path.join("static/user/", "default.jpg")
        super(CustomUser, self).save(*args, **kwargs)
"""        

class LoginRegister(models.Model):
    user = models.ForeignKey("CustomUser")
    login_date = models.DateField(auto_now_add = True)


class Student(models.Model):
    user = models.OneToOneField('CustomUser')
    joined = models.DateTimeField(_('date joined'), default=timezone.now)
    through = models.CharField(_('joined thourgh'), max_length = 50, blank = True)

    def __unicode__(self):
        return self.user.get_legal_name()

    def get_name(self):
        return self.user.get_legal_name()


class Relative(models.Model):
    user = models.OneToOneField('CustomUser')
    joined = models.DateTimeField(_('date joined'), default=timezone.now)
    through = models.CharField(_('joined thourgh'), max_length = 50, blank = True)

    def __unicode__(self):
        return self.user.get_legal_name()

class Relative_Details(models.Model):
    relative = models.OneToOneField("Relative")
    alive = models.BooleanField(default = True)
    instruction=models.CharField(max_length =50,blank=True,null=True)
    profession=models.CharField(max_length =50,blank=True,null=True)
    address_work=models.CharField(max_length =80,blank=True,null=True)
    office_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    office = models.CharField(max_length = 9, validators=[office_regex], verbose_name = _('office phone'))


    def __unicode__(self):
        return self.relative.user.get_legal_name()




class Student_Relative(models.Model):
    student = models.ForeignKey("Student")
    relative = models.ForeignKey("Relative")
    relationship = models.CharField(max_length = 20)
    legal_representative = models.BooleanField(default = False)
    live_together = models.BooleanField(default = False)
    withdraw = models.BooleanField(default = False)
    notifications = models.BooleanField(default = False)

    class Meta:
        unique_together = (('student', 'relative'))

    def __unicode__(self):
        return u"{0}-{1}:{2}".format(self.student.user.get_legal_name(), self.relative.user.get_legal_name(), self.relationship)

    
class Students(models.Model):
    id_students = models.ForeignKey('CustomUser', related_name = "Estudiante", unique = True)
    id_tutor=models.ForeignKey('usuarios_sam.CustomUser', related_name = "Tutor")
    id_father=models.ForeignKey('usuarios_sam.CustomUser', related_name = "Padre",blank=True,null=True)
    id_mother=models.ForeignKey('usuarios_sam.CustomUser', related_name = "Madre",blank=True,null=True)
    applied_grade = models.CharField(max_length =50)
    medical_information = models.CharField(max_length =80)
    id_applications=models.ForeignKey('admisiones_sam.Applications',blank=True,null=True)
    

    def __unicode__(self):
        return self.id_students.get_full_name()

    def get_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        #full_name = ""
        name = "{0} {1} {2}".format(self.id_students.father_last_name, self.id_students.mother_last_name, self.id_students.first_name)
        return name
    
    
class People(models.Model):
    id_people = models.ForeignKey('CustomUser')
    is_dead = models.BooleanField(default=False)
    instruction=models.CharField(max_length =50,blank=True,null=True)
    profession=models.CharField(max_length =50,blank=True,null=True)
    address_work=models.CharField(max_length =80,blank=True,null=True)
    office_regex=RegexValidator(regex=r'^0+\d{8}$', message= u"Ingrese su teléfono en el formato 022345678." )
    office = models.CharField(max_length = 9, validators=[office_regex], verbose_name = u"Teléfono de Oficina")
    e_mail=models.EmailField(_('email address'), max_length=254)
   
    
    def __unicode__(self):
        return self.id_people.get_full_name()

class RelationshipStudent(models.Model):
    id_people=models.ForeignKey('People')
    id_students=models.ForeignKey('Students')
    live_student = models.BooleanField()
    withdraw = models.BooleanField()


class Tutor(models.Model):
    id_tutor = models.ForeignKey('CustomUser', related_name = "Coordinador")
    
    def __unicode__(self):
        return str(self.id_tutor.get_full_name())


class Teacher(models.Model):
    id_teachers = models.ForeignKey('CustomUser', related_name = "Profesor")

    def __unicode__(self):
        return self.id_teachers.get_full_name()


class Temporal_user (models.Model):

    email_s=models.EmailField(_('email address'), max_length=254)
    identificacion_s=models.CharField(max_length =50,blank=True,null=True)
    nombres_s=models.CharField(max_length =50,blank=True,null=True)
    apellido_paterno_s=models.CharField(max_length =50,blank=True,null=True)
    apellido_materno_s=models.CharField(max_length =50,blank=True,null=True)
    relacion_s=models.CharField(max_length =50,blank=True,null=True)
    fecha_nacimiento_s=models.DateTimeField(blank=True,null=True)
    genero_s=models.CharField(max_length =50,blank=True,null=True)
    telefono_s=models.CharField(max_length =50,blank=True,null=True)
    celular_s=models.CharField(max_length =50,blank=True,null=True)
    direccion_s=models.CharField(max_length =50,blank=True,null=True)
    pais_nacimiento_s=models.CharField(max_length =50,blank=True,null=True)
    pais_recidencia_s=models.CharField(max_length =50,blank=True,null=True)
    
    email_t=models.EmailField(_('email address'), max_length=254)
    identificacion_t=models.CharField(max_length =50,blank=True,null=True)
    nombres_t=models.CharField(max_length =50,blank=True,null=True)
    apellido_paterno_t=models.CharField(max_length =50,blank=True,null=True)
    apellido_materno_t=models.CharField(max_length =50,blank=True,null=True)
    relacion_t=models.CharField(max_length =50,blank=True,null=True)
    fecha_nacimiento_t=models.DateTimeField(blank=True,null=True)
    genero_t=models.CharField(max_length =50,blank=True,null=True)
    telefono_t=models.CharField(max_length =50,blank=True,null=True)
    celular_t=models.CharField(max_length =50,blank=True,null=True)
    direccion_t=models.CharField(max_length =50,blank=True,null=True)
    pais_nacimiento_t=models.CharField(max_length =50,blank=True,null=True)
    pais_recidencia_t=models.CharField(max_length =50,blank=True,null=True)
    
    email_p=models.EmailField(_('email address'), max_length=254)
    identificacion_p=models.CharField(max_length =50,blank=True,null=True)
    nombres_p=models.CharField(max_length =50,blank=True,null=True)
    apellido_paterno_p=models.CharField(max_length =50,blank=True,null=True)
    apellido_materno_p=models.CharField(max_length =50,blank=True,null=True)
    relacion_p=models.CharField(max_length =50,blank=True,null=True)
    fecha_nacimiento_p=models.DateTimeField(blank=True,null=True)
    genero_p=models.CharField(max_length =50,blank=True,null=True)
    telefono_p=models.CharField(max_length =50,blank=True,null=True)
    celular_p=models.CharField(max_length =50,blank=True,null=True)
    direccion_p=models.CharField(max_length =50,blank=True,null=True)
    pais_nacimiento_p=models.CharField(max_length =50,blank=True,null=True)
    pais_recidencia_p=models.CharField(max_length =50,blank=True,null=True)
    

    email_m=models.EmailField(_('email address'), max_length=254)
    identificacion_m=models.CharField(max_length =50,blank=True,null=True)
    nombres_m=models.CharField(max_length =50,blank=True,null=True)
    apellido_paterno_m=models.CharField(max_length =50,blank=True,null=True)
    apellido_materno_m=models.CharField(max_length =50,blank=True,null=True)
    relacion_m=models.CharField(max_length =50,blank=True,null=True)
    fecha_nacimiento_m=models.DateTimeField(blank=True,null=True)
    genero_m=models.CharField(max_length =50,blank=True,null=True)
    telefono_m=models.CharField(max_length =50,blank=True,null=True)
    celular_m=models.CharField(max_length =50,blank=True,null=True)
    direccion_m=models.CharField(max_length =50,blank=True,null=True)
    pais_nacimiento_m=models.CharField(max_length =50,blank=True,null=True)
    pais_recidencia_m=models.CharField(max_length =50,blank=True,null=True)
    grado=models.CharField(max_length =50,blank=True,null=True)
    migrado=models.CharField(max_length =5,blank=True,null=True)

# Create your models here.
