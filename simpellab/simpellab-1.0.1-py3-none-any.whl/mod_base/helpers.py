from django.db import transaction

from simpel.simpel_shop.models import CartItem, CartItemBundle

from .models import Blueprint, BlueprintBundle


def save_as_blueprint(request, cart_item):
    user = request.user
    with transaction.atomic():
        blueprint = Blueprint(
            user=user,
            name=cart_item.name,
            product=cart_item.product,
            note=cart_item.note,
        )
        blueprint.save()
        for bundle in cart_item.bundles.all():
            blueprint_bundle = BlueprintBundle(
                blueprint=blueprint,
                product=bundle.product,
                quantity=bundle.quantity,
            )
            blueprint_bundle.save()


def blueprint_to_cart(request, cart, item):
    with transaction.atomic():
        cart_item = CartItem(
            cart=cart,
            name=item.name,
            product=item.product,
            quantity=1,
            note=item.note,
        )
        cart_item.save()
        CartItemBundle.objects.bulk_create(
            [
                CartItemBundle(
                    cart_item=cart_item,
                    product=rec.product,
                    quantity=1,
                )
                for rec in item.bundles.all()
            ],
        )
        return cart_item
