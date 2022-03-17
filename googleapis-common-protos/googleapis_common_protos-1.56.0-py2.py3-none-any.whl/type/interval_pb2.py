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
# source: google/type/interval.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/type/interval.proto",
    package="google.type",
    syntax="proto3",
    serialized_options=b"\n\017com.google.typeB\rIntervalProtoP\001Z<google.golang.org/genproto/googleapis/type/interval;interval\370\001\001\242\002\003GTP",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1agoogle/type/interval.proto\x12\x0bgoogle.type\x1a\x1fgoogle/protobuf/timestamp.proto"h\n\x08Interval\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampBi\n\x0f\x63om.google.typeB\rIntervalProtoP\x01Z<google.golang.org/genproto/googleapis/type/interval;interval\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3',
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR],
)


_INTERVAL = _descriptor.Descriptor(
    name="Interval",
    full_name="google.type.Interval",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="start_time",
            full_name="google.type.Interval.start_time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="end_time",
            full_name="google.type.Interval.end_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=76,
    serialized_end=180,
)

_INTERVAL.fields_by_name[
    "start_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INTERVAL.fields_by_name[
    "end_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name["Interval"] = _INTERVAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Interval = _reflection.GeneratedProtocolMessageType(
    "Interval",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTERVAL,
        "__module__": "google.type.interval_pb2"
        # @@protoc_insertion_point(class_scope:google.type.Interval)
    },
)
_sym_db.RegisterMessage(Interval)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
