from djangoldp.views import LDPViewSet
from datetime import datetime
from .models import Sale

class FutureSalesViewset(LDPViewSet):
    model = Sale
    def get_queryset(self):
        return super().get_queryset().filter(startDate__gt=datetime.today())

class PastSalesViewset(LDPViewSet):
    model = Sale
    def get_queryset(self):
        return super().get_queryset().filter(endDate__lt=datetime.today())

class CurrentSalesViewset(LDPViewSet):
    model = Sale
    def get_queryset(self):
        return super().get_queryset().filter(endDate__gte=datetime.today()).filter(startDate__lte=datetime.today())

