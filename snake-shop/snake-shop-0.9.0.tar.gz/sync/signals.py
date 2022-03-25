from urllib.parse import ParseResult
from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model
from oscarapi.models import ApiKey
from .utils import Syncer
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, m2m_changed
from .models import Shop

User = get_user_model()
Product = get_model('catalogue', 'Product')
ProductAttribute = get_model('catalogue', 'ProductAttribute')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
StockRecord = get_model('partner', 'StockRecord')


class SyncController:
    # These classes are fetching the shop products to filter
    shop_filter = {
        Product: lambda instance: instance,
        ProductAttribute: lambda x: x,#
        ProductAttributeValue: lambda instance: instance.product.shops.all(),#
        ProductAttributeValue.value_multi_option.through: '',
    }
    def __init__(self, instance):
        self.model = instance._meta.model
        self.model_name = instance._meta.model_name
        self.instance = instance
        self.shops = self.shop_filter.get(model, None)(instance) \
            or Shop.objects.all()

    def create(self):
        for shop in self.shops:
            Syncer(self.model_name, shop).sync(instance=self.instance)

    def update(self):
        for shop in self.shops:
            Syncer(self.model_name, shop).sync(instance=self.instance)

    def delete(self):
        for shop in self.shops:
            Syncer(self.model_name, shop).sync(instance=self.instance)

'''
def post_save_instance(instance, created, **kwargs):
    controller = SyncController(instance)
    if created:
        controller.create()
    else:
        controller.update()


def post_delete_instance(instance, **kwargs):
    SyncController(instance).delete()


for model in [Product, ProductAttribute, ProductAttributeValue,
              ProductAttributeValue, ]:
    post_save.connect(post_save_instance, sender=model)
    post_save.connect(post_delete_instance, sender=model)
'''


'''
@receiver([post_save, post_delete], sender=ProductSubscription)
def sync_subscription(instance, **kwargs):
    """ Create unsaved stockrecords and sync"""
    kwargs = instance.get_syncer_kwargs()
    #qs = 

@receiver([post_save, post_delete], sender=Product)
def sync_product(instance, created=False, deleted=False, **kwargs):
    """ sync stockrecords of product """
    for shop in instance.shops.all():
        syncer_kwargs = shop.get_syncer_kwargs()
        Syncer('product', **syncer_kwargs).sync(instance=instance)


@receiver([post_save, post_delete], sender=Product.attributes)
def sync_product_attribute(instance, **kwargs):
    """ sync stockrecords of product """
    for shop in Shop.objects.all():
        syncer_kwargs = shop.get_syncer_kwargs()
        import pdb; pdb.set_trace()  # <---------
        Syncer('productattribute', **syncer_kwargs).sync(instance=instance)


@receiver([post_save, post_delete], sender=ProductAttributeValue)
def sync_product_attribute_value(instance, **kwargs):
    """ sync stockrecords of product """
    for shop in Shop.objects.all():
        syncer_kwargs = shop.get_syncer_kwargs()
        Syncer('productattributevalue', **syncer_kwargs).sync(instance=instance)


@receiver([m2m_changed], sender=ProductAttributeValue.value_multi_option.through)
def sync_product_attribute_value_multi_option(instance, **kwargs):
    """ sync stockrecords of product """
    for shop in Shop.objects.all():
        syncer_kwargs = shop.get_syncer_kwargs()
        Syncer('productattributevalue_value_multi_option', **syncer_kwargs).sync()
'''



'''
        syncer_kwargs = self.get_syncer_kwargs()
        Syncer('tax', **syncer_kwargs).sync()
        Syncer('productclass', **syncer_kwargs).sync()
        Syncer('category', **syncer_kwargs).sync()
        Syncer('attributeoptiongroup', **syncer_kwargs).sync()
        Syncer('attributeoption', **syncer_kwargs).sync()
        Syncer('productattribute', **syncer_kwargs).sync()
'''
