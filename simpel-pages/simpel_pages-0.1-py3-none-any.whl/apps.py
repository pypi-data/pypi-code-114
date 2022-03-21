

from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class SimpelPagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "simpel_pages"
    label = "simpel_pages"
    verbose_name = _("Simpel Pages")

    def ready(self):
        post_migrate.connect(init_app, sender=self)


def init_app(sender, **kwargs):
    """after migrations"""
    from django.contrib.sites.models import Site

    from simpel_themes.models import PathModelTemplate

    from simpel_pages.models import Page

    name = getattr(settings, "SITE_NAME", "Simpel")
    domain = getattr(settings, "SITE_DOMAIN", "127.0.0.1:8000")
    defaults = {"name": name, "domain": domain}
    site, _ = Site.objects.get_or_create(id=getattr(settings, "SITE_ID", 1), defaults=defaults)
    site.name = name
    site.domain = domain
    site.save()

    template, _ = PathModelTemplate.objects.get_or_create(
        template="index.html",
        defaults={
            "name": "Home Page",
        },
    )
    index_page, _ = Page.objects.get_or_create(
        url="/",
        defaults={
            "template": template,
            "title": "Home Page",
        },
    )
    index_page.sites.set([site])
