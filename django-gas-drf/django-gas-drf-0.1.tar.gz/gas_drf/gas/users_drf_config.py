from gas_drf.sites import drfsite

from .users.api_views import UserViewSet


drfsite.register('users', UserViewSet, basename='gas-user')
