from django.http import JsonResponse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.expressions import Q
from oscar.apps.customer.wishlists import views
from oscar.core.loading import get_class
from apps.catalogue.models import Product
from apps.wishlists.mixins import WishlistContextMixin
from apps.wishlists.models import Line
from apps.wishlists.forms import WishListControlForm
from custom.views import DynamicDataView

LineFormsetBase = get_class('wishlists.formsets', 'LineFormset')


class LineFormset(LineFormsetBase):
    def __init__(self, *args, request, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs['request'] = self.request
        return kwargs


class DynamicWishListMixin(views.WishListDetailView):
    form_class = LineFormset
    template_name = 'oscar/customer/wishlists/wishlists_lines.html'

    def post(self, request, *args, **kwargs):
        super().post(request)
        return DynamicDataView().get(self.request)

    def get_sort_by(self):
        sort_by = self.request.GET.get('sort_by', False)
        if sort_by:
            self.request.session['wishlist_sort_by'] = sort_by
            return sort_by
        return self.request.session.get('wishlist_sort_by') or 'position'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['control_form'] = WishListControlForm()
        ctx['control_form'].fields['sort_by'].initial = self.get_sort_by()
        ctx['is_sorted'] = self.get_sort_by() != 'position'
        return ctx

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        if self.get_sort_by() != 'position':
            form.queryset = form.queryset.order_by(self.get_sort_by())
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class RealtimeSearchView(DynamicWishListMixin):
    template_name = 'oscar/customer/wishlists/partials/search_realtime.html'

    def search_products(self, search_string):
        if not search_string:
            return Product.objects.none()
        qs = Product.objects.browsable().filter(
            stockrecords__partner__in=self.request.partners)
        upc_qs = qs.filter(
            Q(upc__icontains=search_string)
        )
        if upc_qs.exists():
            return upc_qs
        qs = qs.annotate(
            similarity=TrigramSimilarity('title', search_string)
        )
        return qs.order_by('-similarity')

    def get(self, request, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.search_products(self.request.GET.get('search', ''))
        wishlist_products = Product.objects.filter(
            wishlists_lines__wishlist=self.object)
        qs = qs.exclude(pk__in=wishlist_products)
        ctx['products'] = qs[:25]#
        return render(self.request, self.get_template_names(), context=ctx)

    def get_template_names(self):
        if self.request.method == 'POST':
            return DynamicWishListMixin.template_name
        return self.template_name

    def post(self, request, *args, product, **kwargs):
        product = Product.objects.get(pk=product)
        wishlist_products = Product.objects.filter(
            wishlists_lines__wishlist=self.object)
        if product not in wishlist_products:
            self.object.add(product, as_first=True)
        ctx = self.get_context_data()
        ctx['form'] = self.form_class(
            request=self.request, instance=self.object)
        return render(self.request, self.get_template_names(), context=ctx)


class WishListDetailView(DynamicWishListMixin):
    form_class = LineFormset
    template_name_lines = 'oscar/customer/wishlists/wishlists_lines.html'

    def form_valid(self, form):
        for subform in form:
            if subform.instance:
                subform.save()
        return JsonResponse({})

    def post(self, request, *args, **kwargs):
        reordering_mode = 'order-only' in request.GET
        if not reordering_mode:
            return super().post(request, *args, **kwargs)

        new_ordering = []
        for item in self.request.POST.getlist('item'):
            if int(item) not in new_ordering:
                new_ordering.append(int(item))
        updated_lines = []
        for i, line in enumerate(self.object.lines.all(), 1):
            new_position = new_ordering.index(i) + 1
            if i != new_position:
                line.position = new_position
                updated_lines.append(line)
        Line.objects.bulk_update(updated_lines, ['position'])

        ctx = self.get_context_data()
        ctx['form'] = self.form_class(
            request=self.request, instance=self.object)
        return render(self.request, self.template_name_lines, context=ctx)

    def get_template_names(self):
        if self.request.GET.get('format', None) == 'ajax':
            return DynamicWishListMixin.template_name
        return views.WishListDetailView.template_name


class WishlistToggleProduct(WishlistContextMixin, views.WishListAddProduct):

    def get_dynamic_data_context(self, request, *args, **kwargs):
        return DynamicDataView().get_context_data(request, *args, **kwargs)

    def get_or_create_wishlist(self, request, *args, **kwargs):
        if 'to_key' in kwargs:
            return request.user.wishlists.get(key=kwargs['to_key'])
        return super().get_or_create_wishlist(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_wishlist_context()

        wishlist_upcs = self.wishlist.lines.values_list(
            'product__upc', flat=True
        )
        if self.product.upc in wishlist_upcs:
            self.remove_product()
        else:
            self.add_product()

        if 'wishlists' in context:
            del context['wishlists']

        context = self.get_wishlist_context()
        context.pop('wishlists')
        product_in_wishlist = self.product.upc in context['wishlist_upcs']
        context['product_in_wishlist'] = product_in_wishlist
        return JsonResponse(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def remove_product(self):
        msg = _("'%(title)s' was removed from your '%(name)s' wish list") % {
            'title': self.product.get_title(),
            'name': self.wishlist.name}
        messages.success(self.request, msg)
        self.wishlist.lines.get(product=self.product).delete()
