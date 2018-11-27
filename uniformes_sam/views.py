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
from uniformes_sam.models import Lista_Estudiantes,Lista_Representante,Estudiantes_Representante,Uniformes,Cab_Proforma,Det_Proforma
from usuarios_sam.models import CustomUser,Students,People,RelationshipStudent
from uniformes_sam.forms import CabProformanewform
from usuarios_sam.outlookservice import create_student, create_tutor, create_parent
from comunicaciones_sam.models import MailerMessage
from datetime import date
from operator import itemgetter
from collections import OrderedDict

# Create your views here.

def Pedido(request):
    prendas=['1','2','3','4','5']
    form = CabProformanewform()
    DetProformaFormSet=modelformset_factory(Det_Proforma,fields=('id_estudiante','referencia', 'descripcion','color','talla','cantidad','precio','subtotal'), extra=8)
    formB=DetProformaFormSet(queryset=Det_Proforma.objects.none())
    
    if request.method == "GET" and "q_representante" in request.GET:
        representante=request.GET["q_representante"]
        palabras = representante.split()
        #request.session['id_formulario']=new_app.pk  #cookies
        
        nombre_rep=Lista_Representante.objects.filter(reduce(operator.and_,(Q(nombres__icontains=x)  for x in palabras)))
           
        representante=Estudiantes_Representante.objects.filter(representante=nombre_rep)
            
        hijos=Lista_Estudiantes.objects.filter(id__in=Estudiantes_Representante.objects.filter(representante=nombre_rep))
        #hijos= representante.lista_estudiantes_set.get(pk=estudiante)        
        return render(request,'uniformes_sam/Proforma.html',{"form":form,"formB":formB,"tutor":nombre_rep,"hijos":hijos})
        
        hijos=[1,2,3]
        
    elif request.method == "POST":
        form = CabProformanewform(request.POST)
        hijos=Lista_Estudiantes.objects.filter(pk=552 )
        #for x in hijos
       
              
        if form.is_valid():
            datos_cab=form.save(commit=False)
            
            #verifico si la cabecera del representante ya se ha guardado
            if cabecera==Cab_Proforma.objects.get(id_rep=datos_cab.id_rep).count()<1:
                datos_cab.save()
                
            if formB.is_valid():
                for x in formB:
                    x.save()
                           
           
            return redirect('Proforma')
            
            
        
        
        else:
            print form.errors
            return render(request,'uniformes_sam/Proforma.html', {"form":form,"formB":formB,"prendas":prendas,"hijos":hijos})
    else:
        form = CabProformanewform()
        return render(request,'uniformes_sam/Proforma.html', {"form":form,"formB":formB,"prendas":prendas})
   
        
def ListaTutor(request):
    
    if request.is_ajax():
        q = request.GET.get('term', '')
        palabras = q.split()
        
        
        representantes = Lista_Representante.objects.filter(reduce(operator.and_, (Q(nombres__icontains=x) for x in palabras)))[:20]
        results = []

        for x in representantes:
            x_json = {}
            x_json["value"] = x.nombres  
            if x_json in results:
                pass
            else:
                results.append(x_json)
        data = json.dumps(results)
    else:
        data = 'fail'
        
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
    
    
    
