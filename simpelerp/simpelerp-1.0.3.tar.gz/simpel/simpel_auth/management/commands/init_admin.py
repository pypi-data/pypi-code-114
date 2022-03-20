from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from django_hookup import core as hookup

from ...settings import simpel_auth_settings as auth_settings

User = get_user_model()


class Command(BaseCommand):
    help = "Init Bot and SuperUser"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            botmin = User.objects.get(username=auth_settings.BOT_USERNAME)
            print("%s has been created" % botmin)
        except User.DoesNotExist:
            botmin = User.objects.create_user(
                username=auth_settings.BOT_USERNAME,
                password=auth_settings.BOT_PASSWORD,
                email=auth_settings.BOT_EMAIL,
                first_name=auth_settings.BOT_USERNAME,
                is_staff=True,
                is_superuser=True,
            )
            print(" Create new bot user '%s'" % botmin)
        botmin.save()

        try:
            superadmin = User.objects.get(username=auth_settings.ADMIN_USERNAME)
            print("%s has been created" % superadmin)
        except User.DoesNotExist:
            superadmin = User.objects.create_user(
                username=auth_settings.ADMIN_USERNAME,
                password=auth_settings.ADMIN_PASSWORD,
                email=auth_settings.ADMIN_EMAIL,
                first_name=auth_settings.ADMIN_USERNAME,
                is_staff=True,
                is_superuser=True,
            )
            print(" Create new admin user '%s'" % superadmin)
        superadmin.save()

        init_perms_funcs = hookup.get_hooks("REGISTER_INITIAL_PERMISSIONS")
        for func in init_perms_funcs:
            func()
