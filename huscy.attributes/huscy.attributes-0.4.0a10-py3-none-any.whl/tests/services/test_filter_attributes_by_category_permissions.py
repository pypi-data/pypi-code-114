import pytest
from django.contrib.auth.models import Permission

from huscy.attributes.models import AttributeSet
from huscy.attributes.services import (
    create_attribute_schema,
    filter_attributes_by_category_permissions,
)


@pytest.fixture
def attribute_schema():
    return create_attribute_schema({
        'type': 'object',
        'properties': {
            'attribute1': {'type': 'string'},
            'category1': {
                'type': 'object',
                'properties': {
                    'attribute2': {'type': 'string'},
                }
            },
            'category2': {
                'type': 'object',
                'properties': {
                    'attribute3': {'type': 'string'},
                }
            },
        },
    })


@pytest.fixture
def attribute_set(attribute_schema):
    return AttributeSet.objects.create(
        attribute_schema=attribute_schema,
        attributes={
            'attribute1': 'foobar',
            'category1': {'attribute2': 'foo'},
            'category2': {'attribute3': 'bar'},
        }
    )


def test_without_category_permissions(user, attribute_set):
    attribute_set = filter_attributes_by_category_permissions(attribute_set, user)

    assert attribute_set.attributes == {
        'attribute1': 'foobar'
    }


def test_one_category_permission(user, attribute_set):
    view_category1_permission = Permission.objects.get(codename='view_attribute_category_category1')
    user.user_permissions.add(view_category1_permission)

    attribute_set = filter_attributes_by_category_permissions(attribute_set, user)

    assert attribute_set.attributes == {
        'attribute1': 'foobar',
        'category1': {'attribute2': 'foo'}
    }


def test_many_category_permissions(user, attribute_set):
    permissions = Permission.objects.filter(codename__contains='view_attribute_category_category')
    user.user_permissions.add(*permissions)

    attribute_set = filter_attributes_by_category_permissions(attribute_set, user)

    assert attribute_set.attributes == {
        'attribute1': 'foobar',
        'category1': {'attribute2': 'foo'},
        'category2': {'attribute3': 'bar'}
    }
