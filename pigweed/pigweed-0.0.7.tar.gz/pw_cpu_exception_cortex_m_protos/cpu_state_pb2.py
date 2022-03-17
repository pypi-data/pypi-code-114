# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pw_cpu_exception_cortex_m_protos/cpu_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pw_cpu_exception_cortex_m_protos/cpu_state.proto',
  package='pw.cpu_exception.cortex_m',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0pw_cpu_exception_cortex_m_protos/cpu_state.proto\x12\x19pw.cpu_exception.cortex_m\"\x89\x03\n\x0e\x41rmV7mCpuState\x12\n\n\x02pc\x18\x01 \x01(\r\x12\n\n\x02lr\x18\x02 \x01(\r\x12\x0b\n\x03psr\x18\x03 \x01(\r\x12\x0b\n\x03msp\x18\x04 \x01(\r\x12\x0b\n\x03psp\x18\x05 \x01(\r\x12\x12\n\nexc_return\x18\x06 \x01(\r\x12\x0c\n\x04\x63\x66sr\x18\x07 \x01(\r\x12\x0e\n\x06msplim\x18\x1b \x01(\r\x12\x0e\n\x06psplim\x18\x1c \x01(\r\x12\r\n\x05mmfar\x18\x08 \x01(\r\x12\x0c\n\x04\x62\x66\x61r\x18\t \x01(\r\x12\x0c\n\x04icsr\x18\n \x01(\r\x12\x0c\n\x04hfsr\x18\x19 \x01(\r\x12\r\n\x05shcsr\x18\x1a \x01(\r\x12\x0f\n\x07\x63ontrol\x18\x0b \x01(\r\x12\n\n\x02r0\x18\x0c \x01(\r\x12\n\n\x02r1\x18\r \x01(\r\x12\n\n\x02r2\x18\x0e \x01(\r\x12\n\n\x02r3\x18\x0f \x01(\r\x12\n\n\x02r4\x18\x10 \x01(\r\x12\n\n\x02r5\x18\x11 \x01(\r\x12\n\n\x02r6\x18\x12 \x01(\r\x12\n\n\x02r7\x18\x13 \x01(\r\x12\n\n\x02r8\x18\x14 \x01(\r\x12\n\n\x02r9\x18\x15 \x01(\r\x12\x0b\n\x03r10\x18\x16 \x01(\r\x12\x0b\n\x03r11\x18\x17 \x01(\r\x12\x0b\n\x03r12\x18\x18 \x01(\r\"^\n\x17SnapshotCpuStateOverlay\x12\x43\n\x10\x61rmv7m_cpu_state\x18\x14 \x01(\x0b\x32).pw.cpu_exception.cortex_m.ArmV7mCpuState'
)




_ARMV7MCPUSTATE = _descriptor.Descriptor(
  name='ArmV7mCpuState',
  full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pc', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.pc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lr', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.lr', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='psr', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.psr', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msp', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.msp', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='psp', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.psp', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exc_return', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.exc_return', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cfsr', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.cfsr', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msplim', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.msplim', index=7,
      number=27, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='psplim', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.psplim', index=8,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mmfar', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.mmfar', index=9,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bfar', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.bfar', index=10,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icsr', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.icsr', index=11,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hfsr', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.hfsr', index=12,
      number=25, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shcsr', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.shcsr', index=13,
      number=26, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='control', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.control', index=14,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r0', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r0', index=15,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r1', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r1', index=16,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r2', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r2', index=17,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r3', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r3', index=18,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r4', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r4', index=19,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r5', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r5', index=20,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r6', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r6', index=21,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r7', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r7', index=22,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r8', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r8', index=23,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r9', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r9', index=24,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r10', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r10', index=25,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r11', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r11', index=26,
      number=23, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r12', full_name='pw.cpu_exception.cortex_m.ArmV7mCpuState.r12', index=27,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=473,
)


_SNAPSHOTCPUSTATEOVERLAY = _descriptor.Descriptor(
  name='SnapshotCpuStateOverlay',
  full_name='pw.cpu_exception.cortex_m.SnapshotCpuStateOverlay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='armv7m_cpu_state', full_name='pw.cpu_exception.cortex_m.SnapshotCpuStateOverlay.armv7m_cpu_state', index=0,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=569,
)

_SNAPSHOTCPUSTATEOVERLAY.fields_by_name['armv7m_cpu_state'].message_type = _ARMV7MCPUSTATE
DESCRIPTOR.message_types_by_name['ArmV7mCpuState'] = _ARMV7MCPUSTATE
DESCRIPTOR.message_types_by_name['SnapshotCpuStateOverlay'] = _SNAPSHOTCPUSTATEOVERLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArmV7mCpuState = _reflection.GeneratedProtocolMessageType('ArmV7mCpuState', (_message.Message,), {
  'DESCRIPTOR' : _ARMV7MCPUSTATE,
  '__module__' : 'pw_cpu_exception_cortex_m_protos.cpu_state_pb2'
  # @@protoc_insertion_point(class_scope:pw.cpu_exception.cortex_m.ArmV7mCpuState)
  })
_sym_db.RegisterMessage(ArmV7mCpuState)

SnapshotCpuStateOverlay = _reflection.GeneratedProtocolMessageType('SnapshotCpuStateOverlay', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTCPUSTATEOVERLAY,
  '__module__' : 'pw_cpu_exception_cortex_m_protos.cpu_state_pb2'
  # @@protoc_insertion_point(class_scope:pw.cpu_exception.cortex_m.SnapshotCpuStateOverlay)
  })
_sym_db.RegisterMessage(SnapshotCpuStateOverlay)


# @@protoc_insertion_point(module_scope)
