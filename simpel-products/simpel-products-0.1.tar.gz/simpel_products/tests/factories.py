import factory as fc
from factory.django import DjangoModelFactory

from ..models import Category, Product, Service, Specification, Unit


class UnitFactory(DjangoModelFactory):

    name = fc.Sequence(lambda n: f"Unit {n}")

    class Meta:
        model = Unit
        django_get_or_create = ("name",)


class CategoryFactory(DjangoModelFactory):

    name = fc.Sequence(lambda n: f"Category {n}")

    class Meta:
        model = Category
        django_get_or_create = ("name",)


class ProductFactory(DjangoModelFactory):

    name = fc.Sequence(lambda n: f"Product {n}")
    unit = fc.SubFactory(UnitFactory)
    category = fc.SubFactory(CategoryFactory)

    class Meta:
        model = Product
        django_get_or_create = ("name",)


class ServiceFactory(ProductFactory):

    name = fc.Sequence(lambda n: f"Service {n}")

    class Meta:
        model = Service
        django_get_or_create = ("name",)


class SpecificationFactory(DjangoModelFactory):
    product = fc.SubFactory(ProductFactory)
    feature = fc.Sequence(lambda n: f"Feature {n}")
    description = fc.Sequence(lambda n: f"Feature Description {n}")

    class Meta:
        model = Specification
        django_get_or_create = ("feature", "product")
