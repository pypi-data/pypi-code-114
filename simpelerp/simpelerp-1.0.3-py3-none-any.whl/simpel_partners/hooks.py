from django_hookup import core as hookup

from .admin import AdminCustomerRegistrationView
from .api.viewsets import PartnerViewSet


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_simpel_partner_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_DEMO_USERS")
def register_simpel_partners_demo_users():
    from .apps import init_demo_users

    init_demo_users()


@hookup.register("REGISTER_ADMIN_VIEW")
def register_profile_admin():
    return (
        "profile/customer/register/",
        AdminCustomerRegistrationView,
        "admin_profile_registation",
    )


@hookup.register("REGISTER_API_VIEWSET")
def register_partner_viewset():
    return {
        "prefix": "partners",
        "viewset": PartnerViewSet,
        "basename": "partner",
    }


# @hookup.register("REGISTER_API_VIEWSET")
# def register_user_partner_viewset():
#     return {
#         "prefix": "partners/me",
#         "viewset": UserPartnerViewSet,
#         "basename": "partner-me",
#     }
