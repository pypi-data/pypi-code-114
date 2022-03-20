from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import LaboratoriumService
from .serializers import LaboratoriumServiceSerializer


class LaboratoriumServiceViewSet(ReadOnlyModelViewSet):
    queryset = LaboratoriumService.objects.all()
    serializer_class = LaboratoriumServiceSerializer
