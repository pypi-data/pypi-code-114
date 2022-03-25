from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Bankcard


class BankcardForm(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user = request.user

    class Meta:
        model = Bankcard
        fields = ['name', 'number']


class PaymentMethodFormBase(forms.Form):
    method_code = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        if 'checkout_session' in kwargs:
            self.checkout_session = kwargs.pop('checkout_session')

        super().__init__(*args, **kwargs)
        self.fields['method_code'].initial = self.code

    def save(self):
        return True

    class Meta:
        abstract = True


class SelectBankAccountForm(forms.Form):
    bank_accounts = forms.ChoiceField()

    def __init__(self, request, shipping_address, *args, **kwargs):
        if request.method == 'POST':
            super().__init__(request.POST, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
        #self.fields['bank_accounts'].widget.attrs['class'] = 'w-100'
        self.fields['bank_accounts'].choices = self.get_choices(request)
        self.fields['bank_accounts'].label = ''

        default_bank_account = shipping_address.default_bank_account
        self.fields['bank_accounts'].initial = getattr(
            default_bank_account, 'id', None)

    def get_choices(self, request):
        yield ('', 'Konto hier auswählen')
        for acc in request.user.bankcards.all():
            yield (acc.pk, '{} - {}'.format(acc.obfuscated_number, acc.name))
