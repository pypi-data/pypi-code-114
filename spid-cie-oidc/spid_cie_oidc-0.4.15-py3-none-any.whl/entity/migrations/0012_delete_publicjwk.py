# Generated by Django 4.0.2 on 2022-03-06 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0011_alter_trustchain_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublicJwk',
        ),
    ]
