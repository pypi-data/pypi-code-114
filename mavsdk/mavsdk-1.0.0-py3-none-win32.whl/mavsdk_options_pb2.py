# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mavsdk_options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14mavsdk_options.proto\x12\x0emavsdk.options\x1a google/protobuf/descriptor.proto**\n\tAsyncType\x12\t\n\x05\x41SYNC\x10\x00\x12\x08\n\x04SYNC\x10\x01\x12\x08\n\x04\x42OTH\x10\x02:6\n\rdefault_value\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\t:0\n\x07\x65psilon\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x01:O\n\nasync_type\x12\x1e.google.protobuf.MethodOptions\x18\xd0\x86\x03 \x01(\x0e\x32\x19.mavsdk.options.AsyncType:3\n\tis_finite\x12\x1e.google.protobuf.MethodOptions\x18\xd1\x86\x03 \x01(\x08\x42\x10\n\x0eoptions.mavsdkb\x06proto3')

_ASYNCTYPE = DESCRIPTOR.enum_types_by_name['AsyncType']
AsyncType = enum_type_wrapper.EnumTypeWrapper(_ASYNCTYPE)
ASYNC = 0
SYNC = 1
BOTH = 2

DEFAULT_VALUE_FIELD_NUMBER = 50000
default_value = DESCRIPTOR.extensions_by_name['default_value']
EPSILON_FIELD_NUMBER = 50001
epsilon = DESCRIPTOR.extensions_by_name['epsilon']
ASYNC_TYPE_FIELD_NUMBER = 50000
async_type = DESCRIPTOR.extensions_by_name['async_type']
IS_FINITE_FIELD_NUMBER = 50001
is_finite = DESCRIPTOR.extensions_by_name['is_finite']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(default_value)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(epsilon)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(async_type)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(is_finite)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016options.mavsdk'
  _ASYNCTYPE._serialized_start=74
  _ASYNCTYPE._serialized_end=116
# @@protoc_insertion_point(module_scope)
