import factory as fc

from simpel.simpel_products.tests.factories import ServiceFactory

from ..models import ConsultancyService


class ConsultancyServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Consultancy {n}")

    class Meta:
        model = ConsultancyService
        django_get_or_create = ("name",)
