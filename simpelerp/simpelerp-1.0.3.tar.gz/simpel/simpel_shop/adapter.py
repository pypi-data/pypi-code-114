from django.db import transaction
from django.utils.translation import gettext_lazy as _

from simpel.simpel_sales.helpers import (
    create_salesorder,
    create_salesquotation,
    get_allowed_product_groups,
)
from simpel.simpel_shop.models import Cart, CartItem, CartItemBundle
from simpel.simpel_shop.settings import simpel_shop_settings as shop_settings


class ShopAdapter:
    valid_action = ["create_salesorder", "create_salesquotation"]
    error_messages = {}

    def __init__(self, request):
        self.request = request
        self.user = request.user
        self.cart = self.get_cart()

    def get_filtered_items(self, group=None):
        if group:
            allowed_products = get_allowed_product_groups(group)
            items = self.cart.items.filter(product__group__code__in=allowed_products)
        else:
            items = self.cart.items.all()
        return items

    def cart_clear(self, **filters):
        with transaction.atomic():
            cart_items = self.cart.items.filter(**filters)
            cart_items.delete()

    def get_cart(self, user=None):
        return Cart.get_for_user(user or self.request.user)

    def remove_item(self, product):
        if isinstance(product, (list, tuple, set)):
            filters = {"product_id__in": [p.id for p in product]}
        else:
            filters = {"product_id__in": [product.id]}
        cart_items = self.cart.items.filter(**filters)
        cart_items.delete()

    def get_checkout_handler(self, action):
        action_map = {
            "create_order": self.create_order,
            "create_quotation": self.create_quotation,
        }
        return action_map[action]

    def create_order(self):
        raise NotImplementedError(_("ShopAdapter subclass should implement checkout method"))

    def create_quotation(self):
        raise NotImplementedError(_("ShopAdapter subclass should implement checkout method"))

    def create_cart_item(self, product, name=None, quantity=1, note=""):
        defaults = {"name": name or product.name, "quantity": quantity, "note": note}
        if shop_settings.UNIQUE_ITEM:
            cart_item, created = CartItem.objects.get_or_create(
                cart=self.cart,
                product=product,
                defaults=defaults,
            )
            if not created:
                cart_item.quantity += 1
        else:
            cart_item = CartItem(cart=self.cart, product=product, **defaults)
            created = True
        cart_item.save()
        return cart_item, created

    def create_cart_item_bundle(self, cart_item, product, quantity=1, required=False):
        item_bundle = CartItemBundle(
            cart_item=cart_item,
            product=product,
            quantity=quantity,
            required=required,
        )
        item_bundle.save()

    def add_item(self, product, name="", quantity=1, note="", bundles=None):
        with transaction.atomic():

            cart_item, created = self.create_cart_item(product, name, quantity, note)

            bundle_ids = []

            if (shop_settings.UNIQUE_ITEM and not created):
                return cart_item

            required_recommendations = cart_item.product.recommended_items.filter(required=True)
            for required_recommendation in required_recommendations:
                if required_recommendation.product.id not in bundle_ids:
                    item_bundle = self.create_cart_item_bundle(
                        cart_item,
                        required_recommendation.product,
                        required_recommendation.quantity,
                    )
                    bundle_ids.append(item_bundle.product.id)

            if bundles is not None:
                for selected_item in bundles:
                    if selected_item.product.id not in bundle_ids:
                        item_bundle = self.create_cart_item_bundle(
                            cart_item,
                            selected_item.product,
                            selected_item.quantity,
                            selected_item.required,
                        )

            cart_item.save()

            return cart_item


class DefaultAdapter(ShopAdapter):
    def get_checkout_handler(self, action):
        action_map = {
            "create_salesorder": create_salesorder,
            "create_salesquotation": create_salesquotation,
        }
        return action_map[action]
