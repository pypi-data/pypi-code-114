from django.db import models
from django.conf import settings

STATUS_CHOICES = (
    ("active", "Active"),
    ("trialing", "Trialing"),
    ("paste_due", "Past due"),
    ("deleted", "Deleted"),
)

SUBSCRIPTION_TYPE_CHOICES = (
    ("monthly", "Monthly"),
    ("sixmonths", "Six months"),
    ("annual", "Annual"),
)


class Customer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.deletion.CASCADE
    )
    status = models.CharField(
        max_length=9, choices=STATUS_CHOICES, blank=False
    )
    unit_price = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    subscription_id = models.CharField(max_length=8)
    subscription_plan_id = models.CharField(max_length=8)
    subscription_type = models.CharField(
        max_length=9, choices=SUBSCRIPTION_TYPE_CHOICES
    )
    cancel_url = models.CharField(max_length=256)
    update_url = models.CharField(max_length=256)
    cancelation_date = models.DateField(blank=True, null=True)
