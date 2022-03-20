from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

from simpel.demo import create_demo

User = get_user_model()


class Command(BaseCommand):
    help = "Install demo data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        call_command('init_accounts')
        call_command('init_admin')
        create_demo()
