import nested_admin
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.contenttypes.admin import GenericStackedInline
from django.utils.translation import ugettext_lazy as _

from ..forms import ProfileInlineFormset
from ..models import LinkedAddress, LinkedContact, Notification, Profile
from ..utils import is_soft_delete, render_notice


class PublicPermission:
    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True


class LinkedAddressInline(PublicPermission, GenericStackedInline):
    model = LinkedAddress
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0


class NestedLinkedAddressInline(
    PublicPermission,
    nested_admin.NestedGenericStackedInline,
):
    model = LinkedAddress
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0


class LinkedContactInline(PublicPermission, GenericStackedInline):
    model = LinkedContact
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0


class NestedLinkedContactInline(
    PublicPermission,
    nested_admin.NestedGenericStackedInline,
):
    model = LinkedContact
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0


class SingleLinkedAddressInline(LinkedAddressInline):
    extra = 0
    max_num = 1


class ProfileInline(admin.StackedInline):
    model = Profile
    formset = ProfileInlineFormset


@admin.register(get_user_model())
class UserAdmin(UserAdminBase):
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Name"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
        (_("Important dates"), {"fields": ("date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    list_filter = ("is_staff", "is_superuser", "date_joined")
    list_display = ("username", "email", "is_staff", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name")

    inlines = [ProfileInline, LinkedAddressInline]

    def get_inlines(self, request, obj=None):
        if not obj:
            return []
        return super().get_inlines(request, obj)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    raw_id_fields = ("recipient",)
    list_display = ("notification", "unread", "deleted")
    list_filter = ("timestamp", "level", "unread", "deleted", "public")
    actions = ["mark_as_read", "mark_as_deleted", "delete_permanent"]
    ordering = ("-timestamp", "unread")
    list_display_links = None

    def notification(self, obj):
        return render_notice(self.request, obj)

    def get_queryset(self, request):
        if is_soft_delete:
            qs = request.user.notifications.active()
        else:
            qs = request.user.notifications.all()
        return qs

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff or request.user.is_superuser

    @admin.action(description=_("Mark selected notification as read"))
    def mark_as_read(self, request, queryset):
        queryset.filter(recipient=request.user).update(unread=False)
        messages.success(request, _("Selected notifications marked as read"))

    @admin.action(description=_("Mark selected notification as deleted"))
    def mark_as_deleted(self, request, queryset):
        queryset.filter(recipient=request.user).update(unread=False, deleted=True)
        messages.success(request, _("Selected notifications marked as deleted"))

    @admin.action(description=_("Delete selected notifications"))
    def delete_permanent(self, request, queryset):
        queryset.filter(recipient=request.user).delete()
        messages.success(request, _("Selected notifications deleted"))

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context)
