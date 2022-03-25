import io
from os.path import expanduser
from socket import gaierror
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.contrib.sites.models import Site
import paramiko
from oscar.apps.communication import abstract_models
from custom.site_manager import DefaultSiteManager, SiteMixin
from .managers import CommunicationTypeManager


class SftpCommunication(models.Model):
    sftp_profile_title = models.CharField(
        _('SFTP profile title'), max_length=150, unique=True,
        help_text=_('Title of this profile'),
    )
    sftp_path = models.CharField(
        _('SFTP path'), max_length=500,
        help_text=_('Directory path on the target system'),
        null=True, blank=True,
    )
    sftp_host = models.CharField(
        _('SFTP hostname'), max_length=150,
        help_text=_('Hostname of the target system to connect to'),
        null=True, blank=True,
    )
    sftp_port = models.PositiveSmallIntegerField(
        _('SFTP port'),
        help_text=_('Port of the target system to connect to'),
        default=22,
    )
    sftp_user = models.CharField(
        _('SFTP username'), max_length=150,
        help_text=_('Username of the target system SFTP account'),
        null=True, blank=True,
    )
    sftp_cert = models.TextField(
        _('SFTP certificate'),
        help_text=_('Certificate of the target system SFTP account'),
        null=True, blank=True,
    )
    sftp_password = models.CharField(
        _('SFTP password'), max_length=150,
        help_text=_('Password of the target system SFTP account or certificate'),
        null=True, blank=True,
    )

    def clean(self):
        path_valid = all(
            [self.sftp_path, self.sftp_host, self.sftp_port]
        )
        if self.sftp_path and not self.sftp_path.endswith('/'):
            self.sftp_path += '/'
        if not path_valid:
            err = ValidationError(
                _('Path, host and port are needed for sftp')
            )
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_path': err,
                'sftp_host': err,
                'sftp_port': err,
            })

        login_valid = all(
            [self.sftp_user]
        )
        if not login_valid:
            err = ValidationError(
                _('User is needed for sftp')
            )
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_user': err,
            })

        try:
            self.sftp_test_write()
        except paramiko.ssh_exception.BadAuthenticationType as err:
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_cert': err,
            }) from err
        except FileNotFoundError as err:
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_path': err,
            }) from err

    def get_full_path(self):
        return f'{self.sftp_user}@{self.sftp_host}:{self.sftp_port}{self.sftp_path}'

    def sftp_test_write(self):
        teststring ='TESTSTRING\n'
        return self.sftp_write('.testfile', teststring,)

    def sftp_write(self, filename, rendered_content):
        sftp_client = self.sftp_get_client()
        sftp_client.chdir(path=self.sftp_path)
        try:
            file = sftp_client.file(filename, mode='rw')
        except PermissionError as err:
            sftp_client.close()
            raise ValidationError({'sftp_path': err}) from err

        file.write(rendered_content)
        file.close()

        file = sftp_client.file(filename, mode='r')
        result = file.read().decode('utf-8') == rendered_content
        file.close()
        #sftp_client.remove(filename)
        sftp_client.close()
        return result

    def local_write(self, filename, rendered_content):
        with open('/tmp/' + filename, 'w') as file:
            file.write(rendered_content)

    def sftp_get_client(self):
        return self.sftp_get_ssh_client().open_sftp()

    def sftp_get_ssh_client(self):
        client = paramiko.client.SSHClient()
        client.load_host_keys(expanduser('~/.ssh/known_hosts'))
        try:
            client.connect(**self.sftp_get_ssh_kwargs())
        except gaierror as err:  # [Errno -2] Name or service not known
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_host': err,
            }) from err
        except OSError as err:
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_port': err,
            }) from err
        except paramiko.ssh_exception.PasswordRequiredException as err:
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_password': err,
            }) from err
        except (paramiko.ssh_exception.AuthenticationException,
                paramiko.ssh_exception.SSHException) as err:
            raise ValidationError({
                NON_FIELD_ERRORS: err,
                'sftp_user': err,
                'sftp_cert': err,
                'sftp_password': err,
            }) from err
        return client

    def sftp_get_ssh_kwargs(self):
        kwargs = {
            'hostname': self.sftp_host,
            'port': self.sftp_port,
            'username': self.sftp_user,
            #'password': self.sftp_password,
            'pkey': self.sftp_get_public_key(),
            'allow_agent': False,
            'look_for_keys': False,
        }
        if self.sftp_password:
            kwargs['password'] = self.sftp_password
        return kwargs

    def sftp_get_public_key(self):
        if self.sftp_cert:
            private_key_file = io.StringIO()
            private_key_file.write(self.sftp_cert)
            private_key_file.seek(0)
            return paramiko.RSAKey.from_private_key(private_key_file)#self.sftp_cert)

    def __str__(self):
        return str(self.sftp_profile_title)

    class Meta:
        verbose_name = _('SFTP Communication Profile')


class EmailRecipient(SiteMixin, models.Model):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    email_address = models.EmailField(
        _('E-Mail Recipient'),
        null=True, blank=True,
    )

    def get_email_address_source_types_str(self):
        codes = self.communicationeventtype_set.values_list('code', flat=True)
        return ', '.join(codes)

    def __str__(self):
        return str(self.email_address)


class FormatChoices(models.IntegerChoices):
    BOTH = 0, _('HTML and plain text')
    HTML = 1, _('HTML')
    PLAIN = 2, _('Plain text')


class EventTypeChoices(models.IntegerChoices):
    EMAIL_CHANGED       = 1, _('E-Mail geändert')
    ORDER_PLACED        = 2, _('Bestellung')
    PASSWORD_CHANGED    = 3, _('Passwortänderung')
    PASSWORD_RESET      = 4, _('Passwortrücksetzung')
    PRODUCT_ALERT       = 5, _('Produktbenachrichtigung')
    REGISTRATION        = 6, _('Registrierung')

    #Custom:
    ORDER_PLACED_INTERNAL_WITH_BANK     = \
        21, _('Bestellungsinformationen mit Bankdaten')
    ORDER_PLACED_INTERNAL_WITHOUT_BANK  = \
        22, _('Bestellungsinformationen ohne Bankdaten')
    ORDER_PLACED_MACHINE1               = \
        23, _('Maschinenlesbare E-Mail 1')
    ORDER_PLACED_INTERNAL_TRANSFER      = \
        24, _('Bestellungsinformationen Überweisung')
    OBJECTS_IMPORTED = 25, _('Objekte importiert')


class CommunicationEventType(SiteMixin, abstract_models.AbstractCommunicationEventType):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    event_type = models.PositiveSmallIntegerField(
        verbose_name=_("Communication event type"),
        choices=EventTypeChoices.choices,
        unique=True,
    )
    format = models.PositiveSmallIntegerField(
        _('E-Mail Format'),
        help_text=_('Choose Format if matching template exists (only Custom)'),
        choices=FormatChoices.choices,
        default=FormatChoices.BOTH,
    )
    sftp_profile = models.ForeignKey(
        SftpCommunication,
        verbose_name=_('SFTP profile'),
        help_text=_('If this is set, we will only write sftp file'),
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    email_recipients = models.ManyToManyField(
        EmailRecipient,
        verbose_name=_('E-Mail recipients'),
        help_text=_('Empfangen alle Nachrichten dieses Typs.'),
        blank=True,
    )
    objects = CommunicationTypeManager()

    def get_messages(self, ctx=None):
        self.email_subject_template = self.email_subject_template or None
        self.email_body_template = self.email_body_template or None
        self.email_body_html_template = self.email_body_html_template or None
        self.sms_template = self.sms_template or None
        messages = super().get_messages(ctx=ctx)
        return messages

    def get_managing_ous(self):
        return self.managing_ous.all()

    def get_email_recipients(self):
        recipients = set()
        if not self.id:
            return recipients

        recipients.update(
            self.email_recipients.values_list('email_address', flat=True)
        )

        return recipients

    def save(self, **kwargs):  #pylint: disable=arguments-differ
        if self.event_type:
            event_type = EventTypeChoices(self.event_type)
            self.code = str(event_type.name)
            self.name = str(event_type.label)
        elif self.code:
            event_type = getattr(EventTypeChoices, self.code)
            self.event_type = event_type
            self.name = self.event_type.label
        return super().save(**kwargs)


class Email(SiteMixin, abstract_models.AbstractEmail):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    subject = models.TextField(
        _('Subject or sftp filename'),
        max_length=255,
        help_text=_('If Sftp profile is set, this is the Filename'),
    )


from oscar.apps.communication.models import *  # noqa isort:skip
