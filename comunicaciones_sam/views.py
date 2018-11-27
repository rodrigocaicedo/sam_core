#from django.shortcuts import render
from django.template import loader
from django.template import Template, Context
#from django.template import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect

from general_sam.models import Matricula, Clase, Grupo, Periodo_Lectivo

from .models import Comunicacion, Adjunto, MailerMessage

from .forms import ComunicacionForm, AdjuntoForm

from admisiones_sam.models import Applications
#from mailqueue.models import MailerMessage


@login_required(login_url = '/user/login/')
def Correo_General(request):
	try:
		periodo_lectivo = Periodo_Lectivo.objects.get(pk = request.session["schoolyear_pk"])
	except:
		periodo_lectivo = Periodo_Lectivo.objects.last()
	form = ComunicacionForm()

	if request.method == "POST":


		subject = request.POST.get('subject')
		content = request.POST.get('html')
		
		#cabecera = "{% extends 'email.html' %}{% load extras %}{% load staticfiles %}{% block contenido %}"
		#pie = "{% endblock %}"
		#content = cabecera+content+pie
		
		comunicacion = Comunicacion.objects.create(name = subject, subject = subject, content = content)

		attachments = []
		adjuntos = []

		for file in request.FILES.getlist('files[]'):

			obj_adjunto = Adjunto.objects.create(attached_to = comunicacion, attachment = file, attachment_mimetype = file.content_type)

			content = file.read()
			archivo = {'{0}'.format(file.name):'data:{0};base64,{1}'.format(file.content_type, content.encode('base64'))}
			attachments.append(archivo)

			adjunto = [file.name, content.encode("base64"), file.content_type]
			adjuntos.append(adjunto)

		lista_envio = ["mariacristinamunoz@montebelloacademy.org"]
		
		for pk_matricula in request.POST.getlist("estudiante[]"):

			estudiante = Matricula.objects.get(pk = pk_matricula).estudiante
			for relacion in estudiante.student_relative_set.filter(notifications = True):
				correo_representante = relacion.relative.user.email
				if correo_representante not in lista_envio:
					lista_envio.append(correo_representante)


		for correo in lista_envio:
			mensaje = MailerMessage()

			mensaje.template = comunicacion
			mensaje.from_address = "comunicaciones@montebelloacademy.org"
			mensaje.app = "envio_correos"
			mensaje.to_address = correo

			mensaje.save()




			#mensaje.general_message(correo, "comunicaciones@montebelloacademy.org", comunicacion.pk, None)


		return lista_envio


	clases = Clase.objects.filter(periodo_lectivo = periodo_lectivo).order_by("nivel__pk")
	return render(request, "comunicaciones_sam/correo_general.html", {"clases":clases, "form":form})



def Send_Email_Applicant(request, info, comunicacion):
	comunicacion = Comunicacion.objects.get(pk = comunicacion) # Tipo de comunicacion a enviarse
	receiver = Applications.objects.get(pk = info) # Aplicante que recibe la info
	message = MailerMessage() # Objeto mensaje de aplicacion mailqueue
	message.template = comunicacion # Asunto del mensaje
	message.from_address = "admisiones@montebelloacademy.org" # Direccion de envio
	message.to_address = receiver.mail_tutor # email del tutor del aplicante
	message.app = "comunicaciones_sam" # aplicacion que envia correo
	#revisar si el mensaje a enviar tiene  adjuntos , si lo hace adjuntar el archivo correspondiente
	try:
		attachments = Adjunto.objects.filter(attached_to = comunicacion)
		for attachment in attachments:
			message.add_attachment(attachment.file_attachment)
	except:
		pass
	#template = Template("My name is {{ aplicante.applies_grade }}.")
	template = Template(comunicacion.content)
	context = Context({"aplicante":receiver,})
	message.html_content = template.render(context)
	message.content = template.render(context)
	message.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))



def run_mail_job(request):
    MailerMessage.objects.send_queued()

    response = HttpResponse()
    response.status_code = 200
    return response


def clear_sent_messages(request):
    MailerMessage.objects.clear_sent_messages()

    response = HttpResponse()
    response.status_code = 200
    return response

# Create your views here.
