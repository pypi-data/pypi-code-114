from django.contrib import admin, messages
from django.utils.text import Truncator
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin

from simpel.simpel_admin.base import AdminFormView, AdminView, ModelAdminMixin
from simpel.simpel_auth.admin import LinkedAddressInline, LinkedContactInline
from simpel.simpel_partners.forms import PartnerForm
from simpel.simpel_partners.resources import PartnerResource

from .models import Partner


class AdminCustomerView(AdminView):
    pass


class AdminCustomerUpdateView(AdminFormView):
    pass


class AdminCustomerRegistrationView(AdminFormView):
    form_class = PartnerForm
    template_name = "admin/simpel_partners/partner_inspect.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"opts": Partner._meta})
        return context


@admin.register(Partner)
class PartnerAdmin(ImportExportMixin, ModelAdminMixin):
    resource_class = PartnerResource
    list_display = ["inner_id", "partner_name", "user", "is_active", "balance", "object_buttons"]
    search_fields = ["inner_id", "name"]
    date_hierarchy = "created_at"
    list_filter = ["partner_type", "is_active", "is_verified", "is_customer", "is_supplier"]
    inlines = [LinkedContactInline, LinkedAddressInline]
    actions = [
        "activate_partner",
        "verify_partner",
        "deactivate_partner",
        "deverify_partner",
    ]

    def has_view_permission(self, request, obj=None):
        return True

    def has_activate_permission(self, request, obj=None):
        return True

    def has_verify_permission(self, request, obj=None):
        return True

    def partner_name(self, obj):
        return Truncator(str(obj)).chars(60)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perms("change_partner_user"):
            return ["user"]
        return super().get_readonly_fields(request, obj)

    @admin.action(permissions=["activate"], description=_("Activate Partner"))
    def activate_partner(self, request, queryset):
        try:
            queryset.update(is_active=True)
            count = queryset.count()
            if count > 1:
                msg = _("Activate %s") % queryset.first()
            else:
                msg = _("Activate %s partners") % count
            messages.success(request, msg)
        except Exception as err:
            messages.error(request, err)

    @admin.action(permissions=["activate"], description=_("Deactivate Partner"))
    def deactivate_partner(self, request, queryset):
        try:
            queryset.update(is_active=False)
            count = queryset.count()
            if count > 1:
                msg = _("Deactivate %s") % queryset.first()
            else:
                msg = _("Deactivate %s partners") % count
            messages.success(request, msg)
        except Exception as err:
            messages.error(request, err)

    @admin.action(permissions=["verify"], description=_("Verify Partner"))
    def verify_partner(self, request, queryset):
        try:
            queryset.update(is_verified=True)
            count = queryset.count()
            if count > 1:
                msg = _("Verify %s") % queryset.first()
            else:
                msg = _("Verify %s partners") % count
            messages.success(request, msg)
        except Exception as err:
            messages.error(request, err)

    @admin.action(permissions=["verify"], description=_("Deverify Partner"))
    def deverify_partner(self, request, queryset):
        try:
            queryset.update(is_verified=False)
            count = queryset.count()
            if count > 1:
                msg = _("Deverify %s") % queryset.first()
            else:
                msg = _("Deverify %s partners") % count
            messages.success(request, msg)
        except Exception as err:
            messages.error(request, err)
