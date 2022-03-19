from django.db import migrations, models

import django_global_log.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DjangoGlobalLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "operator",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="操作人"
                    ),
                ),
                ("path", models.TextField(verbose_name="请求地址")),
                ("code", models.SmallIntegerField(default=200, verbose_name="响应码")),
                (
                    "detail",
                    models.JSONField(
                        default=django_global_log.models.get_default_detail,
                        null=True,
                        verbose_name="详细信息",
                    ),
                ),
                ("duration", models.IntegerField(default=0, verbose_name="请求时长(ms)")),
                ("ip", models.GenericIPAddressField(verbose_name="IP地址")),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
            options={
                "verbose_name": "全局日志",
                "verbose_name_plural": "全局日志",
                "db_table": "django_global_log",
                "ordering": ["-id"],
            },
        ),
    ]
