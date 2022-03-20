from django_hookup import core as hookup

from .api.viewsets import CartItemViewSet, CartViewSet


@hookup.register("REGISTER_API_VIEWSET")
def register_cart_viewset():
    return {
        "prefix": "cart",
        "viewset": CartViewSet,
        "basename": "cart",
    }


@hookup.register("REGISTER_API_VIEWSET")
def register_cart_item_viewset():
    return {
        "prefix": "mycart",
        "viewset": CartItemViewSet,
        "basename": "cartitem",
    }
