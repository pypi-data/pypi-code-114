from django.urls import path
from django.conf import settings
from oscar.core.application import OscarConfig


class SyncConfig(OscarConfig):
    name = 'sync'
    label = 'sync'
    namespace = 'sync'
    default_auto_field = 'django.db.models.BigAutoField'

    default_permission = ['is_staff']

    def ready(self):
        from . import signals  # pylint: disable=import-outside-toplevel
        from .views import SiteProductTableView, SiteProductTableAjaxView
        self.site_product_table_view = SiteProductTableView
        self.site_product_table_ajax_view = SiteProductTableAjaxView

    def get_urls(self):
        if getattr(settings, 'SYNC_TABLE_ENABLED', False):
            urls =[
                path(
                    'tabelle/',
                    self.site_product_table_view.as_view(),
                    name='sync-table'
                ),
                path(
                    'tabelle/<slug:slug>/',
                    self.site_product_table_view.as_view(),
                    name='sync-table'
                ),
                path(
                    'tabelle/',
                    self.site_product_table_ajax_view.as_view(),
                    name='sync-table-ajax'
                ),
                path(
                    'tabelle/<int:product_id>/<slug:code>/',
                    self.site_product_table_ajax_view.as_view()
                ),
                path(
                    'tabelle/<int:product_id>/<slug:code>/<slug:action>/',
                    self.site_product_table_ajax_view.as_view()
                ),
            ]
        else:
            urls = []
        return self.post_process_urls(urls)
