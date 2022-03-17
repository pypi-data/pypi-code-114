# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: archipelagos/common/protobuf/common/data/timeseries/TimeSeriesMetadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from archipelagos.common.protobuf.common import Timestamp_pb2 as archipelagos_dot_common_dot_protobuf_dot_common_dot_Timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLarchipelagos/common/protobuf/common/data/timeseries/TimeSeriesMetadata.proto\x12\x33\x61rchipelagos.common.protobuf.common.data.timeseries\x1a\x33\x61rchipelagos/common/protobuf/common/Timestamp.proto\"\xd4\x06\n\x12TimeSeriesMetadata\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x0f\n\x07summary\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12g\n\x08\x66\x65\x61tures\x18\x07 \x03(\x0b\x32U.archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata.FeaturesEntry\x12\x11\n\tfrequency\x18\x08 \x01(\t\x12k\n\nproperties\x18\t \x03(\x0b\x32W.archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata.PropertiesEntry\x12\x0f\n\x07premium\x18\n \x01(\x08\x12?\n\x07\x63reated\x18\x0b \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x12>\n\x06\x65\x64ited\x18\x0c \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x12\x14\n\x0crefreshedSet\x18\r \x01(\x08\x12\x41\n\trefreshed\x18\x0e \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x12\x19\n\x11oldestDateTimeSet\x18\x0f \x01(\x08\x12\x46\n\x0eoldestDateTime\x18\x10 \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x12\x46\n\x0enewestDateTime\x18\x11 \x01(\x0b\x32..archipelagos.common.protobuf.common.Timestamp\x1a/\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42N\n3archipelagos.common.protobuf.common.data.timeseriesB\x17TimeSeriesMetadataProtob\x06proto3')



_TIMESERIESMETADATA = DESCRIPTOR.message_types_by_name['TimeSeriesMetadata']
_TIMESERIESMETADATA_FEATURESENTRY = _TIMESERIESMETADATA.nested_types_by_name['FeaturesEntry']
_TIMESERIESMETADATA_PROPERTIESENTRY = _TIMESERIESMETADATA.nested_types_by_name['PropertiesEntry']
TimeSeriesMetadata = _reflection.GeneratedProtocolMessageType('TimeSeriesMetadata', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TIMESERIESMETADATA_FEATURESENTRY,
    '__module__' : 'archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata_pb2'
    # @@protoc_insertion_point(class_scope:archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata.FeaturesEntry)
    })
  ,

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TIMESERIESMETADATA_PROPERTIESENTRY,
    '__module__' : 'archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata_pb2'
    # @@protoc_insertion_point(class_scope:archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _TIMESERIESMETADATA,
  '__module__' : 'archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata_pb2'
  # @@protoc_insertion_point(class_scope:archipelagos.common.protobuf.common.data.timeseries.TimeSeriesMetadata)
  })
_sym_db.RegisterMessage(TimeSeriesMetadata)
_sym_db.RegisterMessage(TimeSeriesMetadata.FeaturesEntry)
_sym_db.RegisterMessage(TimeSeriesMetadata.PropertiesEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3archipelagos.common.protobuf.common.data.timeseriesB\027TimeSeriesMetadataProto'
  _TIMESERIESMETADATA_FEATURESENTRY._options = None
  _TIMESERIESMETADATA_FEATURESENTRY._serialized_options = b'8\001'
  _TIMESERIESMETADATA_PROPERTIESENTRY._options = None
  _TIMESERIESMETADATA_PROPERTIESENTRY._serialized_options = b'8\001'
  _TIMESERIESMETADATA._serialized_start=187
  _TIMESERIESMETADATA._serialized_end=1039
  _TIMESERIESMETADATA_FEATURESENTRY._serialized_start=941
  _TIMESERIESMETADATA_FEATURESENTRY._serialized_end=988
  _TIMESERIESMETADATA_PROPERTIESENTRY._serialized_start=990
  _TIMESERIESMETADATA_PROPERTIESENTRY._serialized_end=1039
# @@protoc_insertion_point(module_scope)
