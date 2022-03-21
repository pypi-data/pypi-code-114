from datetime import datetime

import pytest

from django.contrib.auth.models import Permission

from huscy.attributes.models import AttributeSchema
from huscy.attributes.services import create_attribute_schema

pytestmark = pytest.mark.django_db


@pytest.mark.freeze_time('2000-01-01T10:00:00')
def test_create_attribute_schema(django_db_reset_sequences):
    schema = dict(type='object', properties=dict())

    result = create_attribute_schema(schema)

    assert isinstance(result, AttributeSchema)
    assert result.pk == 1
    assert result.schema == schema
    assert result.created_at == datetime(2000, 1, 1, 10)


def test_create_category_permissions():
    schema = {
        'type': 'object',
        'properties': {
            'property1': {'type': 'string'},
            'property2': {'type': 'object', 'properties': {}},
            'property3': {'type': 'number'},
            'property4': {
                'type': 'object',
                'properties': {
                    'property5': {'type': 'string'},
                    'property6': {'type': 'string'},
                }
            }
        }
    }

    assert not Permission.objects.filter(codename__contains='_attribute_category_').exists()

    create_attribute_schema(schema)

    assert 4 == Permission.objects.filter(codename__contains='_attribute_category_').count()
    assert Permission.objects.filter(codename='change_attribute_category_property2').exists()
    assert Permission.objects.filter(codename='change_attribute_category_property4').exists()
    assert Permission.objects.filter(codename='view_attribute_category_property2').exists()
    assert Permission.objects.filter(codename='view_attribute_category_property4').exists()
