import factory  # NOQA
from factory.django import DjangoModelFactory

from ..models import SalesOrder, SalesOrderItem, SalesOrderItemBundle


class SalesOrderFactory(DjangoModelFactory):
    class Meta:
        model = SalesOrder


class SalesOrderItemFactory(DjangoModelFactory):
    class Meta:
        model = SalesOrderItem


class SalesOrderItemBundleFactory(DjangoModelFactory):
    class Meta:
        model = SalesOrderItemBundle
