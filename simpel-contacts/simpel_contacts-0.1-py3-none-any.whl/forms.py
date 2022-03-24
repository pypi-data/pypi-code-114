from django import forms
from django.contrib.auth import get_user_model

from simpel_contacts.abstracts import REQUIRED_ADDRESS_FIELDS

User = get_user_model()
from .models import LinkedAddress


class AbstractAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Set fields in REQUIRED_ADDRESS_FIELDS as required.
        """
        super().__init__(*args, **kwargs)
        field_names = set(self.fields) & set(REQUIRED_ADDRESS_FIELDS)
        for field_name in field_names:
            self.fields[field_name].required = True


class LinkedAddressForm(AbstractAddressForm):
    class Meta:
        model = LinkedAddress
        fields = "__all__"
