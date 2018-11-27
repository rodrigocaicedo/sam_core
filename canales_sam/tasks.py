# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task

import base64

from canales_sam.ticketservice import create_ticket
from canales_sam.models import Registro_Temas
from django.core.mail import send_mail, get_connection, EmailMessage, EmailMultiAlternatives

#@shared_task(default_retry_delay=5, max_retries=20)
@shared_task()
def new_ticket_teacher(payload, message, email_registro):
    ticket = create_ticket(payload)
    send_mail(u"{1} [#{0}]".format(ticket, payload["subject"]) , u"{0}".format(message), "{0}".format(email_registro), ["{0}".format(payload["email"])], fail_silently = False, auth_user = "{0}".format(email_registro), auth_password = "Montebello1", html_message = u"{0}".format(message))

@shared_task()
def new_email(payload, message, email_registro):
	send_mail(u"{0}".format(payload["subject"]) , u"{0}".format(message), "{0}".format(email_registro), ["{0}".format(payload["email"])], fail_silently = False, auth_user = "{0}".format(email_registro), auth_password = "Montebello1", html_message = u"{0}".format(message))
	#send_mail(u'{0} - {1}'.format(subject, student.matricula.estudiante.id_students.get_full_name()) , u"{0}".format(message), "{0}".format(registro.correo_ticket), ["{0}".format(student.matricula.estudiante.id_tutor.email)], fail_silently = False, auth_user = "{0}".format(registro.correo_ticket), auth_password = "Montebello1", html_message = u"{0}".format(message))

    #send_mail("Hola", "que chevere mensaje", "comunicaciones@montebelloacademy.org", ["rodrigocaicedop@outlook.com"], fail_silently=False)
    #return hola
    # Retry when message is not sent

@shared_task()
def new_ticket(payload):
    ticket = create_ticket(payload)



@shared_task()
def new_ticket_teacher2(payload, message, email_registro, adjuntos):
    ticket = create_ticket(payload)
    with get_connection(host="smtp.office365.com",port=587,username="{0}".format(email_registro),password = "Montebello1",fail_silently = False) as connection:
        mensaje = EmailMultiAlternatives(subject=u"{1} [#{0}]".format(ticket, payload["subject"]),body=u"{0}".format(message),from_email="{0}".format(email_registro),to=["{0}".format(payload["email"])], connection = connection)
        for adjunto in adjuntos:
            contenido = base64.decodestring(adjunto[1]) 
            mensaje.attach(adjunto[0], contenido, adjunto[2])


        #attachments = payload["attachments"]
        #for attachment in attachments:
        #    for key, value in attachment.items():
        #        filename = key
        #        file_detail = attachment[key]
        #        file_detail = file_detail[5:]
        #        file_type = file_detail[0:file_detail.index(";")]
        #        file_content = file_detail[file_detail.index(",")+1:]
        #        mensaje.attach(filename, file_content.decode("base64"), file_type)
        mensaje.attach_alternative(message, "text/html")
        mensaje.send()


@shared_task()
def new_email2(payload, message, email_registro, adjuntos):
    with get_connection(host="smtp.office365.com",port=587,username="{0}".format(email_registro),password = "Montebello1",fail_silently = False) as connection:
        mensaje = EmailMultiAlternatives(subject=u"{0}".format(payload["subject"]),body=u"{0}".format(message),from_email="{0}".format(email_registro),to=["{0}".format(payload["email"])], connection = connection)
        for adjunto in adjuntos:
            contenido = base64.decodestring(adjunto[1]) 
            mensaje.attach(adjunto[0], contenido, adjunto[2])
        mensaje.attach_alternative(message, "text/html")
        mensaje.send()