from django.contrib import admin
from oscar.apps.partner import admin as base_admin
from apps.partner.models import Partner, StockRecord


class StockRecordAdmin(base_admin.StockRecordAdmin):
    list_display = ('product', 'partner', 'partner_sku', 'price')
    list_filter = ['partner__site', 'partner']


class PartnerAdmin(admin.ModelAdmin):
    model = Partner
    fields = ['site', 'name', 'priority', 'wishlist_as_link', 'code']
    readonly_fields = ['code']
    list_display = ['site', 'name', 'priority', 'code', 'wishlist_as_link']
    list_filter= ['site']


admin.site.unregister(Partner)
admin.site.register(Partner, PartnerAdmin)
admin.site.unregister(StockRecord)
admin.site.register(StockRecord, StockRecordAdmin)
