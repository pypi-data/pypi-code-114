import pytest

from django.contrib.admin.sites import AdminSite

from huscy.attributes.admin import AttributeSchemaAdmin
from huscy.attributes.models import AttributeSchema

pytestmark = pytest.mark.django_db


@pytest.fixture
def attribute_schema_admin():
    return AttributeSchemaAdmin(model=AttributeSchema, admin_site=AdminSite())


def test_has_change_permission(attribute_schema_admin):
    assert attribute_schema_admin.has_change_permission(request=None) is False


def test_has_delete_permission(attribute_schema_admin):
    assert attribute_schema_admin.has_delete_permission(request=None) is False
