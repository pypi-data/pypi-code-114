import pytest
from model_bakery import baker

from jsonschema.exceptions import ValidationError

from huscy.attributes.services import update_attribute_set

pytestmark = pytest.mark.django_db


def test_update_attributes(attribute_set):
    attributes = attribute_set.attributes
    attributes['attribute3'] = 100.0

    update_attribute_set(attribute_set, attributes)

    attribute_set.refresh_from_db()
    assert attribute_set.attributes == {
        'attribute1': {},
        'attribute2': 'any string',
        'attribute3': 100.0,
    }


def test_update_attributes_with_invalid_data(attribute_set):
    attributes = attribute_set.attributes
    attributes['attribute3'] = 'invalid'

    with pytest.raises(ValidationError) as e:
        update_attribute_set(attribute_set, attributes)

    assert str(e.value).startswith("'invalid' is not of type 'number'")


def test_update_attributes_together_with_attribute_schema_version(attribute_set, schema_v4):
    schema_v5 = schema_v4.copy()
    schema_v5['properties']['attribute4'] = {'type': 'string', 'enum': ['a', 'b']}
    latest_attribute_schema = baker.make('attributes.AttributeSchema', schema=schema_v5)

    attributes = attribute_set.attributes
    attributes['attribute4'] = 'a'

    update_attribute_set(attribute_set, attributes, latest_attribute_schema)

    attribute_set.refresh_from_db()
    assert attribute_set.attribute_schema == latest_attribute_schema
    assert attribute_set.attributes == {
        'attribute1': {},
        'attribute2': 'any string',
        'attribute3': 4.5,
        'attribute4': 'a',
    }


def test_update_attribute_schema_to_lower_version(attribute_set, attribute_schema_v3):
    with pytest.raises(Exception) as e:
        update_attribute_set(attribute_set, attribute_set.attributes, attribute_schema_v3)

    assert str(e.value) == ('New version for attribute schema must be greater than or equals with '
                            'current attribute schema version.')


def test_partial_update_for_attributes(attribute_set_with_categories):
    attribute_set = attribute_set_with_categories

    update_attribute_set(attribute_set, {
        'category1': {'attribute12': 50},
        'category2': {'attribute22': 50}
    })

    attribute_set.refresh_from_db()
    assert attribute_set.attributes == {
        'category1': {'attribute11': 100, 'attribute12': 50},
        'category2': {'attribute21': 100, 'attribute22': 50}
    }
