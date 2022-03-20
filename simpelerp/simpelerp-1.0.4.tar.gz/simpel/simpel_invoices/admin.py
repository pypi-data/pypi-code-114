from django.contrib import admin
from django.utils.translation import gettext_lazy as _

import nested_admin
from import_export.admin import ExportMixin

from simpel.simpel_admin.base import AdminPrintViewMixin, ModelAdminMixin
from simpel.simpel_auth.admin import AdminActivityMixin, NestedLinkedAddressInline
from simpel.simpel_invoices.models import Invoice, InvoiceItem, InvoiceItemBundle
from simpel.simpel_invoices.resources import InvoiceResource

from .forms import InvoiceAdminForm
from .settings import simpel_invoices_settings as invoices_settings


class InvoiceItemBundleInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = InvoiceItemBundle
    extra = 0
    autocomplete_fields = ["product"]


class InvoiceItemInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = InvoiceItem
    autocomplete_fields = ["product"]
    inlines = [InvoiceItemBundleInline]
    extra = 0


class InvoiceAdmin(
    ExportMixin,
    AdminPrintViewMixin,
    AdminActivityMixin,
    ModelAdminMixin,
    nested_admin.NestedModelAdmin,
):
    form = InvoiceAdminForm
    resource_class = InvoiceResource
    inlines = [NestedLinkedAddressInline, InvoiceItemInline]
    # autocomplete_fields = ["customer"]
    date_hierarchy = "created_at"
    search_fields = ["inner_id", "name"]
    list_display = [
        "inner_id",
        "customer",
        "total",
        "downpayment",
        "grand_total",
        "payable",
        "status",
        "col_is_closable",
        "object_buttons",
    ]
    actions = [
        "compute_action",
        "trash_action",
        "validate_action",
        "cancel_action",
        "close_action",
    ]

    @admin.display(description="Closable")
    def col_is_closable(self, obj):
        return obj.is_closable

    def has_change_permission(self, request, obj=None):
        default = super().has_change_permission(request, obj)
        if obj:
            return obj.is_editable and default
        return default

    def has_close_permission(self, request, obj=None):
        default = super().has_close_permission(request, obj)
        if obj:
            return obj.is_closable and default
        return default

    def has_delete_permission(self, request, obj=None):
        default = super().has_delete_permission(request, obj)
        if obj:
            return (obj.is_trash or obj.is_pending) and default
        return default

    def save_form(self, request, form, change=None):
        instance = form.save(commit=False)
        return instance

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ["group", "reference_type", "reference_id"]
        return super().get_readonly_fields(request, obj)

    @admin.action(description=_("Recalculate selected invoices"))
    def compute_action(self, request, queryset):
        for obj in queryset:
            obj.save()


admin.site.register(Invoice, invoices_settings.INVOICE_ADMIN)
