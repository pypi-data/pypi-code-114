"""
Type annotations for qldb-session service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_qldb_session/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_qldb_session.type_defs import AbortTransactionResultTypeDef

    data: AbortTransactionResultTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AbortTransactionResultTypeDef",
    "CommitTransactionRequestTypeDef",
    "CommitTransactionResultTypeDef",
    "EndSessionResultTypeDef",
    "ExecuteStatementRequestTypeDef",
    "ExecuteStatementResultTypeDef",
    "FetchPageRequestTypeDef",
    "FetchPageResultTypeDef",
    "IOUsageTypeDef",
    "PageTypeDef",
    "ResponseMetadataTypeDef",
    "SendCommandRequestRequestTypeDef",
    "SendCommandResultTypeDef",
    "StartSessionRequestTypeDef",
    "StartSessionResultTypeDef",
    "StartTransactionResultTypeDef",
    "TimingInformationTypeDef",
    "ValueHolderTypeDef",
)

AbortTransactionResultTypeDef = TypedDict(
    "AbortTransactionResultTypeDef",
    {
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
    },
)

CommitTransactionRequestTypeDef = TypedDict(
    "CommitTransactionRequestTypeDef",
    {
        "TransactionId": str,
        "CommitDigest": Union[bytes, IO[bytes], StreamingBody],
    },
)

CommitTransactionResultTypeDef = TypedDict(
    "CommitTransactionResultTypeDef",
    {
        "TransactionId": NotRequired[str],
        "CommitDigest": NotRequired[bytes],
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
        "ConsumedIOs": NotRequired["IOUsageTypeDef"],
    },
)

EndSessionResultTypeDef = TypedDict(
    "EndSessionResultTypeDef",
    {
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
    },
)

ExecuteStatementRequestTypeDef = TypedDict(
    "ExecuteStatementRequestTypeDef",
    {
        "TransactionId": str,
        "Statement": str,
        "Parameters": NotRequired[Sequence["ValueHolderTypeDef"]],
    },
)

ExecuteStatementResultTypeDef = TypedDict(
    "ExecuteStatementResultTypeDef",
    {
        "FirstPage": NotRequired["PageTypeDef"],
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
        "ConsumedIOs": NotRequired["IOUsageTypeDef"],
    },
)

FetchPageRequestTypeDef = TypedDict(
    "FetchPageRequestTypeDef",
    {
        "TransactionId": str,
        "NextPageToken": str,
    },
)

FetchPageResultTypeDef = TypedDict(
    "FetchPageResultTypeDef",
    {
        "Page": NotRequired["PageTypeDef"],
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
        "ConsumedIOs": NotRequired["IOUsageTypeDef"],
    },
)

IOUsageTypeDef = TypedDict(
    "IOUsageTypeDef",
    {
        "ReadIOs": NotRequired[int],
        "WriteIOs": NotRequired[int],
    },
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "Values": NotRequired[List["ValueHolderTypeDef"]],
        "NextPageToken": NotRequired[str],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

SendCommandRequestRequestTypeDef = TypedDict(
    "SendCommandRequestRequestTypeDef",
    {
        "SessionToken": NotRequired[str],
        "StartSession": NotRequired["StartSessionRequestTypeDef"],
        "StartTransaction": NotRequired[Mapping[str, Any]],
        "EndSession": NotRequired[Mapping[str, Any]],
        "CommitTransaction": NotRequired["CommitTransactionRequestTypeDef"],
        "AbortTransaction": NotRequired[Mapping[str, Any]],
        "ExecuteStatement": NotRequired["ExecuteStatementRequestTypeDef"],
        "FetchPage": NotRequired["FetchPageRequestTypeDef"],
    },
)

SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef",
    {
        "StartSession": "StartSessionResultTypeDef",
        "StartTransaction": "StartTransactionResultTypeDef",
        "EndSession": "EndSessionResultTypeDef",
        "CommitTransaction": "CommitTransactionResultTypeDef",
        "AbortTransaction": "AbortTransactionResultTypeDef",
        "ExecuteStatement": "ExecuteStatementResultTypeDef",
        "FetchPage": "FetchPageResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSessionRequestTypeDef = TypedDict(
    "StartSessionRequestTypeDef",
    {
        "LedgerName": str,
    },
)

StartSessionResultTypeDef = TypedDict(
    "StartSessionResultTypeDef",
    {
        "SessionToken": NotRequired[str],
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
    },
)

StartTransactionResultTypeDef = TypedDict(
    "StartTransactionResultTypeDef",
    {
        "TransactionId": NotRequired[str],
        "TimingInformation": NotRequired["TimingInformationTypeDef"],
    },
)

TimingInformationTypeDef = TypedDict(
    "TimingInformationTypeDef",
    {
        "ProcessingTimeMilliseconds": NotRequired[int],
    },
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonBinary": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "IonText": NotRequired[str],
    },
)
