# Generated by Django 4.0.2 on 2022-03-05 01:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("spid_cie_oidc_provider", "0002_remove_oidcsession_user_claims"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="oidcsession",
            name="sub",
        ),
        migrations.AddField(
            model_name="issuedtoken",
            name="expires",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issuedtoken",
            name="revoked",
            field=models.BooleanField(default=False),
        ),
    ]
