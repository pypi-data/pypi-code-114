from django_hookup import core as hookup

from .models import InspectionService, InspectionTask  # InspectionCertificate


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_mod_inspection_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_inspection_service_model():
    return InspectionService


@hookup.register("REGISTER_TASK_CHILD_MODELS")
def register_inspection_task():
    return InspectionTask


# @hookup.register("REGISTER_DELIVERABLE_CHILD_MODELS")
# def register_inspection_certificate_model():
#     return InspectionCertificate
