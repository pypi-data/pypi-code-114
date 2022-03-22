from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import LinkedQRCode


class LinkedQRCodeInline(GenericTabularInline):
    ct_field = "linked_object_type"
    ct_fk_field = "linked_object_id"
    model = LinkedQRCode
    extra = 1


@admin.register(LinkedQRCode)
class LinkedQRCodeAdmin(admin.ModelAdmin):
    list_display = ["linked_object", "qr_image", "qr_data"]
