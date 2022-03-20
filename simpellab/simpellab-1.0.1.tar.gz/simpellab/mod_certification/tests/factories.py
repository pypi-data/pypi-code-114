import factory as fc

from simpel.simpel_products.tests.factories import ServiceFactory

from ..models import CertificationService


class CertificationServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Certification {n}")

    class Meta:
        model = CertificationService
        django_get_or_create = ("name",)
