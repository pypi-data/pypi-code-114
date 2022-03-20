from django_hookup import core as hookup

from .models import ConsultancyService


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_mod_consultancy_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_consultancy_service_model():
    return ConsultancyService
