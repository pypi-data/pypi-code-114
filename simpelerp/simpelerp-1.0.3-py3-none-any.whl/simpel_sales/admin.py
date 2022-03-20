from django.contrib import admin, messages
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.contrib.admin.widgets import AdminTextareaWidget
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

import nested_admin
from import_export.admin import ExportMixin

from simpel.simpel_admin.base import AdminPrintViewMixin, ModelAdminMixin
from simpel.simpel_auth.admin import NestedLinkedAddressInline
from simpel.simpel_auth.admin.mixins import AdminActivityMixin
from simpel.simpel_auth.models import Activity
from simpel.simpel_sales.resources import SalesOrderResource, SalesQuotationResource

from .helpers import clone_salesorder, clone_salesquotation, convert_salesquotation
from .models import (
    ProformaInvoice, SalesOrder, SalesOrderItem, SalesOrderItemBundle, SalesQuotation, SalesQuotationItem,
    SalesQuotationItemBundle, SalesSetting,
)
from .settings import simpel_sales_settings as sales_settings


class SalesQuotationItemBundleInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = SalesQuotationItemBundle
    extra = 0
    autocomplete_fields = ["product"]

    def has_change_permission(self, request, obj=None):
        return False


class SalesQuotationItemInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedStackedInline,
):
    model = SalesQuotationItem
    widgets = {"note": AdminTextareaWidget(attrs={"cols": 3})}
    inlines = [SalesQuotationItemBundleInline, NestedLinkedAddressInline]
    extra = 0
    autocomplete_fields = ["product"]


class SalesQuotationAdmin(
    ExportMixin,
    AdminPrintViewMixin,
    AdminActivityMixin,
    ModelAdminMixin,
    nested_admin.NestedModelAdmin,
):
    form = sales_settings.SALESQUOTATION_FORM
    resource_class = SalesQuotationResource
    inlines = [NestedLinkedAddressInline, SalesQuotationItemInline]
    list_filter = ["group", "status"]
    # autocomplete_fields = ["customer"]
    search_fields = ["inner_id", "name"]
    date_hierarchy = "created_at"
    list_display_links = None
    list_display = ["object_detail", "status", "object_buttons"]
    actions = ["validate_action"]

    @admin.display(description=_("Detail"))
    def object_detail(self, obj):
        context = {"object": obj}
        template = "admin/simpel_sales/order_line.html"
        return render_to_string(template, context=context)

    def get_inlines(self, request, obj=None):
        return super().get_inlines(request, obj)

    def has_change_permission(self, request, obj=None):
        default = super().has_change_permission(request, obj)
        if obj:
            return obj.is_editable and default
        else:
            return default

    def has_clone_permission(self, request, obj=None):
        default = super().has_add_permission(request)
        if obj:
            return obj.validate_ignore_condition and default
        else:
            return default

    def has_convert_permission(self, request, obj=None):
        default = request.user.has_perm("simpel_sales.add_salesorder")
        if obj:
            return obj.validate_ignore_condition and default
        else:
            return default

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context)

    def clone_view(self, request, pk, extra_context=None):
        obj = self.get_object(request, pk)

        if not obj.validate_ignore_condition:
            messages.error(request, _("Make sure Sales Quotation status is valid!"))
            return redirect(self.get_inspect_url(obj.id))

        if not self.has_clone_permission(request, obj):
            messages.error(request, _("You don't have permission to clone this quotation!"))
            return redirect(self.get_inspect_url(obj.id))

        if request.method == "POST":
            try:
                cloned = clone_salesquotation(request, obj)
                msg = _("%s cloned to %s.") % (obj, cloned)
                messages.success(request, msg)
                self.log_addition(request, cloned, msg)
                self.log_activity(request, obj, flag=Activity.CLONE, message=msg)
                return redirect(self.get_inspect_url(cloned.id))
            except PermissionError as err:
                messages.error(request, err)
            return redirect(self.get_inspect_url(obj.id))
        else:
            context = {
                "title": _("Confirm clone %s %s.") % (self.opts.verbose_name, obj),
                "object": obj,
                "cancel_url": self.get_inspect_url(obj.id),
            }
            return self.confirmation_view(request, extra_context=context)

    def convert_view(self, request, pk, extra_context=None):
        obj = self.get_object(request, pk)

        if not obj.validate_ignore_condition:
            messages.error(request, _("Make sure Sales Quotation status is valid!"))
            return redirect(self.get_inspect_url(obj.id))

        if not self.has_convert_permission(request, obj):
            messages.error(request, _("You don't have permission to convert this quotation!"))
            return redirect(self.get_inspect_url(obj.id))

        if request.method == "POST":
            try:
                salesorder = convert_salesquotation(request, obj)
                msg = _("%s convert to %s.") % (obj, salesorder)
                messages.success(request, msg)
                self.log_activity(request, salesorder, flag=Activity.CREATION, message=_("Created %s") % salesorder)
                self.log_activity(request, obj, flag=Activity.CONVERTION, message=msg)
                return redirect(reverse(admin_urlname(SalesOrder._meta, "inspect"), args=(salesorder.id,)))
            except Exception as err:
                messages.error(request, err)
            return redirect(self.get_inspect_url(obj.id))
        else:
            context = {
                "title": _("Confirm clone %s %s.") % (self.opts.verbose_name, obj),
                "object": obj,
                "cancel_url": self.get_inspect_url(obj.id),
            }
            return self.confirmation_view(request, extra_context=context)

    def get_print_template(self):
        custom_settings = SalesSetting.for_request(self.request)
        template_item = custom_settings.salesquotation_template
        if template_item is not None:
            return template_item.get_template()
        else:
            return super().get_print_template()

    def get_urls(self):
        urls = [
            path(
                "<int:pk>/clone/",
                self.admin_site.admin_view(self.clone_view),
                name="%s_%s_clone" % (self.opts.app_label, self.opts.model_name),
            ),
            path(
                "<int:pk>/convert/",
                self.admin_site.admin_view(self.convert_view),
                name="%s_%s_convert" % (self.opts.app_label, self.opts.model_name),
            ),
        ] + super().get_urls()
        return urls


class SalesOrderItemBundleInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = SalesOrderItemBundle
    extra = 0
    autocomplete_fields = ["product"]
    readonly_fields = ["price", "total"]


class SalesOrderItemInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedStackedInline,
):
    model = SalesOrderItem
    inlines = [NestedLinkedAddressInline, SalesOrderItemBundleInline]
    extra = 0
    autocomplete_fields = ["product"]
    readonly_fields = ["price", "total"]


class SalesOrderAdmin(
    ExportMixin,
    AdminPrintViewMixin,
    AdminActivityMixin,
    ModelAdminMixin,
    nested_admin.NestedModelAdmin,
):
    form = sales_settings.SALESORDER_FORM
    resource_class = SalesOrderResource
    inlines = [NestedLinkedAddressInline, SalesOrderItemInline]
    # autocomplete_fields = ["customer"]
    date_hierarchy = "created_at"
    search_fields = ["inner_id", "customer__name"]
    list_filter = ["group", "status"]
    list_display_links = None
    list_display = ["object_detail", "status", "group", "object_buttons"]
    actions = [
        "compute_action",
        "validate_action",
        "cancel_action",
        "process_action",
        "complete_action",
        "close_action",
    ]

    @admin.display(description=_("Detail"))
    def object_detail(self, obj):
        context = {"object": obj}
        template = "admin/simpel_sales/order_line.html"
        return render_to_string(template, context=context)

    @admin.action(description=_("Recalculate selected Sales Order"))
    def compute_action(self, request, queryset):
        for obj in queryset:
            obj.save()

    def get_form(self, request, obj=None, change=False, **kwargs):
        return super().get_form(request, obj, change, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            if request.user.is_superuser:
                self.readonly_fields = []
            else:
                self.readonly_fields = ["status", "group"]
        else:
            self.readonly_fields = ["status"]
        return super().get_readonly_fields(request, obj)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user")

    def has_print_permission(self, request, obj=None):
        return obj.is_printable

    def get_print_template(self):
        custom_settings = SalesSetting.for_request(self.request)
        template_item = custom_settings.salesorder_template
        if template_item is not None:
            return template_item.get_template()
        else:
            return super().get_print_template()

    def has_change_permission(self, request, obj=None):
        default = super().has_change_permission(request, obj)
        if obj:
            return obj.is_editable and default
        else:
            return default

    def has_create_workorder_permission(self, request, obj):
        default = request.user.has_perm("simpel_projects.add_workorder")
        if obj:
            return obj.is_valid and not obj.has_workorder
        else:
            return default

    def has_create_invoice_permission(self, request, obj=None):
        default = request.user.has_perm("simpel_invoices.add_invoice")
        if obj:
            return (obj.is_processed or obj.is_complete) and not obj.is_invoiced and default
        else:
            return default

    def inspect_view(self, request, pk, **kwargs):
        obj = self.get_object(request, pk)
        kwargs.update(
            {
                "has_create_invoice_permission": self.has_create_invoice_permission(request, obj),
                "has_create_workorder_permission": self.has_create_workorder_permission(request, obj),
                "has_print_permission": self.has_print_permission(request, obj),
            }
        )
        return super().inspect_view(request, pk, **kwargs)

    def clone_view(self, request, pk, extra_context=None):
        obj = self.get_object(request, pk)
        if request.method == "POST":
            try:
                cloned = clone_salesorder(request, obj)
                msg = _("%s cloned to %s.") % (obj, cloned)
                messages.success(request, msg)
                self.log_activity(request, cloned, flag=Activity.CREATION, message=_("Created %s") % cloned)
                self.log_activity(request, obj, flag=Activity.CLONE, message=msg)
                return redirect(reverse(admin_urlname(SalesOrder._meta, "inspect"), args=(cloned.id,)))
            except Exception as err:
                messages.error(request, err)
            return redirect(self.get_inspect_url(obj.id))
        else:
            context = {
                "title": _("Confirm clone %s %s.") % (self.opts.verbose_name, obj),
                "object": obj,
                "cancel_url": self.get_inspect_url(obj.id),
            }
            return self.confirmation_view(request, extra_context=context)

    def create_invoice_view(self, request, pk):
        obj = self.get_object(request, pk)

        if not self.has_create_invoice_permission(request, obj):
            messages.error(request, _("Make sure Sales Order status is complete or processed!"))
            return redirect(self.get_inspect_url(obj.id))

        if obj.is_invoiced:
            messages.error(request, _("Invoice for %s has been created!") % obj)
            return redirect(self.get_inspect_url(obj.id))

        if request.method == "POST":
            try:
                from simpel.simpel_invoices.helpers import create_invoice

                invoice = create_invoice(request, obj)
                msg = _("Create invoice %s for order %s.") % (invoice, obj)
                messages.success(request, msg)
                self.log_activity(request, invoice, flag=Activity.CREATION, message=_("Create invoice for %s") % obj)
                self.log_activity(request, obj, flag=Activity.CONVERTION, message=msg)
                return redirect(reverse(admin_urlname(invoice._meta, "inspect"), args=(invoice.id,)))
            except Exception as err:
                messages.error(request, err)
            return redirect(self.get_inspect_url(obj.id))
        else:
            context = {
                "title": _("Create invoice for %s %s.") % (self.opts.verbose_name, obj),
                "object": obj,
                "cancel_url": self.get_inspect_url(obj.id),
            }
            return self.confirmation_view(request, extra_context=context)

    def create_workorder_view(self, request, pk):
        obj = self.get_object(request, pk)
        if not obj.is_valid:
            messages.error(request, _("Make sure Sales Order status is valid!"))
            return redirect(self.get_inspect_url(obj.id))
        if request.method == "POST":
            try:
                from simpel.simpel_projects.helpers import convert_salesorder

                workorder = convert_salesorder(request, obj)
                msg = _("Create workorder %s for order %s.") % (workorder, obj)
                messages.success(request, msg)
                self.log_activity(
                    request, workorder, flag=Activity.CREATION, message=_("Create workorder for %s") % obj
                )
                self.log_activity(request, obj, flag=Activity.CONVERTION, message=msg)
                return redirect(reverse(admin_urlname(workorder._meta, "inspect"), args=(workorder.id,)))
            except Exception as err:
                messages.error(request, err)
                return redirect(self.get_inspect_url(obj.id))
        else:
            context = {
                "title": _("Create Work Order for %s %s.") % (self.opts.verbose_name, obj),
                "object": obj,
                "cancel_url": self.get_inspect_url(obj.id),
            }
            return self.confirmation_view(request, extra_context=context)

    def get_urls(self):
        urls = [
            path(
                "<int:pk>/clone/",
                self.admin_site.admin_view(self.clone_view),
                name="%s_%s_clone" % (self.opts.app_label, self.opts.model_name),
            ),
            path(
                "<int:pk>/create_invoice/",
                self.admin_site.admin_view(self.create_invoice_view),
                name="%s_%s_create_invoice" % (self.opts.app_label, self.opts.model_name),
            ),
            path(
                "<int:pk>/create_workorder/",
                self.admin_site.admin_view(self.create_workorder_view),
                name="%s_%s_create_workorder" % (self.opts.app_label, self.opts.model_name),
            ),
        ] + super().get_urls()
        return urls


# @admin.register(SalesOrderItem)
class SalesOrderItemAdmin(admin.ModelAdmin):
    inlines = [SalesOrderItemBundleInline]
    search_fields = ["inner_id", "salesorder__inner_id"]
    list_display = [
        "inner_id",
        "salesorder",
        "product",
        "quantity",
    ]


class ProformaInvoiceAdmin(AdminPrintViewMixin, ModelAdminMixin):
    date_hierarchy = "created_at"
    list_display = ["inner_id", "salesorder", "col_group", "created_at"]
    list_filter = ["salesorder__group"]

    @admin.display(description=_("Group"))
    def col_group(self, obj):
        return obj.salesorder.group


admin.site.register(SalesOrder, sales_settings.SALESORDER_ADMIN)
admin.site.register(SalesQuotation, sales_settings.SALESQUOTATION_ADMIN)
admin.site.register(ProformaInvoice, sales_settings.PROFORMA_INVOICE_ADMIN)
