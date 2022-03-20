from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from simpel.simpel_shop.models import Cart, CartItem

from .serializers import CartItemBundleSerializer, CartItemSerializer, CartSerializer

# from drf_spectacular.utils import extend_schema, inline_serializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        qs = Cart.objects.all()
        return qs


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CartItemSerializer
        elif self.action in ["add_item", "update_item"]:
            return CartItemSerializer
        elif self.action in ["remove_item"]:
            return CartItemSerializer
        elif self.action in ["add_item_parameter", "update_item_parameter"]:
            return CartItemBundleSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = CartItem.objects.all()
        return qs

    def retrieve(self, request, *args, **kwargs):
        """Inspect selected cart item/product"""
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Remove selected cart item/product"""
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """List current User cart items/products"""
        cart = Cart.get_for_user(request.user)
        serializer = self.get_serializer_class()(instance=cart)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Add item/product to current User cart"""
        cart = Cart.get_for_user(request.user)
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(cart=cart)
        response = CartItemSerializer(instance=instance)
        return Response(data=response.data)

    def update(self, request, id, *args, **kwargs):
        """Update selected item/product in current user cart"""
        cart_item = self.get_object()
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.update(cart_item, serializer.data)
        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        response = CartItemSerializer(instance=instance)
        return Response(data=response.data)

    @action(methods=["POST"], detail=True)
    def add_parameter(self, request, *args, **kwargs):
        """Add parameter to selected item/product"""
        instance = self.get_object()
        data = request.data
        data["cart_item"] = instance
        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["PUT", "PATCH"], detail=True, url_path="update-parameter/(?P<param_id>[^/.]+)")
    def update_parameter(self, request, *args, **kwargs):
        """Update selected parameter in item/product"""
        instance = self.get_object()
        param_id = kwargs.get("param_id")
        param = get_object_or_404(CartItemBundleSerializer, cart_item=instance, pk=param_id)
        data = request.data
        data["cart_item"] = instance
        data["parameter"] = param
        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(methods=["DELETE"], detail=True, url_path="remove-parameter/(?P<param_id>[^/.]+)")
    def remove_parameter(self, request, *args, **kwargs):
        """Add selected parameter from selected item/product"""
        instance = self.get_object()
        param_id = kwargs.get("param_id")
        param = get_object_or_404(CartItemBundleSerializer, cart_item=instance, pk=param_id)
        param.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
