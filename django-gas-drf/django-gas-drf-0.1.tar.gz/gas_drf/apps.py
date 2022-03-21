from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GASDRFConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'gas_drf'
    verbose_name = _('GAS DRF')

    def ready(self):
        from .sites import drfsite
        super().ready()
        drfsite.autodiscover()
