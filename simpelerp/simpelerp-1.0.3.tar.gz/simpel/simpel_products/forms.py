from django import forms
from django.utils.translation import gettext_lazy as _


class AddProductToForm(forms.Form):
    reference = forms.CharField(
        required=True,
        help_text=_("Sales Order/Quotation inner id."),
    )
    name = forms.CharField(
        required=False,
        help_text=_("Give your cart item name."),
    )
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
    )

    def __init__(self, *args, **kwargs):
        self.ref_model = kwargs.pop("ref_model")
        self.instance = kwargs.pop("instance")
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["bundles"] = forms.ModelMultipleChoiceField(
            queryset=self.instance.recommended_items.all(),
            required=False,
        )
        self.fields["quantity"] = forms.IntegerField(
            min_value=self.instance.min_order,
            max_value=self.instance.max_order,
            help_text=_("Quantity limit %s - %s") % (self.instance.min_order, self.instance.max_order),
        )

    def clean_reference(self):
        reference = self.cleaned_data["reference"]
        ref_obj = self.ref_model.objects.filter(inner_id=reference).first()
        if not ref_obj:
            raise forms.ValidationError(
                "%s with inner id %s not found!" % (self.ref_model._meta.verbose_name, reference)
            )
        if not ref_obj.is_editable:
            raise forms.ValidationError(
                "%s with inner id %s is not editable!" % (self.ref_model._meta.verbose_name, reference)
            )
        product = ref_obj.items.filter(product=self.instance).first()
        if product is not None:
            raise forms.ValidationError(
                "%s #%s currently has this product." % (self.ref_model._meta.verbose_name, reference)
            )
        if self.instance.group is not None and self.instance.group != ref_obj.group:
            raise forms.ValidationError(
                "Product %s can't added to %s %s." % (self.instance, ref_obj.group, ref_obj._meta.verbose_name)
            )
        return ref_obj
