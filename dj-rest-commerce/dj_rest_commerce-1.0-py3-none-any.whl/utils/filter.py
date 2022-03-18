import django_filters
from commerce.models.product import Product


# Product Filter
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['price', 'is_available']
