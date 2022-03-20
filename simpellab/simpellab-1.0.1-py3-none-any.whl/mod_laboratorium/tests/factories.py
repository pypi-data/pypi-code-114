import factory as fc
from factory.django import DjangoModelFactory

from simpel.simpel_products.tests.factories import ProductFactory, ServiceFactory

from ..models import LaboratoriumCertificate, LaboratoriumService, Parameter


class ParameterFactory(ProductFactory):
    name = fc.Sequence(lambda n: f"Parameter {n}")
    price = 10000.00

    class Meta:
        model = Parameter
        django_get_or_create = ("name",)


class LaboratoriumServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Laboratorium Service {n}")

    class Meta:
        model = LaboratoriumService
        django_get_or_create = ("name",)


class LaboratoriumCertificateFactory(DjangoModelFactory):
    class Meta:
        model = LaboratoriumCertificate
