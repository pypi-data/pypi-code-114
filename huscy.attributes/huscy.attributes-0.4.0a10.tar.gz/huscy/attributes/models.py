from django.contrib.postgres.fields import JSONField
from django.db import models


DEFAULT_ATTRIBUTE_SCHEMA = {
    'type': 'object',
    'properties': {},
}


class AttributeSchema(models.Model):
    schema = JSONField(default=DEFAULT_ATTRIBUTE_SCHEMA)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


def get_latest_attribute_schema_version():
    return AttributeSchema.objects.count()


class AttributeSet(models.Model):
    pseudonym = models.CharField(max_length=128, unique=True)
    attributes = JSONField(default=dict)
    attribute_schema = models.ForeignKey(AttributeSchema, on_delete=models.PROTECT,
                                         default=get_latest_attribute_schema_version)
