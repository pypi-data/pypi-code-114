from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Reset simpellab demo users and initial permissions"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from simpellab.setup import reset_all

        reset_all()
