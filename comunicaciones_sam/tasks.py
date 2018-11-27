from __future__ import absolute_import

from celery import shared_task

from comunicaciones_sam.models import MailerMessage


@shared_task(name="comunicaciones_sam.tasks.send_mail", default_retry_delay=5, max_retries=5, rate_limit = "5/m")
def send_mail(pk):
    message = MailerMessage.objects.get(pk=pk)
    message._send()

    # Retry when message is not sent
    if not message.sent:
        send_mail.retry([message.pk])


@shared_task()
def clear_sent_messages():
    from comunicaciones_sam.models import MailerMessage
    MailerMessage.objects.clear_sent_messages()
