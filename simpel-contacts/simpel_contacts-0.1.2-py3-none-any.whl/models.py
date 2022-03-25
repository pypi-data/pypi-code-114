from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from simpel_contacts.abstracts import AbstractAddress, AbstractContact, AbstractCountry


class Country(AbstractCountry):
    pass


class LinkedContact(AbstractContact):

    linked_object_type = models.ForeignKey(
        ContentType,
        related_name="linked_contacts",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Linked object type"),
    )
    linked_object_id = models.IntegerField(
        null=True,
        blank=True,
        help_text=_("Linked instance primary key."),
    )
    linked_object = GenericForeignKey(
        "linked_object_type",
        "linked_object_id",
    )


class LinkedAddress(AbstractAddress):

    phone = PhoneNumberField(
        _("Phone number"),
        blank=True,
        help_text=_("In case we need to call you about your transaction."),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("Note"),
        help_text=_("Tell us anything we should know."),
    )
    linked_object_type = models.ForeignKey(
        ContentType,
        related_name="linked_address",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Linked object type"),
    )
    linked_object_id = models.IntegerField(
        null=True,
        blank=True,
        help_text=_("Linked instance primary key."),
    )
    linked_object = GenericForeignKey(
        "linked_object_type",
        "linked_object_id",
    )
