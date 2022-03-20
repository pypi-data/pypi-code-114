from django_hookup import core as hookup

from .models import CertificationService


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_simpel_certification_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_certification_service_model():
    return CertificationService
