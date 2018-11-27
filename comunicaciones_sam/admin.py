from django.contrib import admin
from comunicaciones_sam.models import Attachment, Comunicacion, MailerMessage, Direccion_Envio

from django.utils.translation import ugettext_lazy as _


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 0


class MailerAdmin(admin.ModelAdmin):
    #list_display = ('created', 'subject', 'to_address', 'app', 'sent', 'last_attempt', 'reply_to')
    list_display = ('created', 'template', 'to_address', 'app', 'sent', 'last_attempt', 'reply_to')    
    #search_fields = ['to_address', 'subject', 'app', 'bcc_address', 'reply_to']
    search_fields = ['to_address', 'template__subject', 'app', 'bcc_address', 'reply_to']
    actions = ['send_failed']
    inlines = [AttachmentInline]

    def send_failed(self, request, queryset):
        emails = queryset.filter(sent=False)
        for email in emails:
            email.send_mail()
        self.message_user(request, _("Emails queued."))
    send_failed.short_description = _("Send failed")

# Register your models here.

admin.site.register(Direccion_Envio)
admin.site.register(Comunicacion)
admin.site.register(MailerMessage, MailerAdmin)



