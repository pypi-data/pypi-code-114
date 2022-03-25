from oscar.core.application import OscarConfig
from oscar.core.loading import get_class
from django.urls.conf import path
from django.utils.translation import gettext_lazy as _


class DeliveryConfig(OscarConfig):
    name = 'delivery'
    namespace = 'delivery'

    def ready(self):
        super().ready()
        self.delivery_times_form = get_class(
            'delivery.views', 'DeliveryTimesFormView'
        )

    def get_urls(self):
        urls = super().get_urls()
        urls = [
            path(
                '',
                self.delivery_times_form.as_view(),
                name='delivery-times-form'
            ),
        ]
        return self.post_process_urls(urls)
