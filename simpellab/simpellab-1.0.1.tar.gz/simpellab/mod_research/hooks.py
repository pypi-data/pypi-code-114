from django_hookup import core as hookup

from .models import ResearchService


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_mod_research_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_research_service_model():
    return ResearchService
