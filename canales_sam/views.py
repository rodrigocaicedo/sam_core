# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from datetime import date

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from comunicaciones_sam.models import MailerMessage, Comunicacion

from usuarios_sam.models import CustomUser as User

from general_sam.models import Asignacion_Profesores, Matricula_Grupo, Grupo, Materia_Grupo

from comunicaciones_sam.forms import ComunicacionForm, AdjuntoForm

from canales_sam.models import Registro_Temas, Registro_Grupos

from canales_sam.tasks import new_ticket_teacher, new_email, new_ticket, new_ticket_teacher2, new_email2

from canales_sam.forms import TicketForm, TicketTemasForm

from django.core.mail import get_connection, EmailMessage, EmailMultiAlternatives
#from canales_sam.ticketservice import create_ticket
#from django.core.mail import send_mail

#from envio_correos.models import Comunicacion, niveles, Students, Emailsbystudent

# Create your views here.


def is_psicologia(user):
    return user.groups.filter(name = "Psicologia").exists()

def is_dece(user):
    return user.groups.filter(name = "DECE").exists()

def is_disciplina(user):
    return user.groups.filter(name = "Disciplina").exists()

def is_capellania(user):
    return user.groups.filter(name = "Capellania").exists()

def is_extracurriculares(user):
    return user.groups.filter(name = "Extracurriculares").exists()

def is_transporte(user):
    return user.groups.filter(name = "Transporte").exists()




def list_levels(request):
	grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True).exclude(nombre__icontains = "-")
	grupos_vacios = []
	for grupo in grupos:
		matriculados = grupo.matricula_grupo_set.all()
		if matriculados.count() == 0:
			grupos_vacios.append(grupo.pk)
	grupos = grupos.exclude(pk__in = grupos_vacios)
	return render(request, "canales_sam/lista_grupos.html",{"grupos":grupos})


def level(request, id_grupo):
	grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True).exclude(nombre__icontains = "-")#.exclude(nombre__icontains = "Inicial").exclude(nombre__icontains = "inder")
	grupos_vacios = []
	for grupo in grupos:
		matriculados = grupo.matricula_grupo_set.all()
		if matriculados.count() == 0:
			grupos_vacios.append(grupo.pk)
	#grupos = grupos.exclude(pk__in = grupos_vacios)
	try:
		lista_materias = []
		grupo = grupos.get(pk = id_grupo)

		materias = grupo.materia_grupo_set.all().order_by("materia__nombre")


		for materia in materias:
			lista_materias.append(materia.pk)
		if "inder" in grupo.nombre:
			pass
		else:
			otras_materias = Materia_Grupo.objects.filter(grupo__nombre__icontains = grupo.nombre)
			for otra in otras_materias:
				if otra.pk in lista_materias:
					pass
				else:
					lista_materias.append(otra.pk)
		materias = Materia_Grupo.objects.filter(pk__in = lista_materias).order_by("materia__nombre")



		return render(request, "canales_sam/grupo.html", {"grupo":grupo, "materias":materias})
	except:
		return redirect(list_levels)


def message(request, id_asignacion):
	asignacion = Asignacion_Profesores.objects.get(pk = id_asignacion)
	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			tutor = form.cleaned_data["tutor"]
			email = form.cleaned_data["email"]
			subject = form.cleaned_data["subject"]
			message = request.POST.get("message")
			student = form.cleaned_data["student"]


			payload = {"name": tutor,
				"email":email,
				"subject":subject,
				"message":message,
				"student":student,
				"grade":asignacion.actividad.grupo.nombre,
				"topicId":asignacion.profesor.id_teachers.registro_temas_set.first().id_ticket,
			}

			id_ticket = int(asignacion.profesor.id_teachers.registro_temas_set.last().id_ticket)

			aplicante = {"name": tutor, "student":student, "grade":asignacion.actividad.grupo.nombre, "subject":u"{0}".format(subject), "message":u"{0}".format(message)}

			if id_ticket == 0:

				mensaje = MailerMessage()
				mensaje.general_message(asignacion.profesor.id_teachers.registro_temas_set.last().correo_ticket, "comunicaciones@montebelloacademy.org", 34, aplicante)

				return render(request, 'canales_sam/success_parents.html', {})			
			attachments = []
			for file in request.FILES.getlist('files[]'):
				#try:
				#return file.read()
				content = file.read()
				#return content.encode('base64')
				registro = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(registro)
				#return registro
				#except:
					#pass
			payload['attachments'] = attachments
			new_ticket.delay(payload)
			return render(request, 'canales_sam/success_parents.html', {})
		else:
			print form.errors
			return render(request, "canales_sam/message.html", {"asignacion":asignacion, "form":form})
	else:
		form = TicketForm()
		return render(request, "canales_sam/message.html", {"asignacion":asignacion, "form":form})


def list_topics(request):
	temas = Registro_Grupos.objects.all()
	
	return render(request, "canales_sam/temas.html", {"temas":temas})
	

def message_topics(request, id_tema):
	tema = Registro_Grupos.objects.get(pk = id_tema)
	if "coordinacion" in tema.correo_ticket:
		asuntos = [u"Acompañamiento pastoral y familiar",
		u"Guía en el manejo de temas de sexualidad y presunción de situaciones de riesgo",
		u"Consejo y guía espiritual",
		u"Guía o explicación respecto a la interacción entre compañeros y manejo de conflictos", 
		u"Solicitud de cita con un profesor, mentor, coordinador, sicólogo o capellán", 
		u"Comentarios, sugerencias o reclamos concernientes a un profesor, grado o la institución", 
		u"Otros"]
	else:
		asuntos = ""

	if request.method == "POST":
		form = TicketTemasForm(request.POST)
		if form.is_valid():
			tutor = form.cleaned_data["tutor"]
			email = form.cleaned_data["email"]
			subject = form.cleaned_data["subject"]
			message = request.POST.get("message")
			student = form.cleaned_data["student"]
			grade = form.cleaned_data["grade"]
			payload = {"name": tutor,
				"email":email,
				"subject":subject,
				"message":message,
				"student":student,
				"grade":grade,
				"topicId":tema.id_ticket,
			}


			id_ticket = int(tema.id_ticket)

			aplicante = {"name": tutor, "student":student, "grade":u"{0}".format(grade), "subject":u"{0}".format(subject), "message":u"{0}".format(message)}

			if id_ticket == 0:

				mensaje = MailerMessage()
				mensaje.general_message(tema.correo_ticket, "comunicaciones@montebelloacademy.org", 35, aplicante)

				return render(request, 'canales_sam/success_parents.html', {"departamento":tema.nombre})


			attachments = []
			for file in request.FILES.getlist('files[]'):
				#try:
				#return file.read()
				content = file.read()
				#return content.encode('base64')
				registro = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(registro)
				#return registro
				#except:
					#pass



			payload['attachments'] = attachments
			new_ticket.delay(payload)
			return render(request, 'canales_sam/success_parents.html', {"departamento":tema.nombre})
		else:
			print form.errors
			return render(request, "canales_sam/message_topics.html", {"tema":tema, "form":form, "asuntos":asuntos})
	else:
		form = TicketTemasForm()
		return render(request, "canales_sam/message_topics.html", {"tema":tema, "form":form, "asuntos":asuntos})





@login_required(login_url = '/user/login/')
def index(request):
	email =request.user
	try:
		registro = Registro_Temas.objects.get(usuario__email = email)
	except Registro_Temas.DoesNotExist:
		return render(request, "canales_sam/forbidden.html",{})
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		attachment = request.FILES.get('attachment')
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'statusId':'3',
		   'topicId':'{0}'.format(registro.id_ticket),
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertUser':True,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments


			if "Temas Generales" in subject:

				new_email2.delay(payload, message, registro.correo_ticket, adjuntos)
				#send_mail(u'{0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()) , u"{0}".format(message), "{0}".format(registro.correo_ticket), ["{0}".format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email)], fail_silently = False, auth_user = "{0}".format(registro.correo_ticket), auth_password = "Montebello1", html_message = u"{0}".format(message))

			
			else:

				#create_ticket(payload)
				new_ticket_teacher2.delay(payload, message, registro.correo_ticket, adjuntos)


		return render(request, 'canales_sam/success.html', {})





	else:
		try:
			asignaciones = Asignacion_Profesores.objects.filter(profesor__id_teachers__email = email).order_by('actividad__grupo', "actividad__materia")
		except Asignacion_Profesores.DoesNotExist:
			return render(request, "canales_sam/forbidden.html",{})

		grupos = asignaciones.values_list("actividad__grupo", flat = True).distinct()
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, matricula__estado_matricula__fin = None, matricula__estado_matricula__matricula_activa = True , inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")

		#return estudiantes

		return render(request,'canales_sam/index.html', {"asignaciones":asignaciones, "grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})



@login_required(login_url = '/user/login/')
def list_department(request):
	email = request.user
	usuario = User.objects.get(email = email)
	departamentos = Registro_Grupos.objects.filter(grupo__in = usuario.groups.all())
	if not departamentos.exists():
		return render(request, "canales_sam/forbidden.html",{})
	return render(request, "canales_sam/lista_departamentos.html", {"departamentos":departamentos})


@login_required(login_url = '/user/login/')
def message_department(request, id_departamento):
	email = request.user
	usuario = User.objects.get(email = email)
	departamento = Registro_Grupos.objects.get(id = id_departamento)
	if not usuario.groups.filter(id = departamento.grupo.pk).exists():
		return render(request, "canales_sam/forbidden.html",{})
	today = date.today()
	form = ComunicacionForm()
	form2 = AdjuntoForm()	

	if request.method == "POST":
		
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)

		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'topicId':'{0}'.format(departamento.id_ticket),
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			new_ticket_teacher2.delay(payload, message, departamento.correo_ticket, adjuntos)
		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, matricula__estado_matricula__fin = None, matricula__estado_matricula__matricula_activa = True , inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")
		return render(request,'canales_sam/message_departments.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2, "departamento":departamento})


@login_required(login_url = '/user/login/')
@user_passes_test(is_dece)
def message_dece(request):
	email =request.user
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'topicId':'72',
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			new_ticket_teacher2.delay(payload, message, "dece@montebelloacademy.org", adjuntos)
		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")
		return render(request,'canales_sam/message_dece.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})



		
@login_required(login_url = '/user/login/')
@user_passes_test(is_psicologia)
def message_psico(request):
	email =request.user
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		attachment = request.FILES.get('attachment')
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'statusId':'3',
		   'topicId':'74',
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			#return json.dumps(payload)
			new_ticket_teacher2.delay(payload, message, "psicologia_dece@montebelloacademy.org", adjuntos)
		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")

		#return estudiantes

		return render(request,'canales_sam/message_psico.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})


@login_required(login_url = '/user/login/')
@user_passes_test(is_capellania)
def message_cape(request):
	email =request.user
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		attachment = request.FILES.get('attachment')
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'statusId':'3',
		   'topicId':'75',
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			#return json.dumps(payload)
			new_ticket_teacher2.delay(payload, message, "pastoral_dece@montebelloacademy.org", adjuntos)
		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")

		#return estudiantes

		return render(request,'canales_sam/message_cape.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})


@login_required(login_url = '/user/login/')
@user_passes_test(is_disciplina)
def message_disci(request):
	email =request.user
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		attachment = request.FILES.get('attachment')
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'statusId':'3',
		   'topicId':'76',
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			#return json.dumps(payload)
			new_ticket_teacher2.delay(payload, message, "disciplina_dece@montebelloacademy.org", adjuntos)
		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")

		#return estudiantes

		return render(request,'canales_sam/message_disci.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})



@login_required(login_url = '/user/login/')
@user_passes_test(is_extracurriculares)
def message_extras(request):
	email =request.user
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		attachment = request.FILES.get('attachment')
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'statusId':'3',
		   'topicId':'19',
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			#return json.dumps(payload)
			new_ticket_teacher2.delay(payload, message, "extracurriculares@montebelloacademy.org", adjuntos)

		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")

		#return estudiantes

		return render(request,'canales_sam/message_extras.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})


@login_required(login_url = '/user/login/')
@user_passes_test(is_transporte)
def message_trans(request):
	email =request.user
	form = ComunicacionForm()
	form2 = AdjuntoForm()
	
	today = date.today()

	if request.method == "POST":
		
		attachment = request.FILES.get('attachment')
		subject = request.POST.get('subject')
		message = request.POST.get('html')
		students = []
		for value in request.POST:
			if "stud_" in value:
				student = value[5:]
				students.append(student)


		for entry in students:
			student = Matricula_Grupo.objects.get(pk = entry)
			payload = {'name': '{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.get_full_name()),
		   'subject': 'Montebello - {0} - {1}'.format(subject, student.matricula.estudiante.user.get_full_name()),
		   'message': 'data:text/html,{0}'.format(message),
		   'student': '{0}'.format(student.matricula.estudiante.user.get_full_name()),
		   'grade': '{0}'.format(student.grupo.nombre),
		   'email':'{0}'.format(student.matricula.estudiante.student_relative_set.filter(legal_representative = True).first().relative.user.email),
		   'statusId':'3',
		   'topicId':'15',
		   'autorespond':True,
		   'autoreply':True,
		   'alert':False,
		   'alertuser':True

			}

			attachments = []
			adjuntos = []

			for file in request.FILES.getlist('files[]'):

				content = file.read()
				archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type,content.encode('base64'))}
				attachments.append(archivo)

				adjunto = [file.name, content.encode("base64"), file.content_type]
				adjuntos.append(adjunto)

			payload['attachments'] = attachments
			#return json.dumps(payload)
			new_ticket_teacher2.delay(payload, message, "trasnporte@montebelloacademy.org", adjuntos)

		return render(request, 'canales_sam/success.html', {})

	else:

		grupos = Grupo.objects.filter(activo = True, periodo_lectivo__actual = True)
		estudiantes = Matricula_Grupo.objects.filter(matricula__clase__periodo_lectivo__actual = True, inicio__lte = today, fin = None, grupo__in = grupos).order_by("matricula__estudiante__user__father_last_name")

		#return estudiantes

		return render(request,'canales_sam/message_trans.html', {"grupos":grupos, "estudiantes":estudiantes, "form":form, "form2":form2})