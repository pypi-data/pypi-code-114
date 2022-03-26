from uuid import uuid4

from django.db import models

from . import forms
from .validators import validate_non_strict_email


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance._loaded_values = dict(zip(field_names, values))
        return instance

    class Meta:
        abstract = True


class UuidBaseModel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class NonStrictEmailField(models.EmailField):
    default_validators = [validate_non_strict_email]

    def formfield(self, **kwargs):
        kwargs.update({'form_class': forms.NonStrictEmailField})
        return super().formfield(**kwargs)
