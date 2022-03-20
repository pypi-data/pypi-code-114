from django import forms

# from simpel.simpel_payments.models import PaymentGateway
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from django.utils.translation import gettext_lazy as _

from django_select2.forms import Select2Widget

from simpel.simpel_auth.models import LinkedAddress
from simpel.simpel_products.models import Group, Product
from simpel.simpel_sales.helpers import create_salesorder, create_salesquotation
from simpel.simpel_sales.settings import simpel_sales_settings as sales_settings

from .models import Cart, CartItem, CartItemBundle

CustomerModel = sales_settings.CUSTOMER_MODEL


class CheckoutAddressForm(forms.Form):
    def __init__(self, customer=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if customer is not None:
            queryset = customer.addresses.all()
        else:
            queryset = LinkedAddress.objects.none()
        self.fields["billing_address"] = forms.ModelChoiceField(queryset=queryset)
        self.fields["shipping_address"] = forms.ModelChoiceField(queryset=queryset)


class CheckoutForm(forms.Form):
    billing_address = forms.ModelChoiceField(queryset=LinkedAddress.objects.all())
    shipping_address = forms.ModelChoiceField(queryset=LinkedAddress.objects.all())

    def __init__(self, shop_adapter, request=None, *args, **kwargs):
        self.request = request
        self.shop_adapter = shop_adapter
        super().__init__(*args, **kwargs)
        self.fields["group"] = forms.ModelChoiceField(
            required=sales_settings.PRODUCT_GROUPING,
            widget=forms.Select(),
            queryset=Group.objects.all(),
        )
        if self.request.user.is_staff or self.request.user.is_superuser:
            self.fields["customer"] = forms.ModelChoiceField(
                required=True,
                queryset=CustomerModel.objects.filter(is_active=True),
                widget=Select2Widget(attrs={"class": "admin-autocomplete"}),
            )
        self.fields["reference"] = forms.CharField(required=False)

        self.fields["note"] = forms.CharField(
            required=False,
            widget=forms.Textarea(attrs={"rows": 4}),
        )

    def clean_group(self):
        data = self.cleaned_data["group"]
        if sales_settings.PRODUCT_GROUPING:
            cart = Cart.get_for_user(self.request.user)
            if not cart.items.filter(product__group=data).exists():
                raise forms.ValidationError(_("Please add at least one product in your cart"))
        return data

    def get_checkout_handler(self, action):
        action_map = {
            "create_salesorder": create_salesorder,
            "create_salesquotation": create_salesquotation,
        }
        return action_map[action]

    def clean_customer(self):
        data = self.cleaned_data["customer"]
        return data

    def save(self, action):
        billing_address = self.cleaned_data.pop("billing_address")
        shipping_address = self.cleaned_data.pop("shipping_address")
        if sales_settings.PRODUCT_GROUPING:
            items = self.shop_adapter.get_filtered_items(self.cleaned_data["group"].code)
        else:
            items = self.shop_adapter.get_filtered_items()
        handler = self.get_checkout_handler(action)
        self.instance = handler(
            self.request,
            data=self.cleaned_data,
            items=items,
            billing=billing_address,
            shipping=shipping_address,
            delete_item=True,
            from_cart=True,
        )
        return self.instance


class AddItemForm(forms.Form):
    name = forms.CharField(
        required=False,
        help_text=_("Give your cart item name."),
    )
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
    )

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance")
        super().__init__(*args, **kwargs)
        self.fields["quantity"] = forms.IntegerField(
            min_value=self.instance.min_order,
            max_value=self.instance.max_order,
            help_text=_("Quantity limit %s - %s") % (self.instance.min_order, self.instance.max_order),
        )
        self.fields["bundles"] = forms.ModelMultipleChoiceField(
            queryset=self.instance.recommended_items.all(),
            required=False,
        )


class CartItemModelForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = (
            "name",
            "quantity",
            "note",
        )


class CartItemRecommendedBundleForm(forms.ModelForm):
    class Meta:
        model = CartItemBundle
        fields = ("cart_item", "product")
        widgets = {"cart_item": forms.HiddenInput()}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product"] = forms.ModelMultipleChoiceField(
            queryset=self.instance.recommended_items.all(),
            required=False,
        )


class CartItemBundleForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(bundle=True),
        label=_("Bundle/Parameter"),
        widget=AutocompleteSelect(admin_site=admin.site, field=CartItemBundle._meta.get_field("product")),
    )

    class Meta:
        model = CartItemBundle
        fields = ("cart_item", "product")
        widgets = {"cart_item": forms.HiddenInput()}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product"] = forms.ModelMultipleChoiceField(
            queryset=self.instance.recomended_bundles.all(),
            required=False,
        )
