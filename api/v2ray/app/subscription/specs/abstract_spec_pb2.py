# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/subscription/specs/abstract_spec.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*app/subscription/specs/abstract_spec.proto\x12!v2ray.core.app.subscription.specs\x1a\x19google/protobuf/any.proto\"\xe0\x01\n\x13ServerConfiguration\x12\x10\n\x08protocol\x18\x01 \x01(\t\x12/\n\x11protocol_settings\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttransport\x18\x03 \x01(\t\x12\x30\n\x12transport_settings\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08security\x18\x05 \x01(\t\x12/\n\x11security_settings\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\"\x83\x02\n\x18SubscriptionServerConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12[\n\x08metadata\x18\x02 \x03(\x0b\x32I.v2ray.core.app.subscription.specs.SubscriptionServerConfig.MetadataEntry\x12M\n\rconfiguration\x18\x03 \x01(\x0b\x32\x36.v2ray.core.app.subscription.specs.ServerConfiguration\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xed\x01\n\x14SubscriptionDocument\x12W\n\x08metadata\x18\x02 \x03(\x0b\x32\x45.v2ray.core.app.subscription.specs.SubscriptionDocument.MetadataEntry\x12K\n\x06server\x18\x03 \x03(\x0b\x32;.v2ray.core.app.subscription.specs.SubscriptionServerConfig\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x84\x01\n%com.v2ray.core.app.subscription.specsP\x01Z5github.com/v2fly/v2ray-core/v5/app/subscription/specs\xaa\x02!V2Ray.Core.App.Subscription.Specsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.subscription.specs.abstract_spec_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.v2ray.core.app.subscription.specsP\001Z5github.com/v2fly/v2ray-core/v5/app/subscription/specs\252\002!V2Ray.Core.App.Subscription.Specs'
  _globals['_SUBSCRIPTIONSERVERCONFIG_METADATAENTRY']._options = None
  _globals['_SUBSCRIPTIONSERVERCONFIG_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SUBSCRIPTIONDOCUMENT_METADATAENTRY']._options = None
  _globals['_SUBSCRIPTIONDOCUMENT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SERVERCONFIGURATION']._serialized_start=109
  _globals['_SERVERCONFIGURATION']._serialized_end=333
  _globals['_SUBSCRIPTIONSERVERCONFIG']._serialized_start=336
  _globals['_SUBSCRIPTIONSERVERCONFIG']._serialized_end=595
  _globals['_SUBSCRIPTIONSERVERCONFIG_METADATAENTRY']._serialized_start=548
  _globals['_SUBSCRIPTIONSERVERCONFIG_METADATAENTRY']._serialized_end=595
  _globals['_SUBSCRIPTIONDOCUMENT']._serialized_start=598
  _globals['_SUBSCRIPTIONDOCUMENT']._serialized_end=835
  _globals['_SUBSCRIPTIONDOCUMENT_METADATAENTRY']._serialized_start=548
  _globals['_SUBSCRIPTIONDOCUMENT_METADATAENTRY']._serialized_end=595
# @@protoc_insertion_point(module_scope)
