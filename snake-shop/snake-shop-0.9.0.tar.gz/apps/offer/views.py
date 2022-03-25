from django.conf import settings
from oscar.apps.offer import views
from apps.catalogue.views import AjaxProductMixin


class OfferListView(views.OfferListView):
    def get_queryset(self):
        qs = super().get_queryset().order_by('-priority', 'pk')
        qs = qs.filter(partner__in=self.request.partners)
        return qs


class OfferDetailView(AjaxProductMixin, views.OfferDetailView):
    paginate_by = settings.OSCAR_PRODUCTS_PER_PAGE_AJAX
