from django_hookup import core as hookup

from .api.viewsets import CategoryViewSet, ProductViewSet, UnitViewSet
from .models import Asset, Bundle, Fee, Inventory, Service  # NOQA


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_simpel_products_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_DEMO_USERS")
def register_simpel_products_demo_users():
    from .apps import init_demo_users

    init_demo_users()


# @hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
# def register_service_model():
#     return Service


# @hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
# def register_fee_model():
#     return Fee


# @hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
# def register_asset_model():
#     return Asset


# @hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
# def register_inventory_model():
#     return Inventory


# @hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
# def register_bundle_model():
#     return Bundle


@hookup.register("REGISTER_API_VIEWSET")
def register_unit_viewset():
    return {
        "prefix": "products/unit",
        "viewset": UnitViewSet,
        "basename": "unit",
    }


@hookup.register("REGISTER_API_VIEWSET")
def register_category_viewset():
    return {
        "prefix": "products/category",
        "viewset": CategoryViewSet,
        "basename": "category",
    }


# @hookup.register("REGISTER_API_VIEWSET")
# def register_tag_viewset():
#     return {
#         "prefix": "products/tag",
#         "viewset": TagViewSet,
#         "basename": "tag",
#     }


@hookup.register("REGISTER_API_VIEWSET")
def register_product_viewset():
    return {
        "prefix": "products/product",
        "viewset": ProductViewSet,
        "basename": "product",
    }
