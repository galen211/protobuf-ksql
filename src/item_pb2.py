# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='item.proto',
  package='ksql.item',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nitem.proto\x12\tksql.item\"7\n\x0cProtobufItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04item\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x62\x06proto3'
)




_PROTOBUFITEM = _descriptor.Descriptor(
  name='ProtobufItem',
  full_name='ksql.item.ProtobufItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ksql.item.ProtobufItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item', full_name='ksql.item.ProtobufItem.item', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='ksql.item.ProtobufItem.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['ProtobufItem'] = _PROTOBUFITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtobufItem = _reflection.GeneratedProtocolMessageType('ProtobufItem', (_message.Message,), {
  'DESCRIPTOR' : _PROTOBUFITEM,
  '__module__' : 'item_pb2'
  # @@protoc_insertion_point(class_scope:ksql.item.ProtobufItem)
  })
_sym_db.RegisterMessage(ProtobufItem)


# @@protoc_insertion_point(module_scope)
