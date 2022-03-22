from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class SimpelHookupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "simpel_hookup"
    label = "simpel_hookup"
    verbose_name = _("Hookup")

    def ready(self):
        post_migrate.connect(init_app, sender=self)


def init_app(sender, **kwargs):
    pass
