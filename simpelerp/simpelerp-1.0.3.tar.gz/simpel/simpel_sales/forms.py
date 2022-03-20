from django import forms

from .models import SalesOrder, SalesQuotation
from .settings import simpel_sales_settings as sales_settings

CustomerModel = sales_settings.CUSTOMER_MODEL


class SalesOrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=CustomerModel.objects.filter(is_active=True),
    )

    class Meta:
        model = SalesOrder
        fields = [
            "group",
            "customer",
            "reference",
            "discount",
            "note",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        initial = kwargs.pop("initial", dict())
        if instance is not None:
            initial.update({"customer": instance.customer})
        return super().__init__(initial=initial, *args, **kwargs)

    def save(self, commit=True):
        self.instance.customer = self.cleaned_data["customer"]
        instance = super().save(commit)
        return instance


class SalesQuotationForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=CustomerModel.objects.filter(is_active=True),
    )

    class Meta:
        model = SalesQuotation
        fields = [
            "group",
            "customer",
            "note",
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        initial = kwargs.pop("initial", dict())
        if instance is not None:
            initial.update({"customer": instance.customer})
        return super().__init__(initial=initial, *args, **kwargs)

    def save(self, commit=True):
        self.instance.customer = self.cleaned_data["customer"]
        instance = super().save(commit)
        return instance
