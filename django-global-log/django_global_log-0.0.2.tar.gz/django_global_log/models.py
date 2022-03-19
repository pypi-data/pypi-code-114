from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import status


def get_default_detail():
    return {}


class DjangoGlobalLog(models.Model):
    """日志"""

    operator = models.CharField(_("操作人"), max_length=255, null=True, blank=True)
    path = models.TextField(_("请求地址"))
    code = models.SmallIntegerField(_("响应码"), default=status.HTTP_200_OK)
    detail = models.JSONField(_("详细信息"), default=get_default_detail, null=True)
    duration = models.IntegerField(_("请求时长(ms)"), default=0)
    ip = models.GenericIPAddressField(_("IP地址"))
    create_at = models.DateTimeField(_("创建时间"), auto_now_add=True)

    class Meta:
        db_table = "django_global_log"
        verbose_name = _("全局日志")
        verbose_name_plural = verbose_name
        ordering = ["-id"]

    def __str__(self):
        return "{}:{}".format(self.operator, self.path)
