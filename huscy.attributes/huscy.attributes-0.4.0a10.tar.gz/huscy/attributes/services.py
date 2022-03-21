import jsonschema
from django.db.transaction import atomic
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from huscy.attributes.models import AttributeSchema, AttributeSet
from huscy.pseudonyms.services import get_or_create_pseudonym


@atomic
def create_attribute_schema(schema):
    _create_attribute_category_permissions(schema)
    return AttributeSchema.objects.create(schema=schema)


def _create_attribute_category_permissions(schema):
    content_type = ContentType.objects.get_for_model(AttributeSchema)

    for name, value in schema['properties'].items():
        if value['type'] == 'object':
            Permission.objects.get_or_create(
                codename=f'change_attribute_category_{name}',
                name=f'Can change attribute category {name}',
                content_type=content_type
            )
            Permission.objects.get_or_create(
                codename=f'view_attribute_category_{name}',
                name=f'Can view attribute category {name}',
                content_type=content_type
            )


def filter_attributes_by_category_permissions(attribute_set, user):
    for node, node_description in attribute_set.attribute_schema.schema['properties'].items():
        if all([node_description['type'] == 'object',
                node in attribute_set.attributes,
                not user.has_perm(f'attributes.view_attribute_category_{node}')]):
            attribute_set.attributes.pop(node)
    return attribute_set


def get_attribute_schema(version=None):
    queryset = AttributeSchema.objects

    if version is None:
        try:
            return queryset.latest('pk')
        except AttributeSchema.DoesNotExist:
            return queryset.create()
    else:
        return queryset.get(pk=version)


def get_or_create_attribute_set(subject):
    pseudonym = get_or_create_pseudonym(subject, 'attributes.attributeset')

    attribute_set, created = AttributeSet.objects.get_or_create(pseudonym=pseudonym.code)
    return attribute_set


def update_attribute_set(attribute_set, attributes, attribute_schema=None):
    if attribute_schema:
        if attribute_schema.pk < attribute_set.attribute_schema.pk:
            raise Exception('New version for attribute schema must be greater than or equals with '
                            'current attribute schema version.')
        attribute_set.attribute_schema = AttributeSchema.objects.get(pk=attribute_schema.pk)

    _dict_merge(attribute_set.attributes, attributes)
    jsonschema.validate(attribute_set.attributes, attribute_set.attribute_schema.schema)

    attribute_set.save()
    return attribute_set


def _dict_merge(source_dict, merge_dict):
    for key, value in merge_dict.items():
        if key in source_dict and isinstance(source_dict[key], dict) and isinstance(value, dict):
            _dict_merge(source_dict[key], value)
        else:
            source_dict[key] = value
