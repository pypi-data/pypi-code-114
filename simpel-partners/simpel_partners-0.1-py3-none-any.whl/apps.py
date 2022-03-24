from django.apps import AppConfig as BaseAppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class SimpelPartnersConfig(BaseAppConfig):
    icon = "account-box-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel_partners"
    label = "simpel_partners"
    verbose_name = _("Partners")

    def ready(self):
        from . import signals  # NOQA

        post_migrate.connect(init_app, sender=self)
        return super().ready()


def init_app(**kwargs):
    pass


def init_demo_users():
    from simpel.simpel_auth.utils import create_demo_users

    usernames = {
        "partners_manager": "Partners Manager",
        "partners_admin": "Partners Admin",
    }
    create_demo_users(usernames)


def init_permissions():
    # from django.contrib.auth.models import Group
    # from django.db import transaction

    # from simpel.simpel_auth.utils import add_perms, get_perms_dict

    # from . import models

    # with transaction.atomic():
    #     partners_manager, _ = Group.objects.get_or_create(name="Partners Managers")
    #     partners_admin, _ = Group.objects.get_or_create(name="Partners Admin")

    #     actions = ["view", "add", "change", "delete"]
    #     imex = ["import", "export"]

    #     partner = get_perms_dict(actions + imex + ["change_partner_user", "activate", "verify"], models.Partner)

    #     view_groups = [
    #         partners_manager,
    #         partners_admin,
    #     ]
    #     change_groups = [
    #         partners_manager,
    #         partners_admin,
    #     ]
    #     add_groups = [
    #         partners_manager,
    #         partners_admin,
    #     ]
    #     delete_groups = [partners_admin]
    #     import_groups = [partners_admin]
    #     export_groups = [
    #         partners_manager,
    #         partners_admin,
    #     ]
    #     activate_groups = [
    #         partners_manager,
    #         partners_admin,
    #     ]
    #     verify_groups = [
    #         partners_manager,
    #         partners_admin,
    #     ]

    #     add_perms(activate_groups, [partner["activate"]])
    #     add_perms(verify_groups, [partner["verify"]])
    pass
