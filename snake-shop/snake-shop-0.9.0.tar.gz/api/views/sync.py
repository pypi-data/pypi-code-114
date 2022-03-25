from rest_framework import viewsets, serializers, response, routers
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import sync as sync_serializers

__all__ = ['sync_router', 'VIEWSETS']


class SyncViewSetBase(viewsets.ModelViewSet):
    serializer_class: serializers.ModelSerializer
    sync_by = 'sync_id'
    lookup_field = 'sync_id'
    force_delete = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = self.serializer_class.Meta.fields
        self.model = self.serializer_class.Meta.model
        self.queryset = self.model.objects.all()
        self.name = self.model._meta.model_name
        self.base_name = self.name
        self.list_url = f'sync-api:{self.base_name}-list'
        self.hash_url = f'sync-api:{self.base_name}-hash'
        self.detail_url = f'sync-api:{self.base_name}-detail'

    @action(methods=['get'], list=True, detail=False, url_path='hash')
    def hash(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, hash_only=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, hash_only=True)
        return response.Response(serializer.data)


class TaxSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.TaxSerializer


class CategorySyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.CategorySerializer
    force_delete = True


class ProductSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductSerializer


class ProductAttributeSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductAttributeSerializer


class AttributeOptionSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.AttributeOptionSerializer


class AttributeOptionGroupSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.AttributeOptionGroupSerializer


class ProductCategorySyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductCategorySerializer


class ProductClassSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductClassSerializer


class ProductAttributeValueSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductAttributeValueSerializer


class ProductAttributeValueMultiOptionSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductAttributeValueMultiOptionSerializer
    sync_by = serializer_class.Meta.fields
    lookup_field = 'pk'


class ProductImageSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ProductImageSerializer


class ManufacturerSyncViewSet(SyncViewSetBase):
    serializer_class = sync_serializers.ManufacturerSerializer


VIEWSETS = [
    # ''' ProductClass related: '''
    # productclass:
    ProductClassSyncViewSet,
    # attributeoptiongroup:
    AttributeOptionGroupSyncViewSet,
    # attributeoption:
    AttributeOptionSyncViewSet,
    # productattribute:
    ProductAttributeSyncViewSet,

    # ''' Product related: '''
    # tax:
    TaxSyncViewSet,
    # manufacturer:
    ManufacturerSyncViewSet,
    # product:
    ProductSyncViewSet,
    # productattributevalue:
    ProductAttributeValueSyncViewSet,
    # productattributevalue_value_multi_option:
    ProductAttributeValueMultiOptionSyncViewSet,
    # productimage:
    ProductImageSyncViewSet,

    # ''' Category related: '''
    # category:
    CategorySyncViewSet,
    # productcategory:
    ProductCategorySyncViewSet,
]


sync_router = routers.DefaultRouter()
for viewset_class in VIEWSETS:
    basename = viewset_class().base_name
    sync_router.register(basename, viewset_class, basename=basename)
