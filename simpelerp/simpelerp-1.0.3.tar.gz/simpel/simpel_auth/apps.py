from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SimpelAuthConfig(AppConfig):
    icon = "account-multiple-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_auth"
    label = "simpel_auth"
    verbose_name = "Authentication Users"

    def ready(self):
        from . import receivers  # NOQA

        post_migrate.connect(init_app, sender=self)
        return super().ready()


def init_app(sender, **kwargs):
    pass
