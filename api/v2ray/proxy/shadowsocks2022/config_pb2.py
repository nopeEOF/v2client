# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/shadowsocks2022/config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v2ray.common.net import address_pb2 as common_dot_net_dot_address__pb2
from api.v2ray.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"proxy/shadowsocks2022/config.proto\x12 v2ray.core.proxy.shadowsocks2022\x1a\x18\x63ommon/net/address.proto\x1a common/protoext/extensions.proto\"\xa0\x01\n\x0c\x43lientConfig\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03psk\x18\x02 \x01(\x0c\x12\x0c\n\x04ipsk\x18\x04 \x03(\x0c\x12\x32\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x06 \x01(\r:#\x82\xb5\x18\x1f\n\x08outbound\x12\x0fshadowsocks2022\x90\xff)\x01\x42\x81\x01\n$com.v2ray.core.proxy.shadowsocks2022P\x01Z4github.com/v2fly/v2ray-core/v5/proxy/shadowsocks2022\xaa\x02 V2Ray.Core.Proxy.Shadowsocks2022b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.shadowsocks2022.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.v2ray.core.proxy.shadowsocks2022P\001Z4github.com/v2fly/v2ray-core/v5/proxy/shadowsocks2022\252\002 V2Ray.Core.Proxy.Shadowsocks2022'
  _globals['_CLIENTCONFIG']._options = None
  _globals['_CLIENTCONFIG']._serialized_options = b'\202\265\030\037\n\010outbound\022\017shadowsocks2022\220\377)\001'
  _globals['_CLIENTCONFIG']._serialized_start=133
  _globals['_CLIENTCONFIG']._serialized_end=293
# @@protoc_insertion_point(module_scope)