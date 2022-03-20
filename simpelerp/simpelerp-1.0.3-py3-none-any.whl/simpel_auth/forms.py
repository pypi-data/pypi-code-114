import warnings
from operator import itemgetter

import l18n
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.models import BaseInlineFormSet
from django.utils.translation import get_language_info
from django.utils.translation import gettext_lazy as _

from simpel.simpel_core.settings import simpel_core_settings as core_settings

from .models import LinkedAddress, Profile

User = get_user_model()


def get_available_admin_languages():
    return core_settings.SIMPEL_LANGUAGES


def get_available_admin_time_zones():
    if not settings.USE_TZ:
        return []

    return core_settings.SIMPEL_TIMEZONES


def _get_language_choices():
    language_choices = [
        (lang_code, get_language_info(lang_code)["name_local"])
        for lang_code, lang_name in get_available_admin_languages()
    ]
    return sorted(BLANK_CHOICE_DASH + language_choices, key=lambda l: l[1].lower())


def _get_time_zone_choices():
    time_zones = [(tz, str(l18n.tz_fullnames.get(tz, tz))) for tz in get_available_admin_time_zones()]
    time_zones.sort(key=itemgetter(1))
    return BLANK_CHOICE_DASH + time_zones


class AddressForm(forms.ModelForm):
    class Meta:
        model = LinkedAddress
        fields = (
            "address_type",
            "name",
            "phone",
            "address",
            "city",
            "province",
            "country",
            "zipcode",
        )


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
        label=_("Upload a profile picture"),
        required=False,
    )
    preferred_language = forms.ChoiceField(
        required=False,
        choices=_get_language_choices(),
        label=_("Preferred language"),
    )
    current_time_zone = forms.ChoiceField(
        required=False,
        choices=_get_time_zone_choices(),
        label=_("Current time zone"),
    )

    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_avatar = self.instance.avatar
        if len(get_available_admin_languages()) <= 1:
            del self.fields["preferred_language"]
        if len(get_available_admin_time_zones()) <= 1:
            del self.fields["current_time_zone"]

    def save(self, commit=True):
        if commit and self._original_avatar and (self._original_avatar != self.cleaned_data["avatar"]):
            # Call delete() on the storage backend directly, as calling self._original_avatar.delete()
            # will clear the now-updated field on self.instance too
            try:
                self._original_avatar.storage.delete(self._original_avatar.name)
            except IOError:
                # failure to delete the old avatar shouldn't prevent us from continuing
                warnings.warn("Failed to delete old avatar file: %s" % self._original_avatar.name)
        super().save(commit=commit)


class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name")

    def save(self, request, commit=True):
        return super().save(commit)


class AvatarForm(forms.ModelForm):
    avatar = forms.ImageField(
        label=_("Upload a profile picture"),
        required=False,
    )

    class Meta:
        model = Profile
        fields = ("avatar",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_avatar = self.instance.avatar

    def save(self, request, commit=True):
        if commit and self._original_avatar and (self._original_avatar != self.cleaned_data["avatar"]):
            # Call delete() on the storage backend directly, as calling self._original_avatar.delete()
            # will clear the now-updated field on self.instance too
            try:
                self._original_avatar.storage.delete(self._original_avatar.name)
            except IOError:
                # failure to delete the old avatar shouldn't prevent us from continuing
                warnings.warn("Failed to delete old avatar file: %s" % self._original_avatar.name)
        super().save(commit=commit)


class LanguagePreferenceForm(forms.ModelForm):
    preferred_language = forms.ChoiceField(
        required=False,
        choices=_get_language_choices(),
        label=_("Preferred language"),
    )
    current_time_zone = forms.ChoiceField(
        required=False,
        choices=_get_time_zone_choices(),
        label=_("Current time zone"),
    )

    class Meta:
        model = Profile
        fields = ("preferred_language", "current_time_zone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(get_available_admin_languages()) <= 1:
            del self.fields["preferred_language"]
        if len(get_available_admin_time_zones()) <= 1:
            del self.fields["current_time_zone"]

    def save(self, request, commit=True):
        return super().save(commit)


class ProfileInlineFormset(BaseInlineFormSet):
    pass
