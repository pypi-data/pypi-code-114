from oscar.apps.dashboard.catalogue import forms as base_forms
from apps.partner.models import Partner


class StockRecordForm(base_forms.StockRecordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['partner'].required = False
        self.fields['partner_sku'].required = False

    def save(self, commit=True):
        if not self.instance.partner_id:
            self.instance.partner = Partner.default
        if not self.instance.partner_sku and self.instance.product.upc:
            self.instance.partner_sku = self.instance.product.upc
        return base_forms.StockRecordForm.save(self, commit=commit)

    class Meta(base_forms.StockRecordForm.Meta):
        fields = [
            'partner', 'partner_sku',
            'price_currency', 'price',
            'num_in_stock', 'low_stock_threshold',
        ]


class ProductForm(base_forms.ProductForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.is_parent:
            self.fields.pop('container', None)
            self.fields.pop('container_count', None)
            self.fields.pop('box_deposit', None)

    class Meta(base_forms.ProductForm.Meta):
        fields = [
            'title',
            'upc',
            'manufacturer',
            'description',
            'is_public',
            'is_discountable',
            'structure',
            'slug',
            'meta_title',
            'meta_description',
            'reusability',
            'weight',
            'container_count',
            'volume',
            'deposit',
            'container_count',
            'tax',
            'has_box',
            'priority',
        ]
