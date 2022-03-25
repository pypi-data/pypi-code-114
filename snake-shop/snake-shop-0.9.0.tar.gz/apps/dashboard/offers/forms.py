import datetime
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.contrib.sites.models import Site
from oscar.forms.widgets import DateTimePickerInput
from oscar.apps.dashboard.offers import forms as offers_forms
from apps.offer.models import RangeProduct
from apps.catalogue.models import Product
from apps.offer.utils import InkscapeConverter


class MetaDataForm(offers_forms.MetaDataForm):

    def get_initial_for_field(self, field, field_name):
        if field_name == 'partner':
            site = Site.objects.get_current()
            return site.partner_set.last()
        return forms.ModelForm.get_initial_for_field(self, field, field_name)

    class Meta(offers_forms.MetaDataForm.Meta):
        fields = ('partner', 'name', 'description', 'offer_type')


class RestrictionsForm(offers_forms.RestrictionsForm):
    def clean(self):
        try:
            return super().clean()
        except KeyError as err:
            raise ValidationError(err) from err


class OfferRangeProductForm(forms.ModelForm):
    preview_loading_fields = ('product', 'special_price', 'image', 'top',
                              'left', 'title', 'sub_title', 'main_title')

    def __init__(self, range, *args, **kwargs):  # @ReservedAssignment
        self.range = range
        super().__init__(*args, **kwargs)
        self.instance.range = range
        self.fields['special_price_start'].widget = DateTimePickerInput()
        self.fields['special_price_end'].widget = DateTimePickerInput()
        today = datetime.date.today()
        self.fields['special_price_start'].initial = today
        self.fields['product'].choices = self.build_product_choices()
        for fieldname, field in self.fields.items():
            if fieldname in self.preview_loading_fields:
                field.widget.attrs['class'] = 'preview-trigger'

    def build_product_choices(self):
        yield '', '---------'
        qs = Product.objects.filter(is_public=True)
        qs = qs.filter(stockrecords__partner__site=self.range.site)
        for product in qs:
            yield product.id, f'{product.title} ({product.upc})'

    def clean(self):
        cleaned_data = forms.ModelForm.clean(self)
        start = cleaned_data['special_price_start']
        end = cleaned_data['special_price_end']
        if start and end and end < start:
            raise forms.ValidationError(_(
                "The end date must be after the start date"))
        if not cleaned_data.get('product') and not cleaned_data.get('image'):
            raise forms.ValidationError(
                _('Either a product or an image is needed.'),
                code='needed_fields',
            )
        range_product = self.instance

        if not self.validate_product_and_range_unique():
            raise forms.ValidationError(
                '{} exists already in {}'.format(
                    range_product.product,
                    range_product.range,
                )
            )
        return cleaned_data

    def validate_product_and_range_unique(self):
        range_product = self.instance
        if range_product.id:  # It is an update
            return True
        if not range_product.product:  # It is a pure slider element
            return True
        if not RangeProduct.objects.filter(
                    range=self.range, product=range_product.product):
            return True  # It is unique
        return False

    def save(self, commit=True):
        if self.instance.image:
            converter = InkscapeConverter(self.instance, 'png')
            image_file = ImageFile(converter.file, converter.filename)
            self.instance.cached_slide = image_file
        return forms.ModelForm.save(self, commit=commit)

    class Meta:
        model = RangeProduct
        fields = (
            'display_order',
            'product',
            'special_price',
            'image',
            'link',
            'top',
            'left',
            'main_title',
            'title',
            'sub_title',
            'special_price_start',
            'special_price_end',
        )

    class Media:
        extend = False
        css = {
            'all': [
                'filer/css/admin_filer.css',
            ]
        }
        js = (
            'admin/js/core.js',
            'admin/js/vendor/jquery/jquery.min.js',
            'admin/js/jquery.init.js',
            'admin/js/admin/RelatedObjectLookups.js',
            'admin/js/actions.js',
            'admin/js/urlify.js',
            'admin/js/prepopulate.js',
            'filer/js/libs/dropzone.min.js',
            'filer/js/addons/dropzone.init.js',
            'filer/js/addons/popup_handling.js',
            'filer/js/addons/widget.js',
        )
