from hashlib import md5
from rest_framework import serializers
from rest_framework.fields import BooleanField
from drf_extra_fields.fields import Base64ImageField, Base64FileField
from apps.catalogue import models

__all__ = ['TaxSerializer', 'CategorySerializer', 'ProductSerializer',
           'ProductAttributeSerializer', 'AttributeOptionSerializer',
           'AttributeOptionGroupSerializer', 'ProductCategorySerializer',
           'ProductClassSerializer', 'ProductAttributeValueSerializer',
           'ProductImageSerializer', 'ManufacturerSerializer',
           'ProductAttributeValueMultiOptionSerializer']


class CustomImageField(Base64ImageField):
    ALLOWED_TYPES = [*Base64ImageField.ALLOWED_TYPES, 'webp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, represent_in_base64=True, **kwargs)


class CustomFileField(Base64FileField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, represent_in_base64=True, **kwargs)


class CustomBaseSerializer(serializers.ModelSerializer):
    hash = serializers.SerializerMethodField()
    url_field_needed = False

    def __init__(self, *args, hash_only=False, **kwargs):
        self.hash_only = hash_only
        super().__init__(*args, **kwargs)

    def get_hash(self, obj):
        values = []
        for field_name, field in super().get_fields().items():
            if not field.read_only:
                is_foreign_object = isinstance(
                    getattr(obj, field_name), models.models.Model)
                value = getattr(obj, field_name)
                if is_foreign_object:
                    value = getattr(value, 'sync_id', None)
                else:
                    value = field.to_representation(value) if value is not None\
                        else None
                values.append(str(value).strip())
        return md5(','.join(values).encode()).hexdigest()

    def get_fields(self):
        serializer_fields = super().get_fields()
        allowed_fields = serializer_fields.keys()
        if self.hash_only:
            allowed_fields = ['sync_id', 'hash']
            if self.url_field_needed:
                allowed_fields = ['sync_url', *allowed_fields]

        for field in serializer_fields:
            if field.__class__ == BooleanField and not field.required:
                field.default = None
        for field_name in [x for x in serializer_fields.keys()
                           if x not in allowed_fields]:
            serializer_fields.pop(field_name)
        return serializer_fields


class CustomModelSerializerBase(CustomBaseSerializer):
    #sync_id = serializers.UUIDField(read_only=False)
    """ Base class for models that DON'T have sync_id """
    url_field_needed = True
    sync_id = serializers.SerializerMethodField()

    def get_sync_id(self, obj):
        return str(self.get_hash(obj))


class CustomHyperlinkedModelSerializerBase(CustomBaseSerializer,
                                           serializers.HyperlinkedModelSerializer):
    """ Base class for models that have sync_id """


# ProductClass related:
class ProductClassSerializer(CustomHyperlinkedModelSerializerBase):
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:productclass-detail',
        lookup_field='sync_id',
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.ProductClass
        fields = ['sync_url', 'sync_id', 'hash', 'slug', 'name',
                  'requires_shipping', 'track_stock']
        extra_kwargs={'sync_id':{'read_only': False}}


class AttributeOptionGroupSerializer(CustomHyperlinkedModelSerializerBase):
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:attributeoptiongroup-detail',
        lookup_field='sync_id',
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.AttributeOptionGroup
        fields = ['sync_url', 'sync_id', 'hash', 'name']
        extra_kwargs={'sync_id':{'read_only': False}}


class AttributeOptionSerializer(CustomHyperlinkedModelSerializerBase):
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:attributeoption-detail',
        lookup_field='sync_id',
    )
    group = serializers.HyperlinkedRelatedField(
        view_name='sync-api:attributeoptiongroup-detail',
        queryset=models.AttributeOptionGroup.objects,
        lookup_field="sync_id",
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.AttributeOption
        fields = ['sync_url', 'sync_id', 'hash', 'option', 'group']
        extra_kwargs={'sync_id':{'read_only': False}}


class ProductAttributeSerializer(CustomHyperlinkedModelSerializerBase):
    # Needs: product_class, option_group
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:productattribute-detail',
        lookup_field='sync_id',
    )
    product_class = serializers.HyperlinkedRelatedField(
        view_name='sync-api:productclass-detail',
        queryset=models.ProductClass.objects,
        lookup_field="sync_id",
    )
    option_group = serializers.HyperlinkedRelatedField(
        view_name='sync-api:attributeoptiongroup-detail',
        queryset=models.AttributeOptionGroup.objects,
        lookup_field="sync_id",
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.ProductAttribute
        fields = ['sync_url', 'sync_id', 'hash', 'code', 'name', 'type',
                  'required', 'product_class', 'option_group',]
        extra_kwargs={'sync_id':{'read_only': False}}


# Product related:
class TaxSerializer(CustomHyperlinkedModelSerializerBase):
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:tax-detail',
        lookup_field='sync_id',
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.Tax
        fields = ['sync_url', 'sync_id', 'hash', 'name', 'rate']
        extra_kwargs={'sync_id':{'read_only': False}}


class ManufacturerSerializer(CustomHyperlinkedModelSerializerBase):
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:manufacturer-detail',
        lookup_field='sync_id',
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.Manufacturer
        fields = ['sync_url', 'sync_id', 'hash', 'name', 'address', 'url',
                  'hash']
        extra_kwargs={'sync_id':{'read_only': False}}


class ProductSerializer(CustomHyperlinkedModelSerializerBase):
    # Needs: product_class, tax
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:product-detail',
        lookup_field='sync_id',
    )
    product_class = serializers.HyperlinkedRelatedField(
        view_name='sync-api:productclass-detail',
        queryset=models.ProductClass.objects,
        lookup_field="sync_id",
    )
    tax = serializers.HyperlinkedRelatedField(
        view_name='sync-api:tax-detail',
        queryset=models.Tax.objects,
        lookup_field="sync_id",
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.Product
        fields = ['sync_url', 'sync_id', 'hash', 'title','upc', 
                  'container_count', 'deposit', 'weight', 'volume', 'has_box',
                  'slug', 'description', 'meta_title', 'meta_description',
                  'is_discountable', 'tax', 'product_class',]
        extra_kwargs={'sync_id':{'read_only': False}}


class ProductAttributeValueMultiOptionSerializer(CustomModelSerializerBase):
    # NO SYNC ID - Needs: attribute, product, value_option
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:productattributevalue_value_multi_option-detail',
        lookup_field='pk',
    )
    sync_id = serializers.SerializerMethodField()
    productattributevalue = serializers.HyperlinkedRelatedField(
        view_name='sync-api:productattributevalue-detail',
        queryset=models.ProductAttributeValue.objects,
        lookup_field="sync_id",
    )
    attributeoption = serializers.HyperlinkedRelatedField(
        view_name='sync-api:attributeoption-detail',
        queryset=models.AttributeOption.objects,
        lookup_field="sync_id",
    )
    class Meta:
        lookup_field='pk'
        model = models.ProductAttributeValue.value_multi_option.through
        fields = ['sync_url', 'sync_id', 'sync_id', 'hash',
                  'productattributevalue', 'attributeoption']
        extra_kwargs={'sync_id':{'read_only': False}}


class ProductAttributeValueSerializer(CustomHyperlinkedModelSerializerBase):
    # Needs: attribute, product, value_option
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:productattributevalue-detail',
        lookup_field='sync_id',
    )
    product = serializers.HyperlinkedRelatedField(
        view_name='sync-api:product-detail',
        queryset=models.Product.objects,
        lookup_field="sync_id",
    )
    attribute = serializers.HyperlinkedRelatedField(
        view_name='sync-api:productattribute-detail',
        queryset=models.ProductAttribute.objects,
        lookup_field="sync_id",
    )
    value_option = serializers.HyperlinkedRelatedField(
        view_name='sync-api:attributeoption-detail',
        queryset=models.AttributeOption.objects,
        lookup_field="sync_id",
        required=False,
        allow_null=True,
    )
    value_image = CustomImageField(required=False)
    value_file = CustomFileField(required=False)
    class Meta:
        lookup_field = 'sync_id'
        model = models.ProductAttributeValue
        fields = ['sync_url', 'sync_id', 'hash', 'value_text',
                  'value_integer', 'value_boolean', 'value_float',
                  'value_richtext', 'value_date', 'value_datetime',
                  'value_option', 'value_image', 'value_file',
                  'product', 'attribute']
        extra_kwargs={'sync_id':{'read_only': False}}


class ProductImageSerializer(CustomHyperlinkedModelSerializerBase):
    # Needs: product
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:productimage-detail',
        lookup_field='sync_id',
    )
    product = serializers.HyperlinkedRelatedField(
        view_name='sync-api:product-detail',
        queryset=models.Product.objects,
        lookup_field="sync_id",
    )
    original = CustomImageField()#(represent_in_base64=True)
    class Meta:
        lookup_field = 'sync_id'
        model = models.ProductImage
        fields = ['sync_url', 'sync_id', 'hash', 'caption', 'original',
                  'display_order', 'date_created', 'product']
        extra_kwargs={'sync_id':{'read_only': False}}


# Category related:
class CategorySerializer(CustomHyperlinkedModelSerializerBase):
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:category-detail',
        lookup_field='sync_id',
    )
    image = CustomImageField(required=False)
    class Meta:
        lookup_field = 'sync_id'
        model = models.Category
        fields = ['sync_url', 'sync_id', 'hash', 'slug', 'name', 'path',
                  'depth', 'numchild',
                  'description', 'meta_title', 'meta_description', 'image']
        extra_kwargs={'sync_id':{'read_only': False}}


class ProductCategorySerializer(CustomHyperlinkedModelSerializerBase):
    # Needs: product, category
    sync_url = serializers.HyperlinkedIdentityField(
        view_name='sync-api:productcategory-detail',
        lookup_field='sync_id',
    )
    product = serializers.HyperlinkedRelatedField(
        view_name='sync-api:product-detail',
        queryset=models.Product.objects,
        lookup_field="sync_id",
    )
    category = serializers.HyperlinkedRelatedField(
        view_name='sync-api:category-detail',
        queryset=models.Category.objects,
        lookup_field="sync_id",
    )
    class Meta:
        lookup_field = 'sync_id'
        model = models.ProductCategory
        fields = ['sync_url', 'sync_id', 'hash', 'product', 'category']
        extra_kwargs={'sync_id':{'read_only': False}}
