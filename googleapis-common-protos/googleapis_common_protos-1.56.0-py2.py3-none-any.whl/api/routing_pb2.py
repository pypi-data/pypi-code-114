# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/routing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/routing.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\014RoutingProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x18google/api/routing.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"G\n\x0bRoutingRule\x12\x38\n\x12routing_parameters\x18\x02 \x03(\x0b\x32\x1c.google.api.RoutingParameter"8\n\x10RoutingParameter\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x15\n\rpath_template\x18\x02 \x01(\t:K\n\x07routing\x12\x1e.google.protobuf.MethodOptions\x18\xb1\xca\xbc" \x01(\x0b\x32\x17.google.api.RoutingRuleBj\n\x0e\x63om.google.apiB\x0cRoutingProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3',
    dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR],
)


ROUTING_FIELD_NUMBER = 72295729
routing = _descriptor.FieldDescriptor(
    name="routing",
    full_name="google.api.routing",
    index=0,
    number=72295729,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)


_ROUTINGRULE = _descriptor.Descriptor(
    name="RoutingRule",
    full_name="google.api.RoutingRule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="routing_parameters",
            full_name="google.api.RoutingRule.routing_parameters",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=145,
)


_ROUTINGPARAMETER = _descriptor.Descriptor(
    name="RoutingParameter",
    full_name="google.api.RoutingParameter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="field",
            full_name="google.api.RoutingParameter.field",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="path_template",
            full_name="google.api.RoutingParameter.path_template",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=147,
    serialized_end=203,
)

_ROUTINGRULE.fields_by_name["routing_parameters"].message_type = _ROUTINGPARAMETER
DESCRIPTOR.message_types_by_name["RoutingRule"] = _ROUTINGRULE
DESCRIPTOR.message_types_by_name["RoutingParameter"] = _ROUTINGPARAMETER
DESCRIPTOR.extensions_by_name["routing"] = routing
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoutingRule = _reflection.GeneratedProtocolMessageType(
    "RoutingRule",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROUTINGRULE,
        "__module__": "google.api.routing_pb2"
        # @@protoc_insertion_point(class_scope:google.api.RoutingRule)
    },
)
_sym_db.RegisterMessage(RoutingRule)

RoutingParameter = _reflection.GeneratedProtocolMessageType(
    "RoutingParameter",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROUTINGPARAMETER,
        "__module__": "google.api.routing_pb2"
        # @@protoc_insertion_point(class_scope:google.api.RoutingParameter)
    },
)
_sym_db.RegisterMessage(RoutingParameter)

routing.message_type = _ROUTINGRULE
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(routing)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
