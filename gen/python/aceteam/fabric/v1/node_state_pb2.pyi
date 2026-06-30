import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModuleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODULE_STATUS_UNSPECIFIED: _ClassVar[ModuleStatus]
    MODULE_STATUS_RUNNING: _ClassVar[ModuleStatus]
    MODULE_STATUS_STOPPED: _ClassVar[ModuleStatus]
    MODULE_STATUS_ABSENT: _ClassVar[ModuleStatus]

class ModuleHealth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODULE_HEALTH_UNSPECIFIED: _ClassVar[ModuleHealth]
    MODULE_HEALTH_HEALTHY: _ClassVar[ModuleHealth]
    MODULE_HEALTH_STARTING: _ClassVar[ModuleHealth]
    MODULE_HEALTH_UNHEALTHY: _ClassVar[ModuleHealth]
    MODULE_HEALTH_ERROR: _ClassVar[ModuleHealth]
MODULE_STATUS_UNSPECIFIED: ModuleStatus
MODULE_STATUS_RUNNING: ModuleStatus
MODULE_STATUS_STOPPED: ModuleStatus
MODULE_STATUS_ABSENT: ModuleStatus
MODULE_HEALTH_UNSPECIFIED: ModuleHealth
MODULE_HEALTH_HEALTHY: ModuleHealth
MODULE_HEALTH_STARTING: ModuleHealth
MODULE_HEALTH_UNHEALTHY: ModuleHealth
MODULE_HEALTH_ERROR: ModuleHealth

class DesiredModule(_message.Message):
    __slots__ = ("source", "config_ref", "config", "desired_status", "allow_privileged")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_REF_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATUS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    source: str
    config_ref: str
    config: _containers.ScalarMap[str, str]
    desired_status: ModuleStatus
    allow_privileged: bool
    def __init__(self, source: _Optional[str] = ..., config_ref: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ..., desired_status: _Optional[_Union[ModuleStatus, str]] = ..., allow_privileged: _Optional[bool] = ...) -> None: ...

class DesiredState(_message.Message):
    __slots__ = ("protocol_version", "node_id", "revision", "modules", "issued_at")
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    protocol_version: int
    node_id: str
    revision: str
    modules: _containers.RepeatedCompositeFieldContainer[DesiredModule]
    issued_at: _timestamp_pb2.Timestamp
    def __init__(self, protocol_version: _Optional[int] = ..., node_id: _Optional[str] = ..., revision: _Optional[str] = ..., modules: _Optional[_Iterable[_Union[DesiredModule, _Mapping]]] = ..., issued_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ActualModule(_message.Message):
    __slots__ = ("source", "installed_version", "image_digest", "status", "health", "config_ref", "error", "updated_at")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DIGEST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    CONFIG_REF_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    source: str
    installed_version: str
    image_digest: str
    status: ModuleStatus
    health: ModuleHealth
    config_ref: str
    error: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, source: _Optional[str] = ..., installed_version: _Optional[str] = ..., image_digest: _Optional[str] = ..., status: _Optional[_Union[ModuleStatus, str]] = ..., health: _Optional[_Union[ModuleHealth, str]] = ..., config_ref: _Optional[str] = ..., error: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ActualState(_message.Message):
    __slots__ = ("protocol_version", "node_id", "applied_revision", "agent_version", "modules", "reported_at")
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIED_REVISION_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    REPORTED_AT_FIELD_NUMBER: _ClassVar[int]
    protocol_version: int
    node_id: str
    applied_revision: str
    agent_version: str
    modules: _containers.RepeatedCompositeFieldContainer[ActualModule]
    reported_at: _timestamp_pb2.Timestamp
    def __init__(self, protocol_version: _Optional[int] = ..., node_id: _Optional[str] = ..., applied_revision: _Optional[str] = ..., agent_version: _Optional[str] = ..., modules: _Optional[_Iterable[_Union[ActualModule, _Mapping]]] = ..., reported_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
