from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from filer.fields.image import FilerImageField
from mptt.models import MPTTModel, TreeForeignKey
from polymorphic.models import PolymorphicModel
from simpel_numerators.models import NumeratorMixin, NumeratorReset
from simpel_utils.slug import unique_slugify
from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase

from .managers import ProductManager
from .mixins import SellableMixin, StockableMixin


class Unit(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    html = models.CharField(
        max_length=255,
        verbose_name=_("html"),
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=80,
    )

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")
        db_table = "simpel_product_unit"
        permissions = (
            ("import_unit", _("Can import Unit")),
            ("export_unit", _("Can export Unit")),
        )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class Category(MPTTModel):

    parent = TreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
        help_text=_(
            "Categories, unlike tags, can have a hierarchy. You might have a "
            "Jazz category, and under that have children categories for Bebop"
            " and Big Band. Totally optional."
        ),
    )
    name = models.CharField(
        max_length=80,
        unique=True,
        verbose_name=_("Category Name"),
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=80,
    )

    icon = "tag-outline"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "simpel_product_category"
        permissions = (
            ("import_category", _("Can import Category")),
            ("export_category", _("Can export Category")),
        )

    def __str__(self):
        return self.name

    @property
    def opts(self):
        return self.__class__._meta

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError("Parent category cannot be self.")
            if parent.parent and parent.parent == self:
                raise ValidationError("Cannot have circular Parents.")

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class Tag(TagBase):

    icon = "tag-outline"

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        db_table = "simpel_product_tag"

    @property
    def opts(self):
        return self._meta


class Group(models.Model):
    code = models.CharField(
        unique=True,
        default=None,
        max_length=3,
        verbose_name=_("Code"),
    )
    name = models.CharField(
        max_length=80,
        verbose_name=_("Name"),
    )
    icon = "tag-outline"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
        db_table = "simpel_product_group"

    def __str__(self):
        return self.name

    @property
    def opts(self):
        return self.__class__._meta

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    @classmethod
    def get_or_create(cls, code, name):
        obj, _ = cls.objects.get_or_create(code=code, defaults={"name": name})
        return obj


class Product(NumeratorMixin, PolymorphicModel):
    AVAILABLE, FROZEN, DEPRECATED = "Available", "Frozen", "Deprecated"
    STATUS = (
        (AVAILABLE, _("Available")),
        (FROZEN, _("Frozen")),
        (DEPRECATED, _("Deprecated")),
    )
    uid = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Unique ID"),
    )
    thumbnail = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="product_thumbnails",
    )
    parent = models.ForeignKey(
        "self",
        related_name="variants",
        verbose_name=_("parent"),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Only for variants"),
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=AVAILABLE,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        db_index=True,
    )
    alias_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Alias name"),
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=80,
        db_index=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=1000,
        verbose_name=_("Description"),
    )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name=_("Group"),
    )
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Category"),
    )
    tags = TaggableManager(
        through="TaggedProduct",
        blank=True,
        related_name="products",
        verbose_name=_("Tags"),
    )
    price = models.DecimalField(
        _("Price"),
        default=0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
    )
    unit = models.ForeignKey(
        Unit,
        null=True,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name=_("Unit"),
    )
    min_order = models.IntegerField(
        default=1,
        verbose_name=_("Min Order"),
        help_text=_("Minimum order quantity"),
    )
    max_order = models.IntegerField(
        default=999,
        verbose_name=_("Max Order"),
        help_text=_("Maximum order quantity"),
    )
    objects = ProductManager()

    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    effective_at = models.DateTimeField(
        default=timezone.now,
    )
    modified_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    is_partial = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Partial"),
        help_text=_("Can be included as bundled items."),
    )
    is_deliverable = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Deliverable"),
        help_text=_("Has deliverable documents."),
    )
    is_bundle = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Is Bundle"),
    )
    is_stockable = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        editable=False,
        verbose_name=_("Has stock"),
    )
    is_sellable = models.BooleanField(
        null=True,
        blank=True,
        default=True,
        verbose_name=_("Can be Sold"),
    )
    is_purchaseable = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Can be Purchased"),
    )

    allow_comments = models.BooleanField(
        default=True,
        help_text=_("Enable comments"),
    )

    icon = "package-variant-closed"
    doc_prefix = "PRD"
    has_parameters = False
    reset_mode = NumeratorReset.MONTHLY

    objects = ProductManager()

    class Meta:
        db_table = "simpel_product"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)
        index_together = ("name", "category")
        permissions = (
            ("export_product", "Can export Product"),
            ("import_product", "Can import Product"),
        )

    def format_inner_id(self):
        """Inner ID final format"""
        form = [self.get_doc_prefix(), self.format_date(form="%m%y"), self.format_number()]
        inner_id = "{}.{}.{}".format(*form)
        return setattr(self, self.inner_id_field, inner_id)

    @cached_property
    def base_opts(self):
        return Product._meta

    @cached_property
    def opts(self):
        try:
            return self.get_real_instance_class()._meta
        except Exception:
            return self.__class__._meta

    @cached_property
    def specific(self):
        try:
            instance = self.get_real_instance()
            return instance
        except Exception:
            return self

    @cached_property
    def variants_count(self):
        return self.specific.variants.count()

    @cached_property
    def total_price(self):
        return getattr(self.specific, "price", 0)

    @cached_property
    def estimation_price(self):
        """Return total + all recommended fees for this product"""
        return self.specific.total_price + self.total_recommended_items

    @cached_property
    def total_recommended_items(self):
        """Return total recommended fees for this product"""
        summary = sum([item.total for item in self.recommended_items.all()])
        return summary or 0

    def __str__(self):
        if self.parent is not None:
            return "%s - %s" % (self.parent.name, self.name)
        else:
            return self.name

    def get_variants(self):
        return self.specific.variants.all()

    def get_admin_url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        from .settings import products_settings

        return reverse(products_settings.PRODUCT_ABSOLUTE_URL_NAME, kwargs={"pk": self.pk})

    def natural_key(self):
        keys = (self.inner_id,)
        return keys

    def get_group(self):
        return None

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.modified_at = timezone.now()
        if not self.slug:
            unique_slugify(
                self.specific,
                self.specific.name,
                queryset=Product.objects.all(),
            )
        super().save(**kwargs)


class TaggedProduct(TaggedItemBase):
    class Meta:
        db_table = "simpel_product_tagged"
        verbose_name = _("Tagged Product")
        verbose_name_plural = _("Tagged Products")

    content_object = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="tagged_products",
        db_index=True,
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tagged_products",
        db_index=True,
    )

    def __str__(self):
        return str(self.tag)


class Specification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_index=True,
        related_name="specifications",
        verbose_name=_("Product"),
    )
    feature = models.CharField(
        max_length=255,
        verbose_name=_("Feature"),
    )
    description = models.TextField(
        _("Description"),
        null=True,
        blank=True,
        max_length=255,
    )
    value = models.CharField(
        _("Value"),
        max_length=255,
    )
    note = models.CharField(
        _("Note"),
        null=True,
        blank=True,
        max_length=255,
    )

    icon = "card-text-outline"

    class Meta:
        db_table = "simpel_product_specification"
        verbose_name = _("Specification")
        verbose_name_plural = _("Specifications")
        permissions = (
            ("export_specification", "Can export Specification"),
            ("import_specification", "Can import Specification"),
        )

    def __str__(self):
        return self.feature


class Inventory(SellableMixin, StockableMixin, Product):
    doc_prefix = "VEN"

    class Meta:
        db_table = "simpel_product_inventory"
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")
        permissions = (
            ("export_inventory", _("Can export Inventory")),
            ("import_inventory", _("Can import Inventory")),
        )

    def save(self, *args, **kwargs):
        self.is_stockable = True
        return super().save(*args, **kwargs)


class Asset(StockableMixin, Product):
    doc_prefix = "AST"

    class Meta:
        db_table = "simpel_product_asset"
        verbose_name = _("Asset")
        verbose_name_plural = _("Assets")
        permissions = (
            ("export_asset", _("Can export Asset")),
            ("import_asset", _("Can import Asset")),
        )

    def save(self, *args, **kwargs):
        self.is_stockable = True
        return super().save(*args, **kwargs)


class Fee(Product):

    doc_prefix = "FEE"

    class Meta:
        db_table = "simpel_product_fee"
        verbose_name = _("Fee")
        verbose_name_plural = _("Fees")
        permissions = (
            ("export_fee", _("Can export Fee")),
            ("import_fee", _("Can import Fee")),
        )

    def save(self, *args, **kwargs):
        self.is_partial = True
        self.is_deliverable = False
        self.is_stockable = False
        self.is_sellable = True
        self.is_purchaseable = False
        self.is_bundle = False
        self.group = Group.get_or_create("FEE", "Fee")
        return super().save(*args, **kwargs)


class Service(Product):

    doc_prefix = "SRV"

    class Meta:
        db_table = "simpel_product_service"
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        permissions = (
            ("export_service", "Can export Service"),
            ("import_service", "Can import Service"),
        )

    def save(self, *args, **kwargs):
        self.is_stockable = False
        return super().save(*args, **kwargs)


class Bundle(Product):

    doc_prefix = "BDL"

    class Meta:
        db_table = "simpel_product_bundle"
        verbose_name = _("Bundle")
        verbose_name_plural = _("Bundles")
        permissions = (
            ("export_bundle", _("Can export Bundle")),
            ("import_bundle", _("Can import Bundle")),
        )

    def save(self, *args, **kwargs):
        self.is_bundle = True
        return super().save(*args, **kwargs)

    @cached_property
    def total_bundle(self):
        return sum([item.total for item in self.bundle_items.all()])

    @cached_property
    def price(self):
        return 0

    @cached_property
    def total_price(self):
        bundle = 0
        original = getattr(self.specific, "price", 0)
        if self.specific.is_bundle:
            bundle = self.specific.total_bundle
        return original + bundle


class BundleItem(models.Model):
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    item = models.ForeignKey(
        Bundle,
        related_name="bundle_items",
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
    )
    product = models.ForeignKey(
        Product,
        limit_choices_to={"is_partial": True},
        related_name="bundled_with",
        on_delete=models.CASCADE,
        verbose_name=_("Item"),
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Min Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )
    required = models.BooleanField(
        default=False,
        help_text=_("Required bundled item."),
    )

    icon = "card-text-outline"

    class Meta:
        db_table = "simpel_product_bundle_item"
        unique_together = ("product", "item")
        verbose_name = _("Bundle Item")
        verbose_name_plural = _("Bundle Items")
        ordering = ("position",)
        permissions = (
            ("export_bundleitem", _("Can export Bundle Item")),
            ("import_bundleitem", _("Can import Bundle Item")),
        )

    @cached_property
    def price(self):
        return self.product.specific.price

    @cached_property
    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return "%s bundled with %s" % (self.product, self.item)


class RecommendedItem(models.Model):
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    item = models.ForeignKey(
        Product,
        related_name="recommended_items",
        on_delete=models.CASCADE,
        verbose_name=_("product"),
    )
    product = models.ForeignKey(
        Product,
        limit_choices_to={"is_partial": True},
        related_name="recommended_for",
        on_delete=models.CASCADE,
        verbose_name=_("Item"),
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
        help_text=_("Required recommended item."),
    )
    icon = "card-text-outline"

    class Meta:
        db_table = "simpel_product_recommended_item"
        unique_together = ("product", "item")
        verbose_name = _("Recommendation")
        verbose_name_plural = _("Recommendations")
        ordering = ("position",)
        permissions = (
            ("export_recommendeditem", _("Can export Recommended Item")),
            ("import_recommendeditem", _("Can import Recommended Item")),
        )

    @cached_property
    def price(self):
        return self.product.specific.price

    @cached_property
    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return "%s recommended for %s" % (self.product, self.item)
