from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_global_log"
    verbose_name = _("Django访问日志")
