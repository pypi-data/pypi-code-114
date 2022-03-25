from django.urls import path
import oscar.apps.offer.apps as apps


class OfferConfig(apps.OfferConfig):
    name = 'apps.offer'

    def get_urls(self):
        urls = [
            path('', self.list_view.as_view(), name='list'),
            path('<slug:slug>/', self.detail_view.as_view(), name='detail'),
        ]
        return self.post_process_urls(urls)
