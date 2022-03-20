"""
    This module is largely inspired by django-rest-framework settings.
    This module provides the `settings` object, that is used to access
    app settings, checking for user settings first, then falling
    back to the defaults.
"""
from typing import Any, Dict

import pytz
from django.conf import settings
from django.test.signals import setting_changed
from django.utils.module_loading import import_string

SETTINGS_DOC = "https://gitlab.com/sasriawesome/simpel"


SIMPEL_CORE_DEFAULTS: Dict[str, Any] = {
    "DEFAULT_CURRENCY": "IDR",
    "MODEL_TEMPLATE_ADMIN": "simpel.simpel_core.admin.ModelTemplateAdmin",
    "FILE_MODEL_TEMPLATE_ADMIN": "simpel.simpel_core.admin.FileModelTemplateAdmin",
    "PATH_MODEL_TEMPLATE_ADMIN": "simpel.simpel_core.admin.PathModelTemplateAdmin",
    "STRING_MODEL_TEMPLATE_ADMIN": "simpel.simpel_core.admin.StringModelTemplateAdmin",
    "CURRENCY_FORMAT": {
        "USD": {
            "currency_digits": False,
            "format_type": "accounting",
        },
        "IDR": {
            "format": "\xa0¤ #,##0",
            "locale": "id_id",
            "currency_digits": True,
            "format_type": "standart",
        },
    },
    "SIMPEL_LANGUAGES": [
        ("id-ID", "Indonesia"),
        ("en-US", "English (United States)"),
    ],
    "SIMPEL_TIMEZONES": pytz.common_timezones,
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = [
    "MODEL_TEMPLATE_ADMIN",
    "FILE_MODEL_TEMPLATE_ADMIN",
    "PATH_MODEL_TEMPLATE_ADMIN",
    "STRING_MODEL_TEMPLATE_ADMIN",
    "PRINT_VIEW_CLASS",
]

# List of settings that have been removed
REMOVED_SETTINGS = []


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    elif isinstance(val, dict):
        return {key: import_from_string(item, setting_name) for key, item in val.items()}
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        return import_string(val)
    except ImportError as e:
        msg = "Could not import '%s' for SIMPEL_CORE setting '%s'. %s: %s." % (
            val,
            setting_name,
            e.__class__.__name__,
            e,
        )
        raise ImportError(msg)


class AppSettings:
    """
    This module is largely inspired by django-rest-framework settings.
    This module provides the `simpel_core_settings` object, that is used to access
    app settings, checking for user settings first, then falling
    back to the defaults.
    """

    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or SIMPEL_CORE_DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, "_user_settings"):
            self._user_settings = getattr(settings, "SIMPEL_CORE", {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid SIMPEL_CORE settings: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def __check_user_settings(self, user_settings):
        for setting in REMOVED_SETTINGS:
            if setting in user_settings:
                raise RuntimeError(
                    "The '%s' setting has been removed. Please refer to '%s' for available settings."
                    % (setting, SETTINGS_DOC)
                )
        return user_settings

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, "_user_settings"):
            delattr(self, "_user_settings")


simpel_core_settings = AppSettings(None, SIMPEL_CORE_DEFAULTS, IMPORT_STRINGS)


def reload_simpel_core_settings(*args, **kwargs):
    setting = kwargs["setting"]
    if setting == "SIMPEL_CORE":
        simpel_core_settings.reload()


setting_changed.connect(reload_simpel_core_settings)
