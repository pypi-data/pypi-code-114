from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from simpel.simpel_core.helpers import OrderBuilder

from .models import (
    SalesOrder,
    SalesOrderItem,
    SalesOrderItemBundle,
    SalesQuotation,
    SalesQuotationItem,
    SalesQuotationItemBundle,
)
from .settings import simpel_sales_settings as sales_settings
from .signals import after_checkout


def salesorder_pending_validation(customer, order_group=None):
    # Check for pending order by product contenttype
    filter = {"status": SalesOrder.PENDING}
    if order_group:
        filter["code"] = order_group
    pending_orders = customer.sales_orders.filter(**filter)
    pending_count = pending_orders.count()
    pending_limit = sales_settings.SALES["MAX_PENDING_ORDERS_PER_SERVICE"]
    if pending_count >= pending_limit:
        raise ValidationError(_("Maximum order %(max)s reached"), params={"max": pending_limit})


def get_allowed_product_groups(group_code):
    group_map = {
        "LAB": [group_code, "PRM", "FEE"],
        "LIT": [group_code, "PRM", "FEE"],
        "KAL": [group_code, "FEE"],
        "KSL": [group_code, "FEE"],
        "PRO": [group_code, "FEE"],
        "LIB": [group_code, "FEE"],
        "SRV": [group_code, "FEE"],
    }
    try:
        return group_map[group_code]
    except KeyError:
        return []


sales_order_builder = OrderBuilder(
    SalesOrder,
    SalesOrderItem,
    SalesOrderItemBundle,
)

sales_quotation_builder = OrderBuilder(
    SalesQuotation,
    SalesQuotationItem,
    SalesQuotationItemBundle,
)


def create_salesorder(
    request,
    data,
    items,
    delete_item=False,
    billing=None,
    shipping=None,
    from_cart=False,
):
    order = sales_order_builder.create(
        request.user,
        data,
        items,
        billing=billing,
        shipping=shipping,
        delete_item=delete_item,
        from_cart=from_cart,
    )
    after_checkout.send(sender=order.__class__, instance=order, actor=request.user)
    return order


def create_salesquotation(
    request,
    data,
    items,
    delete_item=False,
    billing=None,
    shipping=None,
    from_cart=False,
):
    order = sales_quotation_builder.create(
        request.user,
        data,
        items,
        billing=billing,
        shipping=shipping,
        delete_item=delete_item,
        from_cart=from_cart,
    )
    after_checkout.send(sender=order.__class__, instance=order, actor=request.user)
    return order


def clone_salesquotation(
    request,
    obj,
):
    data = dict(
        group=obj.group,
        customer=obj.customer,
        discount=obj.discount,
        reference=obj.reference,
        note=obj.note,
        data=obj.data,
    )
    cloned = sales_quotation_builder.clone(request.user, data, obj)
    after_checkout.send(sender=cloned.__class__, instance=cloned, actor=request.user)
    return cloned


def clone_salesorder(
    request,
    obj,
    billing=None,
    shipping=None,
):
    data = dict(
        group=obj.group,
        customer=obj.customer,
        discount=obj.discount,
        reference=obj.reference,
        note=obj.note,
        data=obj.data,
    )
    cloned = sales_order_builder.clone(request.user, data, obj)
    after_checkout.send(sender=cloned.__class__, instance=cloned, actor=request.user)
    return cloned


def convert_salesquotation(request, obj):
    data = dict(
        group=obj.group,
        customer=obj.customer,
        discount=obj.discount,
        reference=obj.reference,
        note=obj.note,
        data=obj.data,
    )
    salesorder = sales_order_builder.clone(request.user, data, obj)
    after_checkout.send(sender=salesorder.__class__, instance=salesorder, actor=request.user)
    return salesorder
