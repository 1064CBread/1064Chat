# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: complexdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='complexdata.proto',
  package='ten64chat.data',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x63omplexdata.proto\x12\x0eten64chat.data\")\n\x04UUID\x12\x0f\n\x07lowBits\x18\x01 \x01(\x06\x12\x10\n\x08highBits\x18\x02 \x01(\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='ten64chat.data.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lowBits', full_name='ten64chat.data.UUID.lowBits', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highBits', full_name='ten64chat.data.UUID.highBits', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['UUID'] = _UUID

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), dict(
  DESCRIPTOR = _UUID,
  __module__ = 'complexdata_pb2'
  # @@protoc_insertion_point(class_scope:ten64chat.data.UUID)
  ))
_sym_db.RegisterMessage(UUID)


# @@protoc_insertion_point(module_scope)
