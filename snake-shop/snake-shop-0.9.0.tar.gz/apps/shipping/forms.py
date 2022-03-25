from django import forms
from django.utils.translation import gettext as _

from delivery.models import Postcode


class ShippingMethodForm(forms.Form):
    deliveries = forms.ChoiceField(label=_('Delivery Time'))
    floor_number = forms.ChoiceField(
        label=_("Choose Floor"),
    )

    def __init__(self, method, request, shipping_addr, *args, **kwargs):
        self.method = method
        self.address = shipping_addr

        if request.method == 'POST':
            super().__init__(request.POST, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)

        self.next_deliveries = self.get_next_deliveries()\
            if self.address else []
        self.fields['floor_number'].choices += self.get_floor_choices()
        self.fields['deliveries'].choices = self.get_delivery_choices()

    def get_floor_choices(self):
        return (('', _('Choose Floor')), *self.method.get_number_choices())

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
            return postcode.tour_set.all()
        return []

    def get_next_deliveries(self):
        deliveries = []
        tours = self.get_tours()
        if self.address and tours:
            for tour in self.get_tours():
                deliveries += tour.next_deliveries(num=20)
        return deliveries

    def save(self):
        pass
