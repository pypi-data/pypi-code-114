from django.contrib.auth.models import User
from rest_framework import viewsets

from gas_drf.mixins import GASAuthMixin

from .serializers import UserSerializer


class UserViewSet(GASAuthMixin, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
