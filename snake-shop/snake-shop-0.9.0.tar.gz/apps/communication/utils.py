from django.conf import settings
from django.core.mail import get_connection
from django.db.models import Q
from django.core.mail import EmailMessage, EmailMultiAlternatives
from oscar.apps.communication import utils
from custom.decorators import start_new_thread
from custom.context_processors import main as context_processor_main
from .models import CommunicationEventType, FormatChoices
from django.core.mail.backends.smtp import EmailBackend
from django.http.request import HttpRequest
from django.contrib.sites.models import Site
from apps.communication.models import Email


class Task:
    """ This is a E-Mail sending task to be sent by the oscar dispatcher """
    def __init__(self, site, recipients, messages, event_type, attachments=None):
        #self.site = Site.objects.get_current()
        self.site = site
        if settings.DEBUG or settings.STAGE !='PRODUCTIVE':
            messages['subject'] = '{}  --  <An: {}> {}'.format(
                messages['subject'],
                ', '.join(recipients),
                event_type.code,
            )
            self.recipients = [
                f'{name} <{email}>' for name, email in settings.ADMINS
            ]
        else:
            self.recipients = recipients
        self.messages = messages
        self.attachments = attachments

    @property
    def email(self):
        """
        This is the first part of the original Dispatcher send_email_messages.
        Now every Email can have multiple recipients
        """
        from_email = self.site.configuration.get_email_sender()
        content_attachments, file_attachments = self.prepare_attachments()

        messages = self.messages
        recipients = self.recipients
        # Determine whether we are sending a HTML version too
        if messages['html']:
            email = EmailMultiAlternatives(
                messages['subject'],
                messages['body'],
                from_email=from_email,
                to=recipients,
                attachments=content_attachments,
            )
            email.attach_alternative(messages['html'], "text/html")
        else:
            email = EmailMessage(
                messages['subject'],
                messages['body'],
                from_email=from_email,
                to=recipients,
                attachments=content_attachments,
            )
        for attachment in file_attachments:
            email.attach_file(attachment)
        return email

    def prepare_attachments(self):
        return utils.Dispatcher().prepare_attachments(self.attachments)


class SftpTask:
    def __init__(self, sftp_profile, messages):
        self.sftp_profile = sftp_profile
        self.messages = messages


class CommunicationJob:
    """
    Decides what E-Mail should be sent.
    It is the point of view of the CommunicationEventType.
    """
    def __init__(self, dispatcher, event_type, mail_connection, *args,
                 fail_silently=True, threaded=True, **kwargs):
        self.threaded = threaded
        self.event_type = event_type #self.get_event_type(event_code)
        self.main_email_task = None
        self.email_tasks = []
        self.sftp_tasks = []
        self.mail_connection = mail_connection
        self.logger = dispatcher.logger


    def send(self):
        """
        This method is called after all emails are created.
        """
        self.send_main_email()
        self.send_emails()
        self.dispatch_sftp_messages()

    def send_main_email(self):
        if self.main_email_task:
            self._send_func([self.main_email_task.email])

    def send_emails(self):
        func = self._send_func_threaded if self.threaded else self._send_func
        func([task.email for task in self.email_tasks if task])

    def set_main_email_task(self, task):
        assert self.main_email_task is None
        self.main_email_task = task

    def add_email_task(self, task):
        if task:
            self.email_tasks.append(task)

    @start_new_thread
    def _send_func_threaded(self, *args, **kwargs):
        self._send_func(*args, **kwargs)

    def _send_func(self, emails):
        self.mail_connection.send_messages(emails)
        all_recipients = set()
        for email in emails:
            for recipient in email.recipients():
                all_recipients.add(recipient)
        recipient_str = ', '.join(all_recipients)
        self.logger.info("Sending email to %s" % recipient_str)

    def add_sftp_task(self, sftp_task):
        self.sftp_tasks.append(sftp_task)

    @start_new_thread
    def dispatch_sftp_messages(self):
        for sftp_task in self.sftp_tasks:
            sftp_profile, messages = sftp_task.sftp_profile, sftp_task.messages
            filename, rendered_content = messages['subject'], messages['body']
            if settings.DEBUG:
                sftp_profile.local_write(filename, rendered_content)
            else:
                sftp_profile.sftp_write(filename, rendered_content)

    def __del__(self):
        self.mail_connection.close()


class Dispatcher(utils.Dispatcher):
    """
    For better overview this mixin contains all overwritten methods of original
    oscar Dispatcher
    """
    event_code = None
    threaded = False

    def __init__(self, logger=None, mail_connection=None, fail_silently=True,
                 extra_context=None, **kwargs):
        self.site = Site.objects.get_current()
        self.fail_silently = fail_silently
        self.extra_context = extra_context
        self.mail_connection = self.site.configuration.get_mail_connection()
        super().__init__(logger=logger, mail_connection=self.mail_connection)

    @property
    def event_type(self):
        assert self.event_code
        try:
            commtype = CommunicationEventType.objects.get(code=self.event_code)
        except CommunicationEventType.DoesNotExist:
            commtype = CommunicationEventType(code=self.event_code)
        return commtype

    def get_messages(self, event_code, extra_context=None):
        """
        Dirty solution to inject the event_code for builtin messages.
        EVENT_CODE is needed to determine what additional addresses will
        receive this message, too.
        get_messages and sending them needs to be called from same instance!
        """
        self.event_code = event_code
        messages = super().get_messages(event_code, extra_context=extra_context)
        if self.event_type.id:
            if self.event_type.format == FormatChoices.HTML:
                messages['body'] = ''
            elif self.event_type.format == FormatChoices.PLAIN:
                messages['html'] = ''
        return messages

    def get_base_context(self):
        context = super().get_base_context()
        context.update({
            'site': self.site,
            'CONFIG': self.site.configuration,
            'STAGE': settings.STAGE,
        })
        if self.extra_context:
            context.update(self.extra_context)

        if 'order' in context: #  WEG
            order = context['order']
            context['lines'] = order.lines.all()
            context['line_prices'] = order.line_prices.all()
            context['hide_price'] = order.user.hide_price,
        return context

    def create_email(self, user, messages, email):
        """
        Create ``Email`` instance in database for logging purposes.
        """
        if email and user.is_authenticated:
            return Email.objects.create(
                site=self.site,
                user=user,
                email=user.email,
                subject=email.subject,
                body_text=email.body,
                body_html=messages['html'],
            )

    def send_email_messages(self, *args, **kwargs):
        kwargs['from_email'] = self.site.configuration.get_email_sender()
        return utils.Dispatcher.send_email_messages(self, *args, **kwargs)


class CustomDispatcher(Dispatcher):
    threaded = not settings.DEBUG
    _job = None

    def __init__(self, event_code, site, extra_context=None, **kwargs):
        assert isinstance(event_code, str)
        site = Site.objects.get_current()
        assert isinstance(site, Site)
        self.extra_context = extra_context
        super().__init__(extra_context=extra_context, **kwargs)
        self.event_code = event_code
        self.site = site

    def send_email_messages(self, recipient_email, messages, from_email=None,
                            attachments=None):
        """
        Creates the main email and attaches it to the job.
        This is only called by the default oscar events.
        """
        self.create_main_email(
            recipient_email, messages, attachments=attachments
        )
        self.send_custom(messages=messages)

    def send_custom(self, messages=None):
        """
        Sends a message with custom logic.
        :param messages: Only submitted if it is a django default call.
        """
        self.create_additional_emails(
            messages or self.get_messages(
                self.event_code, extra_context=self.extra_context)
        )
        self.create_ou_emails()
        self.job.send()

    send = send_custom


    @property
    def event_type(self):
        assert self.event_code and self.site
        try:
            commtype = CommunicationEventType.objects.get(
                site=self.site,
                code=self.event_code,
            )
        except CommunicationEventType.DoesNotExist:
            commtype = CommunicationEventType(
                code=self.event_code, site=self.site)
        return commtype

    @property
    def job(self):
        assert self.event_type
        if self._job is None:
            self._job = CommunicationJob(
                self,
                self.event_type,
                self.mail_connection,
                fail_silently=self.fail_silently,
                threaded=self.threaded,
            )
        return self._job

    def create_main_email(self, recipient_email, messages, *args, **kwargs):
        if recipient_email:
            self.job.set_main_email_task(
                Task(
                    self.site,
                    [recipient_email],
                    messages,
                    self.event_type,
                    *args,
                    **kwargs,
                )
            )

    def create_additional_emails(self, messages, *args, **kwargs):
        if self.event_type.id:
            recipients = set(self.event_type.email_recipients.values_list(
                'email_address', flat=True
            ))
            if recipients:
                self.job.add_email_task(
                    Task(
                        self.site,
                        recipients,
                        messages,
                        self.event_type,
                        *args, **kwargs
                    )
                )

        sftp_profile = self.event_type.sftp_profile
        if sftp_profile:
            self.job.add_sftp_task(SftpTask(sftp_profile, messages))

    def create_ou_emails(self):
        if not self.event_type.id:
            return

        for organization_unit in self.get_ous():
            context = self.get_base_context()
            recipients = organization_unit.get_email_recipients(
                order=context.get('order', None)
            )
            extra_context = self.get_ou_context(organization_unit)
            messages = self.get_messages(self.event_code, extra_context)

            if recipients:
                self.job.add_email_task(
                    Task(self.site, recipients, messages, self.event_type)
                )

    def get_ou_context(self, organization_unit):
        context = self.get_base_context()
        result_context = {
            'ou': organization_unit,
        }

        if 'order' in context:
            if organization_unit.product_classes.exists():
                order = context['order']
                product_classes = organization_unit.product_classes.all()

                result_context['product_classes'] = product_classes

                result_context['lines'] = order.lines.filter(
                    product__product_class__in=product_classes
                )

                result_context['line_prices'] = order.line_prices.filter(
                    line__product__product_class__in=product_classes
                )

        return result_context

    def get_ous(self):
        qs = self.event_type.managing_ous.all()
        query = Q()

        order = self.get_order()
        if order:  # filter for product_classes
            query |= Q(
                Q(product_classes__products__line__in=order.lines.all())
                | Q(product_classes=None)
            )

        user = self.get_user()
        if user:
            query |= Q(
                Q(customers__email__in=user.email)
                | Q(customers=None)
            )
        return qs.filter(query)

    def get_order(self):
        context = self.get_base_context()
        if 'order' in context:
            return context.get('order', None)

    def get_user(self):
        context = self.get_base_context()
        return getattr(context, 'user', None)
