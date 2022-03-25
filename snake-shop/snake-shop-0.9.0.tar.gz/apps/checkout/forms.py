from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.exceptions import ValidationError

from oscar.core.loading import get_model
from oscar.apps.checkout import forms as checkout_forms
from oscar.forms import widgets
from oscar.core.utils import datetime_combine

from apps.address import forms as address_forms
from apps.address import models as address_models
from delivery.models import Postcode, Delivery


class SingleShippingMethodForm(forms.Form):
    deliveries = forms.ChoiceField(label=_('Delivery Time'))
    floor_number = forms.ChoiceField(label=_("Choose Floor"),)
    delivery_date = forms.DateField(widget=widgets.DatePickerInput(),)
    delivery_time = forms.TimeField(
        widget=widgets.TimePickerInput(format='%H:%M'),)

    def __init__(self, method, request, shipping_addr, *args, **kwargs):
        self.method = method
        self.request = request
        self.address = shipping_addr

        if request.method == 'POST':
            super().__init__(request.POST, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)

        selected_fields = self.select_fields()
        delete_fields = []
        for fieldname, _ in self.fields.items():
            if fieldname not in selected_fields:
                delete_fields.append(fieldname)
        for fieldname in delete_fields:
            del self.fields[fieldname]

        if 'floor_number' in self.fields and self.method.get_track_floor():
            self.fields['floor_number'].choices += self.get_floor_choices()
            self.fields['floor_number'].initial = self.get_floor_initial()
        if 'deliveries' in self.fields:
            self.next_deliveries = self.get_next_deliveries()\
                if self.address else []
            self.fields['deliveries'].choices = self.get_delivery_choices()
        if 'delivery_date' in self.fields:
            self.fields['delivery_date'].widget.attrs.update({
                'id': 'delivery_date_' + self.method.code,
                'min': self.method.earliest_delivery_date,
            })
        if 'delivery_time' in self.fields:
            self.fields['delivery_time'].widget.attrs['id'] = \
                'delivery_time_' + self.method.code

    def get_result(self):
        '''
        2, 3: Delivery.from_id
        '''
        mode = self.method.form_fields
        if mode in (2, 3):
            delivery = self.clean_deliveries()
        elif mode == 4:
            delivery = self.clean_delivery_date()
        elif mode == 5:
            delivery = self.clean_delivery_time()
        else:
            delivery = None
        return delivery

    @property
    def is_allowed(self):
        return not bool(self.disallowed_reason)

    @property
    def disallowed_reason(self):
        if self.method.postcode_restricted and not self.get_next_deliveries():
            return _('No delivery for %(postcode)s') % {
                'postcode': self.address.postcode
            }

        hide_price = self.request.user.hide_price
        minimum_order_value = self.method.minimum_order_value
        if not hide_price and minimum_order_value > self.get_basket_total():
            return _('Minimum order value is %(min)s') % {
                    'min': self.method.minimum_order_value,
                }

    @property
    def hint(self):
        max_floor_dif = self.method.maximum_floor_difference
        floor_dif = self.method.get_floor_difference(self.address.floor_number)
        if floor_dif and max_floor_dif and floor_dif > max_floor_dif:
            return _('We do not deliver more than %(max_floor)s floors') % {
                'max_floor': max_floor_dif,
            }

    def clean_deliveries(self, delivery=None):
        if delivery is None:
            delivery = Delivery.from_id(
                self.data['deliveries'], self.request.site)

        if not delivery.is_selectable:
            raise ValidationError(_({
                'deliveries': 'Lieferung zum Folgetag ist nur bis 14Uhr '
                'auswählbar. Bitte wählen Sie einen anderen Lieferzeitpunkt.'
            }))
        return delivery

    def clean_delivery_date(self, delivery=None):
        if delivery is None:
            delivery_date = self.fields['delivery_date'].clean(
                self.data['delivery_date']
            )
            delivery = Delivery.objects.get_or_create(
                date=delivery_date,
                target_time=None,
                time=None,
            )[0]

        if not delivery.is_selectable:
            raise ValidationError(_('Can\'t deliver into the past'))
        return delivery

    def clean_delivery_time(self, delivery=None):
        if delivery is None:
            delivery_date = self.fields['delivery_date'].clean(
                self.data['delivery_date'])
            delivery_time = self.fields['delivery_time'].clean(
                self.data['delivery_time'])
            delivery_datetime = datetime_combine(delivery_date, delivery_time)

            earliest = self.method.earliest_delivery_date
            if earliest and delivery_datetime < earliest:
                raise ValidationError(
                    _('Earliest delivery date is: %(earliest_date)s'),
                    params={'earliest_date': earliest.strftime('%A, %-d.%-m.')},
                    code='too_early',
                )

            delivery = Delivery.objects.get_or_create(
                site=self.request.site,
                date=delivery_datetime,
                target_time=delivery_datetime.time(),
                time=None,
            )[0]
        if not delivery.is_selectable:
            raise ValidationError(_('Can\'t deliver into the past'))
        return delivery

    def select_fields(self):
        method = self.method
        result = {
            0: [],
            1: ['floor_number'],
            2: ['deliveries'],
            3: ['floor_number', 'deliveries'],
            4: ['delivery_date'],
            5: ['delivery_date', 'delivery_time'],
        }[method.form_fields]
        return result

    def get_floor_initial(self):
        addr_floor = self.address.floor_number
        if addr_floor is None:
            return None

        numbers = self.method.get_floor_range()
        if not numbers:
            initial = addr_floor
        elif addr_floor in numbers:
            initial = addr_floor
        elif addr_floor > 0:
            initial = max(numbers)
        elif addr_floor < 0:
            initial = min(numbers)
        else:
            initial = None
        return initial

    def code(self):
        return self.method.code

    def description(self):
        return self.method.description

    def calculate(self, *args, **kwargs):
        return self.method.calculate(*args, **kwargs)

    def get_basket_total(self):
        basket = self.request.basket
        return basket.total.incl - basket.deposit.incl

    def get_floor_choices(self):
        choices = self.method.get_number_choices(self.request.basket)
        return (('', _('Choose Floor')), *choices)

    def get_delivery_choices(self):
        choices = [(x.to_id(), x) for x in self.next_deliveries]
        return [('', _('Choose Delivery Time')), *choices]

    def get_postcode_object(self):
        try:
            return Postcode.objects.get(postcode=self.address.postcode)
        except Postcode.DoesNotExist:
            return Postcode(postcode=self.address.postcode)

    def get_tours(self):
        postcode = self.get_postcode_object()
        if postcode.pk:
            return postcode.tour_set.filter(site=self.request.site)
        return []

    def get_next_deliveries(self):
        deliveries = []
        tours = self.get_tours()
        if self.address and tours:
            for tour in self.get_tours():
                deliveries += tour.next_deliveries(num=20)
        return deliveries


class OrderNoteForm(forms.Form):
    note = forms.CharField(
        label=_('Instructions'),
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )
    pre = '/de' if settings.URL_PREFIX_DEFAULT_LANGUAGE else ''

    withdrawal_declaration_accepted = forms.BooleanField(
        label=mark_safe(f'<a href="{pre}/agb/">Allgemeine Geschäftsbedingungen</a> akzeptiert'),
        required=True,
    )
    conditions_accepted = forms.BooleanField(
        label=mark_safe(f'<a href="{pre}/widerrufsrecht/">Widerrufsbelehrung</a> anerkannt'),
        required=True,
    )
    newsletter_accepted = forms.BooleanField(
        label='Newsletter abonnieren',
        required=False,
    )

    def __init__(self, checkout_session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = checkout_session.request.user
        if user.hide_price:
            del self.fields['withdrawal_declaration_accepted']
            del self.fields['conditions_accepted']
            del self.fields['newsletter_accepted']
        elif user.newsletter_accepted:
            del self.fields['newsletter_accepted']

        self.address = address_models.UserAddress.objects.get(
            pk=checkout_session.shipping_user_address_id()
        )
        if self.address.notes:
            self.fields['note'].initial = self.address.notes


class ShippingAddressForm(checkout_forms.ShippingAddressForm):
    class Meta:
        model = get_model('order', 'shippingaddress')
        fields = address_forms.UserAddressForm.Meta.fields


class AddressSelectorForm(forms.Form):
    shipping_address = forms.ChoiceField(
        label=_('Shipping address'),
        widget=forms.RadioSelect,
    )
    billing_address = forms.ChoiceField(
        label=_('Billing address') + ' (optional)',
        widget=forms.RadioSelect,
        required=True,
    )

    def __init__(self, user, addresses, *args, **kwargs):
        self.user = user
        self.addresses = addresses
        super().__init__(*args, **kwargs)
        self.fields['shipping_address'].choices = [
            (address.pk, str(address)) for address in addresses
        ]
        if user.hide_price:
            self.fields['billing_address'].choices = [(-1, 'Wie hinterlegt')]
        else:
            self.fields['billing_address'].choices = [
                (-1, 'Selbe wie Lieferadresse'),
                *[(address.pk, str(address)) for address in addresses],
            ]
        self.fields['shipping_address'].widget.attrs.update(
            {'style': 'list-style-type:none;padding-left:0;'}
        )

    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            shipping_address = address_models.UserAddress.objects.get(
                pk=self.cleaned_data['shipping_address']
            )
            self.set_shipping_address(shipping_address)
            if int(self.cleaned_data['billing_address']) > 0:
                billing_address = address_models.UserAddress.objects.get(
                    pk=self.cleaned_data['billing_address']
                )
            else:
                billing_address = self.cleaned_data['billing_address']
            self.set_billing_address(billing_address)
        return is_valid

    def get_initial_for_field(self, field, field_name):
        if field_name == 'billing_address':
            return -1 if self.user.hide_price \
                else self.get_default_billing_address()
        if field_name == 'shipping_address':
            return self.get_default_shipping_address()
        return super().get_initial_for_field(field, field_name)

    def set_shipping_address(self, address):
        for addr in self.addresses:
            if addr == address:
                addr.is_default_for_shipping = True
            else:
                addr.is_default_for_shipping = False
            addr.save()

    def set_billing_address(self, address):
        for addr in self.addresses:
            if addr == address:
                addr.is_default_for_billing = True
            else:
                addr.is_default_for_billing = False
            addr.save()

    def get_default_shipping_address(self):
        for address in self.addresses:
            if address.is_default_for_shipping:
                return address.pk

    def get_default_billing_address(self):
        for address in self.addresses:
            if address.is_default_for_billing:
                return address.pk
        return -1
