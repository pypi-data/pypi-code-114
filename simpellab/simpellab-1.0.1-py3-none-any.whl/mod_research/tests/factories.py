import factory as fc

from simpel.simpel_products.tests.factories import ServiceFactory

from ..models import ResearchService


class ResearchServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Research {n}")

    class Meta:
        model = ResearchService
        django_get_or_create = ("name",)
