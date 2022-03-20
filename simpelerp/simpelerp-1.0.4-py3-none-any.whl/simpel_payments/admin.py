from django.contrib import admin
from django.template.loader import render_to_string

from import_export.admin import ImportExportMixin
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from simpel.simpel_admin.base import AdminPrintViewMixin, ModelAdminMixin
from simpel.simpel_auth.admin import AdminActivityMixin
from simpel.simpel_payments.resources import PaymentResource

from .models import CashGateway, ManualTransferGateway, Payment, PaymentGateway


@admin.register(PaymentGateway)
class PaymentGatewayAdmin(PolymorphicParentModelAdmin):
    menu_icon = "clipboard-list"
    search_fields = ["name"]
    list_display = ["name", "rate_method", "transfer_fee"]
    child_models = [
        CashGateway,
        ManualTransferGateway,
    ]


@admin.register(ManualTransferGateway)
class ManualTransferGatewayAdmin(PolymorphicChildModelAdmin):
    pass


@admin.register(CashGateway)
class CashPaymentGatewayAdmin(PolymorphicChildModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(
    ImportExportMixin,
    AdminActivityMixin,
    AdminPrintViewMixin,
    ModelAdminMixin,
):
    menu_icon = "clipboard-list"
    readonly_fields = ["user"]
    search_fields = ["inner_id", "source"]
    date_hierarchy = "created_at"
    list_display = ["inner_id", "col_detail", "status", "object_buttons"]
    list_filter = ["created_at", "status"]
    actions = [
        "validate_action",
        "reject_action",
        "approve_action",
        "cancel_action",
    ]
    resource_class = PaymentResource
    autocomplete_fields = ["gateway"]
    inspect_template = "admin/simpel_payments/payment_inspect.html"

    def col_detail(self, obj):
        context = {"object": obj}
        return render_to_string("admin/simpel_payments/payment_line.html", context=context)

    def has_change_permission(self, request, obj=None):
        default = super().has_change_permission(request, obj)
        if obj:
            return obj.is_editable and default
        return default

    def has_cancel_permission(self, request, obj=None):
        default = super().has_cancel_permission(request, obj)
        if obj:
            return obj.is_cancelable and default
        return default

    def has_approve_permission(self, request, obj=None):
        default = super().has_approve_permission(request, obj)
        if obj:
            return default
        return default

    def has_reject_permission(self, request, obj=None):
        default = super().has_reject_permission(request, obj)
        if obj:
            return default
        return default

    def has_delete_permission(self, request, obj=None):
        default = super().has_delete_permission(request, obj)
        if obj:
            return default
        return default

    def save_model(self, request, obj, form, change):
        if obj.user is None:
            obj.user = request.user
        return super().save_model(request, obj, form, change)
