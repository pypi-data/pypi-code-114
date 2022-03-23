# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest

from trytond.modules.company.tests import CompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class PurchaseSupplierLeadTimeTestCase(CompanyTestMixin, ModuleTestCase):
    'Test Purchase Supplier Lead Time module'
    module = 'purchase_supplier_lead_time'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            PurchaseSupplierLeadTimeTestCase))
    return suite
