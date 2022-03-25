from django.contrib.sites.models import Site
from oscar_product_tables.dashboard.views import \
    ProductTableAjaxView, ProductTableView
from oscar_product_tables.plugins import \
    AttachedFieldsPlugin, AttributeFieldsPlugin, PartnerFieldsPlugin
from apps.catalogue.models import Product


class SitePartnerFieldsPlugin(PartnerFieldsPlugin):
    def get_queryset(self):
        site = Site.objects.get_current()
        qs = super().get_queryset().filter(site=site)
        return qs


class SiteTableMixin:
    def get_plugin_classes(self):
        return [
            AttachedFieldsPlugin,
            AttributeFieldsPlugin,
            SitePartnerFieldsPlugin,
        ]

    def get_read_only_plugins(self):
        if hasattr(self, 'request') and self.request.user.is_superuser:
            return []
        return [
            AttachedFieldsPlugin,
            AttributeFieldsPlugin,
        ]

    def get_queryset(self):
        qs = Product.objects.all().order_by('title')
        return qs


class SiteProductTableView(SiteTableMixin, ProductTableView):
    template_name = 'sync/product_table.html'
    template_name_table_page = 'product_tables/table_page.html'
    paginate_by = 500


class SiteProductTableAjaxView(SiteTableMixin, ProductTableAjaxView):
    pass
