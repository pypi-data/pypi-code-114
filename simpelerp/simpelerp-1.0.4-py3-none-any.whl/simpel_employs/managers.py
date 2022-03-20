from django.db import models


class DepartmentManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().select_related("parent")
        return qs


class PositionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("department", "parent")
