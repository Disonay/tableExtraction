# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pdf_table_extractor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19pdf_table_extractor.proto\x12\x12services.extractor\"H\n\x16TableExtractionRequest\x12\x0f\n\x07pdf_url\x18\x01 \x01(\t\x12\x1d\n\x11table_coordinates\x18\x02 \x03(\x02\x42\x02\x10\x01\"\x1f\n\tTableData\x12\x12\n\ntable_data\x18\x01 \x01(\t2p\n\x16TableExtractionService\x12V\n\x07\x45xtract\x12*.services.extractor.TableExtractionRequest\x1a\x1d.services.extractor.TableData\"\x00\x62\x06proto3')



_TABLEEXTRACTIONREQUEST = DESCRIPTOR.message_types_by_name['TableExtractionRequest']
_TABLEDATA = DESCRIPTOR.message_types_by_name['TableData']
TableExtractionRequest = _reflection.GeneratedProtocolMessageType('TableExtractionRequest', (_message.Message,), {
  'DESCRIPTOR' : _TABLEEXTRACTIONREQUEST,
  '__module__' : 'pdf_table_extractor_pb2'
  # @@protoc_insertion_point(class_scope:services.extractor.TableExtractionRequest)
  })
_sym_db.RegisterMessage(TableExtractionRequest)

TableData = _reflection.GeneratedProtocolMessageType('TableData', (_message.Message,), {
  'DESCRIPTOR' : _TABLEDATA,
  '__module__' : 'pdf_table_extractor_pb2'
  # @@protoc_insertion_point(class_scope:services.extractor.TableData)
  })
_sym_db.RegisterMessage(TableData)

_TABLEEXTRACTIONSERVICE = DESCRIPTOR.services_by_name['TableExtractionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TABLEEXTRACTIONREQUEST.fields_by_name['table_coordinates']._options = None
  _TABLEEXTRACTIONREQUEST.fields_by_name['table_coordinates']._serialized_options = b'\020\001'
  _TABLEEXTRACTIONREQUEST._serialized_start=49
  _TABLEEXTRACTIONREQUEST._serialized_end=121
  _TABLEDATA._serialized_start=123
  _TABLEDATA._serialized_end=154
  _TABLEEXTRACTIONSERVICE._serialized_start=156
  _TABLEEXTRACTIONSERVICE._serialized_end=268
# @@protoc_insertion_point(module_scope)