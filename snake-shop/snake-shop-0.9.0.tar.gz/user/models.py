from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.contrib.auth import models as django_auth_models
from django.utils.functional import cached_property
from django.contrib.sites.models import Site
from django.conf import settings

from oscar.apps.customer.abstract_models import AbstractUser
from oscar.models.fields import AutoSlugField

from newsletter.models import Newsletter, Subscription
from delivery.models import Postcode
from config.settings import AUTH_USER_MODEL
from apps.partner.models import Partner
from apps.communication.models import CommunicationEventType


class Group(django_auth_models.Group):
    class Meta:
        proxy=True
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class OrganizationUnit(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=150,
    )
    code = AutoSlugField(
        _('Code'), max_length=128, unique=True, populate_from='name',
        separator='_', uppercase=True, editable=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z_][0-9A-Z_]*$',
                message=_(
                    "Code can only contain the uppercase letters (A-Z), "
                    "digits, and underscores, and can't start with a digit."))],
    )

    description = models.TextField(
        _('Description'),
        blank=True, null=True,
    )
    members = models.ManyToManyField(
        AUTH_USER_MODEL,
        verbose_name=_('Members'),
        help_text=_('Zuständiger Seitenbenutzer. Empfängt Nachrichten aus dem '
                    'Zuständigkeitsbereich dieser Organisationseinheit.'),
        blank=True,
        related_name='ous',
    )
    email_recipients = models.ManyToManyField(
        'communication.EmailRecipient',
        verbose_name=_('E-Mail recipients'),
        help_text=_('Empfängt Nachrichten aus dem Zuständigkeitsbereich dieser '
                    'Organisationseinheit.'),
        blank=True,
    )
    event_types = models.ManyToManyField(
        CommunicationEventType,
        verbose_name=_('Communication event types'),
        help_text=_('Kommunikationsvorgänge dieses Typs werden an die '
                    'Mitglieder und Empfänger dieser Organisationseinheit als '
                    'Kopie gesendet.'),
        blank=True,
        related_name='managing_ous',
    )
    customers = models.ManyToManyField(
        AUTH_USER_MODEL,
        verbose_name=_('Customers'),
        help_text=_('Kunden für die diese Organisationseinheit zuständig ist. '
                    'Kommunikationsvorgänge an diese Kunden werden an die '
                    'Empfänger dieser Organisationseinheit als Kopie gesendet.'
                    ),
        blank=True,
        related_name='managing_ous',
    )
    product_classes = models.ManyToManyField(
        'catalogue.ProductClass',
        verbose_name=_('Product classes'),
        help_text=_('Produktklassen für die diese Organisationseinheit '
                    'zuständig ist. Kommunikationsvorgänge, die Produkte dieses'
                    ' Typs enthalten, werden an die Empfänger dieser '
                    'Organisationseinheit als Kopie gesendet.'),
        blank=True,
        related_name='managing_ous',
    )

    def get_email_recipients(self, order=None):
        """
        :param order: Order object to look for matching product_classes
        """
        recipients = set()
        user = getattr(order, 'user', None)
        ou_customers = self.customers.all()

        if all((ou_customers, user)) and user not in ou_customers:
            return recipients

        recipients.update(
            self.members.values_list('email', flat=True)
        )
        recipients.update(
            self.email_recipients.values_list('email_address', flat=True)
        )
        return recipients

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Organization unit')
        verbose_name_plural = _('Organization units')
        ordering = ['name']


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        null=True,
        blank=True,
    )
    birth_date = models.DateField(_('birth date'), null=True, blank=True)

    old_newsletter_accepted = models.BooleanField(  # Remove
        _('Newsletter accepted'),
        help_text=_('User accepted to receive newsletter'),
        default=False
    )
    def partner(self):
        """ Deprecated, don't use anymore ! Just backwards compatibility """
        return self.partners.first() or Partner.default

    @property
    def is_system_admin(self):
        for admin in settings.ADMINS:
            if self.email == admin[1]:
                return True
        return False

    @property
    def newsletter_accepted(self):
        return self.subscription_set.filter(subscribed=True).exists()

    @newsletter_accepted.setter
    def newsletter_accepted(self, value):
        for subscription in self.subscription_set.all():
            action = 'subscribe' if value else 'unsubscribe'
            subscription.update(action)

    @cached_property
    def hide_price(self):
        return self.partners.filter(priceless_checkout=True).exists()

    @property
    def delivered_addresses(self):
        return self.addresses.filter(postcode__in=Postcode.get_all_postcodes())

    @property
    def id_str(self):
        return f"{self.id:06d}"

    def get_full_name(self):
        if self.first_name and self.last_name:
            return super().get_full_name()
        address = self.addresses.first()
        if address:
            return address.name
        return ''

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'


class AnonymousUser(django_auth_models.AnonymousUser):
    hide_price = False
    is_system_admin = False

    @property
    def partners(self):
        return Partner.objects.none()


@receiver(m2m_changed, sender=User.partners.through)
def users_single(sender, action, instance, pk_set, model, **kwargs):
    """
    A user can only be a member of one partner group.

    pre_add: delete partners for user
    post_remove: add default partner if len 0
    """
    for user in User.objects.filter(pk__in=pk_set):
        sender.objects.filter(user=user).exclude(partner=instance).delete()
        user.partners.remove(Partner.default)


def create_newsletter_subscription(user):
    instance = user
    if instance.subscription_set.count() <= 1:
        newsletter = Newsletter.objects.get_or_create(
            slug=getattr(instance.partners.first(), 'code', 'default'),
            defaults={
                'title': getattr(instance.partners.first(), 'name', 'default'),
            }
        )[0]
        newsletter.site.set(Site.objects.all())
        Subscription.objects.update_or_create(
            user=instance,
            defaults={
                'newsletter': newsletter,
                'subscribed': instance.newsletter_accepted,
            }
        )


@receiver(post_save, sender=User)
def user_newsletter_subscription(instance, **kwargs):
    create_newsletter_subscription(instance)


@receiver(m2m_changed, sender=User.partners.through)
def partner_newsletter_subscription(instance, **kwargs):
    if isinstance(instance, User):
        create_newsletter_subscription(instance)


django_auth_models.AnonymousUser = AnonymousUser


from oscar.apps.customer.models import *  # noqa isort:skip
