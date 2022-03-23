# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class ProductSupplier(metaclass=PoolMeta):
    __name__ = 'purchase.product_supplier'

    global_lead_time = fields.Function(fields.TimeDelta('Global Lead Time',
            help='The global lead time defined for the supplier is used '
            'when there is no individual lead time set for this product.',
            depends=['party']),
            'on_change_with_global_lead_time')

    @fields.depends('company', 'party')
    def on_change_with_global_lead_time(self, name=None):
        # Use getattr because it can be called with an unsaved instance
        lead_time = None
        party = getattr(self, 'party', None)
        if party:
            company = getattr(self, 'company', None)
            lead_time = party.get_multivalue(
                'supplier_lead_time', company=company.id if company else None)
        return lead_time
