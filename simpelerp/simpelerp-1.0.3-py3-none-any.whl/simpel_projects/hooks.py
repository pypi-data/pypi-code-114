from django_hookup import core as hookup

from .models import CancelationDeliverable, DocumentDeliverable


@hookup.register("REGISTER_DELIVERABLE_CHILD_MODELS")
def register_cancelation_deliverable_model():
    return CancelationDeliverable


@hookup.register("REGISTER_DELIVERABLE_CHILD_MODELS")
def register_document_deliverable_model():
    return DocumentDeliverable
