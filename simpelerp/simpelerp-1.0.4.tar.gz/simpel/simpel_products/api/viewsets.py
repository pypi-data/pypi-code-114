from rest_framework.viewsets import ReadOnlyModelViewSet

from simpel.simpel_products.api.serializers import (  # TagSerializer,
    CategorySerializer,
    ProductPolymorphicSerializer,
    UnitSerializer,
)
from simpel.simpel_products.models import Category, Product, Unit


class UnitViewSet(ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class TagViewSet(ReadOnlyModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductPolymorphicSerializer
