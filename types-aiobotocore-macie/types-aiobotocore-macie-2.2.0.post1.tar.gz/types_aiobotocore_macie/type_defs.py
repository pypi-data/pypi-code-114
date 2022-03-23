"""
Type annotations for macie service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_macie/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_macie.type_defs import AssociateMemberAccountRequestRequestTypeDef

    data: AssociateMemberAccountRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import S3OneTimeClassificationTypeType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateMemberAccountRequestRequestTypeDef",
    "AssociateS3ResourcesRequestRequestTypeDef",
    "AssociateS3ResourcesResultTypeDef",
    "ClassificationTypeTypeDef",
    "ClassificationTypeUpdateTypeDef",
    "DisassociateMemberAccountRequestRequestTypeDef",
    "DisassociateS3ResourcesRequestRequestTypeDef",
    "DisassociateS3ResourcesResultTypeDef",
    "FailedS3ResourceTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListMemberAccountsResultTypeDef",
    "ListS3ResourcesRequestRequestTypeDef",
    "ListS3ResourcesResultTypeDef",
    "MemberAccountTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ResourceClassificationTypeDef",
    "S3ResourceClassificationUpdateTypeDef",
    "S3ResourceTypeDef",
    "UpdateS3ResourcesRequestRequestTypeDef",
    "UpdateS3ResourcesResultTypeDef",
)

AssociateMemberAccountRequestRequestTypeDef = TypedDict(
    "AssociateMemberAccountRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
)

AssociateS3ResourcesRequestRequestTypeDef = TypedDict(
    "AssociateS3ResourcesRequestRequestTypeDef",
    {
        "s3Resources": Sequence["S3ResourceClassificationTypeDef"],
        "memberAccountId": NotRequired[str],
    },
)

AssociateS3ResourcesResultTypeDef = TypedDict(
    "AssociateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClassificationTypeTypeDef = TypedDict(
    "ClassificationTypeTypeDef",
    {
        "oneTime": S3OneTimeClassificationTypeType,
        "continuous": Literal["FULL"],
    },
)

ClassificationTypeUpdateTypeDef = TypedDict(
    "ClassificationTypeUpdateTypeDef",
    {
        "oneTime": NotRequired[S3OneTimeClassificationTypeType],
        "continuous": NotRequired[Literal["FULL"]],
    },
)

DisassociateMemberAccountRequestRequestTypeDef = TypedDict(
    "DisassociateMemberAccountRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
)

DisassociateS3ResourcesRequestRequestTypeDef = TypedDict(
    "DisassociateS3ResourcesRequestRequestTypeDef",
    {
        "associatedS3Resources": Sequence["S3ResourceTypeDef"],
        "memberAccountId": NotRequired[str],
    },
)

DisassociateS3ResourcesResultTypeDef = TypedDict(
    "DisassociateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedS3ResourceTypeDef = TypedDict(
    "FailedS3ResourceTypeDef",
    {
        "failedItem": NotRequired["S3ResourceTypeDef"],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListMemberAccountsResultTypeDef = TypedDict(
    "ListMemberAccountsResultTypeDef",
    {
        "memberAccounts": List["MemberAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListS3ResourcesRequestRequestTypeDef = TypedDict(
    "ListS3ResourcesRequestRequestTypeDef",
    {
        "memberAccountId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListS3ResourcesResultTypeDef = TypedDict(
    "ListS3ResourcesResultTypeDef",
    {
        "s3Resources": List["S3ResourceClassificationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberAccountTypeDef = TypedDict(
    "MemberAccountTypeDef",
    {
        "accountId": NotRequired[str],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
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

S3ResourceClassificationTypeDef = TypedDict(
    "S3ResourceClassificationTypeDef",
    {
        "bucketName": str,
        "classificationType": "ClassificationTypeTypeDef",
        "prefix": NotRequired[str],
    },
)

S3ResourceClassificationUpdateTypeDef = TypedDict(
    "S3ResourceClassificationUpdateTypeDef",
    {
        "bucketName": str,
        "classificationTypeUpdate": "ClassificationTypeUpdateTypeDef",
        "prefix": NotRequired[str],
    },
)

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "bucketName": str,
        "prefix": NotRequired[str],
    },
)

UpdateS3ResourcesRequestRequestTypeDef = TypedDict(
    "UpdateS3ResourcesRequestRequestTypeDef",
    {
        "s3ResourcesUpdate": Sequence["S3ResourceClassificationUpdateTypeDef"],
        "memberAccountId": NotRequired[str],
    },
)

UpdateS3ResourcesResultTypeDef = TypedDict(
    "UpdateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
