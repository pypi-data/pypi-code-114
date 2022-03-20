from django.utils.translation import gettext_lazy as _

from dynamic_preferences.preferences import Section
from dynamic_preferences.types import BooleanPreference

from aleksis.core.registries import site_preferences_registry

payments = Section("payments", verbose_name=_("Payments"))


@site_preferences_registry.register
class PublicPayments(BooleanPreference):
    """Allow payments to be made by anyone, not only invoice recipient."""

    section = payments
    name = "public_payments"
    verbose_name = _("Public payments")
    help_text = _(
        "Allow anyone (including guests) to make payments. "
        "Basic invoice information will be visible to anyone who knows the invoice token."
    )
    default = True
    required = False


@site_preferences_registry.register
class EnablePledge(BooleanPreference):
    """Payment pledge payment backend - enable or not."""

    section = payments
    name = "pledge_enabled"
    verbose_name = _("Enable pledged payments")
    default = False
    required = False


@site_preferences_registry.register
class UpdateOnPersonChange(BooleanPreference):
    """Update Invoices if person data changes."""

    section = payments
    name = "update_on_person_change"
    verbose_name = _("Update Invoices if person data changes")
    default = True
    required = False
