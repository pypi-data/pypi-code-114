from django.utils.module_loading import import_string

from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from simpel_hookup import core as hookup
from taggit.models import Tag

from ..models import Category, Product, Service, Specification, Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("lft", "rght", "tree_id")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = "__all__"

# class TaggedProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaggedProduct
#         fields = "__all__"


class BaseProductSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    category = CategorySerializer(required=False)
    specifications = SpecificationSerializer(many=True)

    class Meta:
        exclude = ("polymorphic_ctype", "reg_number")

    def __init__(self, *args, **kwargs):
        # Dynamicly control field to be shown
        # Dont pass fields args to superclass
        fields = kwargs.pop("fields", None)

        super().__init__(*args, **kwargs)

        # Drop any fields that are not specified in fields args
        if fields is not None:
            allowed = set(fields)
            exist_fields = set(self.fields.keys())
            for field_name in exist_fields - allowed:
                self.fields.pop(field_name)


class ProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = Product


class ServiceSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = Service


class ProductPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "producttype"
    model_serializer_mapping = {
        Product: ProductSerializer,
        Service: ServiceSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()

    def to_representation(self, instance):
        return super().to_representation(instance.get_real_instance())

    def __init__(self, *args, **kwargs):
        # Dynamicly control field to be shown in child class
        # Dont pass fields args to superclass
        fields = kwargs.pop("fields", None)

        # Get registered product serializer
        funcs = hookup.get_hooks("REGISTER_PRODUCT_SERIALIZER")
        for func in funcs:
            model_name, serializer = func()
            self.model_serializer_mapping[import_string(model_name)] = serializer

        self.model_serializer_mapping = {
            model: serializer(fields=fields, *args, **kwargs)
            for model, serializer in self.model_serializer_mapping.items()
        }

        super().__init__(*args, **kwargs)
