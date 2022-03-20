import factory  # NOQA
from factory.django import DjangoModelFactory

from ..models import Cancelation, Deliverable, FinalDocument


class DeliverableFactory(DjangoModelFactory):
    class Meta:
        model = Deliverable


class CancelationDeliverableFactory(DjangoModelFactory):
    class Meta:
        model = Cancelation


class FinalDocumentFactory(DjangoModelFactory):
    class Meta:
        model = FinalDocument
