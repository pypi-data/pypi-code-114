from rest_framework import serializers

from simpel.simpel_products.api.serializers import ProductPolymorphicSerializer

from ..models import SalesOrder, SalesOrderItem, SalesOrderItemBundle


class SalesOrderItemBundleSerializer(serializers.ModelSerializer):
    product = ProductPolymorphicSerializer(read_only=True)

    class Meta:
        model = SalesOrderItemBundle
        fields = "__all__"


class SalesOrderItemSerializer(serializers.ModelSerializer):
    sales_order = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all(), required=False)
    product = ProductPolymorphicSerializer(read_only=True)
    bundles = SalesOrderItemBundleSerializer(many=True, read_only=True)

    class Meta:
        model = SalesOrderItem
        fields = "__all__"


class SalesOrderSerializer(serializers.ModelSerializer):
    items = SalesOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = SalesOrder
        fields = "__all__"
