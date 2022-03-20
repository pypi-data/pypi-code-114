from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate


class SimpelCoreConfig(AppConfig):
    icon = "database-clock-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_core"
    label = "simpel_core"
    verbose_name = "Simpel"

    def ready(self):
        post_migrate.connect(init_app, sender=self)
        return super().ready()


def init_app(sender, **kwargs):
    """after migrations"""
    from django.contrib.sites.models import Site

    name = getattr(settings, "SITE_NAME", "Simpel")
    domain = getattr(settings, "SITE_DOMAIN", "127.0.0.1:8000")
    defaults = {"name": name, "domain": domain}
    site, _ = Site.objects.get_or_create(id=getattr(settings, "SITE_ID", 1), defaults=defaults)
    site.name = name
    site.domain = domain
    site.save()
