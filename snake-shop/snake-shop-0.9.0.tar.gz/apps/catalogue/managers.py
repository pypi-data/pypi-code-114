from django.contrib.sites.models import Site
from django.db import models
from django.utils.functional import cached_property
from oscar.apps.catalogue import managers


class SiteProductManager(models.Manager.from_queryset(managers.ProductQuerySet)):
    use_in_migrations = False

    @cached_property
    def site(self):
        return Site.objects.get_current()

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related(
            'product_class',
        )
        qs = qs.prefetch_related(
            'product_options',
            'images',
            'product_class__options',
        )
        return qs

    def browsable(self):
        qs = super().browsable()
        if not self.site.configuration.show_all_products:
            qs = qs.filter(stockrecords__partner__site=self.site)
        return qs.distinct()

    def browsable_dashboard(self):
        qs = super().browsable_dashboard()
        if not self.site.configuration.show_all_products:
            qs = qs.filter(stockrecords__partner__site=self.site)
        return qs.distinct()
