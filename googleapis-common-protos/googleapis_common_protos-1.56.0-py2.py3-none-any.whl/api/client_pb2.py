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
# source: google/api/client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/client.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\013ClientProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n\x17google/api/client.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto:9\n\x10method_signature\x12\x1e.google.protobuf.MethodOptions\x18\x9b\x08 \x03(\t:6\n\x0c\x64\x65\x66\x61ult_host\x12\x1f.google.protobuf.ServiceOptions\x18\x99\x08 \x01(\t:6\n\x0coauth_scopes\x12\x1f.google.protobuf.ServiceOptions\x18\x9a\x08 \x01(\tBi\n\x0e\x63om.google.apiB\x0b\x43lientProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3",
    dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR],
)


METHOD_SIGNATURE_FIELD_NUMBER = 1051
method_signature = _descriptor.FieldDescriptor(
    name="method_signature",
    full_name="google.api.method_signature",
    index=0,
    number=1051,
    type=9,
    cpp_type=9,
    label=3,
    has_default_value=False,
    default_value=[],
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
DEFAULT_HOST_FIELD_NUMBER = 1049
default_host = _descriptor.FieldDescriptor(
    name="default_host",
    full_name="google.api.default_host",
    index=1,
    number=1049,
    type=9,
    cpp_type=9,
    label=1,
    has_default_value=False,
    default_value=b"".decode("utf-8"),
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
OAUTH_SCOPES_FIELD_NUMBER = 1050
oauth_scopes = _descriptor.FieldDescriptor(
    name="oauth_scopes",
    full_name="google.api.oauth_scopes",
    index=2,
    number=1050,
    type=9,
    cpp_type=9,
    label=1,
    has_default_value=False,
    default_value=b"".decode("utf-8"),
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)

DESCRIPTOR.extensions_by_name["method_signature"] = method_signature
DESCRIPTOR.extensions_by_name["default_host"] = default_host
DESCRIPTOR.extensions_by_name["oauth_scopes"] = oauth_scopes
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(
    method_signature
)
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(default_host)
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(oauth_scopes)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
