import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVITY_LEVEL_UNSPECIFIED: _ClassVar[ActivityLevel]
    ACTIVITY_LEVEL_INFO: _ClassVar[ActivityLevel]
    ACTIVITY_LEVEL_SUCCESS: _ClassVar[ActivityLevel]
    ACTIVITY_LEVEL_WARNING: _ClassVar[ActivityLevel]
    ACTIVITY_LEVEL_ERROR: _ClassVar[ActivityLevel]
ACTIVITY_LEVEL_UNSPECIFIED: ActivityLevel
ACTIVITY_LEVEL_INFO: ActivityLevel
ACTIVITY_LEVEL_SUCCESS: ActivityLevel
ACTIVITY_LEVEL_WARNING: ActivityLevel
ACTIVITY_LEVEL_ERROR: ActivityLevel

class NodeActivity(_message.Message):
    __slots__ = ("node_id", "version", "level", "message", "event_ts")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    version: str
    level: ActivityLevel
    message: str
    event_ts: _timestamp_pb2.Timestamp
    def __init__(self, node_id: _Optional[str] = ..., version: _Optional[str] = ..., level: _Optional[_Union[ActivityLevel, str]] = ..., message: _Optional[str] = ..., event_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
