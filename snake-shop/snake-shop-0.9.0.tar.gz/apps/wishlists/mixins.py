from apps.wishlists.models import Line


class WishlistContextMixin:
    @staticmethod
    def from_request(request):
        ctx = {}
        if not request.user.is_authenticated:
            return ctx
        wishlist_product_upcs = {}
        upcs = []
        wishlist_count = 0

        wishlists = request.user.wishlists.all()
        keys = wishlists.values_list('key', flat=True)
        for key in keys:
            wishlist_product_upcs[key] = []
            wishlist_count += 1

        qs = Line.objects.filter(wishlist__in=wishlists)
        values = qs.values_list('wishlist__key', 'product__upc')
        for key, upc in values:
            wishlist_product_upcs[key].append(upc)
            upcs.append(upc)

        ctx['wishlist_upcs'] = list(upcs)
        ctx['wishlists'] = wishlists
        for wishlist in ctx['wishlists']:
            setattr(wishlist, 'upcs', wishlist_product_upcs[wishlist.key])
        return ctx

    def get_wishlist_context(self):
        assert self.request
        return self.from_request(self.request)
