# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/http/simplified/config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v2ray.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2
from api.v2ray.common.net import address_pb2 as common_dot_net_dot_address__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"proxy/http/simplified/config.proto\x12 v2ray.core.proxy.http.simplified\x1a common/protoext/extensions.proto\x1a\x18\x63ommon/net/address.proto\"#\n\x0cServerConfig:\x13\x82\xb5\x18\x0f\n\x07inbound\x12\x04http\"\x86\x01\n\x0c\x43lientConfig\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x1e\n\x16h1_skip_wait_for_reply\x18\x03 \x01(\x08:\x14\x82\xb5\x18\x10\n\x08outbound\x12\x04httpB\x81\x01\n$com.v2ray.core.proxy.http.simplifiedP\x01Z4github.com/v2fly/v2ray-core/v5/proxy/http/simplified\xaa\x02 V2Ray.Core.Proxy.Http.Simplifiedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.http.simplified.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.v2ray.core.proxy.http.simplifiedP\001Z4github.com/v2fly/v2ray-core/v5/proxy/http/simplified\252\002 V2Ray.Core.Proxy.Http.Simplified'
  _globals['_SERVERCONFIG']._options = None
  _globals['_SERVERCONFIG']._serialized_options = b'\202\265\030\017\n\007inbound\022\004http'
  _globals['_CLIENTCONFIG']._options = None
  _globals['_CLIENTCONFIG']._serialized_options = b'\202\265\030\020\n\010outbound\022\004http'
  _globals['_SERVERCONFIG']._serialized_start=132
  _globals['_SERVERCONFIG']._serialized_end=167
  _globals['_CLIENTCONFIG']._serialized_start=170
  _globals['_CLIENTCONFIG']._serialized_end=304
# @@protoc_insertion_point(module_scope)