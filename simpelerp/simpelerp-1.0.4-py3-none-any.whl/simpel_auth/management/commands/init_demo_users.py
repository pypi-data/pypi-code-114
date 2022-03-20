from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django_hookup import core as hookup

User = get_user_model()


class Command(BaseCommand):
    help = "Init demo users"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with transaction.atomic():
            init_perms_funcs = hookup.get_hooks("REGISTER_DEMO_USERS")
            for func in init_perms_funcs:
                func()
