from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ("partner_type", "doc", "idn", "tax_id", "name", "attachment")


class ConfirmationForm(forms.Form):
    confirm = forms.BooleanField(
        help_text=_(
            """
        By becoming our partner, you agree to our Terms of Service and Privacy Policy,
        which we may update from time to time. We’ll occasionally send you account-related emails.
        """
        )
    )
