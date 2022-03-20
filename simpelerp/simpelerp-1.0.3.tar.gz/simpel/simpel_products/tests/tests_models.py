from django.test import TestCase

from . import factories as fcs


class MasterModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.units = fcs.UnitFactory.create_batch(3)
        cls.categories = fcs.CategoryFactory.create_batch(3)
        cls.services = fcs.ServiceFactory.create_batch(3)

    def setUp(self):
        return super().setUp()

    def test_unit_model(self):
        unit = fcs.UnitFactory(name="Orang/Hari")
        unit2 = fcs.UnitFactory(name="Orang Hari")
        self.assertEqual("oranghari", unit.slug)
        self.assertEqual("orang-hari", unit2.slug)
