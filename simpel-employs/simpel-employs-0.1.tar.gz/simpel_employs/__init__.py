from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from simpel_employs.version import get_version

VERSION = (0, 1, 0, "final", 0)

__version__ = get_version(VERSION)


def get_profile_model():
    """
    Return the Person/User Profile model that is active in this project.
    """
    try:
        PROFILE_MODEL = getattr(settings, "PROFILE_MODEL")
        return django_apps.get_model(PROFILE_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("PROFILE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured("PROFILE_MODEL refers to model '%s' that has not been installed" % PROFILE_MODEL)
