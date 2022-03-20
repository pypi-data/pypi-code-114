from django.test import TestCase

from simpel.simpel_products.tests import factories as products_fcs

from . import factories as fcs


class SalesOrderTestCase(TestCase):
    def test_create_sales_order(self):
        salesorder = fcs.SalesOrderFactory()
        salesorder.save()
        product = products_fcs.ServiceFactory()
        product.save()
        salesorder_item = fcs.SalesOrderItemFactory(
            salesorder=salesorder,
            product=product,
            price=product.price,
            quantity=2,
        )
        salesorder_item.save()
