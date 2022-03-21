from django.urls import path, include
import gas_drf.sites

from gas_drf.gas import users_drf_config  # noqa, load users api


urlpatterns = [
    path('gas-api/v1/', include(gas_drf.sites.drfsite.urls)),
]
