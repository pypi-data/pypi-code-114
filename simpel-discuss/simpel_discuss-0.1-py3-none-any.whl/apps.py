from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelDiscussConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpel_discuss'
    app_label = 'simpel_discuss'
    verbose_name = _("Discuss")
    icon = "comment-quote-outline"
