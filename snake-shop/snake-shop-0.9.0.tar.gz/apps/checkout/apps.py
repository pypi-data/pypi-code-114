from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class
import oscar.apps.checkout.apps as apps


class CheckoutConfig(apps.CheckoutConfig):
    name = 'apps.checkout'

    def get_urls(self):
        urls = [
            path('', self.index_view.as_view(), name='index'),

            # Shipping/user address views
            path('lieferanschrift/', self.shipping_address_view.as_view(), name='shipping-address'),
            path('adresse/edit/<int:pk>/', self.user_address_update_view.as_view(), name='user-address-update'),
            path('adresse/delete/<int:pk>/', self.user_address_delete_view.as_view(), name='user-address-delete'),

            # Shipping method views
            path('versandmethode/', self.shipping_method_view.as_view(), name='shipping-method'),

            # Payment views
            path('bezahlung/', self.payment_method_view.as_view(), name='payment-method'),
            path('details/', self.payment_details_view.as_view(), name='payment-details'),

            # Preview and thankyou
            path('vorschau/', self.payment_details_view.as_view(preview=True), name='preview'),
            path('vielen-dank/', self.thankyou_view.as_view(), name='thank-you'),
        ]
        return self.post_process_urls(urls)
