from simpel.simpel_products.api.serializers import BaseProductSerializer

from ..models import LaboratoriumService


class LaboratoriumServiceSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = LaboratoriumService
