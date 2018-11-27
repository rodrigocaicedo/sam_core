from __future__ import unicode_literals

import datetime
import logging


import os

from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.template import Template, Context

from . import defaults
from .utils import get_storage, upload_to

from admisiones_sam.models import Applications

from django.contrib.auth.models import Group

logger = logging.getLogger(__name__)

# Create your models here.


class Direccion_Envio_Grupo(models.Model):
    grupo = models.OneToOneField(Group)
    correo = models.EmailField()

    def __unicode__(self):
        return self.correo



class Direccion_Envio(models.Model):
    correo = models.EmailField(unique = True)
    usuario = models.CharField(max_length = 300)
    clave = models.CharField(max_length = 300)
    host = models.URLField(max_length = 500)
    puerto = models.CharField(max_length = 10)    

    def __unicode__(self):
        return self.correo


class Comunicacion(models.Model):
    created = models.DateField(auto_now_add = True)
    name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    content = models.TextField()

    def __unicode__(self):
        return self.name

class Adjunto(models.Model):
    attached_to = models.ForeignKey("Comunicacion")
    attachment = models.FileField(upload_to = "messages/attachments")
    attachment_mimetype = models.CharField(max_length = 500)

#----------------------------------------------------------------------------
# Method for messages table
class MailerMessageManager(models.Manager):
    def send_queued(self, limit=None):
        if limit is None:
            limit = getattr(settings, 'MAILQUEUE_LIMIT', defaults.MAILQUEUE_LIMIT)

        for email in self.filter(sent=False)[:limit]:
            email.send_mail()

    def clear_sent_messages(self, offset=None):
        """ Deletes sent MailerMessage records """
        if offset is None:
            offset = getattr(settings, 'MAILQUEUE_CLEAR_OFFSET', defaults.MAILQUEUE_CLEAR_OFFSET)

        if type(offset) is int:
            offset = datetime.timedelta(hours=offset)

        delete_before = timezone.now() - offset
        self.filter(sent=True, last_attempt__lte=delete_before).delete()


@python_2_unicode_compatible
class MailerMessage(models.Model):
    created = models.DateTimeField(_('Created'), auto_now_add=True, auto_now=False,
                                   editable=False, null=True)
    template = models.ForeignKey(Comunicacion)
    #subject = models.CharField(_('Subject'), max_length=250, blank=True)
    to_address = models.TextField(_('To'))
    bcc_address = models.TextField(_('BCC'), blank=True)
    from_address = models.EmailField(_('From'), max_length=250)
    reply_to = models.TextField(_('Reply to'), max_length=250, blank=True, null=True)
    #content = models.TextField(_('Content'), blank=True)
    #html_content = models.TextField(_('HTML Content'), blank=True)
    app = models.CharField(_('App'), max_length=250, blank=True)
    sent = models.BooleanField(_('Sent'), default=False, editable=False)
    last_attempt = models.DateTimeField(_('Last attempt'), auto_now=False, auto_now_add=False,
                                        blank=True, null=True, editable=False)

    objects = MailerMessageManager()

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return self.template.subject

    def application_message(self, applicant_pk, message_pk):
        try:

           # template = Comunicacion.objects.get(pk = 1)
            template = Comunicacion.objects.get(pk = message_pk)
            applicant = Applications.objects.get(pk = applicant_pk)
        except:
            return
        self.template = template
        self.from_address = "comunicaciones@montebelloacademy.org"
        self.to_address = applicant.mail_tutor
        self.app = "admisiones_sam"
        

        context = Context({"aplicante":applicant})
        subject_template = Template(template.subject)
        content_template = Template(template.content)

        self.last_attemp = timezone.now()

        from_email = self.from_address
        #subject="1234"
        subject = subject_template.render(context)
        #content = "1234"
        content = content_template.render(context)

        msg = EmailMultiAlternatives(subject,content,from_email)
        msg.attach_alternative(content,"text/html")
        msg.to = [email.strip() for email in self.to_address.split(',') if email.strip()]
        try:
            msg.send()
            self.sent = True
            
        except Exception as e:
            self.do_not_send = True
            logging.basicConfig()
            logger.error('Mail Queue Exception: {0}'.format(e))
        #super(MailerMessage, self).save(*args, **kwargs)
        #return
        self.save()

    #def general_message(self):
    def general_message(self, receiver_email ,sender_email, message_pk, variable):
        try:
           # template = Comunicacion.objects.get(pk = 1)
            template = Comunicacion.objects.get(pk = message_pk)
            sender = Direccion_Envio.objects.get(correo = sender_email)
            #return sender, template
        except:
            return
        self.template = template
        #self.from_address = "comunicaciones@montebelloacademy.org"
        self.from_address = sender.correo
        #self.to_address = applicant.mail_tutor
        self.to_address = receiver_email
        self.app = "General"
        

        context = Context({"aplicante":variable})
        subject_template = Template(template.subject)
        content_template = Template(template.content)

        self.last_attemp = timezone.now()

        subject = subject_template.render(context)
        #content = "1234"
        content = content_template.render(context)
        
        with get_connection(host="smtp.office365.com",port=587,username=sender.usuario,password = sender.clave ,fail_silently = False) as connection:
        #mensaje = EmailMultiAlternatives(subject=u"{0}".format(payload["subject"]),body=u"{0}".format(message),from_email="{0}".format(email_registro),to=["{0}".format(payload["email"])], connection = connection)
        
            msg = EmailMultiAlternatives(subject,content,sender.correo, connection = connection)
            msg.attach_alternative(content,"text/html")
            msg.to = [email.strip() for email in self.to_address.split(',') if email.strip()]
            
            for attachment in self.attachment_set.all():
                path = attachment.file_attachment.path
                if os.path.isfile(path):
                    with open(path, 'rb') as f:
                        content = f.read()
                    msg.attach(attachment.original_filename, content, None)

            for adjunto in self.template.adjunto_set.all():
                archivo = adjunto.attachment
                nombre = archivo.name.split("/")[-1]

                msg.attach(nombre, archivo.read(), adjunto.attachment_mimetype)

            try:
                msg.send()
                self.sent = True
            
            except Exception as e:
                self.do_not_send = True
                logging.basicConfig()
                logger.error('Mail Queue Exception: {0}'.format(e))
        #####super(MailerMessage, self).save(*args, **kwargs)
        #####return
        self.save()   

    def add_attachment(self, attachment):
        """
        Takes a Django `File` object and creates an attachment for this mailer message.
        """
        if self.pk is None:
            self._save_without_sending()

        Attachment.objects.create(email=self, file_attachment=attachment,
                                  original_filename=attachment.file.name.split('/')[-1])

    def _save_without_sending(self, *args, **kwargs):
        """
        Saves the MailerMessage instance without sending the e-mail. This ensures
        other models (e.g. `Attachment`) have something to relate to in the database.
        """
        self.do_not_send = True
        super(MailerMessage, self).save(*args, **kwargs)

    def send_mail(self):
        """ Public api to send mail.  Makes the determinination
         of using celery or not and then calls the appropriate methods.
        """

        if getattr(settings, 'MAILQUEUE_CELERY', defaults.MAILQUEUE_CELERY):
            from .tasks import send_mail
            #from mailqueue.tasks import send_mail
            send_mail.delay(self.pk)
        else:
            self._send()

    def _send(self):
        if not self.sent:
            self.last_attempt = timezone.now()

            context = Context({})
            subject_template = Template(self.template.subject)
            content_template = Template(self.template.content)

            subject = subject_template.render(context)

            from_email = self.from_address

            text_content = content_template.render(context)

            msg = EmailMultiAlternatives(subject, text_content, from_email)

            if self.reply_to:
                msg.extra_headers.update({"reply-to": self.reply_to})

            if self.template.content:
                html_content = content_template.render(context)
                msg.attach_alternative(html_content, "text/html")

            msg.to = [email.strip() for email in self.to_address.split(',') if email.strip()]
            msg.bcc = [email.strip() for email in self.bcc_address.split(',') if email.strip()]

            # Add any additional attachments
            for attachment in self.attachment_set.all():
                path = attachment.file_attachment.path
                if os.path.isfile(path):
                    with open(path, 'rb') as f:
                        content = f.read()
                    msg.attach(attachment.original_filename, content, None)

            for adjunto in self.template.adjunto_set.all():
                archivo = adjunto.attachment
                nombre = archivo.name.split("/")[-1]

                msg.attach(nombre, archivo.read(), adjunto.attachment_mimetype)

            try:
                msg.send()
                self.sent = True
            except Exception as e:
                self.do_not_send = True
                logger.error('Mail Queue Exception: {0}'.format(e))
            self.save()



@python_2_unicode_compatible
class Attachment(models.Model):
    file_attachment = models.FileField(blank=True, null=True)

    #file_attachment = models.FileField(storage=get_storage(), upload_to=upload_to,blank=True, null=True)

    original_filename = models.CharField(default=None, max_length=250, blank=False)
    email = models.ForeignKey(MailerMessage, blank=True, null=True)

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')

    def __str__(self):
        return self.original_filename
