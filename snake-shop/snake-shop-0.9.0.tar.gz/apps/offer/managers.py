from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from django.contrib.sites.models import Site

from oscar.apps.offer import managers as offer_managers
from custom.site_manager import BaseSiteManager


class RangeSiteManager(BaseSiteManager, offer_managers.RangeManager):
    pass


class BrowsableRangeSiteManager(BaseSiteManager, offer_managers.BrowsableRangeManager):
    pass


class ActiveOfferManager(offer_managers.ActiveOfferManager):
    def get_queryset(self):
        site = Site.objects.get_current()
        qs = super().get_queryset()
        qs = qs.filter(partner__site=site)
        return qs


class ActiveRangeProductsMixin(models.Manager):
    def get_active_range_products(self):
        cutoff = now()
        qs = super().get_queryset()
        qs = qs.filter(  # Offer is active
            Q(range__benefit__offers__end_datetime__gte=cutoff)
            | Q(range__benefit__offers__end_datetime=None),
            Q(range__benefit__offers__start_datetime__lte=cutoff)
            | Q(range__benefit__offers__start_datetime=None),
            range__benefit__offers__status='Open',
        )
        qs = qs.filter(  # Special price is active
            Q(special_price_end__gte=cutoff) | Q(special_price_end=None),
            Q(special_price_start__lte=cutoff) | Q(special_price_start=None),
        )
        return qs


class ActiveSpecialPriceManager(ActiveRangeProductsMixin):
    def get_queryset(self):
        qs = self.get_active_range_products()
        qs = qs.filter(
            special_price__isnull=False,
            product__isnull=False,
        )
        qs = qs.order_by('product_id', '-range__benefit__offers__priority')
        qs = qs.distinct('product_id')
        return super().get_queryset().filter(id__in=qs)


class ActiveSlideManager(ActiveRangeProductsMixin):
    def get_queryset(self):
        rp_qs = self.get_active_range_products()
        rp_qs = rp_qs.filter(
            image__isnull=False,
        )
        qs = super().get_queryset()
        qs = qs.filter(id__in=rp_qs)
        qs = qs.order_by('-display_order')
        qs = qs.select_related('image', 'image__file_ptr', 'product')
        return qs
