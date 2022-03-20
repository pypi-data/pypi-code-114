from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelFeedbacksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpel.simpel_feedbacks'
    app_label = 'simpel_feedbacks'
    verbose_name = _("Feedbacks")
    icon = "comment-quote-outline"
