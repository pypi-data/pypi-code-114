from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelPagesConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'simpel.simpel_pages'
    verbose_name = _("Flat Pages")
