# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: archipelagos/common/protobuf/common/data/timeseries/TimeSeriesRequest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from archipelagos.common.protobuf.common import Timestamp_pb2 as archipelagos_dot_common_dot_protobuf_dot_common_dot_Timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKarchipelagos/common/protobuf/common/data/timeseries/TimeSeriesRequest.proto\x12\x33\x61rchipelagos.common.protobuf.common.data.timeseries\x1a\x33\x61rchipelagos/common/protobuf/common/Timestamp.proto\"\xcc\x03\n\x11TimeSeriesRequest\x12\x0e\n\x06\x61piKey\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x10\n\x08startSet\x18\x05 \x01(\x08\x12=\n\x05start\x18\x06 \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x12\x0e\n\x06\x65ndSet\x18\x07 \x01(\x08\x12;\n\x03\x65nd\x18\x08 \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x12\x13\n\x0b\x66\x65\x61turesSet\x18\t \x01(\x08\x12\x10\n\x08\x66\x65\x61tures\x18\n \x03(\t\x12\x0f\n\x07maxSize\x18\x0b \x01(\x12\x12\x11\n\tascending\x18\x0c \x01(\x08\x12\x64\n\x07\x66ilters\x18\r \x03(\x0b\x32S.archipelagos.common.protobuf.common.data.timeseries.TimeSeriesRequest.FiltersEntry\x1a.\n\x0c\x46iltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42M\n3archipelagos.common.protobuf.common.data.timeseriesB\x16TimeSeriesRequestProtob\x06proto3')



_TIMESERIESREQUEST = DESCRIPTOR.message_types_by_name['TimeSeriesRequest']
_TIMESERIESREQUEST_FILTERSENTRY = _TIMESERIESREQUEST.nested_types_by_name['FiltersEntry']
TimeSeriesRequest = _reflection.GeneratedProtocolMessageType('TimeSeriesRequest', (_message.Message,), {

  'FiltersEntry' : _reflection.GeneratedProtocolMessageType('FiltersEntry', (_message.Message,), {
    'DESCRIPTOR' : _TIMESERIESREQUEST_FILTERSENTRY,
    '__module__' : 'archipelagos.common.protobuf.common.data.timeseries.TimeSeriesRequest_pb2'
    # @@protoc_insertion_point(class_scope:archipelagos.common.protobuf.common.data.timeseries.TimeSeriesRequest.FiltersEntry)
    })
  ,
  'DESCRIPTOR' : _TIMESERIESREQUEST,
  '__module__' : 'archipelagos.common.protobuf.common.data.timeseries.TimeSeriesRequest_pb2'
  # @@protoc_insertion_point(class_scope:archipelagos.common.protobuf.common.data.timeseries.TimeSeriesRequest)
  })
_sym_db.RegisterMessage(TimeSeriesRequest)
_sym_db.RegisterMessage(TimeSeriesRequest.FiltersEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3archipelagos.common.protobuf.common.data.timeseriesB\026TimeSeriesRequestProto'
  _TIMESERIESREQUEST_FILTERSENTRY._options = None
  _TIMESERIESREQUEST_FILTERSENTRY._serialized_options = b'8\001'
  _TIMESERIESREQUEST._serialized_start=186
  _TIMESERIESREQUEST._serialized_end=646
  _TIMESERIESREQUEST_FILTERSENTRY._serialized_start=600
  _TIMESERIESREQUEST_FILTERSENTRY._serialized_end=646
# @@protoc_insertion_point(module_scope)
