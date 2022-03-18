import uuid

from django.db import models
from django.contrib.auth.models import User

from commerce.models import Product
from commerce.models.core import CoreEntity
from commerce.utils.enum import STATUS, PAYMENT


class OrderItem(CoreEntity):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Item: {self.item} Quantity: {self.quantity}"

    def get_total_price(self):
        return self.quantity * self.item.price

    def get_total_discounted_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_price() - self.get_total_discounted_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discounted_price()
        return self.get_total_price()


class Order(CoreEntity):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderCustomer')
    ref_code = models.CharField(max_length=20, default="0")
    items = models.ManyToManyField(OrderItem, related_name='orderItem')
    ordered = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=150, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    order_ide = models.CharField(max_length=25, blank=True, null=True, unique=True)
    status = models.IntegerField(choices=STATUS.order_status(), default=STATUS.PENDING.value)
    payment = models.IntegerField(choices=PAYMENT.payment_choices(), default=PAYMENT.CASH_ON_DELIVERY.value)

    def __str__(self):
        return f"OrderID: {self.order_ide} || Orders: {self.items.all()}"

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def save(self, *args, **kwargs):
        system_code = self.order_ide
        if not system_code:
            system_code = uuid.uuid4().hex[:6].upper()
        while Order.objects.filter(order_ide=system_code).exclude(pk=self.pk).exists():
            system_code = uuid.uuid4().hex[:6].upper()
        self.order_ide = system_code
        super(Order, self).save(*args, **kwargs)
