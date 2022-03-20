import factory as fc

from simpel.simpel_products.tests.factories import ServiceFactory

from ..models import InspectionService


class InspectionServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Inspection {n}")

    class Meta:
        model = InspectionService
        django_get_or_create = ("name",)
