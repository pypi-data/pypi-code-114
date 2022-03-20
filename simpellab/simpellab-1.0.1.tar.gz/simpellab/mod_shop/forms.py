from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2.forms import Select2Widget

from simpel.simpel_auth.models import LinkedAddress
from simpel.simpel_shop.models import Cart
from simpellab.mod_base.forms import OrderMixin


class CheckoutAddressForm(forms.Form):
    def __init__(self, customer=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if customer is not None:
            queryset = customer.addresses.all()
        else:
            queryset = LinkedAddress.objects.none()
        self.fields["billing_address"] = forms.ModelChoiceField(queryset=queryset)
        self.fields["shipping_address"] = forms.ModelChoiceField(queryset=queryset)


class CheckoutForm(OrderMixin):
    billing_address = forms.ModelChoiceField(queryset=LinkedAddress.objects.all())
    shipping_address = forms.ModelChoiceField(queryset=LinkedAddress.objects.all())
    reference = forms.CharField(required=False)

    def __init__(self, request=None, *args, **kwargs):
        from simpel.simpel_sales.settings import simpel_sales_settings as sales_settings
        CustomerModel = sales_settings.CUSTOMER_MODEL
        self.request = request
        super().__init__(*args, **kwargs)
        if self.request.user.is_staff or self.request.user.is_superuser:
            self.fields["customer"] = forms.ModelChoiceField(
                required=True,
                queryset=CustomerModel.objects.filter(is_active=True),
                widget=Select2Widget(attrs={"class": "admin-autocomplete"}),
            )

    def clean_group(self):
        data = self.cleaned_data["group"]
        cart = Cart.get_for_user(self.request.user)
        if not cart.items.filter(product__group=data).exists():
            raise forms.ValidationError(_("Please add at least one product in your cart"))
        return data

    def clean_customer(self):
        data = self.cleaned_data["customer"]
        return data
