# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/freedom/config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v2ray.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2
from api.v2ray.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aproxy/freedom/config.proto\x12\x18v2ray.core.proxy.freedom\x1a!common/protocol/server_spec.proto\x1a common/protoext/extensions.proto\"Q\n\x13\x44\x65stinationOverride\x12:\n\x06server\x18\x01 \x01(\x0b\x32*.v2ray.core.common.protocol.ServerEndpoint\"\x8b\x02\n\x06\x43onfig\x12H\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32/.v2ray.core.proxy.freedom.Config.DomainStrategy\x12\x13\n\x07timeout\x18\x02 \x01(\rB\x02\x18\x01\x12K\n\x14\x64\x65stination_override\x18\x03 \x01(\x0b\x32-.v2ray.core.proxy.freedom.DestinationOverride\x12\x12\n\nuser_level\x18\x04 \x01(\r\"A\n\x0e\x44omainStrategy\x12\t\n\x05\x41S_IS\x10\x00\x12\n\n\x06USE_IP\x10\x01\x12\x0b\n\x07USE_IP4\x10\x02\x12\x0b\n\x07USE_IP6\x10\x03\"+\n\x10SimplifiedConfig:\x17\x82\xb5\x18\x13\n\x08outbound\x12\x07\x66reedomBi\n\x1c\x63om.v2ray.core.proxy.freedomP\x01Z,github.com/v2fly/v2ray-core/v5/proxy/freedom\xaa\x02\x18V2Ray.Core.Proxy.Freedomb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.freedom.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.v2ray.core.proxy.freedomP\001Z,github.com/v2fly/v2ray-core/v5/proxy/freedom\252\002\030V2Ray.Core.Proxy.Freedom'
  _globals['_CONFIG'].fields_by_name['timeout']._options = None
  _globals['_CONFIG'].fields_by_name['timeout']._serialized_options = b'\030\001'
  _globals['_SIMPLIFIEDCONFIG']._options = None
  _globals['_SIMPLIFIEDCONFIG']._serialized_options = b'\202\265\030\023\n\010outbound\022\007freedom'
  _globals['_DESTINATIONOVERRIDE']._serialized_start=125
  _globals['_DESTINATIONOVERRIDE']._serialized_end=206
  _globals['_CONFIG']._serialized_start=209
  _globals['_CONFIG']._serialized_end=476
  _globals['_CONFIG_DOMAINSTRATEGY']._serialized_start=411
  _globals['_CONFIG_DOMAINSTRATEGY']._serialized_end=476
  _globals['_SIMPLIFIEDCONFIG']._serialized_start=478
  _globals['_SIMPLIFIEDCONFIG']._serialized_end=521
# @@protoc_insertion_point(module_scope)
