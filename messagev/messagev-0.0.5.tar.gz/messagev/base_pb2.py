# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='messagev.base',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbase.proto\x12\rmessagev.base\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x03\n\x08\x45nvelope\x12\x15\n\rmajor_version\x18\x01 \x01(\r\x12\x15\n\rminor_version\x18\x02 \x01(\r\x12\x12\n\nmessage_id\x18\x03 \x01(\x0c\x12\x13\n\x0bresponse_to\x18\x04 \x01(\x0c\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0esender_node_id\x18\x06 \x01(\t\x12\x18\n\x10receiver_node_id\x18\x07 \x01(\t\x12\x12\n\nmodel_name\x18\x08 \x01(\t\x12\x0e\n\x06res_id\x18\t \x01(\x04\x12\x38\n\x0cmessage_type\x18\n \x01(\x0e\x32\".messagev.base.Envelope.TypeOption\x12\x14\n\x0cmessage_body\x18\x0b \x01(\x0c\"O\n\nTypeOption\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x43OMMAND\x10\x01\x12\x0c\n\x08RESPONSE\x10\x02\x12\x10\n\x0cNOTIFICATION\x10\x03\x12\x07\n\x03LOG\x10\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_ENVELOPE_TYPEOPTION = _descriptor.EnumDescriptor(
  name='TypeOption',
  full_name='messagev.base.Envelope.TypeOption',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMAND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOTIFICATION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=375,
  serialized_end=454,
)
_sym_db.RegisterEnumDescriptor(_ENVELOPE_TYPEOPTION)


_ENVELOPE = _descriptor.Descriptor(
  name='Envelope',
  full_name='messagev.base.Envelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major_version', full_name='messagev.base.Envelope.major_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor_version', full_name='messagev.base.Envelope.minor_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='messagev.base.Envelope.message_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_to', full_name='messagev.base.Envelope.response_to', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='messagev.base.Envelope.timestamp', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_node_id', full_name='messagev.base.Envelope.sender_node_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver_node_id', full_name='messagev.base.Envelope.receiver_node_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='messagev.base.Envelope.model_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='res_id', full_name='messagev.base.Envelope.res_id', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='messagev.base.Envelope.message_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_body', full_name='messagev.base.Envelope.message_body', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENVELOPE_TYPEOPTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=454,
)

_ENVELOPE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ENVELOPE.fields_by_name['message_type'].enum_type = _ENVELOPE_TYPEOPTION
_ENVELOPE_TYPEOPTION.containing_type = _ENVELOPE
DESCRIPTOR.message_types_by_name['Envelope'] = _ENVELOPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Envelope = _reflection.GeneratedProtocolMessageType('Envelope', (_message.Message,), {
  'DESCRIPTOR' : _ENVELOPE,
  '__module__' : 'base_pb2'
  # @@protoc_insertion_point(class_scope:messagev.base.Envelope)
  })
_sym_db.RegisterMessage(Envelope)


# @@protoc_insertion_point(module_scope)
