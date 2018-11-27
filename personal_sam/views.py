#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,unicodedata, operator,os,csv, openpyxl,datetime, random, string
import sqlite3
from openpyxl import Workbook
from openpyxl.cell import Cell
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from django.db.models import Min,Q,Count,Max
from django.db.models.functions import Lower
from django.core.exceptions import ObjectDoesNotExist
from django.forms import modelformset_factory
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext,loader, Context

from personal_sam.tasks import postulacion_email


from personal_sam.models import Type_Permissions,Permissions,Delegated_Activities,State_Permissions
from personal_sam.forms import Permissionsform
from usuarios_sam.models import CustomUser,Tutor
#from usuarios_sam.outlookservice import create_student, create_tutor, create_parent
#from comunicaciones_sam.models import MailerMessage
from datetime import date
from operator import itemgetter
from collections import OrderedDict

from django.contrib.auth.decorators import login_required


def Postulaciones_Personal(request):
    if request.method == "POST":
        postulante = {}
        postulante["apellidos"] = request.POST["apellidos"]
        postulante["nombres"] = request.POST["nombres"]
        postulante["telefono"] = request.POST["telefono"]
        postulante["correo"] = request.POST["correo"]
        postulante["seccion"] =  request.POST["seccion"]
        postulante["area"] = request.POST["area"]
        postulante["comentarios"] = request.POST["comentarios"]

        adjuntos = []

        for file in request.FILES.getlist('files[]'):

            content = file.read()
            adjunto = [file.name, content.encode("base64"), file.content_type]
            adjuntos.append(adjunto)
        
        postulacion_email.delay(postulante, 17, adjuntos)
        return render(request, "personal_sam/postulacion_recibida.html", {"postulante":postulante})
    else:
        return render(request, "personal_sam/postulacion.html", {})





@login_required(login_url='/admin/login/')
def Permission(request):
   
    form = Permissionsform()
    ActivitiesFormSet=modelformset_factory(Delegated_Activities,fields=('activity','hour','responsable','observations'), extra=4)
    formB=ActivitiesFormSet(queryset=Delegated_Activities.objects.none())
    debug=0
    dias=[1,2,3,4,5,6,7,8,9,10]
    horas=[1,2,3,4,5,6,7,8]
    solicitante=CustomUser.objects.get(email=request.user)
    aplicante=solicitante.first_name+' '+solicitante.father_last_name+' '+solicitante.mother_last_name
    
   
    
    if request.method == "POST":
        debug=1
        form = Permissionsform(request.POST)
        formB=ActivitiesFormSet(request.POST)
        coordinador=request.POST.get('r_coordinador', "")
        aplica=request.POST.get('r_aplicante', "")
        
        fecha_inicial=request.POST.get('d_fecha_desde', "")
        fecha_final=request.POST.get('d_fecha_hasta', "")
        dias=request.POST.get('d_dias', "")
        horas=request.POST.get('d_horas', "")
        
        
        tipo_permiso=Type_Permissions.objects.get(type='Inicial')
        
        
        if form.is_valid():
            permiso=form.save(commit=False)
            permiso.id_type=tipo_permiso  # se debe parametrizar con un valor inicial 1
            permiso.applicant=aplica
           
            permiso.date_initial=fecha_inicial
            permiso.date_end=fecha_final
         
            permiso.days=dias
            permiso.hours=horas
            permiso.save()
            
            
            debug=2
            estados=State_Permissions(state='Ingresado',date_initial=permiso.date_initial,date_end=None,user=coordinador,observations='Ingreso del Permiso',id_permissions =permiso)
            estados.save()    
            
            if formB.is_valid():
                debug=3
                for x in formB:
                    debug=4
                    new_item = x.save(commit=False)
                    new_item.id_permissions=permiso
                    
                    new_item.save()
                # falta enviar el mensaje al cordinador para que apruebe el permiso
                return redirect('Permisos')
            else:
                debug=5
                print formB.errors
                return render(request,'personal_sam/Permission.html', {"form":form,"formB":formB,"debug":debug,"aplicante":aplicante,"dias":dias,"horas":horas})
        else:
            debug=6
            print form.errors
            return render(request,'personal_sam/Permission.html', {"form":form,"formB":formB,"debug":form.errors,"aplicante":aplicante,"dias":dias,"horas":horas})
    else:
        debug=7
        form = Permissionsform()
        return render(request,'personal_sam/Permission.html', {"form":form,"formB":formB,"debug":debug,"aplicante":aplicante,"dias":dias,"horas":horas})
        
def PreApprove(request,id):
    
    
    consultapermisos=Type_Permissions.objects.all().distinct()
    tipos=[]
    for x in consultapermisos:
        if x.type in tipos:
            pass
        else:
            tipos.append(x.type)
   
    permiso=Permissions.objects.get(id=id)
    estado=State_Permissions.objects.get(id_permissions=id,date_end__isnull=True)
    actividades=Delegated_Activities.objects.filter(id_permissions=id)
    estados_permisos=['Ingresado','Eliminar','Pre-Aprobado','Negado','Aprobado','Terminado']
   
    ActivitiesFormSet=modelformset_factory(Delegated_Activities,fields=('activity','hour','responsable','observations'), extra=4)
    formB=ActivitiesFormSet(queryset=Delegated_Activities.objects.filter(id_permissions=id))
   
    
    
    
    #form = Permissionsform(request.POST, instance = permiso)
    form = Permissionsform(instance = permiso)
    formB=ActivitiesFormSet(request.POST)  # validar que vuelva a consultar el formset, se deja con una consulta fija
    
    
   
    return  render(request,'personal_sam/PreApprove.html', {"form":form,"formB":actividades,"tipos":tipos,"estado":estado,"lista":estados_permisos})
    
def SearchPreApprove(request):
    
    if request.method == "GET" and "q_coordinador" in request.GET:
    
        coordinador=request.GET["q_coordinador"]
        
        if coordinador:
            palabras = coordinador.split()
            coordinador= 'Rodrigo Caicedo'  #  hacer la busqueda en estados o en usuer los coordinadores  ////solicitud.filter(reduce(operator.and_, (Q(surname_student__icontains=x) | Q(name_student__icontains=x) for x in palabras)))
            permisos= Permissions.objects.all() #hacer la busqueda de todos los permisos cuando el estado sea igual a inicial,fecha final nula,y que el coordinador sea el de parametros de busqueda pasar el estado a pantalla
            return render(request,'personal_sam/SearchPreApprove.html',{"coordinador":coordinador,"permisos":permisos})
    
    else:
        return render(request,'personal_sam/SearchPreApprove.html')
  
  
def Permission_rrhh(request):
   
    form = Permissionsform()
    ActivitiesFormSet=modelformset_factory(Delegated_Activities,fields=('activity','hour','responsable','observations'), extra=4)
    formB=ActivitiesFormSet(queryset=Delegated_Activities.objects.none())
    debug=0
    consultapermisos=Type_Permissions.objects.all().distinct()
    tipos=[]
    for x in consultapermisos:
        if x.type in tipos:
            pass
        else:
            tipos.append(x.type)
    estados_permisos=['Ingresado','Eliminar','Pre-Aprobado','Negado','Aprobado','Terminado']
    
    if request.method == "POST":
        debug=1
        form = Permissionsform(request.POST)
        formB=ActivitiesFormSet(request.POST)
        coordinador=request.POST.get('r_coordinador', "")
        tipo_permiso=Type_Permissions.objects.get(type='Inicial')
       
             
        if form.is_valid():
            permiso=form.save(commit=False)
            permiso.id_type=tipo_permiso  # se debe parametrizar con un valor inicial 1
            permiso.save()
            debug=2
            estados=State_Permissions(state='Ingresado',date_initial=permiso.date,date_end=None,user=coordinador,observations='Ingreso del Permiso',id_permissions =permiso)
            estados.save()    
            
            if formB.is_valid():
                debug=3
                for x in formB:
                    debug=4
                    new_item = x.save(commit=False)
                    new_item.id_permissions=permiso
                    
                    new_item.save()
                # falta enviar el mensaje al cordinador para que apruebe el permiso
                return redirect('PermisosRRHH')
            else:
                debug=5
                print formB.errors
                return render(request,'personal_sam/Permission_rrhh.html', {"form":form,"formB":formB,"debug":formB.errors,"tipos":tipos,"lista":estados_permisos})
        else:
            debug=6
            print form.errors
            return render(request,'personal_sam/Permission_rrhh.html', {"form":form,"formB":formB,"debug":debug,"tipos":tipos,"lista":estados_permisos})
    else:
        debug=7
        form = Permissionsform()
        return render(request,'personal_sam/Permission_rrhh.html', {"form":form,"formB":formB,"debug":debug,"tipos":tipos,"lista":estados_permisos})
        
        
        
def ListTutors(request):
    
    if request.is_ajax():
        q = request.GET.get('term', '')
        palabras = q.split()
       
        tutores = Tutor.objects.filter(reduce(operator.and_, (Q(id_tutor__first_name__icontains=x) | Q(id_tutor__father_last_name__icontains=x) | Q(id_tutor__mother_last_name__icontains=x) for x in palabras)))[:20]
        results = []

        for x in tutores:
            x_json = {}
            x_json["value"] =  x.id_tutor.first_name + " " + x.id_tutor.father_last_name + " " + x.id_tutor.mother_last_name
            if x_json in results:
                pass
            else:
                results.append(x_json)
        data = json.dumps(results)
    else:
        data = 'fail'
        
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)  