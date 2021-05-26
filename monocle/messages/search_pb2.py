# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: monocle/search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="monocle/search.proto",
    package="monocle_search",
    syntax="proto3",
    serialized_options=b"Z\016monocle/search",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x14monocle/search.proto\x12\x0emonocle_search\x1a\x1fgoogle/protobuf/timestamp.proto")\n\x18SearchSuggestionsRequest\x12\r\n\x05index\x18\x01 \x01(\t"{\n\x19SearchSuggestionsResponse\x12\x12\n\ntask_types\x18\x01 \x03(\t\x12\x0f\n\x07\x61uthors\x18\x02 \x03(\t\x12\x11\n\tapprovals\x18\x03 \x03(\t\x12\x12\n\npriorities\x18\x04 \x03(\t\x12\x12\n\nseverities\x18\x05 \x03(\t"/\n\nQueryError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08position\x18\x02 \x01(\r"3\n\x13\x43hangesQueryRequest\x12\r\n\x05index\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t"T\n\x06\x43hange\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"2\n\x07\x43hanges\x12\'\n\x07\x63hanges\x18\x01 \x03(\x0b\x32\x16.monocle_search.Change"w\n\x14\x43hangesQueryResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1a.monocle_search.QueryErrorH\x00\x12(\n\x05items\x18\x02 \x01(\x0b\x32\x17.monocle_search.ChangesH\x00\x42\x08\n\x06resultB\x10Z\x0emonocle/searchb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_SEARCHSUGGESTIONSREQUEST = _descriptor.Descriptor(
    name="SearchSuggestionsRequest",
    full_name="monocle_search.SearchSuggestionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="monocle_search.SearchSuggestionsRequest.index",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=73,
    serialized_end=114,
)


_SEARCHSUGGESTIONSRESPONSE = _descriptor.Descriptor(
    name="SearchSuggestionsResponse",
    full_name="monocle_search.SearchSuggestionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="task_types",
            full_name="monocle_search.SearchSuggestionsResponse.task_types",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="authors",
            full_name="monocle_search.SearchSuggestionsResponse.authors",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="approvals",
            full_name="monocle_search.SearchSuggestionsResponse.approvals",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="priorities",
            full_name="monocle_search.SearchSuggestionsResponse.priorities",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="severities",
            full_name="monocle_search.SearchSuggestionsResponse.severities",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=116,
    serialized_end=239,
)


_QUERYERROR = _descriptor.Descriptor(
    name="QueryError",
    full_name="monocle_search.QueryError",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="monocle_search.QueryError.message",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="position",
            full_name="monocle_search.QueryError.position",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=241,
    serialized_end=288,
)


_CHANGESQUERYREQUEST = _descriptor.Descriptor(
    name="ChangesQueryRequest",
    full_name="monocle_search.ChangesQueryRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="monocle_search.ChangesQueryRequest.index",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="query",
            full_name="monocle_search.ChangesQueryRequest.query",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=290,
    serialized_end=341,
)


_CHANGE = _descriptor.Descriptor(
    name="Change",
    full_name="monocle_search.Change",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="title",
            full_name="monocle_search.Change.title",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="url",
            full_name="monocle_search.Change.url",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created_at",
            full_name="monocle_search.Change.created_at",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=343,
    serialized_end=427,
)


_CHANGES = _descriptor.Descriptor(
    name="Changes",
    full_name="monocle_search.Changes",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="changes",
            full_name="monocle_search.Changes.changes",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=429,
    serialized_end=479,
)


_CHANGESQUERYRESPONSE = _descriptor.Descriptor(
    name="ChangesQueryResponse",
    full_name="monocle_search.ChangesQueryResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="error",
            full_name="monocle_search.ChangesQueryResponse.error",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="items",
            full_name="monocle_search.ChangesQueryResponse.items",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="result",
            full_name="monocle_search.ChangesQueryResponse.result",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=481,
    serialized_end=600,
)

_CHANGE.fields_by_name[
    "created_at"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHANGES.fields_by_name["changes"].message_type = _CHANGE
_CHANGESQUERYRESPONSE.fields_by_name["error"].message_type = _QUERYERROR
_CHANGESQUERYRESPONSE.fields_by_name["items"].message_type = _CHANGES
_CHANGESQUERYRESPONSE.oneofs_by_name["result"].fields.append(
    _CHANGESQUERYRESPONSE.fields_by_name["error"]
)
_CHANGESQUERYRESPONSE.fields_by_name[
    "error"
].containing_oneof = _CHANGESQUERYRESPONSE.oneofs_by_name["result"]
_CHANGESQUERYRESPONSE.oneofs_by_name["result"].fields.append(
    _CHANGESQUERYRESPONSE.fields_by_name["items"]
)
_CHANGESQUERYRESPONSE.fields_by_name[
    "items"
].containing_oneof = _CHANGESQUERYRESPONSE.oneofs_by_name["result"]
DESCRIPTOR.message_types_by_name["SearchSuggestionsRequest"] = _SEARCHSUGGESTIONSREQUEST
DESCRIPTOR.message_types_by_name[
    "SearchSuggestionsResponse"
] = _SEARCHSUGGESTIONSRESPONSE
DESCRIPTOR.message_types_by_name["QueryError"] = _QUERYERROR
DESCRIPTOR.message_types_by_name["ChangesQueryRequest"] = _CHANGESQUERYREQUEST
DESCRIPTOR.message_types_by_name["Change"] = _CHANGE
DESCRIPTOR.message_types_by_name["Changes"] = _CHANGES
DESCRIPTOR.message_types_by_name["ChangesQueryResponse"] = _CHANGESQUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchSuggestionsRequest = _reflection.GeneratedProtocolMessageType(
    "SearchSuggestionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHSUGGESTIONSREQUEST,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.SearchSuggestionsRequest)
    },
)
_sym_db.RegisterMessage(SearchSuggestionsRequest)

SearchSuggestionsResponse = _reflection.GeneratedProtocolMessageType(
    "SearchSuggestionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHSUGGESTIONSRESPONSE,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.SearchSuggestionsResponse)
    },
)
_sym_db.RegisterMessage(SearchSuggestionsResponse)

QueryError = _reflection.GeneratedProtocolMessageType(
    "QueryError",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYERROR,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.QueryError)
    },
)
_sym_db.RegisterMessage(QueryError)

ChangesQueryRequest = _reflection.GeneratedProtocolMessageType(
    "ChangesQueryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHANGESQUERYREQUEST,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.ChangesQueryRequest)
    },
)
_sym_db.RegisterMessage(ChangesQueryRequest)

Change = _reflection.GeneratedProtocolMessageType(
    "Change",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHANGE,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.Change)
    },
)
_sym_db.RegisterMessage(Change)

Changes = _reflection.GeneratedProtocolMessageType(
    "Changes",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHANGES,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.Changes)
    },
)
_sym_db.RegisterMessage(Changes)

ChangesQueryResponse = _reflection.GeneratedProtocolMessageType(
    "ChangesQueryResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHANGESQUERYRESPONSE,
        "__module__": "monocle.search_pb2"
        # @@protoc_insertion_point(class_scope:monocle_search.ChangesQueryResponse)
    },
)
_sym_db.RegisterMessage(ChangesQueryResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
