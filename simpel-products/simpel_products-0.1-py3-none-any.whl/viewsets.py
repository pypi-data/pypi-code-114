from simpel_routers.views import ListView
from simpel_routers.viewsets import ReadOnlyViewSet

from .filters import ProductFilterSet
from .models import Product


class ProductListView(ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(parent=None)


class ProductViewSet(ReadOnlyViewSet):
    model = Product
    filterset_class = ProductFilterSet
    index_view_class = ProductListView

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def index_view(self, request):
        self.request = request
        kwargs = {
            "viewset": self,
            "title": self.get_index_title(),
        }
        view_class = self.index_view_class
        return view_class.as_view(**kwargs)(request)
