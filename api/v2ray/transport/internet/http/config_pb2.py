# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/http/config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v2ray.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2
from api.v2ray.transport.internet.headers.http import config_pb2 as transport_dot_internet_dot_headers_dot_http_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$transport/internet/http/config.proto\x12\"v2ray.core.transport.internet.http\x1a common/protoext/extensions.proto\x1a,transport/internet/headers/http/config.proto\"\x95\x01\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x03(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x42\n\x06header\x18\x04 \x03(\x0b\x32\x32.v2ray.core.transport.internet.headers.http.Header:\x1b\x82\xb5\x18\x17\n\ttransport\x12\x02h2\x8a\xff)\x04httpB\x87\x01\n&com.v2ray.core.transport.internet.httpP\x01Z6github.com/v2fly/v2ray-core/v5/transport/internet/http\xaa\x02\"V2Ray.Core.Transport.Internet.Httpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.http.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.v2ray.core.transport.internet.httpP\001Z6github.com/v2fly/v2ray-core/v5/transport/internet/http\252\002\"V2Ray.Core.Transport.Internet.Http'
  _globals['_CONFIG']._options = None
  _globals['_CONFIG']._serialized_options = b'\202\265\030\027\n\ttransport\022\002h2\212\377)\004http'
  _globals['_CONFIG']._serialized_start=157
  _globals['_CONFIG']._serialized_end=306
# @@protoc_insertion_point(module_scope)
