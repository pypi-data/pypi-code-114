import logging

from pkg_resources import working_set

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import override_settings

from dsbot.client import BotClient

logging.basicConfig(level=logging.WARNING)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--token", default=settings.SLACK_TOKEN, help="Slack token")
        parser.add_argument("--eager", action="store_true")

    def handle(self, verbosity, token, eager, **options):
        logging.root.setLevel(
            {
                0: logging.ERROR,
                1: logging.WARNING,
                2: logging.INFO,
                3: logging.DEBUG,
            }.get(verbosity)
        )

        for entry in working_set.iter_entry_points("dsbot.commands"):
            try:
                entry.load()
            except ImportError:
                logging.exception("Error loading %s", entry)
            else:
                logging.info("Loaded %s", entry)

        with override_settings(CELERY_TASK_ALWAYS_EAGER=eager):
            BotClient(token=token).start()
