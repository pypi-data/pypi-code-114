"""
Authentication module for django rest framework
"""
from rest_framework.authentication import BaseAuthentication


class SharedKeyAuthentication(BaseAuthentication):
    """
    Shared key authentication
    validates provided token in config
    """
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """

        :param request:
        :return:
        """
        pass
