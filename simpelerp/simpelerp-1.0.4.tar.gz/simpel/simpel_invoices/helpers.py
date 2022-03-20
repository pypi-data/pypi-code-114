from simpel.simpel_core.helpers import OrderBuilder
from simpel.simpel_invoices.models import Invoice, InvoiceItem, InvoiceItemBundle

invoice_builder = OrderBuilder(
    Invoice,
    InvoiceItem,
    InvoiceItemBundle,
)


def create_invoice(request, obj):
    data = dict(
        group=obj.group,
        customer=obj.customer,
        discount=obj.discount,
        reference=obj,
        note=obj.note,
        data=obj.data,
    )
    salesorder = invoice_builder.clone(request.user, data, obj)
    return salesorder
