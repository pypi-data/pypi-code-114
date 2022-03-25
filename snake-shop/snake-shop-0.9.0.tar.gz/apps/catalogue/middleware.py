from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from .models import Product


class CatalogueMiddleware(MiddlewareMixin):
    def process_request(self, request):
        is_productive = settings.STAGE == 'PRODUCTIVE'
        if is_productive and request.site.domain != request.get_host():
            raise AttributeError(
                'Wrong site (%s) for this url(%s)!!!' % (
                    request.site.domain, request.get_host()
                )
            )

        def load_products():
            qs = Product.objects.browsable()
            qs = qs.filter(stockrecords__partner__in=request.partners)
            return qs

        request.products = SimpleLazyObject(load_products)
