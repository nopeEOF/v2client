# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/protoext/extensions.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n common/protoext/extensions.proto\x12\x1av2ray.core.common.protoext\x1a google/protobuf/descriptor.proto\"w\n\nMessageOpt\x12\x0c\n\x04type\x18\x01 \x03(\t\x12\x12\n\nshort_name\x18\x02 \x03(\t\x12!\n\x17transport_original_name\x18\xf1\x9f\x05 \x01(\t\x12$\n\x1a\x61llow_restricted_mode_load\x18\xf2\x9f\x05 \x01(\x08\"\xd0\x01\n\x08\x46ieldOpt\x12\x11\n\tany_wants\x18\x01 \x03(\t\x12\x16\n\x0e\x61llowed_values\x18\x02 \x03(\t\x12\x1b\n\x13\x61llowed_value_types\x18\x03 \x03(\t\x12#\n\x1b\x63onvert_time_read_file_into\x18\x04 \x01(\t\x12\x11\n\tforbidden\x18\x05 \x01(\x08\x12%\n\x1d\x63onvert_time_resource_loading\x18\x06 \x01(\t\x12\x1d\n\x15\x63onvert_time_parse_ip\x18\x07 \x01(\t:^\n\x0bmessage_opt\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x0b\x32&.v2ray.core.common.protoext.MessageOpt:X\n\tfield_opt\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x0b\x32$.v2ray.core.common.protoext.FieldOptBo\n\x1e\x63om.v2ray.core.common.protoextP\x01Z.github.com/v2fly/v2ray-core/v5/common/protoext\xaa\x02\x1aV2Ray.Core.Common.ProtoExtb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.protoext.extensions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.v2ray.core.common.protoextP\001Z.github.com/v2fly/v2ray-core/v5/common/protoext\252\002\032V2Ray.Core.Common.ProtoExt'
  _globals['_MESSAGEOPT']._serialized_start=98
  _globals['_MESSAGEOPT']._serialized_end=217
  _globals['_FIELDOPT']._serialized_start=220
  _globals['_FIELDOPT']._serialized_end=428
# @@protoc_insertion_point(module_scope)
