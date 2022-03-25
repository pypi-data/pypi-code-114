from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage
from oscar.apps.catalogue import views
from oscar.core.loading import get_model
from oscar_pg_search.mixins import SearchViewMixin
from apps.wishlists.mixins import WishlistContextMixin

Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'category')


class AjaxProductMixin(WishlistContextMixin):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx.update(self.get_wishlist_context())
        if 'page' in self.request.GET \
                and self.request.GET.get('format') == 'ajax':
            self.template_name = \
                'oscar/catalogue/partials/browse_products.html'
        elif self.request.GET.get('format') == 'sidebar':
            self.template_name = \
                'oscar/catalogue/partials/browse_sidebar_ajax.html'
        if 'object_list' in ctx:  # Only at first page load
            ctx['num_products'] = len(
                ctx['object_list'].values_list('id', flat=True)
            )
        if ctx.get('is_paginated'):
            try:
                ctx['next_page'] = ctx['page_obj'].next_page_number()
            except EmptyPage:
                pass
        return ctx


class CatalogueView(AjaxProductMixin, SearchViewMixin,
                    views.CatalogueView):
    pass


class ProductCategoryView(AjaxProductMixin, SearchViewMixin,
                          views.ProductCategoryView):
    def get_category(self):
        return get_object_or_404(
            Category, slug=self.kwargs['category_slug'].split('/')[-1]
        )


class ProductDetailView(AjaxProductMixin, views.ProductDetailView):
    def get_object(self, queryset=None):
        if hasattr(self, 'object'):
            return self.object
        else:
            return get_object_or_404(
                Product, slug=self.kwargs['product_slug'], upc=self.kwargs['upc']
            )
