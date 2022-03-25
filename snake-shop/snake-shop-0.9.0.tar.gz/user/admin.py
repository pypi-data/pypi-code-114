from django.contrib import admin
from django.contrib.auth.models import Group as GroupBase
from django.utils.translation import gettext_lazy as _
from .models import OrganizationUnit, Group


class OrganizationUnitAdmin(admin.ModelAdmin):
    model = OrganizationUnit
    readonly_fields = (
        'code',
    )
    fieldsets = (
        (None, {
            'fields': ('name', 'code', 'description',)
        }),
        (_('Mitglieder und E-Mail Empfang'), {
            'description': '',
            'classes': ('collapse',),
            'fields': ('members', 'email_recipients', 'event_types'),
        }),
        (_('Responsibilities'), {
            'description': '',
            'classes': ('collapse',),
            'fields': ('customers', 'product_classes'),
        }),
    )
    list_display = (
        'name',
        'get_members_str',
        'get_event_types_str',
        'get_customers_str',
        'get_product_classes_str',
    )
    filter_horizontal = (
        'members',
        'email_recipients',
        'event_types',
        'customers',
        'product_classes',
    )

    @admin.display(description=_('Empfänger'))
    def get_members_str(self, obj):
        return ', '.join((str(x) for x in obj.get_email_recipients()))

    @admin.display(description=_('Communication event types'))
    def get_event_types_str(self, obj):
        return ', '.join((str(x) for x in obj.event_types.all()))

    @admin.display(description=_('Customers'))
    def get_customers_str(self, obj):
        return ', '.join((str(x) for x in obj.customers.all()))

    @admin.display(description=_('Product classes'))
    def get_product_classes_str(self, obj):
        return ', '.join((str(x) for x in obj.product_classes.all()))


admin.site.unregister(GroupBase)
admin.site.register(Group)
admin.site.register(OrganizationUnit, OrganizationUnitAdmin)
