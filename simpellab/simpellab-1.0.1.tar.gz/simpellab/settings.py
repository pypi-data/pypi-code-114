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

from .mod_base.models import ProductGroup

SETTINGS_DOC = "https://github.com/realnoobs/simpellab"

SIMPEL_DEFAULTS: Dict[str, Any] = {
    "SIMPEL_LANGUAGES": [
        ("id-ID", "Indonesia"),
        ("en-US", "English (United States)"),
    ],
    "SIMPEL_USER_TIMEZONES": pytz.common_timezones,
    "CART": {
        "SESSION_KEY": "cart",
        "MAX_CART_ITEM": 12,
        "USER_BLUEPRINT_LIMIT": 20,
        "BLUEPRINT_VALID_GROUPS": [
            ProductGroup.LABORATORIUM,
            ProductGroup.INSPECTION,
        ],
    },
    "INVOICES": {
        "INVOICE_DUE_DATE_LIMIT_DAY": 14,
    },
    "LABORATORIUM": {},
    "PARTNERS": {
        "MODERATE_ACTIVATION": True,
    },
    "PRODUCTS": {},
    "SALES": {
        "PENDING_ORDER_EXPIRATION_DAY": 3,
        "MAX_PENDING_ORDERS_PER_SERVICE": 5,
    },
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = [
    "PRODUCTS_PRODUCT_CHILD_MODELS",
    "SALES_SALESORDER_CHILD_MODELS",
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
        msg = "Could not import '%s' for SIMPEL setting '%s'. %s: %s." % (
            val,
            setting_name,
            e.__class__.__name__,
            e,
        )
        raise ImportError(msg)


class AppSettings:
    """
    This module is largely inspired by django-rest-framework settings.
    This module provides the `simpel_settings` object, that is used to access
    app settings, checking for user settings first, then falling
    back to the defaults.
    """

    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or SIMPEL_DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, "_user_settings"):
            self._user_settings = getattr(settings, "SIMPEL", {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid SIMPEL settings: '%s'" % attr)

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


simpel_settings = AppSettings(None, SIMPEL_DEFAULTS, IMPORT_STRINGS)


def reload_simpel_settings(*args, **kwargs):
    setting = kwargs["setting"]
    if setting == "SIMPEL":
        simpel_settings.reload()


setting_changed.connect(reload_simpel_settings)
