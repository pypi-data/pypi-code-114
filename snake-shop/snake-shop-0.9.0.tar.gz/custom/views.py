from decimal import Decimal as D
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.messages import get_messages
from django.conf import settings
from oscar.core.loading import get_model


class HomeView(TemplateView):
    template_name = 'oscar/home.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.hide_price:
            return redirect('catalogue:index')

        context = self.get_context_data(**kwargs)
        if not context['slider_elements'] and not context['products']:
            return redirect('catalogue:index')

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        from apps.wishlists.mixins import WishlistContextMixin
        Product = get_model('catalogue', 'Product')
        RangeProduct = get_model('offer', 'RangeProduct')

        qs = Product.objects.browsable()
        qs = qs.filter(stockrecords__partner__in=self.request.partners)

        ctx = super().get_context_data()
        ctx.update(WishlistContextMixin.from_request(self.request))
        ctx['slider_elements'] = RangeProduct.active_slides.all()

        rp_qs = RangeProduct.active_special_prices.filter(
            product__in=qs)

        qs = qs.filter(rangeproduct__in=rp_qs)

        if not settings.DEBUG:  # shuffle
            qs = qs.order_by('?')

        ctx['products'] = qs[:100]
        return ctx


class ToggleSidebarView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        if 'collapsed_sidebars' not in request.session:
            request.session['collapsed_sidebars'] = {}
        collapsed_sidebars = request.session['collapsed_sidebars']

        sidebar_block = request.GET.get('sidebar-block')

        if sidebar_block in collapsed_sidebars and collapsed_sidebars[sidebar_block]:
            collapsed_sidebars[sidebar_block] = False
        else:
            collapsed_sidebars[sidebar_block] = True
        request.session['collapsed_sidebars'] = collapsed_sidebars
        return JsonResponse(collapsed_sidebars)


class DynamicDataView(View):
    """ This returns various data that can be updated with Jquery ajax """
    def get_context_data(self, request, *args, **kwargs):
        """
        This Context is also loaded from the Page-wide processor and
        from apps.customer.wishlists.views import WishlistToggleProduct
        """
        # TODO: Bad patterns caused by not loaded models during start load
        Line = get_model('wishlists', 'Line')

        context = {}
        basket = request.basket

        try:
            context['basket_value'] = basket.total_incl_tax
        except TypeError:
            context['basket_value'] = D('0.00')

        context['basket_upcs'] = list(
            request.basket.lines.values_list('product__upc', flat=True)
        )
        context['basket_items'] = len(context['basket_upcs'])

        if not request.user.is_authenticated:
            return context

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

        context['wishlist_product_upcs'] = wishlist_product_upcs
        context['wishlist_upcs'] = list(upcs)
        context['wishlist_items'] = len(upcs)
        context['wishlist_count'] = wishlist_count
        context['wishlists'] = wishlists
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        if 'wishlists' in context:
            del context['wishlists']
        return JsonResponse(context)


class MessageAjaxView(TemplateView):
    http_method_names = ['get']
    template_name = 'oscar/partials/alert_message.html'

    def get_context_data(self, request, *args, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context.update({
            'messages': get_messages(request)
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return self.render_to_response(context)
