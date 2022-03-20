from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from simpel.simpel_auth.models import LinkedAddress
from simpel.simpel_products.models import Product

from .managers import CartManager


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        db_index=True,
        on_delete=models.CASCADE,
    )
    objects = CartManager()

    class Meta:
        db_table = "simpel_shop"
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    @classmethod
    def get_for_user(cls, user):
        cart = getattr(user, "cart", None)
        if cart is None:
            cart, _ = cls.objects.get_or_create(user=user)
        return cart

    @cached_property
    def items_count(self):
        return self.items.count()

    @cached_property
    def total_order(self):
        return self.get_total_order()

    def get_total_order(self):
        return sum([item.total for item in self.items.all()])

    def admin_add_item(self, product, quantity=1):
        item = CartItem(cart=self, product=product, quantity=quantity)
        item.save()
        return item

    def __str__(self):
        return "%s Cart" % self.user


class CartItem(models.Model):
    # Reference & Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    cart = models.ForeignKey(
        Cart,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="cart_items",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )
    note = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )

    deliverable_informations = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    icon = "cart-outline"

    class Meta:
        db_table = "simpel_shop_item"
        index_together = ("cart", "product")
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
        ordering = ("position",)

    def __str__(self):
        return "%s:%s - %s" % (self.product, self.quantity, self.product.total_price)

    @cached_property
    def user(self):
        return self.cart.user

    @cached_property
    def group(self):
        return self.product.group

    @cached_property
    def deliverable_information(self):
        return self.deliverable_informations.filter(address_type=LinkedAddress.DELIVERABLE).first()

    @cached_property
    def group_verbose(self):
        return self.group.name

    @cached_property
    def bundle(self):
        return self.bundles.count()

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
        # Get product bundled items if is bundle.
        product_bundles = 0
        if self.product.specific.is_bundle:
            product_bundles = sum([bundle.total for bundle in self.product.specific.bundle_items.all()])
        # get cart item bundles
        cart_bundles = sum([bundle.total for bundle in self.bundles.all()])
        return cart_bundles + product_bundles

    def get_subtotal(self):
        return self.get_price() + self.get_total_bundles()

    def get_total(self):
        return self.get_subtotal() * Decimal(self.quantity)


class CartItemBundle(models.Model):
    # Reference & Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    cart_item = models.ForeignKey(
        CartItem,
        related_name="bundles",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="cart_item_bundles",
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
    required = models.BooleanField(
        default=False,
        editable=False,
        help_text=_("Required bundled item."),
    )

    class Meta:
        db_table = "simpel_shop_item_bundle"
        unique_together = ("cart_item", "product")
        index_together = ("cart_item", "product")
        ordering = ("position",)
        verbose_name = _("Cart Item Bundle")
        verbose_name_plural = _("Cart Item Bundles")

    def __str__(self):
        return "%s:%s - %s" % (self.product.name, self.quantity, self.product.specific.price)

    @cached_property
    def user(self):
        return self.cart_item.user

    @cached_property
    def price(self):
        return self.get_price()

    @cached_property
    def total(self):
        return self.get_total()

    def get_price(self):
        return self.product.total_price

    def get_total(self):
        return self.get_price() * Decimal(self.quantity)
