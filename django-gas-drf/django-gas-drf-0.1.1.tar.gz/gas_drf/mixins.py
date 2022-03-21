from rest_framework.authentication import SessionAuthentication

from .permissions import HasValidRole


class GASAuthMixin:
    authentication_classes = [SessionAuthentication]
    permission_classes = [HasValidRole]
    base_role = 'admins'
    roles = set()
