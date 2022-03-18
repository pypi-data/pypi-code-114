from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from djangoldp.models import Model
from djangoldp_circle.models import Circle
from djangoldp.views import LDPViewSet
from djangoldp.serializers import LDPSerializer
from django.template import loader
from rest_framework import serializers


class CurrentStockSerializer(LDPSerializer):
    currentstock = serializers.SerializerMethodField()

    def get_currentstock(self, obj):
        products = obj.productstock.all()
        stock= obj.stock
        for product in products:
            stock += product.stockAdd or 0
            stock -= product.stockRemove or 0
        return stock

class CurrentStock(LDPViewSet):
    serializer_class = CurrentStockSerializer

class Product(Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nom du produit")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    externalLink = models.URLField(blank=True, null=True, verbose_name="Lien externe")
    stock = models.IntegerField(blank=True, null=True, verbose_name="Stock initial")
    price = models.IntegerField(blank=True, null=True, verbose_name="Prix")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdProducts', null=True, blank=True, on_delete=models.SET_NULL)
    creationDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta(Model.Meta):
        auto_author = 'author'
        owner_field = 'author'
        anonymous_perms = ['view', 'add']
        authenticated_perms = ['inherit']
        owner_perms = ['inherit', 'change', 'control', 'delete']
        rdf_type = 'sib:product'
        view_set = CurrentStock

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid

class Sale(Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nom de la vente")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    startDate =  models.DateField(blank=True, null=True, verbose_name="Date de début")
    endDate = models.DateField(verbose_name="Date de fin", blank=True, null=True )
    product = models.ManyToManyField(Product, blank=True, max_length=50, verbose_name="produits", related_name="sale")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdSales', null=True, blank=True, on_delete=models.SET_NULL)
    creationDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    circle = models.ForeignKey(Circle, null=True, blank=True, related_name="sale", on_delete=models.SET_NULL)
    
    class Meta(Model.Meta):
        nested_fields = ['circle', 'author']
        ordering = ['startDate']
        auto_author = 'author'
        owner_field = 'author'
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add']
        owner_perms = ['inherit', 'change', 'control', 'delete']
        rdf_type = 'sib:sale'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid

STATUS_CHOICES = [
    ('pending', 'En attente'),
    ('validated', 'Payée'),
    ('cancelled', 'Annulée'),
]

class Order(Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='clientorder', null=True, blank=True, on_delete=models.SET_NULL)
    sale = models.ForeignKey(Sale, null=True, blank=True, on_delete=models.CASCADE,  verbose_name="vente", related_name="saleorder")
    orderstatus = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True, null=True, verbose_name="Status de la commande")
    totalprice = models.CharField(max_length=50, blank=True, null=True, verbose_name="prix total")
    transactionDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta(Model.Meta):
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'change', 'control', 'delete']
        rdf_type = 'sib:order'

    def __str__(self):
        if self.sale.name and self.client.username and self.transactionDate:
            return "%s - %s - %s" % (self.sale.name, self.client.username , self.transactionDate)
        else:
            return self.urlid

class Productstock(Model):
    product = models.ForeignKey(Product, blank=True, max_length=50, on_delete=models.CASCADE,verbose_name="produits", related_name="productstock")
    stockAdd = models.IntegerField(blank=True, null=True, verbose_name="Ajout de stock")
    stockRemove = models.IntegerField(blank=True, null=True, verbose_name="Quantité commandée")
    order = models.ForeignKey(Order, null=True, blank=True, max_length=50, on_delete=models.CASCADE, verbose_name="commande", related_name="orderstock")
    transactionDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta(Model.Meta):
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'change', 'control', 'delete']
    
    def __str__(self):
        if self.product.name and self.transactionDate:
            return "%s - %s" % (self.product.name , self.transactionDate)
        else:
            return self.urlid


@receiver(post_save, sender=Order)
def on_order(sender, instance, created, **kwargs):
    if created:
       messageorder = loader.render_to_string('owner_order.txt', {'order': instance})
       messageorderresponse = loader.render_to_string('client_order.txt', {'order': instance})
       send_mail('Une nouvelle commande a été effectuée', messageorder, 'contact@startinblox.com',  {instance.sale.author.email})
       send_mail('Votre commande a bien été prise en compte', messageorderresponse, 'contact@startinblox.com', {instance.client.email})
