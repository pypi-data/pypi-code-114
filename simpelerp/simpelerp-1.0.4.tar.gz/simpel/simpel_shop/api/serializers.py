from rest_framework import serializers

from simpel.simpel_products.api.serializers import ProductPolymorphicSerializer

from ..models import Cart, CartItem, CartItemBundle


class CartItemBundleSerializer(serializers.ModelSerializer):
    product = ProductPolymorphicSerializer(read_only=True)

    class Meta:
        model = CartItemBundle
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), required=False)
    product = ProductPolymorphicSerializer(read_only=True)
    bundles = CartItemBundleSerializer(many=True, read_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"
