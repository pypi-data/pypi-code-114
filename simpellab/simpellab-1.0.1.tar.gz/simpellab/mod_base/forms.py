from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from simpel.simpel_products.models import Group
from simpel.simpel_sales.models import SalesOrder, SalesQuotation
from simpel.simpel_sales.settings import simpel_sales_settings as sales_settings

CustomerModel = sales_settings.CUSTOMER_MODEL


class OrderMixin(forms.Form):
    group = forms.ModelChoiceField(
        required=False,
        widget=forms.Select(),
        queryset=Group.objects.filter(
            code__in=[
                "LAB",
                "LIT",
                "KAL",
                "LIB",
                "PRO",
                "KSL",
                "LAT",
                "SRV",
            ]
        ),
    )
    sampling_options = forms.BooleanField(required=False)
    sampling_schedule = forms.DateField(widget=AdminDateWidget(), required=False)
    sampling_estimation = forms.IntegerField(initial=1)
    note = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 3}))
    data = forms.CharField(required=False, widget=forms.HiddenInput())

    def clean_sampling_schedule(self):
        sampling = self.cleaned_data["sampling_options"]
        data = self.cleaned_data["sampling_schedule"]
        if sampling:
            if data is None:
                raise forms.ValidationError(_("Please insert sampling schedule"))
            valid_schedule = data >= timezone.now().date()
            if not valid_schedule:
                raise forms.ValidationError("%s is earlier than today " % data)
        else:
            data = timezone.now().date()
        return data

    def clean_sampling_estimation(self):
        sampling = self.cleaned_data["sampling_options"]
        data = self.cleaned_data["sampling_estimation"]
        valid_number = int(data) >= 1
        if sampling and not valid_number:
            raise forms.ValidationError(_("Minimum sampling estimation is 1."))
        return data


class BaseOrderForm(OrderMixin, forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=CustomerModel.objects.filter(is_active=True),
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        if instance is not None and bool(instance.data):
            kwargs["initial"] = {
                "customer": instance.customer,
                "sampling_options": instance.data.get("sampling_options", False),
                "sampling_schedule": instance.data.get("sampling_schedule", timezone.now()),
                "sampling_estimation": instance.data.get("sampling_estimation", 1),
            }
        else:
            kwargs["initial"] = {
                "sampling_options": False,
                "sampling_schedule": timezone.now(),
                "sampling_estimation": 1,
            }
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        customer = self.cleaned_data.pop("customer", None)
        data = {
            "sampling_options": self.cleaned_data.pop("sampling_options"),
            "sampling_schedule": self.cleaned_data.pop("sampling_schedule").strftime("%d-%m-%Y"),
            "sampling_estimation": self.cleaned_data.pop("sampling_estimation"),
        }
        self.instance.customer = customer
        self.instance.data = data
        instance = super().save(commit)
        return instance


class SalesOrderForm(BaseOrderForm):
    class Meta:
        model = SalesOrder
        fields = [
            "group",
            "customer",
            "reference",
            "discount",
            "note",
            "status",
            "data",
            "sampling_options",
            "sampling_schedule",
            "sampling_estimation",
        ]


class SalesQuotationForm(BaseOrderForm):
    class Meta:
        model = SalesQuotation
        fields = [
            "group",
            "customer",
            "note",
            "data",
            "sampling_options",
            "sampling_schedule",
            "sampling_estimation",
        ]
