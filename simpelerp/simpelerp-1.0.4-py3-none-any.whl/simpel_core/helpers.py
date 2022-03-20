from django.contrib.auth import get_permission_codename
from django.contrib.auth.models import Permission
from django.db import transaction

from simpel.simpel_auth.models import LinkedAddress, LinkedContact


class PermissionHelper:
    """
    Provides permission-related helper functions to help determine what a
    user can do with a 'typical' model (where permissions are granted
    model-wide), and to a specific instance of that model.
    """

    def __init__(self, model):
        self.model = model
        self.opts = model._meta

    def get_all_model_permissions(self):
        """
        Return a queryset of all Permission objects pertaining to the `model`
        specified at initialisation.
        """

        return Permission.objects.filter(
            content_type__app_label=self.opts.app_label,
            content_type__model=self.opts.model_name,
        )

    def get_perm_codename(self, action):
        return get_permission_codename(action, self.opts)

    def user_has_specific_permission(self, user, perm_codename):
        """
        Combine `perm_codename` with `self.opts.app_label` to call the provided
        Django user's built-in `has_perm` method.
        """
        return user.has_perm("%s.%s" % (self.opts.app_label, perm_codename))

    def user_has_any_permissions(self, user):
        """
        Return a boolean to indicate whether `user` has any model-wide
        permissions
        """
        for perm in self.get_all_model_permissions().values("codename"):
            if self.user_has_specific_permission(user, perm["codename"]):
                return True
        return False

    def user_can_list(self, user):
        """
        Return a boolean to indicate whether `user` is permitted to access the
        list view for self.model
        """
        return self.user_has_any_permissions(user)

    def user_can_create(self, user):
        """
        Return a boolean to indicate whether `user` is permitted to create new
        instances of `self.model`
        """
        perm_codename = self.get_perm_codename("add")
        return self.user_has_specific_permission(user, perm_codename)

    def user_can_inspect_obj(self, user, obj):
        """
        Return a boolean to indicate whether `user` is permitted to 'inspect'
        a specific `self.model` instance.
        """
        return self.user_has_any_permissions(user)

    def user_can_edit_obj(self, user, obj):
        """
        Return a boolean to indicate whether `user` is permitted to 'change'
        a specific `self.model` instance.
        """
        perm_codename = self.get_perm_codename("change")
        return self.user_has_specific_permission(user, perm_codename)

    def user_can_delete_obj(self, user, obj):
        """
        Return a boolean to indicate whether `user` is permitted to 'delete'
        a specific `self.model` instance.
        """
        perm_codename = self.get_perm_codename("delete")
        return self.user_has_specific_permission(user, perm_codename)

    def user_can_unpublish_obj(self, user, obj):
        return False

    def user_can_copy_obj(self, user, obj):
        return False

    def user_is_owner_or_admin(self, user, obj, owner_field):
        obj_owner = getattr(obj, owner_field, None)
        if (obj_owner and obj_owner is user) or user.is_superadmin:
            return True
        else:
            return False

    def user_is_member(self, group_name):
        """Return a boolean to indicate whether `user` is a member of a
        specific `group` instance."""
        return False


class OrderBuilder(object):
    def __init__(
        self,
        order_model,
        item_model,
        bundle_model,
    ):
        self.bundle_ids = list()
        self.order_model = order_model
        self.item_model = item_model
        self.bundle_model = bundle_model

    def create_order(self, user, data):
        """Create an order"""
        order = self.order_model(user=user, **data)
        order.save()
        return order

    def create_item(self, order, item):
        newitem = self.item_model(
            **{
                self.order_model._meta.model_name: order,
                "name": item.product.name,
                "alias_name": item.name,
                "product": item.product,
                "quantity": item.quantity,
            }
        )
        newitem.save()
        return newitem

    def create_item_bundle(self, item, bundle):
        item_bundle = self.bundle_model(
            item=item,
            name=bundle.product.name,
            product=bundle.product,
            quantity=bundle.quantity,
        )
        item_bundle.save()
        return item_bundle

    def create_linked_contact(self, obj, contact, group=None):
        new_address = LinkedContact(
            linked_object=obj,
            **contact.to_dict(),
        )
        if group is not None:
            new_address.group = group
        new_address.save()
        return new_address

    def create_linked_address(self, obj, address, address_type=None):
        new_address = LinkedAddress(
            linked_object=obj,
            **address.to_dict(),
        )
        if address_type is not None:
            new_address.address_type = address_type
        new_address.save()
        return new_address

    def create(
        self, user, data, items, billing=None, shipping=None, delete_item=False, from_cart=False
    ):
        with transaction.atomic():
            order = self.create_order(user, data=data)

            # Prepare billing address
            if billing is None:
                billing = order.customer.get_address(LinkedAddress.BILLING)
            if shipping is None:
                shipping = billing
            if billing:
                self.create_linked_address(order, billing, LinkedAddress.BILLING)
            if shipping:
                self.create_linked_address(order, shipping, LinkedAddress.SHIPPING)

            # Add items
            for item in items:
                orderitem = self.create_item(order, item)
                bundle_ids = []
                bundled_products = getattr(item.product.specific, "bundle_items", None)
                if bundled_products:
                    for bundle in bundled_products.all():
                        self.create_item_bundle(orderitem, bundle)
                        bundle_ids.append(bundle.product.id)

                req_recommends = item.product.recommended_items.filter(required=True)
                for req_recommend in req_recommends:
                    if req_recommend.product.id not in bundle_ids:
                        self.create_item_bundle(orderitem, req_recommend)
                        bundle_ids.append(req_recommend.product.id)

                if from_cart:
                    for cart_bundle in item.bundles.all():
                        if cart_bundle.product.id not in bundle_ids:
                            self.create_item_bundle(orderitem, cart_bundle)
                            bundle_ids.append(cart_bundle.product.id)

                # Attach deliverable information
                del_info = getattr(item, "deliverable_information", None)
                if item.product.is_deliverable and del_info is not None:
                    new_del_info = self.create_linked_address(
                        orderitem,
                        del_info,
                        address_type=LinkedAddress.DELIVERABLE,
                    )
                    new_del_info.save()

                if delete_item:
                    item.delete()
                orderitem.save()
            order.save()
            return order

    def clone(self, user, data, obj):
        with transaction.atomic():
            order = self.create_order(user, data)
            # Prepare billing address
            billing = getattr(obj, "billing_address", None)
            shipping = getattr(obj, "shipping_address", None)
            if billing:
                self.create_linked_address(order, billing, LinkedAddress.BILLING)
            if shipping:
                self.create_linked_address(order, shipping, LinkedAddress.SHIPPING)
            # clone order items
            for item in obj.items.all():
                new_item = self.create_item(order, item)
                # clone item bundle
                for bundle in item.bundles.all():
                    bundle = self.create_item_bundle(new_item, bundle)
                    # Attach deliverable information
                del_info = getattr(item, "deliverable_information", None)
                if item.product.is_deliverable and del_info is not None:
                    new_del_info = self.create_linked_address(
                        new_item,
                        del_info,
                        address_type=LinkedAddress.DELIVERABLE,
                    )
                    new_del_info.save()

                new_item.save()
            order.save()
            return order
