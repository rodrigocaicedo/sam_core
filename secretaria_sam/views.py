#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect

from django.http import HttpResponseRedirect

from general_sam.models import Matricula, Aptitud_Matricula, Periodo_Lectivo, Clase, Nivel

from secretaria_sam.forms import Edita_Aptitud_Form

from usuarios_sam.models import Student

from admisiones_sam.models import AcademicSecretary

from datetime import date

from django.contrib.auth.decorators import login_required


def activar_periodo(request, periodo_lectivo):
	periodo_lectivo = Periodo_Lectivo.objects.get(pk = periodo_lectivo)
	request.session["schoolyear"] = u"{0} - {1}".format(periodo_lectivo.inicio.strftime("%Y"), periodo_lectivo.fin.strftime("%Y"))
	request.session["schoolyear_pk"] = periodo_lectivo.pk
	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def activacion_periodo_lectivo(request):
	if request.method == "POST":
		id_periodo_lectivo = request.POST["periodo_lectivo"]
		periodo_lectivo = Periodo_Lectivo.objects.get(pk = id_periodo_lectivo)
		periodos_activos = Periodo_Lectivo.objects.filter(actual = True)
		for x in periodos_activos:
			x.activo = False
			x.save()
		periodo_lectivo.actual = True
		periodo_lectivo.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	else:
		periodos_lectivos = Periodo_Lectivo.objects.filter(fin__gt = date.today())
		return render_to_response("secretaria_sam/activar_periodo_lectivo.html", {"periodos":periodos_lectivos})

"""
def edicion_aptitud_matricula(request, aptitud_matricula):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")
	periodo_lectivo = periodo_seleccionado

	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	aptitud_matricula = Aptitud_Matricula.objects.get(pk = aptitud_matricula)
	form = Edita_Aptitud_Form(aptitud_matricula)

	if request.method == "POST":
		form = Edita_Aptitud_Form(request.POST, instance = aptitud_matricula)
		if form.is_valid():
			form.save()
		
		else:
			print form.errors
		return render()
	else:
		return render()

"""

def editar_matricula(request, matricula_id):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	periodo_lectivo = periodo_seleccionado
	periodo_lectivo = periodo_seleccionado
	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")
	matricula = Matricula.objects.get(pk = matricula_id)
	clase = Clase.objects.get(pk = request.POST.get("clase",""))
	if matricula.clase == clase:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/secretaria/matriculas/'))
	else:
		matricula.clase = clase
		matricula.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/secretaria/matriculas/'))






def eliminar_pedido_matricula(request, apto_id):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	periodo_lectivo = periodo_seleccionado
	periodo_lectivo = periodo_seleccionado
	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")	

	apto = Aptitud_Matricula.objects.get(pk = apto_id)
	apto.resuelto = date.today()
	if apto.observaciones:
		apto.observaciones = apto.observaciones + " " + request.POST.get("observaciones", "")
	else:
		apto.observaciones = request.POST.get("observaciones", "")
	apto.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/secretaria/matriculas/'))


def pedido_matricula(request, apto_id):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")
	periodo_lectivo = periodo_seleccionado
	periodo_lectivo = periodo_seleccionado
	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")	

	apto = Aptitud_Matricula.objects.get(pk = apto_id)
	nivel = Nivel.objects.get(pk = request.POST["nivel"])
	if apto.nivel == nivel:
		pass
	else:
		apto.resuelto = date.today()
		if apto.observaciones:
			apto.observaciones = apto.observaciones + " " + request.POST.get("observaciones", "")
		else:
			apto.observaciones = request.POST.get("observaciones", "")
		apto.save()
		apto.pk = None
		apto.nivel = Nivel.objects.get(pk = request.POST["nivel"])
		apto.observaciones = u"SECRETARÍA: Nuevo pedido" + apto.observaciones
		apto.resuelto = None
		apto.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/secretaria/matriculas/'))	



def retirar_matricula(request, matricula_id):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")
	periodo_lectivo = periodo_seleccionado
	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	matricula = Matricula.objects.get(pk = matricula_id)
	estado_anterior = matricula.estado_matricula_set.get(fin = None)
	estado_anterior.fin = date.today()
	estado_anterior.save()
	estado_nuevo = matricula.estado_matricula_set.create(observaciones = request.POST["observaciones"], matricula_activa = False)
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/secretaria/matriculas/activas/'))


def reingresar_matricula(request, matricula_id):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")
	periodo_lectivo = periodo_seleccionado
	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	matricula = Matricula.objects.get(pk = matricula_id)
	estado_anterior = matricula.estado_matricula_set.get(fin = None)
	estado_anterior.fin = date.today()
	estado_anterior.save()
	estado_nuevo = matricula.estado_matricula_set.create(observaciones = request.POST["observaciones"], matricula_activa = True)
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/secretaria/matriculas/retirados/'))



@login_required()
def matriculacion_individual(request):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_seleccionado = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")
	periodo_lectivo = periodo_seleccionado

	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	#periodo_lectivo = proximos.first()
	niveles = Nivel.objects.filter(activo = True)
	validaciones = AcademicSecretary.objects.filter(state = 1, id_applications__school_period__per_startdate__year = periodo_seleccionado.inicio.strftime("%Y") , id_applications__school_period__per_enddate__year = periodo_seleccionado.fin.strftime("%Y") )
	matriculas = Matricula.objects.filter(clase__periodo_lectivo = periodo_lectivo)
	matricula_activos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = True)
	matricula_inactivos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = False)
	aptos_matriculacion = Aptitud_Matricula.objects.filter(periodo_lectivo = periodo_lectivo, resuelto = None).order_by("nivel", "estudiante__user__father_last_name", "estudiante__user__mother_last_name", "estudiante__user__first_name")
	for x in aptos_matriculacion:
		clases = Clase.objects.filter(periodo_lectivo = periodo_lectivo, nivel = x.nivel)
		if clases.count() == 0:
			if x.nivel.seccion.nombre == "Preescolar":
				paralelo = "A"
			else:
				paralelo = "1"
			clase = Clase.objects.create(periodo_lectivo = periodo_lectivo, nivel = x.nivel, paralelo = paralelo)

	clases = Clase.objects.filter(periodo_lectivo = periodo_lectivo)

	if request.method == "POST":
		for x in request.POST:
			try:
				apto = Aptitud_Matricula.objects.get(pk = x)
				clase = Clase.objects.get(pk = request.POST[x])
			except:
				continue
				
			matricula = Matricula.objects.create(estudiante= apto.estudiante, clase = clase, tipo = "OR")
			estado = matricula.estado_matricula_set.create(matricula_activa = True)
			apto.matriculado = True
			apto.resuelto = date.today()
			apto.save()
			
		matriculas = Matricula.objects.filter(clase__periodo_lectivo = periodo_lectivo)
		matricula_activos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = True)
		matricula_inactivos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = False)
		aptos_matriculacion = Aptitud_Matricula.objects.filter(periodo_lectivo = periodo_lectivo,  resuelto = None).order_by("nivel", "estudiante__user__father_last_name", "estudiante__user__mother_last_name", "estudiante__user__first_name")

		return render(request, "secretaria_sam/matriculacion_individual.html", {"niveles": niveles, "validaciones":validaciones, "activos": matricula_activos, "inactivos":matricula_inactivos, "aptos":aptos_matriculacion, "clases":clases})
	else:
		return render(request, "secretaria_sam/matriculacion_individual.html", {"niveles":niveles, "validaciones":validaciones, "activos": matricula_activos, "inactivos":matricula_inactivos, "aptos":aptos_matriculacion, "clases":clases})


def lista_matriculas(request):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_lectivo = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")

	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	matriculas = Matricula.objects.filter(clase__periodo_lectivo = periodo_lectivo)
	matricula_activos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = True)
	matricula_inactivos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = False)
	aptos_matriculacion = Aptitud_Matricula.objects.filter(periodo_lectivo = periodo_lectivo,  resuelto = None).order_by("nivel", "estudiante__user__father_last_name", "estudiante__user__mother_last_name", "estudiante__user__first_name")
	return render(request, "secretaria_sam/lista_matriculas.html", {"inactivos":matricula_inactivos, "aptos":aptos_matriculacion, "matriculas":matriculas, "activos":matricula_activos})


def lista_matriculas_retirados(request):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_lectivo = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")

	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	matriculas = Matricula.objects.filter(clase__periodo_lectivo = periodo_lectivo)
	matricula_retirados = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = False)
	matricula_activos = matriculas.filter(estado_matricula__fin = None, estado_matricula__matricula_activa = True)
	aptos_matriculacion = Aptitud_Matricula.objects.filter(periodo_lectivo = periodo_lectivo,  resuelto = None).order_by("nivel", "estudiante__user__father_last_name", "estudiante__user__mother_last_name", "estudiante__user__first_name")

	return render(request, "secretaria_sam/lista_matriculas_retirados.html", {"aptos":aptos_matriculacion, "activos":matricula_activos, "matriculas":matriculas, "retirados":matricula_retirados})


def lista_clases(request):
	if not request.user.groups.filter(name="Secretaria").exists():
		return Hola
	id_periodo = request.session["schoolyear_pk"]
	periodo_lectivo = Periodo_Lectivo.objects.get(pk = id_periodo)
	#en la matriculacion individual, se debe elegir el año lectivo y la clase para al estudiante que ingresa.
	#anterior = Periodo_Lectivo.objects.get(actual = True)
	#proximos = Periodo_Lectivo.objects.filter(inicio__gte = anterior.fin).order_by("inicio")

	if periodo_lectivo.actual == False:
		return render(request, "secretaria_sam/periodo_cerrado.html")

	clases = Clase.objects.filter(periodo_lectivo = periodo_lectivo).order_by("pk")
	return render(request, "secretaria_sam/lista_clases.html", {"clases":clases})

def detalle_clase(request, clase_id):
	clase = Clase.objects.get(pk = clase_id)
	estudiantes = Matricula.objects.filter(clase = clase).order_by("estudiante__user__father_last_name", "estudiante__user__mother_last_name", "estudiante__user__first_name")
	return render(request, "secretaria_sam/detalle_clase.html", {"clase":clase, "estudiantes":estudiantes})

def lista_estudiantes(request):
	estudiantes = Matricula.objects.filter(clase__periodo_lectivo__actual = True).order_by("estudiante__user_father_last_name", "estudiante__user_mother_last_name", "estudiante__user_first_name")
	return render(request, "secretaria_sam/lista_estudiantes.html", {"estudiantes":estudiantes})

def detalle_estudiante(request, estudiante_id):
	estudiante = Student.objects.get(pk = estudiante_id)
	matriculas = Matricula.objects.filter(estudiante = estudiante)
	return render(request, "secretaria_sam/detalle_estudiante.html", {"estudiante":estudiante, "matriculas":matriculas})

# Create your views here.
