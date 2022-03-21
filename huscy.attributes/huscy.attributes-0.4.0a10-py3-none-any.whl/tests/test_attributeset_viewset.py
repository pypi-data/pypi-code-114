import pytest
from model_bakery import baker

from django.contrib.auth.models import Permission
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from huscy.attributes.serializer import AttributeSchemaSerializer


def test_admin_user_can_retrieve_attribute_set(admin_client, attribute_set, subject):
    response = retrieve_attribute_set(admin_client, subject)

    assert HTTP_200_OK == response.status_code


def test_admin_user_can_update_attribute_set(admin_client, attribute_set, subject):
    response = update_attribute_set(admin_client, attribute_set, subject)

    assert HTTP_200_OK == response.status_code


def test_user_with_permission_can_retrieve_attribute_set(client, user, attribute_set, subject):
    view_permission = Permission.objects.get(codename='view_attributeset')
    user.user_permissions.add(view_permission)

    response = retrieve_attribute_set(client, subject)

    assert HTTP_200_OK == response.status_code


def test_user_with_permission_can_update_attribute_set(client, user, attribute_set, subject):
    change_subject_permission = Permission.objects.get(codename='change_subject')
    change_attributeset_permission = Permission.objects.get(codename='change_attributeset')
    user.user_permissions.add(change_subject_permission, change_attributeset_permission)

    response = update_attribute_set(client, attribute_set, subject)

    assert HTTP_200_OK == response.status_code


@pytest.mark.parametrize('permission', ['change_subject', 'change_attributeset'])
def test_user_with_either_change_subject_or_change_attributeset_perms_cannot_update_attribute_set(
        client, user, attribute_set, subject, permission):
    user.user_permissions.add(Permission.objects.get(codename=permission))

    response = update_attribute_set(client, attribute_set, subject)

    assert HTTP_403_FORBIDDEN == response.status_code


def test_user_without_permission_cannot_retrieve_attribute_set(client, attribute_set, subject):
    response = retrieve_attribute_set(client, subject)

    assert HTTP_403_FORBIDDEN == response.status_code


def test_user_without_permission_cannot_update_attribute_set(client, attribute_set, subject):
    response = update_attribute_set(client, attribute_set, subject)

    assert HTTP_403_FORBIDDEN == response.status_code


def test_anonymous_user_cannot_retrieve_attribute_set(anonymous_client, attribute_set, subject):
    response = retrieve_attribute_set(anonymous_client, subject)

    assert HTTP_403_FORBIDDEN == response.status_code


def test_anonymous_user_can_update_attribute_set(anonymous_client, attribute_set, subject):
    response = update_attribute_set(anonymous_client, attribute_set, subject)

    assert HTTP_403_FORBIDDEN == response.status_code


@pytest.mark.skip
def test_create_attribute_set_if_it_does_not_exist(django_db_reset_sequences, client, user,
                                                   attribute_schema_v2):
    view_permission = Permission.objects.get(codename='view_attributeset')
    user.user_permissions.add(view_permission)

    subject = baker.make('subjects.Subject')

    response = retrieve_attribute_set(client, subject)

    expected = {
        'attributes': {},
        'attribute_schema': AttributeSchemaSerializer(attribute_schema_v2).data
    }

    assert HTTP_200_OK == response.status_code
    assert expected == response.json()


def test_update_categorized_attribute_without_permission(client, user,
                                                         attribute_set_with_categories, subject):
    user.user_permissions.add(
        Permission.objects.get(codename='change_subject'),
        Permission.objects.get(codename='change_attributeset'),
    )

    response = client.put(
        reverse('attributeset-detail', kwargs=dict(pk=subject.id)),
        data={
            'attribute_schema': attribute_set_with_categories.attribute_schema.pk,
            'attributes': {
                'category1': {'attribute12': 99}
            },
        },
        format='json',
    )

    assert HTTP_403_FORBIDDEN == response.status_code


def test_update_categorized_attribute_with_permission(client, user,
                                                      attribute_set_with_categories, subject):
    user.user_permissions.add(
        Permission.objects.get(codename='change_subject'),
        Permission.objects.get(codename='change_attributeset'),
        Permission.objects.get(codename='change_attribute_category_category1'),
    )

    response = client.put(
        reverse('attributeset-detail', kwargs=dict(pk=subject.id)),
        data={
            'attribute_schema': attribute_set_with_categories.attribute_schema.pk,
            'attributes': {
                'category1': {'attribute12': 99}
            },
        },
        format='json',
    )

    assert HTTP_200_OK == response.status_code


def retrieve_attribute_set(client, subject):
    return client.get(reverse('attributeset-detail', kwargs=dict(pk=subject.id)))


def update_attribute_set(client, attribute_set, subject):
    return client.put(
        reverse('attributeset-detail', kwargs=dict(pk=subject.id)),
        data={
            'attribute_schema': attribute_set.attribute_schema.pk,
            'attributes': {
                'attribute1': {},
                'attribute2': 'another string',
                'attribute3': 1.0
            },
        },
        format='json',
    )
