from urllib.parse import urlencode, ParseResult

from django.db import models
from django.urls import reverse
from drf_spectacular.drainage import add_trace_message, has_override, get_override, warn
from drf_spectacular.extensions import OpenApiFilterExtension
from drf_spectacular.generators import SchemaGenerator as SpectacularSchemaGenerator
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import ComponentRegistry, is_list_serializer, is_serializer, build_array_type, \
    append_meta, force_instance, build_object_type, get_view_model, is_basic_type, build_basic_type
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from form_schema_generator.settings import form_schema_generator_settings


class UISchemaGenerator(SpectacularSchemaGenerator):

    def get_view(self, api_url, api_method):
        endpoints = self.get_all_endpoints()
        for path, path_regex, method, view in endpoints:
            if api_url == path and api_method.upper() == method:
                return view

        return None

    # def get_serializer_by_endpoint(self, api_url, api_method):
    #     api_serializer = None
    #     endpoints = self.get_all_endpoints()
    #     for path, path_regex, method, view in endpoints:
    #         if api_url == path and api_method.upper() == method:
    #             api_serializer = view.schema.get_request_serializer()
    #             break
    #
    #     return api_serializer

    def get_all_endpoints(self):
        self._initialise_endpoints()
        return self._get_paths_and_endpoints()


class UIAutoSchema(AutoSchema):

    def __init__(self):
        super().__init__()
        self.registry = ComponentRegistry()

    def _map_serializer_field(self, field, direction, bypass_extensions=False):
        result = super()._map_serializer_field(field, direction, bypass_extensions)
        meta = self._get_serializer_field_meta(field)

        if is_list_serializer(field) and is_serializer(field.child):
            component = self.resolve_serializer(field.child, direction)
            result = append_meta(build_array_type(component.schema), meta) if component else None
        elif is_serializer(field):
            component = self.resolve_serializer(field, direction)
            result = append_meta(component.schema, meta) if component else None
        elif isinstance(field, serializers.MultipleChoiceField):
            result = append_meta(build_array_type(build_choice_field(field)), meta)
        elif isinstance(field, serializers.ChoiceField):
            result = append_meta(build_choice_field(field), meta)

        # TODO: 릴레이션필드의 url형태로 제공할 수 있도록
        # Related fields.
        # elif isinstance(field, serializers.PrimaryKeyRelatedField):
        #     if getattr(field, 'queryset', None) is not None:
        #         meta['x-fields-url'] = get_fields_api_url(field)
        #         model_field = field.queryset.model._meta.pk
        #         required = set()
        #         if field.required:
        #             required.add(model_field.name)
        #         # 나중에 바꿔줘야할 수도 있음 ... 복합키는 어떻게 처리하지.. 튜플로???
        #         properties = {model_field.name: build_choice_field(field)}
        #         result = append_meta(build_object_type(properties=properties, required=required), meta)

        return result


def get_fields_api_url(field):
    if getattr(field, 'queryset', None) is None:
        return ""
    serializer = field.parent
    path = reverse(form_schema_generator_settings['MODEL_CHOICES_API'])
    query = urlencode(
        {
            'serializer': f'{serializer.__module__}.{serializer.__class__.__name__}',
            'source': field.source
        }
    )
    return ParseResult(path=path, query=query).geturl()


def build_choice_field(field):
    one_of = [{'const': key, 'title': value} for key, value in field.choices.items()]
    schema = {
        'type': 'string',
        'oneOf': one_of
    }
    return schema


def get_schema(url, method):
    # TODO: singletone 으로 uiautoschema, uischemagenerator 만들기
    # TODO: list 형태일 때와 나머지일때 분기처리
    auto_schema = UIAutoSchema()
    view = UISchemaGenerator().get_view(url, method)
    auto_schema.view = view

    if view.schema._is_list_view():
        filter_backends = getattr(view, 'filter_backends', [])
        return get_filter_schema(filter_backends, auto_schema)
    else:
        serializer_class = view.schema.get_request_serializer()
        serializer = force_instance(serializer_class)
        return get_serializer_schema(serializer, auto_schema)


def get_schema_operation_parameters(filter_extension, auto_schema):
    model = get_view_model(auto_schema.view)
    if not model:
        return []

    filterset_class = filter_extension.target.get_filterset_class(auto_schema.view, model.objects.none())
    if not filterset_class:
        return []

    results = []
    with add_trace_message(filterset_class.__name__):
        for field_name, filter_field in filterset_class.base_filters.items():
            result = filter_extension.resolve_filter_field(
                auto_schema, model, filterset_class, field_name, filter_field
            )
            for r in result:
                if not r['schema'].get('title'):
                    model_field = filter_extension._get_model_field(filter_field, model)
                    r['schema']['title'] = r.get('description') or \
                                           auto_schema._map_model_field(model_field, None).get('title') or \
                                           r['name']

            results += result
    return results


def get_filter_schema(filter_backends, auto_schema):
    parameters = []
    for filter_backend in filter_backends:
        filter_extension = OpenApiFilterExtension.get_match(filter_backend())
        if filter_extension:
            parameters += get_schema_operation_parameters(filter_extension, auto_schema)

    schema = build_object_type(
        properties={param['name']: param['schema'] for param in parameters}
    )
    schema['title'] = '필터'
    return schema


def get_serializer_schema(serializer, auto_schema):
    schema = {}
    if is_list_serializer(serializer):
        child = serializer.child
        if is_serializer(child):
            component = auto_schema.resolve_serializer(child, 'request')
            schema = build_array_type(component.schema)
        else:
            schema = build_array_type(auto_schema._map_serializer_field(child, 'request'))
        schema['title'] = get_serializer_title(child)
    elif is_serializer(serializer):
        component = auto_schema.resolve_serializer(serializer, 'request')
        schema = getattr(component, 'schema', {})
        schema['title'] = get_serializer_title(serializer)

    return schema


def get_serializer_title(serializer):
    serializer_meta = getattr(serializer, 'Meta', False)
    if getattr(serializer_meta, 'verbose_name', False):
        title = getattr(serializer_meta, 'verbose_name')
    elif type(serializer) == ModelSerializer:
        title = serializer_meta.model._meta.verbose_name
    else:
        title = type(serializer).__name__
        if title.endswith('Serializer'):
            title = title[:-10]

    return title


def get_url_choices():
    schema_generator = UISchemaGenerator()
    endpoints = schema_generator.get_all_endpoints()
    return set([
        endpoint[0]
        for endpoint in endpoints
        if endpoint[2] in ['PUT', 'PATCH', 'POST']
    ])


FORM_GENERATABLE_URLS = set()
