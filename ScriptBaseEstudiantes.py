#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuarios_sam.models import CustomUser,Students,Temporal_user
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuarios_sam.authhelper import get_consent_url , get_signin_url, get_token_from_code, get_access_token, get_token_from_shared_secret
import time
from usuarios_sam.outlookservice import get_me, get_my_messages, get_my_photo, get_users

from PIL import Image
from io import BytesIO


def CargaDatos():

    todos=Temporal_user.objects.all().order_by("id")
    ban=0
    for x in todos:
        #Ingreso la informacion del estudiante
          
        usuario_estudiante = CustomUser.objects.create(email=x.email_s,
                                                        identity=x.identificacion_s,
                                                        first_name=x.nombres_s,
                                                        father_last_name=x.apellido_paterno_s,
                                                        mother_last_name=x.apellido_materno_s,
                                                        birthdate=x.fecha_nacimiento_s,
                                                        gender=x.genero_s,
                                                        phone=x.telefono_s,
                                                        cell=x.celular_s,
                                                        address=x.direccion_s,
                                                        birth_country=x.pais_nacimiento_s,
                                                        country_home=x.pais_recidencia_s
                                                        )
        usuario_estudiante.save()
        print usuario_estudiante.pk
         
        # si el representante tiene mas de un hijo y ya se ingreso su informacion
        
        try:
            representante_existe=CustomUser.objects.get(email=x.email_t)
            ban=1
        except CustomUser.DoesNotExist:
            ban=0
            
        if ban==0:   
            usuario_representante = CustomUser.objects.create(email=x.email_t,
                                                            identity=x.identificacion_t,
                                                            first_name=x.nombres_t,
                                                            father_last_name=x.apellido_paterno_t,
                                                            mother_last_name=x.apellido_materno_t,
                                                            birthdate=x.fecha_nacimiento_t,
                                                            gender=x.genero_t,
                                                            phone=x.telefono_t,
                                                            cell=x.celular_t,
                                                            address=x.direccion_t,
                                                            birth_country=x.pais_nacimiento_t,
                                                            country_home=x.pais_recidencia_t
                                                            ) 
             
       
            usuario_representante.save()
            print usuario_representante.pk
          
       
        
        
        
        
        try:
            estudiante=CustomUser.objects.get(email=x.email_s)
        except CustomUser.DoesNotExist:
            estudiante=''
           
        
        
        try:
            representante=CustomUser.objects.get(email=x.email_t)
        except CustomUser.DoesNotExist:
            representante=None   
            
            
        try:
            papa=CustomUser.objects.get(email=x.email_p)
        except CustomUser.DoesNotExist:
            papa=None
            
            
        try:
            mama=CustomUser.objects.get(email=x.email_m)
        except CustomUser.DoesNotExist:
            mama=None
         
        #si la relacion del tutor es mama o papa ya no debo crear otro usuario
        if x.relacion_t!='PADRE' and papa==None:
        
            # si existe correo de papa ingreso la información del papa
            if x.email_p != "":
                usuario_papa = CustomUser.objects.create(email=x.email_p,
                                                            identity=x.identificacion_p,
                                                            first_name=x.nombres_p,
                                                            father_last_name=x.apellido_paterno_p,
                                                            mother_last_name=x.apellido_materno_p,
                                                            birthdate=x.fecha_nacimiento_p,
                                                            gender=x.genero_p,
                                                            phone=x.telefono_p,
                                                            cell=x.celular_p,
                                                            address=x.direccion_p,
                                                            birth_country=x.pais_nacimiento_p,
                                                            country_home=x.pais_recidencia_p
                                                            ) 
             
             
                usuario_papa.save()
                try:
                    papa=CustomUser.objects.get(email=x.email_p)
                except CustomUser.DoesNotExist:
                    papa=None
            else:
                papa=None
        else:
            papa=CustomUser.objects.get(email=x.email_t) 
           
        if x.relacion_t!='MADRE' and mama==None: 
            if x.email_m != "": 
                usuario_mama = CustomUser.objects.create(email=x.email_m,
                                                            identity=x.identificacion_m,
                                                            first_name=x.nombres_m,
                                                            father_last_name=x.apellido_paterno_m,
                                                            mother_last_name=x.apellido_materno_m,
                                                            birthdate=x.fecha_nacimiento_m,
                                                            gender=x.genero_m,
                                                            phone=x.telefono_m,
                                                            cell=x.celular_m,
                                                            address=x.direccion_m,
                                                            birth_country=x.pais_nacimiento_m,
                                                            country_home=x.pais_recidencia_m
                                                            ) 
             
             
                usuario_mama.save()
                try:
                    mama=CustomUser.objects.get(email=x.email_m)
                except CustomUser.DoesNotExist:
                    mama=None 
            else:
                mama=None
         
        else:
            mama=CustomUser.objects.get(email=x.email_t)     
            
        # creo el estudiante
        estudiantes=Students.objects.create(id_students = estudiante,
                                                id_tutor=representante,
                                                id_father=papa,
                                                id_mother=mama,
                                                applied_grade = x.grado,
                                                medical_information = "",
                                                id_applications=None)
                                                
       #creo los datos adicionales de representante,papa,mama
      # personas=People.objects.create(id_people = 
       #                                 is_dead = 
        #                                instruction=
         #                               profession=
          #                              address_work=
           #                               e_mail=
                        
                                      #)
       
     

