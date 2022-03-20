import factory as fc

from simpel.simpel_products.tests.factories import ServiceFactory

from ..models import TrainingService


class TrainingServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Training {n}")

    class Meta:
        model = TrainingService
        django_get_or_create = ("name",)
