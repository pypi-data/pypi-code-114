from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from simpel.simpel_auth.models import LinkedAddress, LinkedContact
from simpel.simpel_products.models import Product

from .managers import BlueprintManager


class Blueprint(models.Model):

    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name="bluprints",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    product = models.ForeignKey(
        Product,
        related_name="blueprints",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    note = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )
    public = models.BooleanField(
        default=False,
        help_text=_("Make this blueprint public, everyone can copy an see this blueprint."),
    )

    addresses = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    contacts = GenericRelation(
        LinkedContact,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    objects = BlueprintManager()
    icon = "text-box-outline"

    class Meta:
        db_table = "simpel_blueprint"
        index_together = ("user", "product")
        verbose_name = _("Blueprints")
        verbose_name_plural = _("Blueprints")
        ordering = ("-created_at",)

    def __str__(self):
        return "%s" % (self.product)

    @cached_property
    def price(self):
        return self.get_price()

    @cached_property
    def subtotal(self):
        return self.get_subtotal()

    @cached_property
    def total(self):
        return self.get_total()

    def get_price(self):
        return self.product.total_price

    def get_total_bundles(self):
        return sum([item.total for item in self.bundles.all()])

    def get_subtotal(self):
        return self.get_price() + self.get_total_bundles()

    def get_total(self):
        return self.get_subtotal()


class BlueprintBundle(models.Model):
    # Reference & Meta Fields

    blueprint = models.ForeignKey(
        Blueprint,
        related_name="bundles",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="blueprint_bundles",
        null=False,
        blank=False,
        limit_choices_to={"is_partial": True},
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )

    class Meta:
        db_table = "simpel_blueprint_item_bundle"
        index_together = ("blueprint", "product")
        unique_together = ("blueprint", "product")
        verbose_name = _("Blueprint Bundle")
        verbose_name_plural = _("Blueprint Bundles")

    @cached_property
    def price(self):
        return self.get_price()

    @cached_property
    def total(self):
        return self.get_total()

    def get_price(self):
        return self.product.total_price

    def get_total(self):
        return self.get_price() * self.quantity
