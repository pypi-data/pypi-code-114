"""
Type annotations for cloudsearch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import AccessPoliciesStatusTypeDef

    data: AccessPoliciesStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AlgorithmicStemmingType,
    AnalysisSchemeLanguageType,
    IndexFieldTypeType,
    OptionStateType,
    PartitionInstanceTypeType,
    SuggesterFuzzyMatchingType,
    TLSSecurityPolicyType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPoliciesStatusTypeDef",
    "AnalysisOptionsTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "AnalysisSchemeTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "BuildSuggestersRequestRequestTypeDef",
    "BuildSuggestersResponseTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "DefineAnalysisSchemeRequestRequestTypeDef",
    "DefineAnalysisSchemeResponseTypeDef",
    "DefineExpressionRequestRequestTypeDef",
    "DefineExpressionResponseTypeDef",
    "DefineIndexFieldRequestRequestTypeDef",
    "DefineIndexFieldResponseTypeDef",
    "DefineSuggesterRequestRequestTypeDef",
    "DefineSuggesterResponseTypeDef",
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    "DeleteAnalysisSchemeResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteExpressionRequestRequestTypeDef",
    "DeleteExpressionResponseTypeDef",
    "DeleteIndexFieldRequestRequestTypeDef",
    "DeleteIndexFieldResponseTypeDef",
    "DeleteSuggesterRequestRequestTypeDef",
    "DeleteSuggesterResponseTypeDef",
    "DescribeAnalysisSchemesRequestRequestTypeDef",
    "DescribeAnalysisSchemesResponseTypeDef",
    "DescribeAvailabilityOptionsRequestRequestTypeDef",
    "DescribeAvailabilityOptionsResponseTypeDef",
    "DescribeDomainEndpointOptionsRequestRequestTypeDef",
    "DescribeDomainEndpointOptionsResponseTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeExpressionsRequestRequestTypeDef",
    "DescribeExpressionsResponseTypeDef",
    "DescribeIndexFieldsRequestRequestTypeDef",
    "DescribeIndexFieldsResponseTypeDef",
    "DescribeScalingParametersRequestRequestTypeDef",
    "DescribeScalingParametersResponseTypeDef",
    "DescribeServiceAccessPoliciesRequestRequestTypeDef",
    "DescribeServiceAccessPoliciesResponseTypeDef",
    "DescribeSuggestersRequestRequestTypeDef",
    "DescribeSuggestersResponseTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainStatusTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionStatusTypeDef",
    "ExpressionTypeDef",
    "IndexDocumentsRequestRequestTypeDef",
    "IndexDocumentsResponseTypeDef",
    "IndexFieldStatusTypeDef",
    "IndexFieldTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseTypeDef",
    "LiteralArrayOptionsTypeDef",
    "LiteralOptionsTypeDef",
    "OptionStatusTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingParametersStatusTypeDef",
    "ScalingParametersTypeDef",
    "ServiceEndpointTypeDef",
    "SuggesterStatusTypeDef",
    "SuggesterTypeDef",
    "TextArrayOptionsTypeDef",
    "TextOptionsTypeDef",
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "UpdateScalingParametersRequestRequestTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

AnalysisOptionsTypeDef = TypedDict(
    "AnalysisOptionsTypeDef",
    {
        "Synonyms": NotRequired[str],
        "Stopwords": NotRequired[str],
        "StemmingDictionary": NotRequired[str],
        "JapaneseTokenizationDictionary": NotRequired[str],
        "AlgorithmicStemming": NotRequired[AlgorithmicStemmingType],
    },
)

AnalysisSchemeStatusTypeDef = TypedDict(
    "AnalysisSchemeStatusTypeDef",
    {
        "Options": "AnalysisSchemeTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

AnalysisSchemeTypeDef = TypedDict(
    "AnalysisSchemeTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": AnalysisSchemeLanguageType,
        "AnalysisOptions": NotRequired["AnalysisOptionsTypeDef"],
    },
)

AvailabilityOptionsStatusTypeDef = TypedDict(
    "AvailabilityOptionsStatusTypeDef",
    {
        "Options": bool,
        "Status": "OptionStatusTypeDef",
    },
)

BuildSuggestersRequestRequestTypeDef = TypedDict(
    "BuildSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

BuildSuggestersResponseTypeDef = TypedDict(
    "BuildSuggestersResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DateArrayOptionsTypeDef = TypedDict(
    "DateArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)

DateOptionsTypeDef = TypedDict(
    "DateOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)

DefineAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DefineAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisScheme": "AnalysisSchemeTypeDef",
    },
)

DefineAnalysisSchemeResponseTypeDef = TypedDict(
    "DefineAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": "AnalysisSchemeStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineExpressionRequestRequestTypeDef = TypedDict(
    "DefineExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "Expression": "ExpressionTypeDef",
    },
)

DefineExpressionResponseTypeDef = TypedDict(
    "DefineExpressionResponseTypeDef",
    {
        "Expression": "ExpressionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineIndexFieldRequestRequestTypeDef = TypedDict(
    "DefineIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexField": "IndexFieldTypeDef",
    },
)

DefineIndexFieldResponseTypeDef = TypedDict(
    "DefineIndexFieldResponseTypeDef",
    {
        "IndexField": "IndexFieldStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineSuggesterRequestRequestTypeDef = TypedDict(
    "DefineSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "Suggester": "SuggesterTypeDef",
    },
)

DefineSuggesterResponseTypeDef = TypedDict(
    "DefineSuggesterResponseTypeDef",
    {
        "Suggester": "SuggesterStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeName": str,
    },
)

DeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "DeleteAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": "AnalysisSchemeStatusTypeDef",
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
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExpressionRequestRequestTypeDef = TypedDict(
    "DeleteExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionName": str,
    },
)

DeleteExpressionResponseTypeDef = TypedDict(
    "DeleteExpressionResponseTypeDef",
    {
        "Expression": "ExpressionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIndexFieldRequestRequestTypeDef = TypedDict(
    "DeleteIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexFieldName": str,
    },
)

DeleteIndexFieldResponseTypeDef = TypedDict(
    "DeleteIndexFieldResponseTypeDef",
    {
        "IndexField": "IndexFieldStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuggesterRequestRequestTypeDef = TypedDict(
    "DeleteSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterName": str,
    },
)

DeleteSuggesterResponseTypeDef = TypedDict(
    "DeleteSuggesterResponseTypeDef",
    {
        "Suggester": "SuggesterStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisSchemesRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisSchemesRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)

DescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "DescribeAnalysisSchemesResponseTypeDef",
    {
        "AnalysisSchemes": List["AnalysisSchemeStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "DescribeAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "Deployed": NotRequired[bool],
    },
)

DescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "DescribeAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": "AvailabilityOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "Deployed": NotRequired[bool],
    },
)

DescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainsRequestRequestTypeDef = TypedDict(
    "DescribeDomainsRequestRequestTypeDef",
    {
        "DomainNames": NotRequired[Sequence[str]],
    },
)

DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef",
    {
        "DomainStatusList": List["DomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExpressionsRequestRequestTypeDef = TypedDict(
    "DescribeExpressionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)

DescribeExpressionsResponseTypeDef = TypedDict(
    "DescribeExpressionsResponseTypeDef",
    {
        "Expressions": List["ExpressionStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexFieldsRequestRequestTypeDef = TypedDict(
    "DescribeIndexFieldsRequestRequestTypeDef",
    {
        "DomainName": str,
        "FieldNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)

DescribeIndexFieldsResponseTypeDef = TypedDict(
    "DescribeIndexFieldsResponseTypeDef",
    {
        "IndexFields": List["IndexFieldStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingParametersRequestRequestTypeDef = TypedDict(
    "DescribeScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeScalingParametersResponseTypeDef = TypedDict(
    "DescribeScalingParametersResponseTypeDef",
    {
        "ScalingParameters": "ScalingParametersStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Deployed": NotRequired[bool],
    },
)

DescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSuggestersRequestRequestTypeDef = TypedDict(
    "DescribeSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)

DescribeSuggestersResponseTypeDef = TypedDict(
    "DescribeSuggestersResponseTypeDef",
    {
        "Suggesters": List["SuggesterStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentSuggesterOptionsTypeDef = TypedDict(
    "DocumentSuggesterOptionsTypeDef",
    {
        "SourceField": str,
        "FuzzyMatching": NotRequired[SuggesterFuzzyMatchingType],
        "SortExpression": NotRequired[str],
    },
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": "DomainEndpointOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": NotRequired[bool],
        "TLSSecurityPolicy": NotRequired[TLSSecurityPolicyType],
    },
)

DomainStatusTypeDef = TypedDict(
    "DomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "RequiresIndexDocuments": bool,
        "ARN": NotRequired[str],
        "Created": NotRequired[bool],
        "Deleted": NotRequired[bool],
        "DocService": NotRequired["ServiceEndpointTypeDef"],
        "SearchService": NotRequired["ServiceEndpointTypeDef"],
        "Processing": NotRequired[bool],
        "SearchInstanceType": NotRequired[str],
        "SearchPartitionCount": NotRequired[int],
        "SearchInstanceCount": NotRequired[int],
        "Limits": NotRequired["LimitsTypeDef"],
    },
)

DoubleArrayOptionsTypeDef = TypedDict(
    "DoubleArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[float],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)

DoubleOptionsTypeDef = TypedDict(
    "DoubleOptionsTypeDef",
    {
        "DefaultValue": NotRequired[float],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)

ExpressionStatusTypeDef = TypedDict(
    "ExpressionStatusTypeDef",
    {
        "Options": "ExpressionTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "ExpressionName": str,
        "ExpressionValue": str,
    },
)

IndexDocumentsRequestRequestTypeDef = TypedDict(
    "IndexDocumentsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

IndexDocumentsResponseTypeDef = TypedDict(
    "IndexDocumentsResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexFieldStatusTypeDef = TypedDict(
    "IndexFieldStatusTypeDef",
    {
        "Options": "IndexFieldTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

IndexFieldTypeDef = TypedDict(
    "IndexFieldTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": IndexFieldTypeType,
        "IntOptions": NotRequired["IntOptionsTypeDef"],
        "DoubleOptions": NotRequired["DoubleOptionsTypeDef"],
        "LiteralOptions": NotRequired["LiteralOptionsTypeDef"],
        "TextOptions": NotRequired["TextOptionsTypeDef"],
        "DateOptions": NotRequired["DateOptionsTypeDef"],
        "LatLonOptions": NotRequired["LatLonOptionsTypeDef"],
        "IntArrayOptions": NotRequired["IntArrayOptionsTypeDef"],
        "DoubleArrayOptions": NotRequired["DoubleArrayOptionsTypeDef"],
        "LiteralArrayOptions": NotRequired["LiteralArrayOptionsTypeDef"],
        "TextArrayOptions": NotRequired["TextArrayOptionsTypeDef"],
        "DateArrayOptions": NotRequired["DateArrayOptionsTypeDef"],
    },
)

IntArrayOptionsTypeDef = TypedDict(
    "IntArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[int],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)

IntOptionsTypeDef = TypedDict(
    "IntOptionsTypeDef",
    {
        "DefaultValue": NotRequired[int],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)

LatLonOptionsTypeDef = TypedDict(
    "LatLonOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "MaximumReplicationCount": int,
        "MaximumPartitionCount": int,
    },
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "DomainNames": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LiteralArrayOptionsTypeDef = TypedDict(
    "LiteralArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)

LiteralOptionsTypeDef = TypedDict(
    "LiteralOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)

OptionStatusTypeDef = TypedDict(
    "OptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
        "UpdateVersion": NotRequired[int],
        "PendingDeletion": NotRequired[bool],
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

ScalingParametersStatusTypeDef = TypedDict(
    "ScalingParametersStatusTypeDef",
    {
        "Options": "ScalingParametersTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ScalingParametersTypeDef = TypedDict(
    "ScalingParametersTypeDef",
    {
        "DesiredInstanceType": NotRequired[PartitionInstanceTypeType],
        "DesiredReplicationCount": NotRequired[int],
        "DesiredPartitionCount": NotRequired[int],
    },
)

ServiceEndpointTypeDef = TypedDict(
    "ServiceEndpointTypeDef",
    {
        "Endpoint": NotRequired[str],
    },
)

SuggesterStatusTypeDef = TypedDict(
    "SuggesterStatusTypeDef",
    {
        "Options": "SuggesterTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

SuggesterTypeDef = TypedDict(
    "SuggesterTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": "DocumentSuggesterOptionsTypeDef",
    },
)

TextArrayOptionsTypeDef = TypedDict(
    "TextArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceFields": NotRequired[str],
        "ReturnEnabled": NotRequired[bool],
        "HighlightEnabled": NotRequired[bool],
        "AnalysisScheme": NotRequired[str],
    },
)

TextOptionsTypeDef = TypedDict(
    "TextOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
        "HighlightEnabled": NotRequired[bool],
        "AnalysisScheme": NotRequired[str],
    },
)

UpdateAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "MultiAZ": bool,
    },
)

UpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "UpdateAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": "AvailabilityOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
    },
)

UpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScalingParametersRequestRequestTypeDef = TypedDict(
    "UpdateScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
        "ScalingParameters": "ScalingParametersTypeDef",
    },
)

UpdateScalingParametersResponseTypeDef = TypedDict(
    "UpdateScalingParametersResponseTypeDef",
    {
        "ScalingParameters": "ScalingParametersStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccessPolicies": str,
    },
)

UpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
