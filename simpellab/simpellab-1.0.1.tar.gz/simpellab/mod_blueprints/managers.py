from django.db import models


class BlueprintManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
