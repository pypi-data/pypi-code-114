# from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # , status

from simpel.simpel_sales.models import SalesOrder

from .serializers import SalesOrderSerializer

# from rest_framework.decorators import action
# from rest_framework.response import Response


# from drf_spectacular.utils import extend_schema, inline_serializer


class SalesOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SalesOrderSerializer

    def get_queryset(self):
        qs = SalesOrder.objects.all()
        return qs
