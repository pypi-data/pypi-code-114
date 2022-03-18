from rest_framework import serializers

from commerce.models.product import Product
from commerce.models.category import Tag
from commerce.serializers.category_serializer import CategorySerializer, TagSerializer


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        read_only_fields = ('owner',)
        fields = (
            'id', 'item_name', 'owner', 'categories', 'tags', 'is_available', 'price', 'discount_price',
            'short_description', 'model_number', 'brand_name', 'serial_number', 'item_type', 'item_image',
            'galley_image', 'galley_image2', 'galley_image3', 'created_at', 'updated_at'

        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categories'] = CategorySerializer(instance.categories).data
        return response

    def get_or_create_tag(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, create = Tag.objects.get_or_create(pk=tag.get('id'), defaults=tag)
            tag_ids.append(tag_instance.pk)
        return tag_ids

    def create_or_update_tag(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, create = Tag.objects.update_or_create(pk=tag.get('id'), defaults=tag)
            tag_ids.append(tag_instance.pk)
        return tag_ids

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        product = Product.objects.create(**validated_data)
        product.tags.set(self.get_or_create_tag(tags))
        return product

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        instance.tags.set(self.create_or_update_tag(tags))
        return instance


class GenericProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 2
        fields = '__all__'
