"""
Type annotations for dataexchange service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dataexchange.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AssetTypeType,
    CodeType,
    JobErrorLimitNameType,
    JobErrorResourceTypesType,
    OriginType,
    ServerSideEncryptionTypesType,
    StateType,
    TypeType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "ApiGatewayApiAssetTypeDef",
    "AssetDestinationEntryTypeDef",
    "AssetDetailsTypeDef",
    "AssetEntryTypeDef",
    "AssetSourceEntryTypeDef",
    "AutoExportRevisionDestinationEntryTypeDef",
    "AutoExportRevisionToS3RequestDetailsTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateEventActionRequestRequestTypeDef",
    "CreateEventActionResponseTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateRevisionRequestRequestTypeDef",
    "CreateRevisionResponseTypeDef",
    "DataSetEntryTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteEventActionRequestRequestTypeDef",
    "DeleteRevisionRequestRequestTypeDef",
    "DetailsTypeDef",
    "EventActionEntryTypeDef",
    "EventTypeDef",
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    "ExportAssetsToS3RequestDetailsTypeDef",
    "ExportAssetsToS3ResponseDetailsTypeDef",
    "ExportRevisionsToS3RequestDetailsTypeDef",
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    "ExportServerSideEncryptionTypeDef",
    "GetAssetRequestRequestTypeDef",
    "GetAssetResponseTypeDef",
    "GetDataSetRequestRequestTypeDef",
    "GetDataSetResponseTypeDef",
    "GetEventActionRequestRequestTypeDef",
    "GetEventActionResponseTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetRevisionRequestRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "ImportAssetFromApiGatewayApiRequestDetailsTypeDef",
    "ImportAssetFromApiGatewayApiResponseDetailsTypeDef",
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    "ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef",
    "ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef",
    "ImportAssetsFromS3RequestDetailsTypeDef",
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    "JobEntryTypeDef",
    "JobErrorTypeDef",
    "ListDataSetRevisionsRequestRequestTypeDef",
    "ListDataSetRevisionsResponseTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListEventActionsRequestRequestTypeDef",
    "ListEventActionsResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListRevisionAssetsRequestRequestTypeDef",
    "ListRevisionAssetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OriginDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "RedshiftDataShareAssetSourceEntryTypeDef",
    "RedshiftDataShareAssetTypeDef",
    "RequestDetailsTypeDef",
    "ResponseDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionDestinationEntryTypeDef",
    "RevisionEntryTypeDef",
    "RevisionPublishedTypeDef",
    "RevokeRevisionRequestRequestTypeDef",
    "RevokeRevisionResponseTypeDef",
    "S3SnapshotAssetTypeDef",
    "SendApiAssetRequestRequestTypeDef",
    "SendApiAssetResponseTypeDef",
    "StartJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssetRequestRequestTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateEventActionRequestRequestTypeDef",
    "UpdateEventActionResponseTypeDef",
    "UpdateRevisionRequestRequestTypeDef",
    "UpdateRevisionResponseTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ExportRevisionToS3": NotRequired["AutoExportRevisionToS3RequestDetailsTypeDef"],
    },
)

ApiGatewayApiAssetTypeDef = TypedDict(
    "ApiGatewayApiAssetTypeDef",
    {
        "ApiDescription": NotRequired[str],
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKey": NotRequired[str],
        "ApiName": NotRequired[str],
        "ApiSpecificationDownloadUrl": NotRequired[str],
        "ApiSpecificationDownloadUrlExpiresAt": NotRequired[datetime],
        "ProtocolType": NotRequired[Literal["REST"]],
        "Stage": NotRequired[str],
    },
)

AssetDestinationEntryTypeDef = TypedDict(
    "AssetDestinationEntryTypeDef",
    {
        "AssetId": str,
        "Bucket": str,
        "Key": NotRequired[str],
    },
)

AssetDetailsTypeDef = TypedDict(
    "AssetDetailsTypeDef",
    {
        "S3SnapshotAsset": NotRequired["S3SnapshotAssetTypeDef"],
        "RedshiftDataShareAsset": NotRequired["RedshiftDataShareAssetTypeDef"],
        "ApiGatewayApiAsset": NotRequired["ApiGatewayApiAssetTypeDef"],
    },
)

AssetEntryTypeDef = TypedDict(
    "AssetEntryTypeDef",
    {
        "Arn": str,
        "AssetDetails": "AssetDetailsTypeDef",
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "UpdatedAt": datetime,
        "SourceId": NotRequired[str],
    },
)

AssetSourceEntryTypeDef = TypedDict(
    "AssetSourceEntryTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

AutoExportRevisionDestinationEntryTypeDef = TypedDict(
    "AutoExportRevisionDestinationEntryTypeDef",
    {
        "Bucket": str,
        "KeyPattern": NotRequired[str],
    },
)

AutoExportRevisionToS3RequestDetailsTypeDef = TypedDict(
    "AutoExportRevisionToS3RequestDetailsTypeDef",
    {
        "RevisionDestination": "AutoExportRevisionDestinationEntryTypeDef",
        "Encryption": NotRequired["ExportServerSideEncryptionTypeDef"],
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

CreateDataSetRequestRequestTypeDef = TypedDict(
    "CreateDataSetRequestRequestTypeDef",
    {
        "AssetType": AssetTypeType,
        "Description": str,
        "Name": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventActionRequestRequestTypeDef = TypedDict(
    "CreateEventActionRequestRequestTypeDef",
    {
        "Action": "ActionTypeDef",
        "Event": "EventTypeDef",
    },
)

CreateEventActionResponseTypeDef = TypedDict(
    "CreateEventActionResponseTypeDef",
    {
        "Action": "ActionTypeDef",
        "Arn": str,
        "CreatedAt": datetime,
        "Event": "EventTypeDef",
        "Id": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "Details": "RequestDetailsTypeDef",
        "Type": TypeType,
    },
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRevisionRequestRequestTypeDef = TypedDict(
    "CreateRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "Comment": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRevisionResponseTypeDef = TypedDict(
    "CreateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSetEntryTypeDef = TypedDict(
    "DataSetEntryTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "UpdatedAt": datetime,
        "OriginDetails": NotRequired["OriginDetailsTypeDef"],
        "SourceId": NotRequired[str],
    },
)

DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)

DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)

DeleteEventActionRequestRequestTypeDef = TypedDict(
    "DeleteEventActionRequestRequestTypeDef",
    {
        "EventActionId": str,
    },
)

DeleteRevisionRequestRequestTypeDef = TypedDict(
    "DeleteRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)

DetailsTypeDef = TypedDict(
    "DetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": NotRequired[
            "ImportAssetFromSignedUrlJobErrorDetailsTypeDef"
        ],
        "ImportAssetsFromS3JobErrorDetails": NotRequired[List["AssetSourceEntryTypeDef"]],
    },
)

EventActionEntryTypeDef = TypedDict(
    "EventActionEntryTypeDef",
    {
        "Action": "ActionTypeDef",
        "Arn": str,
        "CreatedAt": datetime,
        "Event": "EventTypeDef",
        "Id": str,
        "UpdatedAt": datetime,
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "RevisionPublished": NotRequired["RevisionPublishedTypeDef"],
    },
)

ExportAssetToSignedUrlRequestDetailsTypeDef = TypedDict(
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)

ExportAssetToSignedUrlResponseDetailsTypeDef = TypedDict(
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "SignedUrl": NotRequired[str],
        "SignedUrlExpiresAt": NotRequired[datetime],
    },
)

ExportAssetsToS3RequestDetailsTypeDef = TypedDict(
    "ExportAssetsToS3RequestDetailsTypeDef",
    {
        "AssetDestinations": Sequence["AssetDestinationEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
        "Encryption": NotRequired["ExportServerSideEncryptionTypeDef"],
    },
)

ExportAssetsToS3ResponseDetailsTypeDef = TypedDict(
    "ExportAssetsToS3ResponseDetailsTypeDef",
    {
        "AssetDestinations": List["AssetDestinationEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
        "Encryption": NotRequired["ExportServerSideEncryptionTypeDef"],
    },
)

ExportRevisionsToS3RequestDetailsTypeDef = TypedDict(
    "ExportRevisionsToS3RequestDetailsTypeDef",
    {
        "DataSetId": str,
        "RevisionDestinations": Sequence["RevisionDestinationEntryTypeDef"],
        "Encryption": NotRequired["ExportServerSideEncryptionTypeDef"],
    },
)

ExportRevisionsToS3ResponseDetailsTypeDef = TypedDict(
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    {
        "DataSetId": str,
        "RevisionDestinations": List["RevisionDestinationEntryTypeDef"],
        "Encryption": NotRequired["ExportServerSideEncryptionTypeDef"],
        "EventActionArn": NotRequired[str],
    },
)

ExportServerSideEncryptionTypeDef = TypedDict(
    "ExportServerSideEncryptionTypeDef",
    {
        "Type": ServerSideEncryptionTypesType,
        "KmsKeyArn": NotRequired[str],
    },
)

GetAssetRequestRequestTypeDef = TypedDict(
    "GetAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)

GetAssetResponseTypeDef = TypedDict(
    "GetAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": "AssetDetailsTypeDef",
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSetRequestRequestTypeDef = TypedDict(
    "GetDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)

GetDataSetResponseTypeDef = TypedDict(
    "GetDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventActionRequestRequestTypeDef = TypedDict(
    "GetEventActionRequestRequestTypeDef",
    {
        "EventActionId": str,
    },
)

GetEventActionResponseTypeDef = TypedDict(
    "GetEventActionResponseTypeDef",
    {
        "Action": "ActionTypeDef",
        "Arn": str,
        "CreatedAt": datetime,
        "Event": "EventTypeDef",
        "Id": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRevisionRequestRequestTypeDef = TypedDict(
    "GetRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)

GetRevisionResponseTypeDef = TypedDict(
    "GetRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportAssetFromApiGatewayApiRequestDetailsTypeDef = TypedDict(
    "ImportAssetFromApiGatewayApiRequestDetailsTypeDef",
    {
        "ApiId": str,
        "ApiName": str,
        "ApiSpecificationMd5Hash": str,
        "DataSetId": str,
        "ProtocolType": Literal["REST"],
        "RevisionId": str,
        "Stage": str,
        "ApiDescription": NotRequired[str],
        "ApiKey": NotRequired[str],
    },
)

ImportAssetFromApiGatewayApiResponseDetailsTypeDef = TypedDict(
    "ImportAssetFromApiGatewayApiResponseDetailsTypeDef",
    {
        "ApiId": str,
        "ApiName": str,
        "ApiSpecificationMd5Hash": str,
        "ApiSpecificationUploadUrl": str,
        "ApiSpecificationUploadUrlExpiresAt": datetime,
        "DataSetId": str,
        "ProtocolType": Literal["REST"],
        "RevisionId": str,
        "Stage": str,
        "ApiDescription": NotRequired[str],
        "ApiKey": NotRequired[str],
    },
)

ImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {
        "AssetName": str,
    },
)

ImportAssetFromSignedUrlRequestDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
    },
)

ImportAssetFromSignedUrlResponseDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "RevisionId": str,
        "Md5Hash": NotRequired[str],
        "SignedUrl": NotRequired[str],
        "SignedUrlExpiresAt": NotRequired[datetime],
    },
)

ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef",
    {
        "AssetSources": Sequence["RedshiftDataShareAssetSourceEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)

ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef",
    {
        "AssetSources": List["RedshiftDataShareAssetSourceEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)

ImportAssetsFromS3RequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3RequestDetailsTypeDef",
    {
        "AssetSources": Sequence["AssetSourceEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)

ImportAssetsFromS3ResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    {
        "AssetSources": List["AssetSourceEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)

JobEntryTypeDef = TypedDict(
    "JobEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "Errors": NotRequired[List["JobErrorTypeDef"]],
    },
)

JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "Code": CodeType,
        "Message": str,
        "Details": NotRequired["DetailsTypeDef"],
        "LimitName": NotRequired[JobErrorLimitNameType],
        "LimitValue": NotRequired[float],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[JobErrorResourceTypesType],
    },
)

ListDataSetRevisionsRequestRequestTypeDef = TypedDict(
    "ListDataSetRevisionsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDataSetRevisionsResponseTypeDef = TypedDict(
    "ListDataSetRevisionsResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List["RevisionEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSetsRequestRequestTypeDef = TypedDict(
    "ListDataSetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Origin": NotRequired[str],
    },
)

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSets": List["DataSetEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventActionsRequestRequestTypeDef = TypedDict(
    "ListEventActionsRequestRequestTypeDef",
    {
        "EventSourceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEventActionsResponseTypeDef = TypedDict(
    "ListEventActionsResponseTypeDef",
    {
        "EventActions": List["EventActionEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DataSetId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RevisionId": NotRequired[str],
    },
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List["JobEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRevisionAssetsRequestRequestTypeDef = TypedDict(
    "ListRevisionAssetsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRevisionAssetsResponseTypeDef = TypedDict(
    "ListRevisionAssetsResponseTypeDef",
    {
        "Assets": List["AssetEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OriginDetailsTypeDef = TypedDict(
    "OriginDetailsTypeDef",
    {
        "ProductId": str,
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

RedshiftDataShareAssetSourceEntryTypeDef = TypedDict(
    "RedshiftDataShareAssetSourceEntryTypeDef",
    {
        "DataShareArn": str,
    },
)

RedshiftDataShareAssetTypeDef = TypedDict(
    "RedshiftDataShareAssetTypeDef",
    {
        "Arn": str,
    },
)

RequestDetailsTypeDef = TypedDict(
    "RequestDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": NotRequired["ExportAssetToSignedUrlRequestDetailsTypeDef"],
        "ExportAssetsToS3": NotRequired["ExportAssetsToS3RequestDetailsTypeDef"],
        "ExportRevisionsToS3": NotRequired["ExportRevisionsToS3RequestDetailsTypeDef"],
        "ImportAssetFromSignedUrl": NotRequired["ImportAssetFromSignedUrlRequestDetailsTypeDef"],
        "ImportAssetsFromS3": NotRequired["ImportAssetsFromS3RequestDetailsTypeDef"],
        "ImportAssetsFromRedshiftDataShares": NotRequired[
            "ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef"
        ],
        "ImportAssetFromApiGatewayApi": NotRequired[
            "ImportAssetFromApiGatewayApiRequestDetailsTypeDef"
        ],
    },
)

ResponseDetailsTypeDef = TypedDict(
    "ResponseDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": NotRequired["ExportAssetToSignedUrlResponseDetailsTypeDef"],
        "ExportAssetsToS3": NotRequired["ExportAssetsToS3ResponseDetailsTypeDef"],
        "ExportRevisionsToS3": NotRequired["ExportRevisionsToS3ResponseDetailsTypeDef"],
        "ImportAssetFromSignedUrl": NotRequired["ImportAssetFromSignedUrlResponseDetailsTypeDef"],
        "ImportAssetsFromS3": NotRequired["ImportAssetsFromS3ResponseDetailsTypeDef"],
        "ImportAssetsFromRedshiftDataShares": NotRequired[
            "ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef"
        ],
        "ImportAssetFromApiGatewayApi": NotRequired[
            "ImportAssetFromApiGatewayApiResponseDetailsTypeDef"
        ],
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

RevisionDestinationEntryTypeDef = TypedDict(
    "RevisionDestinationEntryTypeDef",
    {
        "Bucket": str,
        "RevisionId": str,
        "KeyPattern": NotRequired[str],
    },
)

RevisionEntryTypeDef = TypedDict(
    "RevisionEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "UpdatedAt": datetime,
        "Comment": NotRequired[str],
        "Finalized": NotRequired[bool],
        "SourceId": NotRequired[str],
        "RevocationComment": NotRequired[str],
        "Revoked": NotRequired[bool],
        "RevokedAt": NotRequired[datetime],
    },
)

RevisionPublishedTypeDef = TypedDict(
    "RevisionPublishedTypeDef",
    {
        "DataSetId": str,
    },
)

RevokeRevisionRequestRequestTypeDef = TypedDict(
    "RevokeRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "RevocationComment": str,
    },
)

RevokeRevisionResponseTypeDef = TypedDict(
    "RevokeRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3SnapshotAssetTypeDef = TypedDict(
    "S3SnapshotAssetTypeDef",
    {
        "Size": float,
    },
)

SendApiAssetRequestRequestTypeDef = TypedDict(
    "SendApiAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "Body": NotRequired[str],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
        "RequestHeaders": NotRequired[Mapping[str, str]],
        "Method": NotRequired[str],
        "Path": NotRequired[str],
    },
)

SendApiAssetResponseTypeDef = TypedDict(
    "SendApiAssetResponseTypeDef",
    {
        "Body": str,
        "ResponseHeaders": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRequestRequestTypeDef = TypedDict(
    "StartJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAssetRequestRequestTypeDef = TypedDict(
    "UpdateAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "Name": str,
        "RevisionId": str,
    },
)

UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": "AssetDetailsTypeDef",
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSetRequestRequestTypeDef = TypedDict(
    "UpdateDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
        "Description": NotRequired[str],
        "Name": NotRequired[str],
    },
)

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEventActionRequestRequestTypeDef = TypedDict(
    "UpdateEventActionRequestRequestTypeDef",
    {
        "EventActionId": str,
        "Action": NotRequired["ActionTypeDef"],
    },
)

UpdateEventActionResponseTypeDef = TypedDict(
    "UpdateEventActionResponseTypeDef",
    {
        "Action": "ActionTypeDef",
        "Arn": str,
        "CreatedAt": datetime,
        "Event": "EventTypeDef",
        "Id": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRevisionRequestRequestTypeDef = TypedDict(
    "UpdateRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "Comment": NotRequired[str],
        "Finalized": NotRequired[bool],
    },
)

UpdateRevisionResponseTypeDef = TypedDict(
    "UpdateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
