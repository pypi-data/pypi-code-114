import functools
from functools import wraps
from typing import Callable

from django.conf.urls import url
from django.db.models import fields as dg_fields
from django.http.response import HttpResponseBase

from rest_framework import response, status
from rest_framework.exceptions import APIException
from rest_framework.serializers import SerializerMetaclass, Serializer, ListSerializer
from rest_framework.relations import RelatedField, ManyRelatedField
from rest_framework import fields as rf_fields

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema

from django_grpc_framework import proto_serializers
from django_grpc_framework.services import Service


__all__ = ["SerializerHandler"]


def upper(name):
    def _upper(name): return f"{name[0].upper()}{name[1:]}"
    new_name = ""
    for i in name.split("_"):
        new_name += _upper(i)
    return new_name


def instance(obj): return obj() if isinstance(obj, Callable) else obj


PROTO_TYPE_MAP = {
    rf_fields.IntegerField: "int32",
    rf_fields.FloatField: "float",
    rf_fields.DecimalField: "string",
    rf_fields.CharField: "string",
    rf_fields.UUIDField: "string",
    rf_fields.DateField: "string",
    rf_fields.TimeField: "string",
    rf_fields.DateTimeField: "string",
    rf_fields.BooleanField: "bool",

    dg_fields.IntegerField: "int32",
    dg_fields.AutoField: "int32",
    dg_fields.FloatField: "float",
    dg_fields.DecimalField: "string",
    dg_fields.CharField: "string",
    dg_fields.UUIDField: "string",
    dg_fields.DateField: "string",
    dg_fields.TimeField: "string",
    dg_fields.DateTimeField: "string",
    dg_fields.BooleanField: "bool",

    dg_fields.BinaryField: "bytes",
    dg_fields.TextField: "string",
    dg_fields.GenericIPAddressField: "string",
    dg_fields.IPAddressField: "string",
    dg_fields.FilePathField: "string",

    int: "int32",
    float: "float",
    str: "string",
    bool: "bool",
}


class SerializerHandler:
    proto_services = {}
    lazy_callbacks = []

    def __init__(self, package, add_grpc_prefix):
        self.add_grpc_prefix = add_grpc_prefix
        self.package = package

    @property
    def pb2(self):
        return __import__(f"{self.package}_pb2")

    @property
    def pb2_grpc(self):
        return __import__(f"{self.package}_pb2_grpc")

    def get_grpc_handlers(self, server):
        for callback in self.lazy_callbacks:
            callback()
        for service, item in self.proto_services.items():
            getattr(self.pb2_grpc, f"add_{service}Servicer_to_server")(
                item['cls'].as_servicer(), server)

    def get_empty(self):
        return getattr(self.pb2, "Empty")()

    def get_proto_cls(self, serializers):
        clsname = serializers.__class__.proto_cls_name
        if hasattr(self.pb2, clsname):
            return getattr(self.pb2, clsname)

    def generate_proto(self):
        def json_to_message(data, indent=''):
            if "message" in data["type"]:
                fields = [""]
                count = 0
                for i, value in enumerate(data["fields"]):
                    count_content = ''
                    if not "message" in value["type"]:
                        count += 1
                        count_content = f" = {count};"

                    message_content = json_to_message(value, indent + '\t')
                    field_content = f'{message_content}{count_content}'
                    fields.append(field_content)
                fields_content = f"\n".join(fields)
                return f'{indent}{data["type"]} {data["name"]} {{{fields_content}\n{indent}}}'

            return f'{indent}{data["type"]} {data["name"]}'

        services = [""]
        messages = [""]
        for service, item in self.proto_services.items():
            methods = [""]
            for method in item["methods"]:
                methods.append(
                    f'rpc {method["name"]}( {method["request"]["name"]} ) returns ( {method["response"]["name"]} ) {{}}')
                messages.append(json_to_message(method["request"]))
                messages.append(json_to_message(method["response"]))

            methods_content = "\n\t".join(methods)
            services.append(f'service {service}{{{methods_content}\n}}')

        services_content = "\n".join(services)
        messages_content = "\n\n".join(messages)
        return f'syntax = "proto3";\npackage {self.package};\n{services_content}\n{messages_content}'

    def to_proto_message(self, serializers, prefix=''):
        if serializers is None:
            return {
                "name": "Empty",
                "type": "message",
                "fields": []
            }
        if isinstance(serializers, ListSerializer):
            serializers = serializers.child

        message_name = upper(prefix + serializers.__class__.__name__)
        message = {
            "name": message_name,
            "type": "message",
            "fields": []
        }
        serializers.__class__.proto_cls_name = message_name

        for fieldname, value in serializers.get_fields().items():
            item = {
                "name": fieldname,
                "type": "message",
                "fields": []
            }
            if isinstance(value, Serializer):
                message["fields"].append(self.to_proto_message(value))
                item["type"] = value.__class__.__name__
            elif hasattr(value, 'child'):
                message["fields"].append(self.to_proto_message(value.child))
                item["type"] = value.child.__class__.__name__
            elif isinstance(value, rf_fields.ChoiceField):
                item["type"] = PROTO_TYPE_MAP.get(type(value.choices[0]))
            elif isinstance(value, RelatedField):
                value = value.queryset.model._meta.pk.target_field
                item["type"] = PROTO_TYPE_MAP.get(type(value))
            elif isinstance(value, ManyRelatedField):
                value = value.child_relation.queryset.model._meta.pk
                item["type"] = PROTO_TYPE_MAP.get(type(value))
                item["type"] = f'repeated {item["type"]}'
            else:
                item["type"] = PROTO_TYPE_MAP.get(type(value)) or type(value)
            if hasattr(value, 'many') and getattr(value, 'many'):
                item["type"] = f'repeated {item["type"]}'
            message["fields"].append(item)
        return message

    def prepare_proto(self, func, request_serializers, response_serializers, handler=None):
        appname = func.__module__.split(".")[0]
        classname, funcname = func.__qualname__.split(".")

        appname = upper(appname)
        funcname = upper(funcname)
        classname = upper(classname)

        servicename = classname
        prefix = ''
        if self.add_grpc_prefix:
            servicename = f"{appname}{classname}Contoller"
            prefix = servicename

        self.proto_services.setdefault(servicename, {
            "cls": None,
            "methods": []
        })
        self.lazy_callbacks.append(functools.partial(
            self.support_proto_serializers, request_serializers))
        self.lazy_callbacks.append(functools.partial(
            self.support_proto_serializers, response_serializers))

        method = {
            "name": funcname,
            "request": self.to_proto_message(
                instance(request_serializers), prefix),
            "response": self.to_proto_message(
                instance(response_serializers), prefix)
        }

        self.proto_services[servicename]["cls"] = self.proto_services[servicename]["cls"] or type(
            servicename, (Service,), {})

        setattr(self.proto_services[servicename]["cls"], funcname, handler)

        self.proto_services[servicename]["methods"].append(method)
        return self.proto_services[servicename]["cls"], funcname

    def support_proto_serializers(self, serializers):
        if serializers is None:
            return

        class T(proto_serializers.ModelProtoSerializer, serializers):
            pass

        proto_cls = self.get_proto_cls(instance(serializers))
        if hasattr(T, "Meta"):
            T.Meta.proto_class = proto_cls
        else:
            class Meta:
                proto_class = proto_cls
            T.Meta = Meta

        serializers.proto_cls = T

    def serializer(self, request_serializers=None, response_serializers=None, add_swagger=False, add_grpc=False):
        '''支持接口序列化
            另外支持生成 swagger、grpc 接口

        @param: request_serializers
            请求字段序列化
        @param: response_serializers
            返回字段序列化
        @param: add_swagger
            值为dict类型，该值为 swagger_auto_schema 的关键字参数

        '''
        response_code = status.HTTP_200_OK
        if response_serializers is None:
            response_code = status.HTTP_204_NO_CONTENT

        def wrapper(f):
            if add_grpc:
                @wraps(f)
                def service(_, request, context):
                    s = request_serializers.proto_cls(message=request)
                    s.is_valid()
                    request = type("tmp", (), {
                        "data": s.data,
                        "query_params": {}
                    })
                    res = f(_, request)
                    if response_serializers is None:
                        return self.get_empty()

                    if isinstance(res, HttpResponseBase):
                        res = res.data

                    res = response_serializers.proto_cls().data_to_message(res)
                    return res
                self.prepare_proto(f, request_serializers,
                                   response_serializers, service)

            if add_swagger:
                swagger_kw = {
                    "request_body": request_serializers,
                    "responses": {
                        response_code: response_serializers or ''
                    }
                }
                if isinstance(add_swagger, dict):
                    swagger_kw.update(add_swagger)
                swagger_auto_schema(**swagger_kw)(f)

            @wraps(f)
            def wrapped(self, request, *args, **kw):
                if isinstance(request_serializers, SerializerMetaclass):
                    reqinfo = request_serializers(data=request.data)
                    reqinfo.is_valid(raise_exception=True)
                    request.data.update(reqinfo.data)

                res = f(self, request, *args, **kw)

                if not isinstance(res, HttpResponseBase):
                    res = response.Response(
                        data=res,
                        status=response_code,
                        content_type="application/json"
                    )

                if isinstance(response_serializers, SerializerMetaclass):
                    if isinstance(res.data, dict):
                        resinfo = response_serializers(data=res.data)
                        try:
                            resinfo.is_valid(raise_exception=True)
                        except Exception as e:
                            raise APIException(e)
                        res.data = resinfo.data
                return res

            return wrapped
        return wrapper

    def get_swagger_urls(self, doc_title, version='', public=True):
        swagger_views = get_schema_view(
            openapi.Info(
                title=doc_title,
                default_version=version,
            ),
            public=public
        )

        return [
            url(r'^swagger(?P<format>\.json|\.yaml)$',
                swagger_views.without_ui(cache_timeout=0),
                name='schema-json'),
            url(r'^swagger/$',
                swagger_views.with_ui('swagger', cache_timeout=0),
                name='schema-swagger-ui'),
            url('redoc/', swagger_views.with_ui('redoc',
                cache_timeout=0), name='schema-redoc')
        ]
