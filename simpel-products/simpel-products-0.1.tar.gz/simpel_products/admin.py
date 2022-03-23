from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.contrib.auth import get_permission_codename
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportMixin
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin
from simpel_admin.base import AdminReadOnlyMixin, ModelAdminMixin
from simpel_utils.currency import currency

from .helpers import get_product_models
from .models import (  # NOQA
    Asset, Bundle, BundleItem, Category, Fee, Group, Inventory, Product, RecommendedItem, Service, Specification, Unit,
)
from .resources import (
    BundleItemResource, BundleResource, CategoryResource, FeeResource, ProductResource, RecommendedItemResource,
    ServiceResource, SpecificationResource, UnitResource,
)
from .settings import products_settings  # NOQA

CartItem = products_settings.CARTITEM_MODEL


@admin.register(Category)
class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    menu_icon = "tag"
    inspect_enabled = False
    list_display = ["name", "slug", "parent"]
    search_fields = ["name", "slug"]
    list_select_related = ["parent"]
    resource_class = CategoryResource


@admin.register(Group)
class GroupAdmin(ImportExportMixin, admin.ModelAdmin):
    menu_icon = "tag"
    inspect_enabled = False
    list_display = ["name", "id"]


@admin.register(Unit)
class UnitAdmin(ImportExportMixin, admin.ModelAdmin):
    menu_icon = "tag"
    inspect_enabled = False
    search_fields = ["name"]
    list_display = ["name", "slug", "html"]
    resource_class = UnitResource


@admin.register(Specification)
class SpecificationAdmin(ImportExportMixin, AdminReadOnlyMixin, ModelAdminMixin):
    list_display = ["product", "feature", "value"]
    resource_class = SpecificationResource


@admin.register(RecommendedItem)
class RecommendedItemAdmin(ImportExportMixin, ModelAdminMixin):
    list_display = ["product", "item", "quantity", "price"]
    resource_class = RecommendedItemResource


class SpecificationInline(admin.StackedInline):
    extra = 0
    model = Specification


class BaseProductAdmin(ModelAdminMixin):
    menu_icon = "package"
    list_per_page = 30
    list_filter = ["group", "category", "is_partial", "status"]
    search_fields = ["name", "inner_id"]
    date_hierarchy = "created_at"
    raw_id_fields = ["parent", "category", "unit"]
    list_display = [
        "inner_id",
        "object_detail",
        # "col_name",
        # "status",
        "col_partial",
        "col_bundle",
        "col_deliverable",
        # "col_estimation",
        "object_buttons",
    ]
    fields = [
        "thumbnail",
        "parent",
        "name",
        "alias_name",
        "description",
        "group",
        "category",
        "tags",
        "unit",
        "min_order",
        "max_order",
        "status",
        "is_sellable",
        "is_purchaseable",
        # "is_partial",
        # "is_bundle",
        # "is_deliverable",
    ]
    inlines = [SpecificationInline]
    inspect_template = "admin/simpel_products/product_inspect.html"

    @admin.display(description=_("Detail"))
    def object_detail(self, obj):
        context = {"object": obj}
        template = "admin/simpel_products/product_line.html"
        return render_to_string(template, context=context)

    @admin.display(description=_("Name"))
    def col_name(self, obj):
        return Truncator(obj.name).chars(45)

    @admin.display(description=mark_safe("<div class='text-end'>%s<div>" % _("Price")))
    def col_price(self, obj):
        return mark_safe("<div class='text-end'>%s<div>" % currency(obj.specific.estimation_price))

    @admin.display(description=mark_safe("<div class='text-end'>%s<div>" % _("Estimation")))
    def col_estimation(self, obj):
        return mark_safe("<div class='text-end'>%s<div>" % currency(obj.specific.estimation_price))

    @admin.display(
        boolean=True,
        ordering="is_deliverable",
        description=mark_safe(
            """<span class='d-inline-block p-0'
                     data-bs-toggle='popover'
                     data-bs-trigger='hover'
                     data-bs-placement='top'
                     data-bs-content='Has deliverable.'
                >DV</span>
            """
        ),
    )
    def col_deliverable(self, obj):
        return obj.is_deliverable

    @admin.display(
        boolean=True,
        ordering="is_partial",
        description=mark_safe(
            """<span class='d-inline-block p-0'
                     data-bs-toggle='popover'
                     data-bs-trigger='hover'
                     data-bs-placement='top'
                     data-bs-content='Is partial.'
                >PT</span>
            """
        ),
    )
    def col_partial(self, obj):
        return obj.is_partial

    @admin.display(
        boolean=True,
        ordering="is_bundle",
        description=mark_safe(
            """<span class='d-inline-block p-0'
                     data-bs-toggle='popover'
                     data-bs-trigger='hover'
                     data-bs-placement='top'
                     data-bs-content='Is Bundle.'
                >BD</span>
            """
        ),
    )
    def col_bundle(self, obj):
        return obj.is_bundle

    def get_queryset(self, request=None):
        qs = super().get_queryset(request)
        return qs

    def get_object_buttons_childs(self, request, obj):
        childs = super().get_object_buttons_childs(request, obj)
        if CartItem is not None and obj.specific.parent is None:
            cart_add_item_url = reverse(
                admin_urlname(CartItem._meta, "add_item"),
                args=(obj.id,),
            )
            childs.append(
                {
                    "url": cart_add_item_url,
                    "label": _("Add to Cart"),
                }
            )
        return childs

    def get_changelist(self, request, **kwargs):
        """
        Return the Product ChangeList class for use on the changelist where products filtered with
        parent=None == None.
        """
        from django.contrib.admin.views.main import ChangeList as ChangeListClass

        class ChangeList(ChangeListClass):
            def get_queryset(self, request):
                qs = super().get_queryset(request)
                return qs.filter(parent=None)

        return ChangeList


class ProductAdmin(BaseProductAdmin):
    fields = BaseProductAdmin.fields + [
        "price"
    ]


class ProductParentAdmin(PolymorphicParentModelAdmin, BaseProductAdmin):
    """Parent admin Product Model, set child model in settings"""

    child_models = []
    resource_class = ProductResource
    change_list_template = "admin/simpel_products/changelist_parent.html"

    @admin.display(
        boolean=True,
        ordering="is_bundle",
        description=mark_safe("<div class='text-end'>%s<div>" % _("Display Price")),
    )
    def display_price(self, obj):
        return mark_safe("<div class='text-end'>%s<div>" % currency(obj.specific.estimation_price))

    def get_queryset(self, request=None):
        qs = super().get_queryset(request)
        return qs

    def get_child_models(self):
        """
        Register child model using defaults from settings
        """
        return get_product_models()

    def inspect_view(self, request, pk, *args, **kwargs):
        kwargs["base_opts"] = self.opts
        kwargs["cart_item_opts"] = getattr(CartItem, "_meta", None)
        return super().inspect_view(request, pk, *args, **kwargs)


class ProductChildAdmin(ImportExportMixin, PolymorphicChildModelAdmin, BaseProductAdmin):
    base_model = Product
    show_in_index = True
    raw_id_fields = ["parent"]
    change_list_template = "admin/simpel_products/changelist_child.html"

    def has_view_permission(self, request, obj=None):
        opts = self.base_model._meta
        codename = get_permission_codename("view", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def changelist_view(self, request, extra_context=None):
        extra_context = {"base_opts": self.base_model._meta}
        return super().changelist_view(request, extra_context)

    def inspect_view(self, request, pk, *args, **kwargs):
        kwargs["base_opts"] = self.base_model._meta
        kwargs["cart_item_opts"] = getattr(CartItem, "_meta", None)
        return super().inspect_view(request, pk, *args, **kwargs)


class ServiceAdmin(ProductChildAdmin):
    resource_class = ServiceResource
    fields = ProductChildAdmin.fields + ["price"]


class FeeAdmin(ProductChildAdmin):
    resource_class = FeeResource
    inlines = []
    fields = fields = [
        "parent",
        "name",
        "description",
        "group",
        "category",
        "unit",
        "min_order",
        "max_order",
        "status",
        "price",
    ]


class AssetAdmin(ProductChildAdmin):
    fields = [
        "parent",
        "is_partial",
        "sn",
        "name",
        "alias_name",
        "description",
        "group",
        "category",
        "tags",
        "unit",
        "price",
        "min_stock",
        "max_stock",
        "min_order",
        "max_order",
        "status",
    ]


class InventoryAdmin(ProductChildAdmin):
    fields = [
        "parent",
        "is_partial",
        "sn",
        "name",
        "alias_name",
        "description",
        "group",
        "category",
        "tags",
        "unit",
        "price",
        "min_stock",
        "max_stock",
        "min_order",
        "max_order",
        "status",
    ]


class BundleItemInline(admin.TabularInline):
    extra = 0
    model = BundleItem
    fk_name = "item"
    autocomplete_fields = ["product"]


class RecommendedItemInline(admin.TabularInline):
    extra = 0
    model = RecommendedItem
    fk_name = "item"
    autocomplete_fields = ["product"]


class BundleItemAdmin(ImportExportMixin, AdminReadOnlyMixin, ModelAdminMixin):
    list_display = ["product", "item", "quantity"]
    resource_class = BundleItemResource


class BundleAdmin(ProductChildAdmin):
    resource_class = BundleResource
    fields = ProductChildAdmin.fields
    inlines = ProductChildAdmin.inlines + [BundleItemInline, RecommendedItemInline]


admin_map = {
    Fee: FeeAdmin,
    Asset: AssetAdmin,
    Inventory: InventoryAdmin,
    Bundle: BundleAdmin,
    Service: ServiceAdmin,
}

if products_settings.PRODUCT_ADMIN is None:
    if not products_settings.PRODUCT_TYPES:
        admin.site.register(Product, ProductAdmin)
    else:
        admin.site.register(Product, ProductParentAdmin)
        for product in products_settings.PRODUCT_TYPES:
            admin.site.register(product, admin_map[product])
else:
    admin.site.register(Product, products_settings.PRODUCT_ADMIN)
