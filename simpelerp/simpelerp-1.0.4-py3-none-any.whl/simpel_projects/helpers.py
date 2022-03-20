from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django_hookup import core as hook

from .models import Deliverable, Task, WorkOrder


def get_task_childs_models():
    child_models = []
    funcs = hook.get_hooks("REGISTER_TASK_CHILD_MODELS")
    child_classes = [func() for func in funcs]
    for klass in child_classes:
        if issubclass(klass, Task):
            child_models.append(klass)
        else:
            raise ImproperlyConfigured("Hook REGISTER_TASK_CHILD_MODELS should return Deliverable subclass")
    return child_models


def get_deliverable_childs_models():
    child_models = []
    funcs = hook.get_hooks("REGISTER_DELIVERABLE_CHILD_MODELS")
    deliverable_classes = [func() for func in funcs]
    for klass in deliverable_classes:
        if issubclass(klass, Deliverable):
            child_models.append(klass)
        else:
            raise ImproperlyConfigured("Hook REGISTER_DELIVERABLE_CHILD_MODELS should return Deliverable subclass")
    return child_models


def get_workorder_childs_models():
    child_models = []
    funcs = hook.get_hooks("REGISTER_WORKORDER_CHILD_MODELS")
    klasses = [func() for func in funcs]
    for klass in klasses:
        if issubclass(klass, WorkOrder):
            child_models.append(klass)
        else:
            raise ImproperlyConfigured("Hook REGISTER_WORKORDER_CHILD_MODELS should return WorkOrder subclass")
    return child_models


def convert_salesorder(request, salesorder):
    # Check if sales order valid to process
    with transaction.atomic():
        workorder = WorkOrder(
            user=request.user,
            group=salesorder.group,
            customer=salesorder.customer,
            reference=salesorder,
            title=_("%s Work Order for %s") % (salesorder.group, salesorder),
            content=salesorder.note,
        )
        workorder.save()

        # Add work order task
        for item in salesorder.items.filter(product__group=salesorder.group):
            task = Task(
                workorder=workorder,
                name=item.name,
                reference=item,
                quantity=item.quantity,
                note=item.note,
            )
            task.save()

        return workorder
