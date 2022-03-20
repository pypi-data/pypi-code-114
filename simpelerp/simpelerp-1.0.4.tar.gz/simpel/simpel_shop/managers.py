from django.db import models

from simpel.simpel_core.abstracts import ParanoidManager


class BlueprintParameterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class CartManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class CartItemManager(ParanoidManager):
    def get_queryset(self):
        return super().get_queryset()


class BlueprintManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
