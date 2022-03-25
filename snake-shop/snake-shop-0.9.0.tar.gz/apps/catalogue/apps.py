from django.urls import include, path, re_path
from django.conf import settings
import oscar.apps.catalogue.apps as apps
from oscar.core.loading import get_class


class CatalogueConfig(apps.CatalogueConfig):
    name = 'apps.catalogue'

    def get_urls(self):
        urls = [
            path('', self.catalogue_view.as_view(), name='index'),
            re_path(
                r'^(?P<product_slug>[\w-]*)_(?P<upc>\d+)/$',
                self.detail_view.as_view(),
                name='detail',
            ),
            re_path(
                r'^kategorie/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                self.category_view.as_view(),
                name='category',
            ),
            re_path(
                r'^kategorie/(?P<category_slug>[\w-]+(/[\w-]+)*)/$',
                self.category_view.as_view(),
                name='category',
            ),
            path(
                'ranges/<slug:slug>/',
                self.range_view.as_view(),
                name='range'
            ),
            re_path(
                r'^(?P<product_slug>[\w-]*)_(?P<product_pk>\d+)/rezensionen/',
                include(self.reviews_app.urls[0])
            ),
        ]
        return self.post_process_urls(urls)
