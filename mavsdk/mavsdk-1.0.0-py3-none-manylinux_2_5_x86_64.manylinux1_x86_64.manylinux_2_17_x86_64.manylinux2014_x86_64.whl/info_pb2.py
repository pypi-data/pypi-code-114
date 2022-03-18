# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: info/info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finfo/info.proto\x12\x0fmavsdk.rpc.info\x1a\x14mavsdk_options.proto\"\x1d\n\x1bGetFlightInformationRequest\"\x82\x01\n\x1cGetFlightInformationResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12\x30\n\x0b\x66light_info\x18\x02 \x01(\x0b\x32\x1b.mavsdk.rpc.info.FlightInfo\"\x1a\n\x18GetIdentificationRequest\"\x86\x01\n\x19GetIdentificationResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12\x37\n\x0eidentification\x18\x02 \x01(\x0b\x32\x1f.mavsdk.rpc.info.Identification\"\x13\n\x11GetProductRequest\"q\n\x12GetProductResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12)\n\x07product\x18\x02 \x01(\x0b\x32\x18.mavsdk.rpc.info.Product\"\x13\n\x11GetVersionRequest\"q\n\x12GetVersionResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12)\n\x07version\x18\x02 \x01(\x0b\x32\x18.mavsdk.rpc.info.Version\"\x17\n\x15GetSpeedFactorRequest\"`\n\x16GetSpeedFactorResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12\x14\n\x0cspeed_factor\x18\x02 \x01(\x01\"6\n\nFlightInfo\x12\x14\n\x0ctime_boot_ms\x18\x01 \x01(\r\x12\x12\n\nflight_uid\x18\x02 \x01(\x04\":\n\x0eIdentification\x12\x14\n\x0chardware_uid\x18\x01 \x01(\t\x12\x12\n\nlegacy_uid\x18\x02 \x01(\x04\"[\n\x07Product\x12\x11\n\tvendor_id\x18\x01 \x01(\x05\x12\x13\n\x0bvendor_name\x18\x02 \x01(\t\x12\x12\n\nproduct_id\x18\x03 \x01(\x05\x12\x14\n\x0cproduct_name\x18\x04 \x01(\t\"\xa7\x02\n\x07Version\x12\x17\n\x0f\x66light_sw_major\x18\x01 \x01(\x05\x12\x17\n\x0f\x66light_sw_minor\x18\x02 \x01(\x05\x12\x17\n\x0f\x66light_sw_patch\x18\x03 \x01(\x05\x12\x1e\n\x16\x66light_sw_vendor_major\x18\x04 \x01(\x05\x12\x1e\n\x16\x66light_sw_vendor_minor\x18\x05 \x01(\x05\x12\x1e\n\x16\x66light_sw_vendor_patch\x18\x06 \x01(\x05\x12\x13\n\x0bos_sw_major\x18\x07 \x01(\x05\x12\x13\n\x0bos_sw_minor\x18\x08 \x01(\x05\x12\x13\n\x0bos_sw_patch\x18\t \x01(\x05\x12\x1a\n\x12\x66light_sw_git_hash\x18\n \x01(\t\x12\x16\n\x0eos_sw_git_hash\x18\x0b \x01(\t\"\xc5\x01\n\nInfoResult\x12\x32\n\x06result\x18\x01 \x01(\x0e\x32\".mavsdk.rpc.info.InfoResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"o\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\'\n#RESULT_INFORMATION_NOT_RECEIVED_YET\x10\x02\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x03\x32\x9d\x04\n\x0bInfoService\x12y\n\x14GetFlightInformation\x12,.mavsdk.rpc.info.GetFlightInformationRequest\x1a-.mavsdk.rpc.info.GetFlightInformationResponse\"\x04\x80\xb5\x18\x01\x12p\n\x11GetIdentification\x12).mavsdk.rpc.info.GetIdentificationRequest\x1a*.mavsdk.rpc.info.GetIdentificationResponse\"\x04\x80\xb5\x18\x01\x12[\n\nGetProduct\x12\".mavsdk.rpc.info.GetProductRequest\x1a#.mavsdk.rpc.info.GetProductResponse\"\x04\x80\xb5\x18\x01\x12[\n\nGetVersion\x12\".mavsdk.rpc.info.GetVersionRequest\x1a#.mavsdk.rpc.info.GetVersionResponse\"\x04\x80\xb5\x18\x01\x12g\n\x0eGetSpeedFactor\x12&.mavsdk.rpc.info.GetSpeedFactorRequest\x1a\'.mavsdk.rpc.info.GetSpeedFactorResponse\"\x04\x80\xb5\x18\x01\x42\x1b\n\x0eio.mavsdk.infoB\tInfoProtob\x06proto3')



_GETFLIGHTINFORMATIONREQUEST = DESCRIPTOR.message_types_by_name['GetFlightInformationRequest']
_GETFLIGHTINFORMATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetFlightInformationResponse']
_GETIDENTIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['GetIdentificationRequest']
_GETIDENTIFICATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetIdentificationResponse']
_GETPRODUCTREQUEST = DESCRIPTOR.message_types_by_name['GetProductRequest']
_GETPRODUCTRESPONSE = DESCRIPTOR.message_types_by_name['GetProductResponse']
_GETVERSIONREQUEST = DESCRIPTOR.message_types_by_name['GetVersionRequest']
_GETVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['GetVersionResponse']
_GETSPEEDFACTORREQUEST = DESCRIPTOR.message_types_by_name['GetSpeedFactorRequest']
_GETSPEEDFACTORRESPONSE = DESCRIPTOR.message_types_by_name['GetSpeedFactorResponse']
_FLIGHTINFO = DESCRIPTOR.message_types_by_name['FlightInfo']
_IDENTIFICATION = DESCRIPTOR.message_types_by_name['Identification']
_PRODUCT = DESCRIPTOR.message_types_by_name['Product']
_VERSION = DESCRIPTOR.message_types_by_name['Version']
_INFORESULT = DESCRIPTOR.message_types_by_name['InfoResult']
_INFORESULT_RESULT = _INFORESULT.enum_types_by_name['Result']
GetFlightInformationRequest = _reflection.GeneratedProtocolMessageType('GetFlightInformationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFLIGHTINFORMATIONREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetFlightInformationRequest)
  })
_sym_db.RegisterMessage(GetFlightInformationRequest)

GetFlightInformationResponse = _reflection.GeneratedProtocolMessageType('GetFlightInformationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFLIGHTINFORMATIONRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetFlightInformationResponse)
  })
_sym_db.RegisterMessage(GetFlightInformationResponse)

GetIdentificationRequest = _reflection.GeneratedProtocolMessageType('GetIdentificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIDENTIFICATIONREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetIdentificationRequest)
  })
_sym_db.RegisterMessage(GetIdentificationRequest)

GetIdentificationResponse = _reflection.GeneratedProtocolMessageType('GetIdentificationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETIDENTIFICATIONRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetIdentificationResponse)
  })
_sym_db.RegisterMessage(GetIdentificationResponse)

GetProductRequest = _reflection.GeneratedProtocolMessageType('GetProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetProductRequest)
  })
_sym_db.RegisterMessage(GetProductRequest)

GetProductResponse = _reflection.GeneratedProtocolMessageType('GetProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetProductResponse)
  })
_sym_db.RegisterMessage(GetProductResponse)

GetVersionRequest = _reflection.GeneratedProtocolMessageType('GetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetVersionRequest)
  })
_sym_db.RegisterMessage(GetVersionRequest)

GetVersionResponse = _reflection.GeneratedProtocolMessageType('GetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetVersionResponse)
  })
_sym_db.RegisterMessage(GetVersionResponse)

GetSpeedFactorRequest = _reflection.GeneratedProtocolMessageType('GetSpeedFactorRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEEDFACTORREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetSpeedFactorRequest)
  })
_sym_db.RegisterMessage(GetSpeedFactorRequest)

GetSpeedFactorResponse = _reflection.GeneratedProtocolMessageType('GetSpeedFactorResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEEDFACTORRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetSpeedFactorResponse)
  })
_sym_db.RegisterMessage(GetSpeedFactorResponse)

FlightInfo = _reflection.GeneratedProtocolMessageType('FlightInfo', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTINFO,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.FlightInfo)
  })
_sym_db.RegisterMessage(FlightInfo)

Identification = _reflection.GeneratedProtocolMessageType('Identification', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFICATION,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.Identification)
  })
_sym_db.RegisterMessage(Identification)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.Product)
  })
_sym_db.RegisterMessage(Product)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.Version)
  })
_sym_db.RegisterMessage(Version)

InfoResult = _reflection.GeneratedProtocolMessageType('InfoResult', (_message.Message,), {
  'DESCRIPTOR' : _INFORESULT,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.InfoResult)
  })
_sym_db.RegisterMessage(InfoResult)

_INFOSERVICE = DESCRIPTOR.services_by_name['InfoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016io.mavsdk.infoB\tInfoProto'
  _INFOSERVICE.methods_by_name['GetFlightInformation']._options = None
  _INFOSERVICE.methods_by_name['GetFlightInformation']._serialized_options = b'\200\265\030\001'
  _INFOSERVICE.methods_by_name['GetIdentification']._options = None
  _INFOSERVICE.methods_by_name['GetIdentification']._serialized_options = b'\200\265\030\001'
  _INFOSERVICE.methods_by_name['GetProduct']._options = None
  _INFOSERVICE.methods_by_name['GetProduct']._serialized_options = b'\200\265\030\001'
  _INFOSERVICE.methods_by_name['GetVersion']._options = None
  _INFOSERVICE.methods_by_name['GetVersion']._serialized_options = b'\200\265\030\001'
  _INFOSERVICE.methods_by_name['GetSpeedFactor']._options = None
  _INFOSERVICE.methods_by_name['GetSpeedFactor']._serialized_options = b'\200\265\030\001'
  _GETFLIGHTINFORMATIONREQUEST._serialized_start=58
  _GETFLIGHTINFORMATIONREQUEST._serialized_end=87
  _GETFLIGHTINFORMATIONRESPONSE._serialized_start=90
  _GETFLIGHTINFORMATIONRESPONSE._serialized_end=220
  _GETIDENTIFICATIONREQUEST._serialized_start=222
  _GETIDENTIFICATIONREQUEST._serialized_end=248
  _GETIDENTIFICATIONRESPONSE._serialized_start=251
  _GETIDENTIFICATIONRESPONSE._serialized_end=385
  _GETPRODUCTREQUEST._serialized_start=387
  _GETPRODUCTREQUEST._serialized_end=406
  _GETPRODUCTRESPONSE._serialized_start=408
  _GETPRODUCTRESPONSE._serialized_end=521
  _GETVERSIONREQUEST._serialized_start=523
  _GETVERSIONREQUEST._serialized_end=542
  _GETVERSIONRESPONSE._serialized_start=544
  _GETVERSIONRESPONSE._serialized_end=657
  _GETSPEEDFACTORREQUEST._serialized_start=659
  _GETSPEEDFACTORREQUEST._serialized_end=682
  _GETSPEEDFACTORRESPONSE._serialized_start=684
  _GETSPEEDFACTORRESPONSE._serialized_end=780
  _FLIGHTINFO._serialized_start=782
  _FLIGHTINFO._serialized_end=836
  _IDENTIFICATION._serialized_start=838
  _IDENTIFICATION._serialized_end=896
  _PRODUCT._serialized_start=898
  _PRODUCT._serialized_end=989
  _VERSION._serialized_start=992
  _VERSION._serialized_end=1287
  _INFORESULT._serialized_start=1290
  _INFORESULT._serialized_end=1487
  _INFORESULT_RESULT._serialized_start=1376
  _INFORESULT_RESULT._serialized_end=1487
  _INFOSERVICE._serialized_start=1490
  _INFOSERVICE._serialized_end=2031
# @@protoc_insertion_point(module_scope)
