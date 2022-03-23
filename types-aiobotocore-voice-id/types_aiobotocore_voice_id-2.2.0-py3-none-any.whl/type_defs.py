"""
Type annotations for voice-id service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_voice_id.type_defs import AuthenticationConfigurationTypeDef

    data: AuthenticationConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AuthenticationDecisionType,
    DomainStatusType,
    DuplicateRegistrationActionType,
    ExistingEnrollmentActionType,
    FraudDetectionActionType,
    FraudDetectionDecisionType,
    FraudsterRegistrationJobStatusType,
    SpeakerEnrollmentJobStatusType,
    SpeakerStatusType,
    StreamingStatusType,
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
    "AuthenticationConfigurationTypeDef",
    "AuthenticationResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteFraudsterRequestRequestTypeDef",
    "DeleteSpeakerRequestRequestTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeFraudsterRegistrationJobRequestRequestTypeDef",
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    "DescribeFraudsterRequestRequestTypeDef",
    "DescribeFraudsterResponseTypeDef",
    "DescribeSpeakerEnrollmentJobRequestRequestTypeDef",
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    "DescribeSpeakerRequestRequestTypeDef",
    "DescribeSpeakerResponseTypeDef",
    "DomainSummaryTypeDef",
    "DomainTypeDef",
    "EnrollmentConfigTypeDef",
    "EnrollmentJobFraudDetectionConfigTypeDef",
    "EvaluateSessionRequestRequestTypeDef",
    "EvaluateSessionResponseTypeDef",
    "FailureDetailsTypeDef",
    "FraudDetectionConfigurationTypeDef",
    "FraudDetectionResultTypeDef",
    "FraudRiskDetailsTypeDef",
    "FraudsterRegistrationJobSummaryTypeDef",
    "FraudsterRegistrationJobTypeDef",
    "FraudsterTypeDef",
    "InputDataConfigTypeDef",
    "JobProgressTypeDef",
    "KnownFraudsterRiskTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFraudsterRegistrationJobsRequestRequestTypeDef",
    "ListFraudsterRegistrationJobsResponseTypeDef",
    "ListSpeakerEnrollmentJobsRequestRequestTypeDef",
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    "ListSpeakersRequestRequestTypeDef",
    "ListSpeakersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OptOutSpeakerRequestRequestTypeDef",
    "OptOutSpeakerResponseTypeDef",
    "OutputDataConfigTypeDef",
    "RegistrationConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SpeakerEnrollmentJobSummaryTypeDef",
    "SpeakerEnrollmentJobTypeDef",
    "SpeakerSummaryTypeDef",
    "SpeakerTypeDef",
    "StartFraudsterRegistrationJobRequestRequestTypeDef",
    "StartFraudsterRegistrationJobResponseTypeDef",
    "StartSpeakerEnrollmentJobRequestRequestTypeDef",
    "StartSpeakerEnrollmentJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateDomainResponseTypeDef",
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "AcceptanceThreshold": int,
    },
)

AuthenticationResultTypeDef = TypedDict(
    "AuthenticationResultTypeDef",
    {
        "AudioAggregationEndedAt": NotRequired[datetime],
        "AudioAggregationStartedAt": NotRequired[datetime],
        "AuthenticationResultId": NotRequired[str],
        "Configuration": NotRequired["AuthenticationConfigurationTypeDef"],
        "CustomerSpeakerId": NotRequired[str],
        "Decision": NotRequired[AuthenticationDecisionType],
        "GeneratedSpeakerId": NotRequired[str],
        "Score": NotRequired[int],
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "Name": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "Domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

DeleteFraudsterRequestRequestTypeDef = TypedDict(
    "DeleteFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
    },
)

DeleteSpeakerRequestRequestTypeDef = TypedDict(
    "DeleteSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "Domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "DescribeFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobId": str,
    },
)

DescribeFraudsterRegistrationJobResponseTypeDef = TypedDict(
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    {
        "Job": "FraudsterRegistrationJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFraudsterRequestRequestTypeDef = TypedDict(
    "DescribeFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
    },
)

DescribeFraudsterResponseTypeDef = TypedDict(
    "DescribeFraudsterResponseTypeDef",
    {
        "Fraudster": "FraudsterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "DescribeSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobId": str,
    },
)

DescribeSpeakerEnrollmentJobResponseTypeDef = TypedDict(
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    {
        "Job": "SpeakerEnrollmentJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpeakerRequestRequestTypeDef = TypedDict(
    "DescribeSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)

DescribeSpeakerResponseTypeDef = TypedDict(
    "DescribeSpeakerResponseTypeDef",
    {
        "Speaker": "SpeakerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "DomainId": NotRequired[str],
        "DomainStatus": NotRequired[DomainStatusType],
        "Name": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "UpdatedAt": NotRequired[datetime],
    },
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "DomainId": NotRequired[str],
        "DomainStatus": NotRequired[DomainStatusType],
        "Name": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "UpdatedAt": NotRequired[datetime],
    },
)

EnrollmentConfigTypeDef = TypedDict(
    "EnrollmentConfigTypeDef",
    {
        "ExistingEnrollmentAction": NotRequired[ExistingEnrollmentActionType],
        "FraudDetectionConfig": NotRequired["EnrollmentJobFraudDetectionConfigTypeDef"],
    },
)

EnrollmentJobFraudDetectionConfigTypeDef = TypedDict(
    "EnrollmentJobFraudDetectionConfigTypeDef",
    {
        "FraudDetectionAction": NotRequired[FraudDetectionActionType],
        "RiskThreshold": NotRequired[int],
    },
)

EvaluateSessionRequestRequestTypeDef = TypedDict(
    "EvaluateSessionRequestRequestTypeDef",
    {
        "DomainId": str,
        "SessionNameOrId": str,
    },
)

EvaluateSessionResponseTypeDef = TypedDict(
    "EvaluateSessionResponseTypeDef",
    {
        "AuthenticationResult": "AuthenticationResultTypeDef",
        "DomainId": str,
        "FraudDetectionResult": "FraudDetectionResultTypeDef",
        "SessionId": str,
        "SessionName": str,
        "StreamingStatus": StreamingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
        "StatusCode": NotRequired[int],
    },
)

FraudDetectionConfigurationTypeDef = TypedDict(
    "FraudDetectionConfigurationTypeDef",
    {
        "RiskThreshold": int,
    },
)

FraudDetectionResultTypeDef = TypedDict(
    "FraudDetectionResultTypeDef",
    {
        "AudioAggregationEndedAt": NotRequired[datetime],
        "AudioAggregationStartedAt": NotRequired[datetime],
        "Configuration": NotRequired["FraudDetectionConfigurationTypeDef"],
        "Decision": NotRequired[FraudDetectionDecisionType],
        "FraudDetectionResultId": NotRequired[str],
        "Reasons": NotRequired[List[Literal["KNOWN_FRAUDSTER"]]],
        "RiskDetails": NotRequired["FraudRiskDetailsTypeDef"],
    },
)

FraudRiskDetailsTypeDef = TypedDict(
    "FraudRiskDetailsTypeDef",
    {
        "KnownFraudsterRisk": "KnownFraudsterRiskTypeDef",
    },
)

FraudsterRegistrationJobSummaryTypeDef = TypedDict(
    "FraudsterRegistrationJobSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "FailureDetails": NotRequired["FailureDetailsTypeDef"],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired["JobProgressTypeDef"],
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
    },
)

FraudsterRegistrationJobTypeDef = TypedDict(
    "FraudsterRegistrationJobTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "FailureDetails": NotRequired["FailureDetailsTypeDef"],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired["JobProgressTypeDef"],
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "RegistrationConfig": NotRequired["RegistrationConfigTypeDef"],
    },
)

FraudsterTypeDef = TypedDict(
    "FraudsterTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "GeneratedFraudsterId": NotRequired[str],
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)

JobProgressTypeDef = TypedDict(
    "JobProgressTypeDef",
    {
        "PercentComplete": NotRequired[int],
    },
)

KnownFraudsterRiskTypeDef = TypedDict(
    "KnownFraudsterRiskTypeDef",
    {
        "RiskScore": int,
        "GeneratedFraudsterId": NotRequired[str],
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "DomainSummaries": List["DomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFraudsterRegistrationJobsRequestRequestTypeDef = TypedDict(
    "ListFraudsterRegistrationJobsRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFraudsterRegistrationJobsResponseTypeDef = TypedDict(
    "ListFraudsterRegistrationJobsResponseTypeDef",
    {
        "JobSummaries": List["FraudsterRegistrationJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpeakerEnrollmentJobsRequestRequestTypeDef = TypedDict(
    "ListSpeakerEnrollmentJobsRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSpeakerEnrollmentJobsResponseTypeDef = TypedDict(
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    {
        "JobSummaries": List["SpeakerEnrollmentJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpeakersRequestRequestTypeDef = TypedDict(
    "ListSpeakersRequestRequestTypeDef",
    {
        "DomainId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSpeakersResponseTypeDef = TypedDict(
    "ListSpeakersResponseTypeDef",
    {
        "NextToken": str,
        "SpeakerSummaries": List["SpeakerSummaryTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptOutSpeakerRequestRequestTypeDef = TypedDict(
    "OptOutSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)

OptOutSpeakerResponseTypeDef = TypedDict(
    "OptOutSpeakerResponseTypeDef",
    {
        "Speaker": "SpeakerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
    },
)

RegistrationConfigTypeDef = TypedDict(
    "RegistrationConfigTypeDef",
    {
        "DuplicateRegistrationAction": NotRequired[DuplicateRegistrationActionType],
        "FraudsterSimilarityThreshold": NotRequired[int],
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

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
)

SpeakerEnrollmentJobSummaryTypeDef = TypedDict(
    "SpeakerEnrollmentJobSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "FailureDetails": NotRequired["FailureDetailsTypeDef"],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired["JobProgressTypeDef"],
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
    },
)

SpeakerEnrollmentJobTypeDef = TypedDict(
    "SpeakerEnrollmentJobTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "EnrollmentConfig": NotRequired["EnrollmentConfigTypeDef"],
        "FailureDetails": NotRequired["FailureDetailsTypeDef"],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired["JobProgressTypeDef"],
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
    },
)

SpeakerSummaryTypeDef = TypedDict(
    "SpeakerSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "CustomerSpeakerId": NotRequired[str],
        "DomainId": NotRequired[str],
        "GeneratedSpeakerId": NotRequired[str],
        "Status": NotRequired[SpeakerStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)

SpeakerTypeDef = TypedDict(
    "SpeakerTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "CustomerSpeakerId": NotRequired[str],
        "DomainId": NotRequired[str],
        "GeneratedSpeakerId": NotRequired[str],
        "Status": NotRequired[SpeakerStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)

StartFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "StartFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "DataAccessRoleArn": str,
        "DomainId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ClientToken": NotRequired[str],
        "JobName": NotRequired[str],
        "RegistrationConfig": NotRequired["RegistrationConfigTypeDef"],
    },
)

StartFraudsterRegistrationJobResponseTypeDef = TypedDict(
    "StartFraudsterRegistrationJobResponseTypeDef",
    {
        "Job": "FraudsterRegistrationJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "StartSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "DataAccessRoleArn": str,
        "DomainId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ClientToken": NotRequired[str],
        "EnrollmentConfig": NotRequired["EnrollmentConfigTypeDef"],
        "JobName": NotRequired[str],
    },
)

StartSpeakerEnrollmentJobResponseTypeDef = TypedDict(
    "StartSpeakerEnrollmentJobResponseTypeDef",
    {
        "Job": "SpeakerEnrollmentJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDomainRequestRequestTypeDef = TypedDict(
    "UpdateDomainRequestRequestTypeDef",
    {
        "DomainId": str,
        "Name": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Description": NotRequired[str],
    },
)

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "Domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
