from oscar.apps.payment.admin import *  # noqa


class SourceTypeAdmin(admin.ModelAdmin):
    model = SourceType
    list_display = (
        'code',
        'name',
        'enabled',
        'display_order',
        'description',
        'minimum_order_value',
        'company_only',
        'bankcard_needed',
        'get_partners',
    )
    list_filter = (
        'enabled',
        'minimum_order_value',
        'company_only',
        'bankcard_needed',
        'partners',
    )
    filter_horizontal = ('partners',)

    def get_partners(self, obj):
        return "\n".join([p.name for p in obj.partners.all()])


admin.site.unregister(SourceType)
admin.site.register(SourceType, SourceTypeAdmin)
