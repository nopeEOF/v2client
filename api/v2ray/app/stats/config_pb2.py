# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/stats/config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v2ray.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pp/stats/config.proto\x12\x14v2ray.core.app.stats\x1a common/protoext/extensions.proto\"\x1e\n\x06\x43onfig:\x14\x82\xb5\x18\x10\n\x07service\x12\x05stats\"N\n\rChannelConfig\x12\x10\n\x08\x42locking\x18\x01 \x01(\x08\x12\x17\n\x0fSubscriberLimit\x18\x02 \x01(\x05\x12\x12\n\nBufferSize\x18\x03 \x01(\x05\x42]\n\x18\x63om.v2ray.core.app.statsP\x01Z(github.com/v2fly/v2ray-core/v5/app/stats\xaa\x02\x14V2Ray.Core.App.Statsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.stats.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.v2ray.core.app.statsP\001Z(github.com/v2fly/v2ray-core/v5/app/stats\252\002\024V2Ray.Core.App.Stats'
  _globals['_CONFIG']._options = None
  _globals['_CONFIG']._serialized_options = b'\202\265\030\020\n\007service\022\005stats'
  _globals['_CONFIG']._serialized_start=82
  _globals['_CONFIG']._serialized_end=112
  _globals['_CHANNELCONFIG']._serialized_start=114
  _globals['_CHANNELCONFIG']._serialized_end=192
# @@protoc_insertion_point(module_scope)