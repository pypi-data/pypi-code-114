from django.conf.urls import url
from .views import FutureSalesViewset, PastSalesViewset, CurrentSalesViewset

urlpatterns = [
    url(r'^sales/future/', FutureSalesViewset.urls(model_prefix="sale-future")),
    url(r'^sales/past/', PastSalesViewset.urls(model_prefix="sale-past")),
    url(r'^sales/current/', CurrentSalesViewset.urls(model_prefix="sale-current"))
]
