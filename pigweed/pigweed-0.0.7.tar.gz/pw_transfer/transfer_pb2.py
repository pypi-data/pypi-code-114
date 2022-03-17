# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pw_transfer/transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pw_transfer/transfer.proto',
  package='pw.transfer',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1apw_transfer/transfer.proto\x12\x0bpw.transfer\"\xe9\x03\n\x05\x43hunk\x12\x13\n\x0btransfer_id\x18\x01 \x01(\r\x12\x1a\n\rpending_bytes\x18\x02 \x01(\rH\x00\x88\x01\x01\x12!\n\x14max_chunk_size_bytes\x18\x03 \x01(\rH\x01\x88\x01\x01\x12#\n\x16min_delay_microseconds\x18\x04 \x01(\rH\x02\x88\x01\x01\x12\x0e\n\x06offset\x18\x05 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x1c\n\x0fremaining_bytes\x18\x07 \x01(\x04H\x03\x88\x01\x01\x12\x13\n\x06status\x18\x08 \x01(\rH\x04\x88\x01\x01\x12\x19\n\x11window_end_offset\x18\t \x01(\r\x12*\n\x04type\x18\n \x01(\x0e\x32\x17.pw.transfer.Chunk.TypeH\x05\x88\x01\x01\"a\n\x04Type\x12\x11\n\rTRANSFER_DATA\x10\x00\x12\x12\n\x0eTRANSFER_START\x10\x01\x12\x19\n\x15PARAMETERS_RETRANSMIT\x10\x02\x12\x17\n\x13PARAMETERS_CONTINUE\x10\x03\x42\x10\n\x0e_pending_bytesB\x17\n\x15_max_chunk_size_bytesB\x19\n\x17_min_delay_microsecondsB\x12\n\x10_remaining_bytesB\t\n\x07_statusB\x07\n\x05_type2s\n\x08Transfer\x12\x32\n\x04Read\x12\x12.pw.transfer.Chunk\x1a\x12.pw.transfer.Chunk(\x01\x30\x01\x12\x33\n\x05Write\x12\x12.pw.transfer.Chunk\x1a\x12.pw.transfer.Chunk(\x01\x30\x01\x62\x06proto3'
)



_CHUNK_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='pw.transfer.Chunk.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSFER_DATA', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRANSFER_START', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARAMETERS_RETRANSMIT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARAMETERS_CONTINUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=326,
  serialized_end=423,
)
_sym_db.RegisterEnumDescriptor(_CHUNK_TYPE)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='pw.transfer.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transfer_id', full_name='pw.transfer.Chunk.transfer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_bytes', full_name='pw.transfer.Chunk.pending_bytes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_chunk_size_bytes', full_name='pw.transfer.Chunk.max_chunk_size_bytes', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_delay_microseconds', full_name='pw.transfer.Chunk.min_delay_microseconds', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='pw.transfer.Chunk.offset', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='pw.transfer.Chunk.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remaining_bytes', full_name='pw.transfer.Chunk.remaining_bytes', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='pw.transfer.Chunk.status', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='window_end_offset', full_name='pw.transfer.Chunk.window_end_offset', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='pw.transfer.Chunk.type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHUNK_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_pending_bytes', full_name='pw.transfer.Chunk._pending_bytes',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_max_chunk_size_bytes', full_name='pw.transfer.Chunk._max_chunk_size_bytes',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_min_delay_microseconds', full_name='pw.transfer.Chunk._min_delay_microseconds',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_remaining_bytes', full_name='pw.transfer.Chunk._remaining_bytes',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_status', full_name='pw.transfer.Chunk._status',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_type', full_name='pw.transfer.Chunk._type',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=44,
  serialized_end=533,
)

_CHUNK.fields_by_name['type'].enum_type = _CHUNK_TYPE
_CHUNK_TYPE.containing_type = _CHUNK
_CHUNK.oneofs_by_name['_pending_bytes'].fields.append(
  _CHUNK.fields_by_name['pending_bytes'])
_CHUNK.fields_by_name['pending_bytes'].containing_oneof = _CHUNK.oneofs_by_name['_pending_bytes']
_CHUNK.oneofs_by_name['_max_chunk_size_bytes'].fields.append(
  _CHUNK.fields_by_name['max_chunk_size_bytes'])
_CHUNK.fields_by_name['max_chunk_size_bytes'].containing_oneof = _CHUNK.oneofs_by_name['_max_chunk_size_bytes']
_CHUNK.oneofs_by_name['_min_delay_microseconds'].fields.append(
  _CHUNK.fields_by_name['min_delay_microseconds'])
_CHUNK.fields_by_name['min_delay_microseconds'].containing_oneof = _CHUNK.oneofs_by_name['_min_delay_microseconds']
_CHUNK.oneofs_by_name['_remaining_bytes'].fields.append(
  _CHUNK.fields_by_name['remaining_bytes'])
_CHUNK.fields_by_name['remaining_bytes'].containing_oneof = _CHUNK.oneofs_by_name['_remaining_bytes']
_CHUNK.oneofs_by_name['_status'].fields.append(
  _CHUNK.fields_by_name['status'])
_CHUNK.fields_by_name['status'].containing_oneof = _CHUNK.oneofs_by_name['_status']
_CHUNK.oneofs_by_name['_type'].fields.append(
  _CHUNK.fields_by_name['type'])
_CHUNK.fields_by_name['type'].containing_oneof = _CHUNK.oneofs_by_name['_type']
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'pw_transfer.transfer_pb2'
  # @@protoc_insertion_point(class_scope:pw.transfer.Chunk)
  })
_sym_db.RegisterMessage(Chunk)



_TRANSFER = _descriptor.ServiceDescriptor(
  name='Transfer',
  full_name='pw.transfer.Transfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=535,
  serialized_end=650,
  methods=[
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='pw.transfer.Transfer.Read',
    index=0,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_CHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='pw.transfer.Transfer.Write',
    index=1,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_CHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSFER)

DESCRIPTOR.services_by_name['Transfer'] = _TRANSFER

# @@protoc_insertion_point(module_scope)
