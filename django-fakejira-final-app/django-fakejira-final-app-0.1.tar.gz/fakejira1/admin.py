from django.contrib import admin
from . import models


class ShippingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'customer', 'shipping_status',)

    model = models.Shipping

    list_display = (
        "pk",
        "product",
        "customer",
        "shipping_status",
    )
    list_filter = (
        "product",
        "customer",
        "shipping_status",
    )
    list_editable = (
        "product",
        "customer",
        "shipping_status",
    )
    search_fields = (
        "product",
        "customer",
        "shipping_status",
    )

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.task.delete()
        queryset.delete()



admin.site.register(models.Shipping, ShippingAdmin)

