from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (Email, SftpCommunication, EmailRecipient,
                     CommunicationEventType)


class CommunicationEventTypeAdmin(admin.ModelAdmin):
    readonly_fields = (
        'code',
        'name',
    )
    list_display = (
        'name',
        'code',
        'category',
        'sftp_profile',
        'get_email_recipients_str',
        'get_managing_ous_str',
        'date_updated',
    )
    filter_horizontal = ('email_recipients',)

    @admin.display(description=_('Managing organization units'))
    def get_managing_ous_str(self, obj):
        return ', '.join(obj.get_managing_ous().values_list('name', flat=True))

    @admin.display(description=_('Receiving E-Mail Addresses'))
    def get_email_recipients_str(self, obj):
        """ used in admin """
        return ', '.join(sorted(obj.get_email_recipients())) or '-'


class EmailRecipientAdmin(admin.ModelAdmin):
    list_display = (
        'email_address',
        'get_email_address_source_types_str',
    )


admin.site.register(Email)
admin.site.register(SftpCommunication)
admin.site.register(EmailRecipient, EmailRecipientAdmin)
admin.site.register(CommunicationEventType, CommunicationEventTypeAdmin)
