from django.urls import path
from oscar.apps.dashboard.offers import apps
from oscar.core.loading import get_class


class OffersDashboardConfig(apps.OffersDashboardConfig):
    name = 'apps.dashboard.offers'

    def ready(self):
        apps.OffersDashboardConfig.ready(self)
        self.product_offer_list_view = get_class(
            'dashboard.offers.views', 'OfferRangeProductListView')
        self.product_offer_detail_view = get_class(
            'dashboard.offers.views', 'OfferRangeProductUpdateView')
        self.product_offer_create_view = get_class(
            'dashboard.offers.views', 'OfferRangeProductCreateView')
        self.product_offer_update_view = get_class(
            'dashboard.offers.views', 'OfferRangeProductUpdateView')
        self.product_offer_delete_view = get_class(
            'dashboard.offers.views', 'OfferRangeProductDeleteView')
        self.slide_view = get_class(
            'dashboard.offers.views', 'SlideView')
        self.slide_preview = get_class(
            'dashboard.offers.views', 'SlideViewPreview')
        self.zipped_slides_view = get_class(
            'dashboard.offers.views', 'ZippedSlidesView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path(
                '<int:offer_pk>/product-offers/',
                self.product_offer_list_view.as_view(),
                name='product-offer-list'
            ),
            path(
                '<int:offer_pk>/product-offer/create',
                self.product_offer_create_view.as_view(),
                name='product-offer-create'
            ),
            path(
                '<int:offer_pk>/product-offer/<int:pk>/',
                self.product_offer_update_view.as_view(),
                name='product-offer-detail'
            ),
            path(
                '<int:offer_pk>/product-offer/<int:pk>/update/',
                self.product_offer_update_view.as_view(),
                name='product-offer-update'
            ),
            path(
                '<int:offer_pk>/product-offer/<int:pk>/delete/',
                self.product_offer_delete_view.as_view(),
                name='product-offer-delete'
            ),
            path(
                '<int:range_pk>/slide/preview/',
                self.slide_preview.as_view(),
                name='slide-preview',
            ),
            path(
                'slide/<int:range_product_pk>/<slug:suffix>/',
                self.slide_view.as_view(),
                name='slide',
            ),
            path(
                '<int:offer_pk>/slides.zip',
                self.zipped_slides_view.as_view(),
                name='slide-zipped',
            ),
        ]
        return self.post_process_urls(urls)
