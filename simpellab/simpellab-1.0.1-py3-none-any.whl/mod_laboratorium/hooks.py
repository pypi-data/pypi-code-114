from django_hookup import core as hookup

from .models import LaboratoriumService, LaboratoriumTask


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_mod_laboratorium_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_laboratorium_service():
    return LaboratoriumService


@hookup.register("REGISTER_TASK_CHILD_MODELS")
def register_laboratorium_task():
    return LaboratoriumTask


# @hookup.register("REGISTER_DELIVERABLE_CHILD_MODELS")
# def register_laboratorium_certificate():
#     return LaboratoriumCertificate


# @hookup.register("REGISTER_API_VIEWSET")
# def register_labservice_viewset():
#     return {
#         "prefix": "products/laboratorium",
#         "viewset": LaboratoriumServiceViewSet,
#         "basename": "laboratoriumservice",
#     }
