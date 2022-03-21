import pytest

from huscy.attributes import services
from huscy.attributes.models import AttributeSchema

pytestmark = pytest.mark.django_db


def test_create_new_schema_if_none_exists():
    assert not AttributeSchema.objects.exists()

    attribute_schema = services.get_attribute_schema()

    assert 1 == AttributeSchema.objects.count()
    attribute_schema.schema == {'type': 'object', 'properties': {}}


def test_get_attribute_schema_without_version_number(attribute_schema_v4, schema_v4):
    assert schema_v4 == services.get_attribute_schema().schema


def test_get_attribute_schema_with_version_number(django_db_reset_sequences,
                                                  attribute_schema_v4, schema_v2):
    assert schema_v2 == services.get_attribute_schema(version=2).schema


def test_get_attribute_schema_with_invalid_version_number(django_db_reset_sequences,
                                                          attribute_schema_v4):
    with pytest.raises(AttributeSchema.DoesNotExist):
        services.get_attribute_schema(version=7)
