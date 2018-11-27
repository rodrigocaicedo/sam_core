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
from biblioteca_sam.models import Reader,Borrowing,Book
from biblioteca_sam.forms import Bookform,ReaderForm,Borrowingform
from usuarios_sam.models import CustomUser,Students,People,RelationshipStudent
from datetime import date
from operator import itemgetter
from collections import OrderedDict

# Create your views here.


def NewBook(request):

    idiomas=['Español','Inglés','Francés','Alemán','Portugués','Otros']
    categoria=['Lengua','Inglés','Ciencias Sociales','Ciencias Naturales','Filosofía','Matemáticas','Historia','Otros']
    
    if request.method == "POST":
        form = Bookform(request.POST)
        if form.is_valid():
            libro=form.save(commit=False)
            libro.boo_state=True
            libro.save()
            new_form = Bookform()
            return render(request,'biblioteca_sam/create_book.html',{"form":new_form,"idiomas":idiomas,"categoria":categoria})
        else:
            print form.errors
            return render(request,'biblioteca_sam/create_book.html',{"form":form,"idiomas":idiomas,"categoria":categoria})
    else:
        form = Bookform()
        return render(request,'biblioteca_sam/create_book.html',{"form":form,"idiomas":idiomas,"categoria":categoria})

def search_book(request):
    
    libros=Book.objects.filter(boo_state=True)
    categoria=['Lengua','Inglés','Ciencias Sociales','Ciencias Naturales','Filosofía','Matemáticas','Historia','Otros']
    
    if request.method == "GET" and "q_titulo" in request.GET:
    
        titulo=request.GET["q_titulo"]
        autor=request.GET["q_autor"]
        idioma=request.GET["q_idioma"]
        if titulo:   
            palabras = titulo.split()
            libros=Book.objects.filter(reduce(operator.and_, (Q(boo_title__icontains=x)  for x in palabras)),boo_state=True)
            return render(request,'biblioteca_sam/search_book.html',{"libros":libros,"categoria":categoria})
        
        elif autor:
            palabras = autor.split()
            libros=Book.objects.filter(reduce(operator.and_, (Q(boo_author__icontains=x)  for x in palabras)),boo_state=True)
            return render(request,'biblioteca_sam/search_book.html',{"libros":libros,"categoria":categoria})
        
        elif idioma:
            palabras = idioma.split()
            libros=Book.objects.filter(reduce(operator.and_, (Q(boo_language__icontains=x)  for x in palabras)),boo_state=True)
            return render(request,'biblioteca_sam/search_book.html',{"libros":libros,"categoria":categoria})
          
        else:
            return render(request,'biblioteca_sam/search_book.html',{"libros":libros})
    else:
        return render(request,'biblioteca_sam/search_book.html',{"libros":libros,"categoria":categoria})
    

def delete_book(request, boo_id):
    
    #,bor_datereturn__isnull=True
    
    book = Book.objects.get(pk = boo_id)
    libro=0
    
    try:
        libro=Borrowing.objects.filter(boo_id=boo_id).count()   # el libro no se encuentra prestado.
    except ObjectDoesNotExist:
        libro=0
        
    if libro==0: # el libro nunga se ha prestado
        book.delete()
        return redirect('/biblioteca/consulta')
    else:   # si ya se presto en alguna ocacion se da de baja.
        book.boo_state=False
        book.save()      
        return redirect('/biblioteca/consulta')        
        
      
def edit_book(request, boo_id):
    
    idiomas=['Español','Inglés','Francés','Alemán','Portugués','Otros']
    categoria=['Lengua','Inglés','Ciencias Sociales','Ciencias Naturales','Filosofía','Matemáticas','Historia','Otros']
    
    book = Book.objects.get(pk = boo_id)
   
    if request.method == "POST":
        form = Bookform(request.POST, instance = book)	
        if form.is_valid():
            form.save()
            return redirect('/biblioteca/consulta')
        else:
            print form.errors
            return render(request,'biblioteca_sam/edit_book.html',{"form":form,"book":book,"idiomas":idiomas,"categoria":categoria})
    else:
       
        form = Bookform(instance = book)
        return render(request,'biblioteca_sam/edit_book.html',{"form":form,"book":book,"idiomas":idiomas,"categoria":categoria})
		
def register_book(request, boo_id):
    prestado=0
    form = Borrowingform()	
    debug=0
    estudiantes=CustomUser.objects.all()   #falta hacer la validacion con la tabla de students para saber que solo se selecciono los estudiantes que estan registrados en usuarios 
    
    try:
        prestado=Borrowing.objects.filter(boo=boo_id).count()   # , bor_datereturn__isnull=True  el libro se encuentra prestado.
        debug=1
    except ObjectDoesNotExist:
        prestado=0  # el libro no se encuentra prestado
        debug=2
   
    if prestado==0:  # si el libro no esta prestado 
        debug=3
        if request.method == "POST":
            debug=4
            
            alumno=request.POST.get('q_estudiante', "") 
            
            if form.is_valid():
                debug=5
                item=form.save(commit=False)
                item.boo=boo_id
                item.rea=alumno
                item.save()
                return redirect('/biblioteca/consulta')
            else:
                debug=6
                print form.errors
                return render(request,'biblioteca_sam/register_book.html',{"form":form,"estudiantes":estudiantes,"libro":boo_id,"debug":debug})
        else:
            debug=7
            return render(request,'biblioteca_sam/register_book.html',{"form":form,"estudiantes":estudiantes,"libro":boo_id,"debug":debug})
    else: 
        return render(request,'biblioteca_sam/register_message.html') 
        debug=8
       

def ListBook(request):
    
    if request.is_ajax():
        q = request.GET.get('term', '')
        palabras = q.split()
       
        libros = Book.objects.filter(reduce(operator.and_, (Q(boo_title__icontains=x) for x in palabras)))[:20]
        results = []

        for x in libros:
            x_json = {}
            x_json["value"] =  x.boo_title 
            if x_json in results:
                pass
            else:
                results.append(x_json)
        data = json.dumps(results)
    else:
        data = 'fail'
        
    mimetype = 'application/json'
    return HttpResponse(data, mimetype) 


def ListAuthor(request):
    
    if request.is_ajax():
        q = request.GET.get('term', '')
        palabras = q.split()
       
        autor = Book.objects.filter(reduce(operator.and_, (Q(boo_author__icontains=x) for x in palabras)))[:20]
        results = []

        for x in autor:
            x_json = {}
            x_json["value"] =  x.boo_author 
            if x_json in results:
                pass
            else:
                results.append(x_json)
        data = json.dumps(results)
    else:
        data = 'fail'
        
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)      