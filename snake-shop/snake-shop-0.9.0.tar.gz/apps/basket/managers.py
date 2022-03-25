from django.db import models


class BasketLineManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('attributes')