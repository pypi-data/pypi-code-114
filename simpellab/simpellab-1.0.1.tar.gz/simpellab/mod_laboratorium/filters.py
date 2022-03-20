from django_filters import filters
from django_filters.filterset import FilterSet

from .models import Parameter


class ParameterFilterSet(FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    code = filters.CharFilter(field_name="code", lookup_expr="icontains")

    class Meta:
        model = Parameter
        fields = ("name", "code")
