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
from facturacion_sam.models import Invoices
from facturacion_sam.forms import Invoicesnewform
from usuarios_sam.models import CustomUser,Students,People,RelationshipStudent
from usuarios_sam.outlookservice import create_student, create_tutor, create_parent
from comunicaciones_sam.models import MailerMessage
from general_sam.models import Matricula, Nivel, Periodo_Lectivo, Clase, Aptitud_Matricula
from datetime import date
#from models import Prompts
from operator import itemgetter
from collections import OrderedDict




def invoice_new(request,email_s):
    debug=1
    if request.method == "POST":
        form = Invoicesnewform(request.POST)
        debug=2
        if form.is_valid():
            debug=3
            
            new_app = form.save(commit=False)
            new_app.date_update=date.today()
            new_app.id_students=email_s
            
            new_app.save()
            
            #si tiene mas de un hijo revisar si se debe poner a todos con el mismo dato
            
            return  render(request, "facturacion_sam/MessageSave.html")
        else:
            debug=4
            print form.errors
            return render(request, "facturacion_sam/facturas.html", {"form":form,"debug":debug})
    else:
        debug=5
        form = Invoicesnewform()
        return render(request, "facturacion_sam/facturas.html", {"form":form,"debug":debug})

def MessageSave (request):
   
    return render(request,"facturacion_sam/MessageSave.html")      
        
def relation(request,email_r):
    null