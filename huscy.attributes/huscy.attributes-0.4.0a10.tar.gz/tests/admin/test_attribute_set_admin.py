import pytest

from django.contrib.admin.sites import AdminSite

from huscy.attributes.admin import AttributeSetAdmin
from huscy.attributes.models import AttributeSet

pytestmark = pytest.mark.django_db


@pytest.fixture
def attribute_set_admin():
    return AttributeSetAdmin(model=AttributeSet, admin_site=AdminSite())


def test_attribute_schema(attribute_set_admin, attribute_set):
    assert attribute_set_admin._attribute_schema(attribute_set) == attribute_set.attribute_schema.id


def test_has_add_permission(attribute_set_admin):
    assert attribute_set_admin.has_add_permission(request=None) is False


def test_has_change_permission(attribute_set_admin):
    assert attribute_set_admin.has_change_permission(request=None) is False


def test_has_delete_permission(attribute_set_admin):
    assert attribute_set_admin.has_delete_permission(request=None) is False
