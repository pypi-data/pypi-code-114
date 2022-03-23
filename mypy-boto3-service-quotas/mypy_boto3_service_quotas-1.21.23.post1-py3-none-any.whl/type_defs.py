"""
Type annotations for service-quotas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_service_quotas.type_defs import DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef

    data: DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ErrorCodeType,
    PeriodUnitType,
    RequestStatusType,
    ServiceQuotaTemplateAssociationStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    "ErrorReasonTypeDef",
    "GetAWSDefaultServiceQuotaRequestRequestTypeDef",
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    "GetRequestedServiceQuotaChangeRequestRequestTypeDef",
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "GetServiceQuotaRequestRequestTypeDef",
    "GetServiceQuotaResponseTypeDef",
    "ListAWSDefaultServiceQuotasRequestRequestTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ListServiceQuotasRequestRequestTypeDef",
    "ListServiceQuotasResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "QuotaPeriodTypeDef",
    "RequestServiceQuotaIncreaseRequestRequestTypeDef",
    "RequestServiceQuotaIncreaseResponseTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceInfoTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ServiceQuotaTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = TypedDict(
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)

ErrorReasonTypeDef = TypedDict(
    "ErrorReasonTypeDef",
    {
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

GetAWSDefaultServiceQuotaRequestRequestTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)

GetAWSDefaultServiceQuotaResponseTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    {
        "Quota": "ServiceQuotaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    {
        "ServiceQuotaTemplateAssociationStatus": ServiceQuotaTemplateAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRequestedServiceQuotaChangeRequestRequestTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeRequestRequestTypeDef",
    {
        "RequestId": str,
    },
)

GetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    {
        "RequestedQuota": "RequestedServiceQuotaChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)

GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceQuotaRequestRequestTypeDef = TypedDict(
    "GetServiceQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)

GetServiceQuotaResponseTypeDef = TypedDict(
    "GetServiceQuotaResponseTypeDef",
    {
        "Quota": "ServiceQuotaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAWSDefaultServiceQuotasRequestRequestTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAWSDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List["ServiceQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "Status": NotRequired[RequestStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "Status": NotRequired[RequestStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            "ServiceQuotaIncreaseRequestInTemplateTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceQuotasRequestRequestTypeDef = TypedDict(
    "ListServiceQuotasRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListServiceQuotasResponseTypeDef = TypedDict(
    "ListServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List["ServiceQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "NextToken": str,
        "Services": List["ServiceInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricInfoTypeDef = TypedDict(
    "MetricInfoTypeDef",
    {
        "MetricNamespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "MetricDimensions": NotRequired[Dict[str, str]],
        "MetricStatisticRecommendation": NotRequired[str],
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

PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef",
    {
        "QuotaCode": str,
        "ServiceCode": str,
        "AwsRegion": str,
        "DesiredValue": float,
    },
)

PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuotaPeriodTypeDef = TypedDict(
    "QuotaPeriodTypeDef",
    {
        "PeriodValue": NotRequired[int],
        "PeriodUnit": NotRequired[PeriodUnitType],
    },
)

RequestServiceQuotaIncreaseRequestRequestTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "DesiredValue": float,
    },
)

RequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseResponseTypeDef",
    {
        "RequestedQuota": "RequestedServiceQuotaChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestedServiceQuotaChangeTypeDef = TypedDict(
    "RequestedServiceQuotaChangeTypeDef",
    {
        "Id": NotRequired[str],
        "CaseId": NotRequired[str],
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "DesiredValue": NotRequired[float],
        "Status": NotRequired[RequestStatusType],
        "Created": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Requester": NotRequired[str],
        "QuotaArn": NotRequired[str],
        "GlobalQuota": NotRequired[bool],
        "Unit": NotRequired[str],
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

ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
    },
)

ServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "DesiredValue": NotRequired[float],
        "AwsRegion": NotRequired[str],
        "Unit": NotRequired[str],
        "GlobalQuota": NotRequired[bool],
    },
)

ServiceQuotaTypeDef = TypedDict(
    "ServiceQuotaTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaArn": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "Value": NotRequired[float],
        "Unit": NotRequired[str],
        "Adjustable": NotRequired[bool],
        "GlobalQuota": NotRequired[bool],
        "UsageMetric": NotRequired["MetricInfoTypeDef"],
        "Period": NotRequired["QuotaPeriodTypeDef"],
        "ErrorReason": NotRequired["ErrorReasonTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
