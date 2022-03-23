"""
Type annotations for route53-recovery-readiness service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53_recovery_readiness.type_defs import CellOutputTypeDef

    data: CellOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import ReadinessType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CellOutputTypeDef",
    "CreateCellRequestRequestTypeDef",
    "CreateCellResponseTypeDef",
    "CreateCrossAccountAuthorizationRequestRequestTypeDef",
    "CreateCrossAccountAuthorizationResponseTypeDef",
    "CreateReadinessCheckRequestRequestTypeDef",
    "CreateReadinessCheckResponseTypeDef",
    "CreateRecoveryGroupRequestRequestTypeDef",
    "CreateRecoveryGroupResponseTypeDef",
    "CreateResourceSetRequestRequestTypeDef",
    "CreateResourceSetResponseTypeDef",
    "DNSTargetResourceTypeDef",
    "DeleteCellRequestRequestTypeDef",
    "DeleteCrossAccountAuthorizationRequestRequestTypeDef",
    "DeleteReadinessCheckRequestRequestTypeDef",
    "DeleteRecoveryGroupRequestRequestTypeDef",
    "DeleteResourceSetRequestRequestTypeDef",
    "GetArchitectureRecommendationsRequestRequestTypeDef",
    "GetArchitectureRecommendationsResponseTypeDef",
    "GetCellReadinessSummaryRequestRequestTypeDef",
    "GetCellReadinessSummaryResponseTypeDef",
    "GetCellRequestRequestTypeDef",
    "GetCellResponseTypeDef",
    "GetReadinessCheckRequestRequestTypeDef",
    "GetReadinessCheckResourceStatusRequestRequestTypeDef",
    "GetReadinessCheckResourceStatusResponseTypeDef",
    "GetReadinessCheckResponseTypeDef",
    "GetReadinessCheckStatusRequestRequestTypeDef",
    "GetReadinessCheckStatusResponseTypeDef",
    "GetRecoveryGroupReadinessSummaryRequestRequestTypeDef",
    "GetRecoveryGroupReadinessSummaryResponseTypeDef",
    "GetRecoveryGroupRequestRequestTypeDef",
    "GetRecoveryGroupResponseTypeDef",
    "GetResourceSetRequestRequestTypeDef",
    "GetResourceSetResponseTypeDef",
    "ListCellsRequestRequestTypeDef",
    "ListCellsResponseTypeDef",
    "ListCrossAccountAuthorizationsRequestRequestTypeDef",
    "ListCrossAccountAuthorizationsResponseTypeDef",
    "ListReadinessChecksRequestRequestTypeDef",
    "ListReadinessChecksResponseTypeDef",
    "ListRecoveryGroupsRequestRequestTypeDef",
    "ListRecoveryGroupsResponseTypeDef",
    "ListResourceSetsRequestRequestTypeDef",
    "ListResourceSetsResponseTypeDef",
    "ListRulesOutputTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourcesRequestRequestTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "MessageTypeDef",
    "NLBResourceTypeDef",
    "PaginatorConfigTypeDef",
    "R53ResourceRecordTypeDef",
    "ReadinessCheckOutputTypeDef",
    "ReadinessCheckSummaryTypeDef",
    "RecommendationTypeDef",
    "RecoveryGroupOutputTypeDef",
    "ResourceResultTypeDef",
    "ResourceSetOutputTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RuleResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetResourceTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCellRequestRequestTypeDef",
    "UpdateCellResponseTypeDef",
    "UpdateReadinessCheckRequestRequestTypeDef",
    "UpdateReadinessCheckResponseTypeDef",
    "UpdateRecoveryGroupRequestRequestTypeDef",
    "UpdateRecoveryGroupResponseTypeDef",
    "UpdateResourceSetRequestRequestTypeDef",
    "UpdateResourceSetResponseTypeDef",
)

CellOutputTypeDef = TypedDict(
    "CellOutputTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

CreateCellRequestRequestTypeDef = TypedDict(
    "CreateCellRequestRequestTypeDef",
    {
        "CellName": str,
        "Cells": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateCellResponseTypeDef = TypedDict(
    "CreateCellResponseTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCrossAccountAuthorizationRequestRequestTypeDef = TypedDict(
    "CreateCrossAccountAuthorizationRequestRequestTypeDef",
    {
        "CrossAccountAuthorization": str,
    },
)

CreateCrossAccountAuthorizationResponseTypeDef = TypedDict(
    "CreateCrossAccountAuthorizationResponseTypeDef",
    {
        "CrossAccountAuthorization": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReadinessCheckRequestRequestTypeDef = TypedDict(
    "CreateReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceSetName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateReadinessCheckResponseTypeDef = TypedDict(
    "CreateReadinessCheckResponseTypeDef",
    {
        "ReadinessCheckArn": str,
        "ReadinessCheckName": str,
        "ResourceSet": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecoveryGroupRequestRequestTypeDef = TypedDict(
    "CreateRecoveryGroupRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
        "Cells": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRecoveryGroupResponseTypeDef = TypedDict(
    "CreateRecoveryGroupResponseTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceSetRequestRequestTypeDef = TypedDict(
    "CreateResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": Sequence["ResourceTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateResourceSetResponseTypeDef = TypedDict(
    "CreateResourceSetResponseTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List["ResourceTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DNSTargetResourceTypeDef = TypedDict(
    "DNSTargetResourceTypeDef",
    {
        "DomainName": NotRequired[str],
        "HostedZoneArn": NotRequired[str],
        "RecordSetId": NotRequired[str],
        "RecordType": NotRequired[str],
        "TargetResource": NotRequired["TargetResourceTypeDef"],
    },
)

DeleteCellRequestRequestTypeDef = TypedDict(
    "DeleteCellRequestRequestTypeDef",
    {
        "CellName": str,
    },
)

DeleteCrossAccountAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteCrossAccountAuthorizationRequestRequestTypeDef",
    {
        "CrossAccountAuthorization": str,
    },
)

DeleteReadinessCheckRequestRequestTypeDef = TypedDict(
    "DeleteReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
    },
)

DeleteRecoveryGroupRequestRequestTypeDef = TypedDict(
    "DeleteRecoveryGroupRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
    },
)

DeleteResourceSetRequestRequestTypeDef = TypedDict(
    "DeleteResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
    },
)

GetArchitectureRecommendationsRequestRequestTypeDef = TypedDict(
    "GetArchitectureRecommendationsRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetArchitectureRecommendationsResponseTypeDef = TypedDict(
    "GetArchitectureRecommendationsResponseTypeDef",
    {
        "LastAuditTimestamp": datetime,
        "NextToken": str,
        "Recommendations": List["RecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCellReadinessSummaryRequestRequestTypeDef = TypedDict(
    "GetCellReadinessSummaryRequestRequestTypeDef",
    {
        "CellName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetCellReadinessSummaryResponseTypeDef = TypedDict(
    "GetCellReadinessSummaryResponseTypeDef",
    {
        "NextToken": str,
        "Readiness": ReadinessType,
        "ReadinessChecks": List["ReadinessCheckSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCellRequestRequestTypeDef = TypedDict(
    "GetCellRequestRequestTypeDef",
    {
        "CellName": str,
    },
)

GetCellResponseTypeDef = TypedDict(
    "GetCellResponseTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadinessCheckRequestRequestTypeDef = TypedDict(
    "GetReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
    },
)

GetReadinessCheckResourceStatusRequestRequestTypeDef = TypedDict(
    "GetReadinessCheckResourceStatusRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetReadinessCheckResourceStatusResponseTypeDef = TypedDict(
    "GetReadinessCheckResourceStatusResponseTypeDef",
    {
        "NextToken": str,
        "Readiness": ReadinessType,
        "Rules": List["RuleResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadinessCheckResponseTypeDef = TypedDict(
    "GetReadinessCheckResponseTypeDef",
    {
        "ReadinessCheckArn": str,
        "ReadinessCheckName": str,
        "ResourceSet": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadinessCheckStatusRequestRequestTypeDef = TypedDict(
    "GetReadinessCheckStatusRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetReadinessCheckStatusResponseTypeDef = TypedDict(
    "GetReadinessCheckStatusResponseTypeDef",
    {
        "Messages": List["MessageTypeDef"],
        "NextToken": str,
        "Readiness": ReadinessType,
        "Resources": List["ResourceResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecoveryGroupReadinessSummaryRequestRequestTypeDef = TypedDict(
    "GetRecoveryGroupReadinessSummaryRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetRecoveryGroupReadinessSummaryResponseTypeDef = TypedDict(
    "GetRecoveryGroupReadinessSummaryResponseTypeDef",
    {
        "NextToken": str,
        "Readiness": ReadinessType,
        "ReadinessChecks": List["ReadinessCheckSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecoveryGroupRequestRequestTypeDef = TypedDict(
    "GetRecoveryGroupRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
    },
)

GetRecoveryGroupResponseTypeDef = TypedDict(
    "GetRecoveryGroupResponseTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceSetRequestRequestTypeDef = TypedDict(
    "GetResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
    },
)

GetResourceSetResponseTypeDef = TypedDict(
    "GetResourceSetResponseTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List["ResourceTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCellsRequestRequestTypeDef = TypedDict(
    "ListCellsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCellsResponseTypeDef = TypedDict(
    "ListCellsResponseTypeDef",
    {
        "Cells": List["CellOutputTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCrossAccountAuthorizationsRequestRequestTypeDef = TypedDict(
    "ListCrossAccountAuthorizationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCrossAccountAuthorizationsResponseTypeDef = TypedDict(
    "ListCrossAccountAuthorizationsResponseTypeDef",
    {
        "CrossAccountAuthorizations": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReadinessChecksRequestRequestTypeDef = TypedDict(
    "ListReadinessChecksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListReadinessChecksResponseTypeDef = TypedDict(
    "ListReadinessChecksResponseTypeDef",
    {
        "NextToken": str,
        "ReadinessChecks": List["ReadinessCheckOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecoveryGroupsRequestRequestTypeDef = TypedDict(
    "ListRecoveryGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRecoveryGroupsResponseTypeDef = TypedDict(
    "ListRecoveryGroupsResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryGroups": List["RecoveryGroupOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceSetsRequestRequestTypeDef = TypedDict(
    "ListResourceSetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListResourceSetsResponseTypeDef = TypedDict(
    "ListResourceSetsResponseTypeDef",
    {
        "NextToken": str,
        "ResourceSets": List["ResourceSetOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesOutputTypeDef = TypedDict(
    "ListRulesOutputTypeDef",
    {
        "ResourceType": str,
        "RuleDescription": str,
        "RuleId": str,
    },
)

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "NextToken": str,
        "Rules": List["ListRulesOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourcesRequestRequestTypeDef = TypedDict(
    "ListTagsForResourcesRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageText": NotRequired[str],
    },
)

NLBResourceTypeDef = TypedDict(
    "NLBResourceTypeDef",
    {
        "Arn": NotRequired[str],
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

R53ResourceRecordTypeDef = TypedDict(
    "R53ResourceRecordTypeDef",
    {
        "DomainName": NotRequired[str],
        "RecordSetId": NotRequired[str],
    },
)

ReadinessCheckOutputTypeDef = TypedDict(
    "ReadinessCheckOutputTypeDef",
    {
        "ReadinessCheckArn": str,
        "ResourceSet": str,
        "ReadinessCheckName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ReadinessCheckSummaryTypeDef = TypedDict(
    "ReadinessCheckSummaryTypeDef",
    {
        "Readiness": NotRequired[ReadinessType],
        "ReadinessCheckName": NotRequired[str],
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "RecommendationText": str,
    },
)

RecoveryGroupOutputTypeDef = TypedDict(
    "RecoveryGroupOutputTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": NotRequired[Dict[str, str]],
    },
)

ResourceResultTypeDef = TypedDict(
    "ResourceResultTypeDef",
    {
        "LastCheckedTimestamp": datetime,
        "Readiness": ReadinessType,
        "ComponentId": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)

ResourceSetOutputTypeDef = TypedDict(
    "ResourceSetOutputTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List["ResourceTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ComponentId": NotRequired[str],
        "DnsTargetResource": NotRequired["DNSTargetResourceTypeDef"],
        "ReadinessScopes": NotRequired[Sequence[str]],
        "ResourceArn": NotRequired[str],
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

RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "LastCheckedTimestamp": datetime,
        "Messages": List["MessageTypeDef"],
        "Readiness": ReadinessType,
        "RuleId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TargetResourceTypeDef = TypedDict(
    "TargetResourceTypeDef",
    {
        "NLBResource": NotRequired["NLBResourceTypeDef"],
        "R53Resource": NotRequired["R53ResourceRecordTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateCellRequestRequestTypeDef = TypedDict(
    "UpdateCellRequestRequestTypeDef",
    {
        "CellName": str,
        "Cells": Sequence[str],
    },
)

UpdateCellResponseTypeDef = TypedDict(
    "UpdateCellResponseTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReadinessCheckRequestRequestTypeDef = TypedDict(
    "UpdateReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceSetName": str,
    },
)

UpdateReadinessCheckResponseTypeDef = TypedDict(
    "UpdateReadinessCheckResponseTypeDef",
    {
        "ReadinessCheckArn": str,
        "ReadinessCheckName": str,
        "ResourceSet": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecoveryGroupRequestRequestTypeDef = TypedDict(
    "UpdateRecoveryGroupRequestRequestTypeDef",
    {
        "Cells": Sequence[str],
        "RecoveryGroupName": str,
    },
)

UpdateRecoveryGroupResponseTypeDef = TypedDict(
    "UpdateRecoveryGroupResponseTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourceSetRequestRequestTypeDef = TypedDict(
    "UpdateResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": Sequence["ResourceTypeDef"],
    },
)

UpdateResourceSetResponseTypeDef = TypedDict(
    "UpdateResourceSetResponseTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List["ResourceTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
