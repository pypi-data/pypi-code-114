from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from django_global_log.models import DjangoGlobalLog

USER_MODEL = get_user_model()


@admin.register(DjangoGlobalLog)
class LogAdmin(admin.ModelAdmin):
    list_display = ["id", "operator_name", "path", "code", "ip", "create_at"]
    list_filter = ["code"]

    @admin.display(description=_("操作人"))
    def operator_name(self, obj):
        try:
            return USER_MODEL.objects.get(pk=obj.operator).username
        except Exception:
            return obj.operator
