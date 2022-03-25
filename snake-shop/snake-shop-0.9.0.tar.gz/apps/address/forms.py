from django import forms
from django.conf import settings
from oscar.forms.mixins import PhoneNumberMixin

from . import models


class AbstractAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        Set fields in OSCAR_REQUIRED_ADDRESS_FIELDS as required.
        """
        super().__init__(*args, **kwargs)
        field_names = (set(self.fields)
                       & set(settings.OSCAR_REQUIRED_ADDRESS_FIELDS))
        for field_name in field_names:
            self.fields[field_name].required = True


class UserAddressForm(AbstractAddressForm, PhoneNumberMixin):

    is_company = forms.BooleanField(label='Geschäftskunden-Adresse', required=False)

    class Meta:
        model = models.UserAddress
        fields = [
            'is_company', 'company', 'cost_center', 'title', 'first_name', 'last_name',
            'line1', 'line4', 'postcode', 'floor_number', 'phone_number',
            'notes'
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user = user
        if self.instance.get_is_company() is not True:
            self.fields['company'].widget.attrs['disabled'] = True
            self.fields['cost_center'].widget.attrs['disabled'] = True
        js = '{}{}{}{}{}{}{}{}'.format(
            'if($(this).is(":checked")){',
            '$("#id_company").removeAttr("disabled");',
            '$("#id_cost_center").removeAttr("disabled");',
            '$("#id_company").attr("required","required");',
            '}else{',
            '$("#id_company").attr("disabled","disabled");',
            '$("#id_cost_center").attr("disabled","disabled");',
            '$("#id_company").removeAttr("required");}',
        )
        self.fields['is_company'].widget.attrs['onchange'] = js

    def clean(self):
        result = AbstractAddressForm.clean(self)
        if self.cleaned_data['is_company'] and not self.cleaned_data['company']:
            raise forms.ValidationError("Gewerbliche Adressen benötigen einen überprüfbaren Unternehmensnamen.")
        if not self.cleaned_data['is_company'] and 'company' in self.cleaned_data:
            self.cleaned_data.pop('company')
        return result
