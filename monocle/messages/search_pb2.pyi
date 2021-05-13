"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SearchSuggestionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEX_FIELD_NUMBER: builtins.int
    index: typing.Text = ...
    def __init__(
        self,
        *,
        index: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["index", b"index"]
    ) -> None: ...

global___SearchSuggestionsRequest = SearchSuggestionsRequest

class SearchSuggestionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASK_TYPES_FIELD_NUMBER: builtins.int
    AUTHORS_FIELD_NUMBER: builtins.int
    APPROVALS_FIELD_NUMBER: builtins.int
    PRIORITIES_FIELD_NUMBER: builtins.int
    SEVERITIES_FIELD_NUMBER: builtins.int
    task_types: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    authors: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    approvals: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    priorities: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    severities: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    def __init__(
        self,
        *,
        task_types: typing.Optional[typing.Iterable[typing.Text]] = ...,
        authors: typing.Optional[typing.Iterable[typing.Text]] = ...,
        approvals: typing.Optional[typing.Iterable[typing.Text]] = ...,
        priorities: typing.Optional[typing.Iterable[typing.Text]] = ...,
        severities: typing.Optional[typing.Iterable[typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "approvals",
            b"approvals",
            "authors",
            b"authors",
            "priorities",
            b"priorities",
            "severities",
            b"severities",
            "task_types",
            b"task_types",
        ],
    ) -> None: ...

global___SearchSuggestionsResponse = SearchSuggestionsResponse