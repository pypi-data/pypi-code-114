# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring


from raven import Client

from tanzanite.backend.app.app.core.celery_app import celery_app
from tanzanite.backend.app.app.core.config import settings

client_sentry = Client(settings.SENTRY_DSN)


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    return f"test task returned '{word}'"
