"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyRequestRequestTypeDef

    data: AddProfileKeyRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ConflictResolvingModelType,
    DataPullModeType,
    FieldContentTypeType,
    GenderType,
    IdentityResolutionJobStatusType,
    JobScheduleDayOfTheWeekType,
    MarketoConnectorOperatorType,
    OperatorPropertiesKeysType,
    PartyTypeType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    StatusType,
    TaskTypeType,
    TriggerTypeType,
    ZendeskConnectorOperatorType,
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
    "AddProfileKeyRequestRequestTypeDef",
    "AddProfileKeyResponseTypeDef",
    "AddressTypeDef",
    "AppflowIntegrationTypeDef",
    "AppflowIntegrationWorkflowAttributesTypeDef",
    "AppflowIntegrationWorkflowMetricsTypeDef",
    "AppflowIntegrationWorkflowStepTypeDef",
    "AutoMergingTypeDef",
    "BatchTypeDef",
    "ConflictResolutionTypeDef",
    "ConnectorOperatorTypeDef",
    "ConsolidationTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateIntegrationWorkflowRequestRequestTypeDef",
    "CreateIntegrationWorkflowResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyRequestRequestTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectRequestRequestTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteProfileResponseTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DomainStatsTypeDef",
    "ExportingConfigTypeDef",
    "ExportingLocationTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FlowDefinitionTypeDef",
    "GetAutoMergingPreviewRequestRequestTypeDef",
    "GetAutoMergingPreviewResponseTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetDomainResponseTypeDef",
    "GetIdentityResolutionJobRequestRequestTypeDef",
    "GetIdentityResolutionJobResponseTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetMatchesRequestRequestTypeDef",
    "GetMatchesResponseTypeDef",
    "GetProfileObjectTypeRequestRequestTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowStepsRequestRequestTypeDef",
    "GetWorkflowStepsResponseTypeDef",
    "IdentityResolutionJobTypeDef",
    "IncrementalPullConfigTypeDef",
    "IntegrationConfigTypeDef",
    "JobScheduleTypeDef",
    "JobStatsTypeDef",
    "ListAccountIntegrationsRequestRequestTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    "ListIdentityResolutionJobsResponseTypeDef",
    "ListIntegrationItemTypeDef",
    "ListIntegrationsRequestRequestTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectTypesRequestRequestTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ListProfileObjectsRequestRequestTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkflowsItemTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchItemTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "MergeProfilesRequestRequestTypeDef",
    "MergeProfilesResponseTypeDef",
    "ObjectFilterTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "ProfileTypeDef",
    "PutIntegrationRequestRequestTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectRequestRequestTypeDef",
    "PutProfileObjectResponseTypeDef",
    "PutProfileObjectTypeRequestRequestTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3ExportingConfigTypeDef",
    "S3ExportingLocationTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "SearchProfilesRequestRequestTypeDef",
    "SearchProfilesResponseTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddressTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateProfileResponseTypeDef",
    "WorkflowAttributesTypeDef",
    "WorkflowMetricsTypeDef",
    "WorkflowStepItemTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

AddProfileKeyRequestRequestTypeDef = TypedDict(
    "AddProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": Sequence[str],
        "DomainName": str,
    },
)

AddProfileKeyResponseTypeDef = TypedDict(
    "AddProfileKeyResponseTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "Address1": NotRequired[str],
        "Address2": NotRequired[str],
        "Address3": NotRequired[str],
        "Address4": NotRequired[str],
        "City": NotRequired[str],
        "County": NotRequired[str],
        "State": NotRequired[str],
        "Province": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
    },
)

AppflowIntegrationTypeDef = TypedDict(
    "AppflowIntegrationTypeDef",
    {
        "FlowDefinition": "FlowDefinitionTypeDef",
        "Batches": NotRequired[Sequence["BatchTypeDef"]],
    },
)

AppflowIntegrationWorkflowAttributesTypeDef = TypedDict(
    "AppflowIntegrationWorkflowAttributesTypeDef",
    {
        "SourceConnectorType": SourceConnectorTypeType,
        "ConnectorProfileName": str,
        "RoleArn": NotRequired[str],
    },
)

AppflowIntegrationWorkflowMetricsTypeDef = TypedDict(
    "AppflowIntegrationWorkflowMetricsTypeDef",
    {
        "RecordsProcessed": int,
        "StepsCompleted": int,
        "TotalSteps": int,
    },
)

AppflowIntegrationWorkflowStepTypeDef = TypedDict(
    "AppflowIntegrationWorkflowStepTypeDef",
    {
        "FlowName": str,
        "Status": StatusType,
        "ExecutionMessage": str,
        "RecordsProcessed": int,
        "BatchRecordsStartTime": str,
        "BatchRecordsEndTime": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)

AutoMergingTypeDef = TypedDict(
    "AutoMergingTypeDef",
    {
        "Enabled": bool,
        "Consolidation": NotRequired["ConsolidationTypeDef"],
        "ConflictResolution": NotRequired["ConflictResolutionTypeDef"],
    },
)

BatchTypeDef = TypedDict(
    "BatchTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "ConflictResolvingModel": ConflictResolvingModelType,
        "SourceName": NotRequired[str],
    },
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Marketo": NotRequired[MarketoConnectorOperatorType],
        "S3": NotRequired[S3ConnectorOperatorType],
        "Salesforce": NotRequired[SalesforceConnectorOperatorType],
        "ServiceNow": NotRequired[ServiceNowConnectorOperatorType],
        "Zendesk": NotRequired[ZendeskConnectorOperatorType],
    },
)

ConsolidationTypeDef = TypedDict(
    "ConsolidationTypeDef",
    {
        "MatchingAttributesList": Sequence[Sequence[str]],
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": NotRequired[str],
        "DeadLetterQueueUrl": NotRequired[str],
        "Matching": NotRequired["MatchingRequestTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntegrationWorkflowRequestRequestTypeDef = TypedDict(
    "CreateIntegrationWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "IntegrationConfig": "IntegrationConfigTypeDef",
        "ObjectTypeName": str,
        "RoleArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateIntegrationWorkflowResponseTypeDef = TypedDict(
    "CreateIntegrationWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired["AddressTypeDef"],
        "ShippingAddress": NotRequired["AddressTypeDef"],
        "MailingAddress": NotRequired["AddressTypeDef"],
        "BillingAddress": NotRequired["AddressTypeDef"],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)

DeleteIntegrationResponseTypeDef = TypedDict(
    "DeleteIntegrationResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileKeyRequestRequestTypeDef = TypedDict(
    "DeleteProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": Sequence[str],
        "DomainName": str,
    },
)

DeleteProfileKeyResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileObjectRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ProfileObjectUniqueKey": str,
        "ObjectTypeName": str,
        "DomainName": str,
    },
)

DeleteProfileObjectResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)

DeleteProfileObjectTypeResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "DomainName": str,
    },
)

DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)

DomainStatsTypeDef = TypedDict(
    "DomainStatsTypeDef",
    {
        "ProfileCount": NotRequired[int],
        "MeteringProfileCount": NotRequired[int],
        "ObjectCount": NotRequired[int],
        "TotalSize": NotRequired[int],
    },
)

ExportingConfigTypeDef = TypedDict(
    "ExportingConfigTypeDef",
    {
        "S3Exporting": NotRequired["S3ExportingConfigTypeDef"],
    },
)

ExportingLocationTypeDef = TypedDict(
    "ExportingLocationTypeDef",
    {
        "S3Exporting": NotRequired["S3ExportingLocationTypeDef"],
    },
)

FieldSourceProfileIdsTypeDef = TypedDict(
    "FieldSourceProfileIdsTypeDef",
    {
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[str],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[str],
        "ShippingAddress": NotRequired[str],
        "MailingAddress": NotRequired[str],
        "BillingAddress": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "FlowName": str,
        "KmsArn": str,
        "SourceFlowConfig": "SourceFlowConfigTypeDef",
        "Tasks": Sequence["TaskTypeDef"],
        "TriggerConfig": "TriggerConfigTypeDef",
        "Description": NotRequired[str],
    },
)

GetAutoMergingPreviewRequestRequestTypeDef = TypedDict(
    "GetAutoMergingPreviewRequestRequestTypeDef",
    {
        "DomainName": str,
        "Consolidation": "ConsolidationTypeDef",
        "ConflictResolution": "ConflictResolutionTypeDef",
    },
)

GetAutoMergingPreviewResponseTypeDef = TypedDict(
    "GetAutoMergingPreviewResponseTypeDef",
    {
        "DomainName": str,
        "NumberOfMatchesInSample": int,
        "NumberOfProfilesInSample": int,
        "NumberOfProfilesWillBeMerged": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": "DomainStatsTypeDef",
        "Matching": "MatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityResolutionJobRequestRequestTypeDef = TypedDict(
    "GetIdentityResolutionJobRequestRequestTypeDef",
    {
        "DomainName": str,
        "JobId": str,
    },
)

GetIdentityResolutionJobResponseTypeDef = TypedDict(
    "GetIdentityResolutionJobResponseTypeDef",
    {
        "DomainName": str,
        "JobId": str,
        "Status": IdentityResolutionJobStatusType,
        "Message": str,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "LastUpdatedAt": datetime,
        "JobExpirationTime": datetime,
        "AutoMerging": "AutoMergingTypeDef",
        "ExportingLocation": "ExportingLocationTypeDef",
        "JobStats": "JobStatsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)

GetIntegrationResponseTypeDef = TypedDict(
    "GetIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchesRequestRequestTypeDef = TypedDict(
    "GetMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetMatchesResponseTypeDef = TypedDict(
    "GetMatchesResponseTypeDef",
    {
        "NextToken": str,
        "MatchGenerationDate": datetime,
        "PotentialMatches": int,
        "Matches": List["MatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)

GetProfileObjectTypeResponseTypeDef = TypedDict(
    "GetProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileObjectTypeTemplateRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    {
        "TemplateId": str,
    },
)

GetProfileObjectTypeTemplateResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Status": StatusType,
        "ErrorDescription": str,
        "StartDate": datetime,
        "LastUpdatedAt": datetime,
        "Attributes": "WorkflowAttributesTypeDef",
        "Metrics": "WorkflowMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowStepsRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetWorkflowStepsResponseTypeDef = TypedDict(
    "GetWorkflowStepsResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Items": List["WorkflowStepItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityResolutionJobTypeDef = TypedDict(
    "IdentityResolutionJobTypeDef",
    {
        "DomainName": NotRequired[str],
        "JobId": NotRequired[str],
        "Status": NotRequired[IdentityResolutionJobStatusType],
        "JobStartTime": NotRequired[datetime],
        "JobEndTime": NotRequired[datetime],
        "JobStats": NotRequired["JobStatsTypeDef"],
        "ExportingLocation": NotRequired["ExportingLocationTypeDef"],
        "Message": NotRequired[str],
    },
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "DatetimeTypeFieldName": NotRequired[str],
    },
)

IntegrationConfigTypeDef = TypedDict(
    "IntegrationConfigTypeDef",
    {
        "AppflowIntegration": NotRequired["AppflowIntegrationTypeDef"],
    },
)

JobScheduleTypeDef = TypedDict(
    "JobScheduleTypeDef",
    {
        "DayOfTheWeek": JobScheduleDayOfTheWeekType,
        "Time": str,
    },
)

JobStatsTypeDef = TypedDict(
    "JobStatsTypeDef",
    {
        "NumberOfProfilesReviewed": NotRequired[int],
        "NumberOfMatchesFound": NotRequired[int],
        "NumberOfMergesDone": NotRequired[int],
    },
)

ListAccountIntegrationsRequestRequestTypeDef = TypedDict(
    "ListAccountIntegrationsRequestRequestTypeDef",
    {
        "Uri": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeHidden": NotRequired[bool],
    },
)

ListAccountIntegrationsResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainItemTypeDef = TypedDict(
    "ListDomainItemTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": NotRequired[Dict[str, str]],
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Items": List["ListDomainItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityResolutionJobsRequestRequestTypeDef = TypedDict(
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIdentityResolutionJobsResponseTypeDef = TypedDict(
    "ListIdentityResolutionJobsResponseTypeDef",
    {
        "IdentityResolutionJobsList": List["IdentityResolutionJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIntegrationItemTypeDef = TypedDict(
    "ListIntegrationItemTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ObjectTypeName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "ObjectTypeNames": NotRequired[Dict[str, str]],
        "WorkflowId": NotRequired[str],
    },
)

ListIntegrationsRequestRequestTypeDef = TypedDict(
    "ListIntegrationsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeHidden": NotRequired[bool],
    },
)

ListIntegrationsResponseTypeDef = TypedDict(
    "ListIntegrationsResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfileObjectTypeItemTypeDef = TypedDict(
    "ListProfileObjectTypeItemTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ListProfileObjectTypeTemplateItemTypeDef = TypedDict(
    "ListProfileObjectTypeTemplateItemTypeDef",
    {
        "TemplateId": NotRequired[str],
        "SourceName": NotRequired[str],
        "SourceObject": NotRequired[str],
    },
)

ListProfileObjectTypeTemplatesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProfileObjectTypeTemplatesResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeTemplateItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfileObjectTypesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProfileObjectTypesResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfileObjectsItemTypeDef = TypedDict(
    "ListProfileObjectsItemTypeDef",
    {
        "ObjectTypeName": NotRequired[str],
        "ProfileObjectUniqueKey": NotRequired[str],
        "Object": NotRequired[str],
    },
)

ListProfileObjectsRequestRequestTypeDef = TypedDict(
    "ListProfileObjectsRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "ProfileId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ObjectFilter": NotRequired["ObjectFilterTypeDef"],
    },
)

ListProfileObjectsResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseTypeDef",
    {
        "Items": List["ListProfileObjectsItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsItemTypeDef = TypedDict(
    "ListWorkflowsItemTypeDef",
    {
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "WorkflowId": str,
        "Status": StatusType,
        "StatusDescription": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": NotRequired[Literal["APPFLOW_INTEGRATION"]],
        "Status": NotRequired[StatusType],
        "QueryStartDate": NotRequired[Union[datetime, str]],
        "QueryEndDate": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Items": List["ListWorkflowsItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)

MatchItemTypeDef = TypedDict(
    "MatchItemTypeDef",
    {
        "MatchId": NotRequired[str],
        "ProfileIds": NotRequired[List[str]],
        "ConfidenceScore": NotRequired[float],
    },
)

MatchingRequestTypeDef = TypedDict(
    "MatchingRequestTypeDef",
    {
        "Enabled": bool,
        "JobSchedule": NotRequired["JobScheduleTypeDef"],
        "AutoMerging": NotRequired["AutoMergingTypeDef"],
        "ExportingConfig": NotRequired["ExportingConfigTypeDef"],
    },
)

MatchingResponseTypeDef = TypedDict(
    "MatchingResponseTypeDef",
    {
        "Enabled": NotRequired[bool],
        "JobSchedule": NotRequired["JobScheduleTypeDef"],
        "AutoMerging": NotRequired["AutoMergingTypeDef"],
        "ExportingConfig": NotRequired["ExportingConfigTypeDef"],
    },
)

MergeProfilesRequestRequestTypeDef = TypedDict(
    "MergeProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MainProfileId": str,
        "ProfileIdsToBeMerged": Sequence[str],
        "FieldSourceProfileIds": NotRequired["FieldSourceProfileIdsTypeDef"],
    },
)

MergeProfilesResponseTypeDef = TypedDict(
    "MergeProfilesResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectFilterTypeDef = TypedDict(
    "ObjectFilterTypeDef",
    {
        "KeyName": str,
        "Values": Sequence[str],
    },
)

ObjectTypeFieldTypeDef = TypedDict(
    "ObjectTypeFieldTypeDef",
    {
        "Source": NotRequired[str],
        "Target": NotRequired[str],
        "ContentType": NotRequired[FieldContentTypeType],
    },
)

ObjectTypeKeyTypeDef = TypedDict(
    "ObjectTypeKeyTypeDef",
    {
        "StandardIdentifiers": NotRequired[List[StandardIdentifierType]],
        "FieldNames": NotRequired[List[str]],
    },
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileId": NotRequired[str],
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired["AddressTypeDef"],
        "ShippingAddress": NotRequired["AddressTypeDef"],
        "MailingAddress": NotRequired["AddressTypeDef"],
        "BillingAddress": NotRequired["AddressTypeDef"],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

PutIntegrationRequestRequestTypeDef = TypedDict(
    "PutIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": NotRequired[str],
        "ObjectTypeName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "FlowDefinition": NotRequired["FlowDefinitionTypeDef"],
        "ObjectTypeNames": NotRequired[Mapping[str, str]],
    },
)

PutIntegrationResponseTypeDef = TypedDict(
    "PutIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProfileObjectRequestRequestTypeDef = TypedDict(
    "PutProfileObjectRequestRequestTypeDef",
    {
        "ObjectTypeName": str,
        "Object": str,
        "DomainName": str,
    },
)

PutProfileObjectResponseTypeDef = TypedDict(
    "PutProfileObjectResponseTypeDef",
    {
        "ProfileObjectUniqueKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "PutProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": NotRequired[str],
        "ExpirationDays": NotRequired[int],
        "EncryptionKey": NotRequired[str],
        "AllowProfileCreation": NotRequired[bool],
        "SourceLastUpdatedTimestampFormat": NotRequired[str],
        "Fields": NotRequired[Mapping[str, "ObjectTypeFieldTypeDef"]],
        "Keys": NotRequired[Mapping[str, Sequence["ObjectTypeKeyTypeDef"]]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

PutProfileObjectTypeResponseTypeDef = TypedDict(
    "PutProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

S3ExportingConfigTypeDef = TypedDict(
    "S3ExportingConfigTypeDef",
    {
        "S3BucketName": str,
        "S3KeyName": NotRequired[str],
    },
)

S3ExportingLocationTypeDef = TypedDict(
    "S3ExportingLocationTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "S3KeyName": NotRequired[str],
    },
)

S3SourcePropertiesTypeDef = TypedDict(
    "S3SourcePropertiesTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": NotRequired[str],
    },
)

SalesforceSourcePropertiesTypeDef = TypedDict(
    "SalesforceSourcePropertiesTypeDef",
    {
        "Object": str,
        "EnableDynamicFieldUpdate": NotRequired[bool],
        "IncludeDeletedRecords": NotRequired[bool],
    },
)

ScheduledTriggerPropertiesTypeDef = TypedDict(
    "ScheduledTriggerPropertiesTypeDef",
    {
        "ScheduleExpression": str,
        "DataPullMode": NotRequired[DataPullModeType],
        "ScheduleStartTime": NotRequired[Union[datetime, str]],
        "ScheduleEndTime": NotRequired[Union[datetime, str]],
        "Timezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "FirstExecutionFrom": NotRequired[Union[datetime, str]],
    },
)

SearchProfilesRequestRequestTypeDef = TypedDict(
    "SearchProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "KeyName": str,
        "Values": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Items": List["ProfileTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Marketo": NotRequired["MarketoSourcePropertiesTypeDef"],
        "S3": NotRequired["S3SourcePropertiesTypeDef"],
        "Salesforce": NotRequired["SalesforceSourcePropertiesTypeDef"],
        "ServiceNow": NotRequired["ServiceNowSourcePropertiesTypeDef"],
        "Zendesk": NotRequired["ZendeskSourcePropertiesTypeDef"],
    },
)

SourceFlowConfigTypeDef = TypedDict(
    "SourceFlowConfigTypeDef",
    {
        "ConnectorType": SourceConnectorTypeType,
        "SourceConnectorProperties": "SourceConnectorPropertiesTypeDef",
        "ConnectorProfileName": NotRequired[str],
        "IncrementalPullConfig": NotRequired["IncrementalPullConfigTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "SourceFields": Sequence[str],
        "TaskType": TaskTypeType,
        "ConnectorOperator": NotRequired["ConnectorOperatorTypeDef"],
        "DestinationField": NotRequired[str],
        "TaskProperties": NotRequired[Mapping[OperatorPropertiesKeysType, str]],
    },
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "TriggerType": TriggerTypeType,
        "TriggerProperties": NotRequired["TriggerPropertiesTypeDef"],
    },
)

TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": NotRequired["ScheduledTriggerPropertiesTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAddressTypeDef = TypedDict(
    "UpdateAddressTypeDef",
    {
        "Address1": NotRequired[str],
        "Address2": NotRequired[str],
        "Address3": NotRequired[str],
        "Address4": NotRequired[str],
        "City": NotRequired[str],
        "County": NotRequired[str],
        "State": NotRequired[str],
        "Province": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
    },
)

UpdateDomainRequestRequestTypeDef = TypedDict(
    "UpdateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": NotRequired[int],
        "DefaultEncryptionKey": NotRequired[str],
        "DeadLetterQueueUrl": NotRequired[str],
        "Matching": NotRequired["MatchingRequestTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "AdditionalInformation": NotRequired[str],
        "AccountNumber": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired["UpdateAddressTypeDef"],
        "ShippingAddress": NotRequired["UpdateAddressTypeDef"],
        "MailingAddress": NotRequired["UpdateAddressTypeDef"],
        "BillingAddress": NotRequired["UpdateAddressTypeDef"],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkflowAttributesTypeDef = TypedDict(
    "WorkflowAttributesTypeDef",
    {
        "AppflowIntegration": NotRequired["AppflowIntegrationWorkflowAttributesTypeDef"],
    },
)

WorkflowMetricsTypeDef = TypedDict(
    "WorkflowMetricsTypeDef",
    {
        "AppflowIntegration": NotRequired["AppflowIntegrationWorkflowMetricsTypeDef"],
    },
)

WorkflowStepItemTypeDef = TypedDict(
    "WorkflowStepItemTypeDef",
    {
        "AppflowIntegration": NotRequired["AppflowIntegrationWorkflowStepTypeDef"],
    },
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
