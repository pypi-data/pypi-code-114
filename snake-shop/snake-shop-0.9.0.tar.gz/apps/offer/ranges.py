from django.utils.functional import cached_property
from oscar.core.loading import get_model
from crum import get_current_request
from apps.offer.models import RangeProduct

Product = get_model('catalogue', 'Product')


class BoxProducts:
    name = "Kistenprodukte"

    def get_all_product_ids(self):
        request = get_current_request()
        qs = request.products
        qs = qs .filter(has_box=True)
        qs = qs.exclude(
            rangeproduct__in=RangeProduct.active_special_prices.all()
        )
        return qs.values_list('id', flat=True)

    @cached_property
    def all_product_ids(self):
        return list(self.get_all_product_ids())

    def contains_product(self, product):
        return product.id in self.all_product_ids

    def num_products(self):
        return len(self.all_product_ids)

    def all_products(self):
        return Product.objects.filter(id__in=self.all_product_ids)
