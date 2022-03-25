from oscar.apps.shipping.admin import *  # noqa
from .models import ShippedFloor


class ShippedFloorInline(admin.TabularInline):
    model = ShippedFloor
    extra = 0


class OrderAndItemChargesAdmin(admin.ModelAdmin):
    inlines = [ShippedFloorInline]
    filter_horizontal = ('partners', 'countries', )
    list_display = ('name', 'description', 'price_per_order',
                    'price_per_item', 'free_shipping_threshold',
                    'minimum_order_value', 'next_day_limit', 'form_fields',
                    'get_partners')
    list_filter = ('partners', )

    def get_partners(self, obj):
        return "\n".join([p.name for p in obj.partners.all()])


admin.site.unregister(WeightBased)
admin.site.unregister(OrderAndItemCharges)
admin.site.register(OrderAndItemCharges, OrderAndItemChargesAdmin)
