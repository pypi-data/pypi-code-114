from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Category, Product, Unit
from .serializers import CategorySerializer, ProductPolymorphicSerializer, UnitSerializer  # TagSerializer,


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
