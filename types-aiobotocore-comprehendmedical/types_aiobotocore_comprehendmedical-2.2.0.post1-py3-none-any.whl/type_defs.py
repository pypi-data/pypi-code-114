"""
Type annotations for comprehendmedical service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_comprehendmedical/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_comprehendmedical.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Union

from typing_extensions import NotRequired

from .literals import (
    AttributeNameType,
    EntitySubTypeType,
    EntityTypeType,
    ICD10CMAttributeTypeType,
    ICD10CMEntityTypeType,
    ICD10CMRelationshipTypeType,
    ICD10CMTraitNameType,
    JobStatusType,
    RelationshipTypeType,
    RxNormAttributeTypeType,
    RxNormEntityTypeType,
    SNOMEDCTAttributeTypeType,
    SNOMEDCTEntityCategoryType,
    SNOMEDCTEntityTypeType,
    SNOMEDCTRelationshipTypeType,
    SNOMEDCTTraitNameType,
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
    "AttributeTypeDef",
    "CharactersTypeDef",
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "DescribeEntitiesDetectionV2JobRequestRequestTypeDef",
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobRequestRequestTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobRequestRequestTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobRequestRequestTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DescribeSNOMEDCTInferenceJobRequestRequestTypeDef",
    "DescribeSNOMEDCTInferenceJobResponseTypeDef",
    "DetectEntitiesRequestRequestTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2RequestRequestTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "DetectPHIRequestRequestTypeDef",
    "DetectPHIResponseTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InferICD10CMRequestRequestTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormRequestRequestTypeDef",
    "InferRxNormResponseTypeDef",
    "InferSNOMEDCTRequestRequestTypeDef",
    "InferSNOMEDCTResponseTypeDef",
    "InputDataConfigTypeDef",
    "ListEntitiesDetectionV2JobsRequestRequestTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsRequestRequestTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsRequestRequestTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsRequestRequestTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "ListSNOMEDCTInferenceJobsRequestRequestTypeDef",
    "ListSNOMEDCTInferenceJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "SNOMEDCTAttributeTypeDef",
    "SNOMEDCTConceptTypeDef",
    "SNOMEDCTDetailsTypeDef",
    "SNOMEDCTEntityTypeDef",
    "SNOMEDCTTraitTypeDef",
    "StartEntitiesDetectionV2JobRequestRequestTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobRequestRequestTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobRequestRequestTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobRequestRequestTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StartSNOMEDCTInferenceJobRequestRequestTypeDef",
    "StartSNOMEDCTInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobRequestRequestTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobRequestRequestTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobRequestRequestTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobRequestRequestTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
    "StopSNOMEDCTInferenceJobRequestRequestTypeDef",
    "StopSNOMEDCTInferenceJobResponseTypeDef",
    "TraitTypeDef",
    "UnmappedAttributeTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": NotRequired[EntitySubTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "RelationshipType": NotRequired[RelationshipTypeType],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[EntityTypeType],
        "Traits": NotRequired[List["TraitTypeDef"]],
    },
)

CharactersTypeDef = TypedDict(
    "CharactersTypeDef",
    {
        "OriginalTextCharacters": NotRequired[int],
    },
)

ComprehendMedicalAsyncJobFilterTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "LanguageCode": NotRequired[Literal["en"]],
        "DataAccessRoleArn": NotRequired[str],
        "ManifestFilePath": NotRequired[str],
        "KMSKey": NotRequired[str],
        "ModelVersion": NotRequired[str],
    },
)

DescribeEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeICD10CMInferenceJobResponseTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePHIDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribePHIDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePHIDetectionJobResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeRxNormInferenceJobResponseTypeDef = TypedDict(
    "DescribeRxNormInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSNOMEDCTInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeSNOMEDCTInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeSNOMEDCTInferenceJobResponseTypeDef = TypedDict(
    "DescribeSNOMEDCTInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesRequestRequestTypeDef = TypedDict(
    "DetectEntitiesRequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesV2RequestRequestTypeDef = TypedDict(
    "DetectEntitiesV2RequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectEntitiesV2ResponseTypeDef = TypedDict(
    "DetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectPHIRequestRequestTypeDef = TypedDict(
    "DetectPHIRequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectPHIResponseTypeDef = TypedDict(
    "DetectPHIResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Score": NotRequired[float],
        "Text": NotRequired[str],
        "Category": NotRequired[EntityTypeType],
        "Type": NotRequired[EntitySubTypeType],
        "Traits": NotRequired[List["TraitTypeDef"]],
        "Attributes": NotRequired[List["AttributeTypeDef"]],
    },
)

ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": NotRequired[ICD10CMAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List["ICD10CMTraitTypeDef"]],
        "Category": NotRequired[ICD10CMEntityTypeType],
        "RelationshipType": NotRequired[ICD10CMRelationshipTypeType],
    },
)

ICD10CMConceptTypeDef = TypedDict(
    "ICD10CMConceptTypeDef",
    {
        "Description": NotRequired[str],
        "Code": NotRequired[str],
        "Score": NotRequired[float],
    },
)

ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[Literal["MEDICAL_CONDITION"]],
        "Type": NotRequired[ICD10CMEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List["ICD10CMAttributeTypeDef"]],
        "Traits": NotRequired[List["ICD10CMTraitTypeDef"]],
        "ICD10CMConcepts": NotRequired[List["ICD10CMConceptTypeDef"]],
    },
)

ICD10CMTraitTypeDef = TypedDict(
    "ICD10CMTraitTypeDef",
    {
        "Name": NotRequired[ICD10CMTraitNameType],
        "Score": NotRequired[float],
    },
)

InferICD10CMRequestRequestTypeDef = TypedDict(
    "InferICD10CMRequestRequestTypeDef",
    {
        "Text": str,
    },
)

InferICD10CMResponseTypeDef = TypedDict(
    "InferICD10CMResponseTypeDef",
    {
        "Entities": List["ICD10CMEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InferRxNormRequestRequestTypeDef = TypedDict(
    "InferRxNormRequestRequestTypeDef",
    {
        "Text": str,
    },
)

InferRxNormResponseTypeDef = TypedDict(
    "InferRxNormResponseTypeDef",
    {
        "Entities": List["RxNormEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InferSNOMEDCTRequestRequestTypeDef = TypedDict(
    "InferSNOMEDCTRequestRequestTypeDef",
    {
        "Text": str,
    },
)

InferSNOMEDCTResponseTypeDef = TypedDict(
    "InferSNOMEDCTResponseTypeDef",
    {
        "Entities": List["SNOMEDCTEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "SNOMEDCTDetails": "SNOMEDCTDetailsTypeDef",
        "Characters": "CharactersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Bucket": str,
        "S3Key": NotRequired[str],
    },
)

ListEntitiesDetectionV2JobsRequestRequestTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["ComprehendMedicalAsyncJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListICD10CMInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListICD10CMInferenceJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["ComprehendMedicalAsyncJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListICD10CMInferenceJobsResponseTypeDef = TypedDict(
    "ListICD10CMInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPHIDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListPHIDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["ComprehendMedicalAsyncJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPHIDetectionJobsResponseTypeDef = TypedDict(
    "ListPHIDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRxNormInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListRxNormInferenceJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["ComprehendMedicalAsyncJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRxNormInferenceJobsResponseTypeDef = TypedDict(
    "ListRxNormInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSNOMEDCTInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListSNOMEDCTInferenceJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["ComprehendMedicalAsyncJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSNOMEDCTInferenceJobsResponseTypeDef = TypedDict(
    "ListSNOMEDCTInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Bucket": str,
        "S3Key": NotRequired[str],
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

RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": NotRequired[RxNormAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List["RxNormTraitTypeDef"]],
    },
)

RxNormConceptTypeDef = TypedDict(
    "RxNormConceptTypeDef",
    {
        "Description": NotRequired[str],
        "Code": NotRequired[str],
        "Score": NotRequired[float],
    },
)

RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[Literal["MEDICATION"]],
        "Type": NotRequired[RxNormEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List["RxNormAttributeTypeDef"]],
        "Traits": NotRequired[List["RxNormTraitTypeDef"]],
        "RxNormConcepts": NotRequired[List["RxNormConceptTypeDef"]],
    },
)

RxNormTraitTypeDef = TypedDict(
    "RxNormTraitTypeDef",
    {
        "Name": NotRequired[Literal["NEGATION"]],
        "Score": NotRequired[float],
    },
)

SNOMEDCTAttributeTypeDef = TypedDict(
    "SNOMEDCTAttributeTypeDef",
    {
        "Category": NotRequired[SNOMEDCTEntityCategoryType],
        "Type": NotRequired[SNOMEDCTAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "RelationshipType": NotRequired[SNOMEDCTRelationshipTypeType],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List["SNOMEDCTTraitTypeDef"]],
        "SNOMEDCTConcepts": NotRequired[List["SNOMEDCTConceptTypeDef"]],
    },
)

SNOMEDCTConceptTypeDef = TypedDict(
    "SNOMEDCTConceptTypeDef",
    {
        "Description": NotRequired[str],
        "Code": NotRequired[str],
        "Score": NotRequired[float],
    },
)

SNOMEDCTDetailsTypeDef = TypedDict(
    "SNOMEDCTDetailsTypeDef",
    {
        "Edition": NotRequired[str],
        "Language": NotRequired[str],
        "VersionDate": NotRequired[str],
    },
)

SNOMEDCTEntityTypeDef = TypedDict(
    "SNOMEDCTEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[SNOMEDCTEntityCategoryType],
        "Type": NotRequired[SNOMEDCTEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List["SNOMEDCTAttributeTypeDef"]],
        "Traits": NotRequired[List["SNOMEDCTTraitTypeDef"]],
        "SNOMEDCTConcepts": NotRequired[List["SNOMEDCTConceptTypeDef"]],
    },
)

SNOMEDCTTraitTypeDef = TypedDict(
    "SNOMEDCTTraitTypeDef",
    {
        "Name": NotRequired[SNOMEDCTTraitNameType],
        "Score": NotRequired[float],
    },
)

StartEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)

StartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "StartICD10CMInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)

StartICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StartICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "StartPHIDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)

StartPHIDetectionJobResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "StartRxNormInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)

StartRxNormInferenceJobResponseTypeDef = TypedDict(
    "StartRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSNOMEDCTInferenceJobRequestRequestTypeDef = TypedDict(
    "StartSNOMEDCTInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)

StartSNOMEDCTInferenceJobResponseTypeDef = TypedDict(
    "StartSNOMEDCTInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "StopICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StopICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "StopPHIDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopPHIDetectionJobResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "StopRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopRxNormInferenceJobResponseTypeDef = TypedDict(
    "StopRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSNOMEDCTInferenceJobRequestRequestTypeDef = TypedDict(
    "StopSNOMEDCTInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopSNOMEDCTInferenceJobResponseTypeDef = TypedDict(
    "StopSNOMEDCTInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TraitTypeDef = TypedDict(
    "TraitTypeDef",
    {
        "Name": NotRequired[AttributeNameType],
        "Score": NotRequired[float],
    },
)

UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": NotRequired[EntityTypeType],
        "Attribute": NotRequired["AttributeTypeDef"],
    },
)
