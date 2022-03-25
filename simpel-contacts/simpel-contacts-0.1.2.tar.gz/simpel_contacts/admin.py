from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

import nested_admin
from simpel_utils.loading import get_model

from .models import LinkedAddress, LinkedContact


class PublicPermission:
    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True


class CountryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "display_order"]
    list_filter = ["is_shipping_country"]
    search_fields = ["name", "printable_name", "iso_3166_1_a2", "iso_3166_1_a3"]


class LinkedAddressInline(PublicPermission, GenericStackedInline):
    model = LinkedAddress
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0
    autocomplete_fields = ["country"]


class NestedLinkedAddressInline(
    PublicPermission,
    nested_admin.NestedGenericStackedInline,
):
    model = LinkedAddress
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0
    autocomplete_fields = ["country"]


class LinkedContactInline(PublicPermission, GenericStackedInline):
    model = LinkedContact
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0
    autocomplete_fields = ["country"]


class NestedLinkedContactInline(
    PublicPermission,
    nested_admin.NestedGenericStackedInline,
):
    model = LinkedContact
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    extra = 0
    autocomplete_fields = ["country"]


class SingleLinkedAddressInline(LinkedAddressInline):
    extra = 0
    max_num = 1
    autocomplete_fields = ["country"]


admin.site.register(get_model("simpel_contacts", "country"), CountryAdmin)
