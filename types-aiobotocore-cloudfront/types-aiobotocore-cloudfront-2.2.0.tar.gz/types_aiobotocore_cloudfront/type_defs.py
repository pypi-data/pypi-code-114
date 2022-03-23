"""
Type annotations for cloudfront service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_cloudfront.type_defs import ActiveTrustedKeyGroupsTypeDef

    data: ActiveTrustedKeyGroupsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    CachePolicyCookieBehaviorType,
    CachePolicyHeaderBehaviorType,
    CachePolicyQueryStringBehaviorType,
    CachePolicyTypeType,
    CertificateSourceType,
    EventTypeType,
    FrameOptionsListType,
    FunctionStageType,
    GeoRestrictionTypeType,
    HttpVersionType,
    ICPRecordalStatusType,
    ItemSelectionType,
    MethodType,
    MinimumProtocolVersionType,
    OriginProtocolPolicyType,
    OriginRequestPolicyCookieBehaviorType,
    OriginRequestPolicyHeaderBehaviorType,
    OriginRequestPolicyQueryStringBehaviorType,
    OriginRequestPolicyTypeType,
    PriceClassType,
    RealtimeMetricsSubscriptionStatusType,
    ReferrerPolicyListType,
    ResponseHeadersPolicyAccessControlAllowMethodsValuesType,
    ResponseHeadersPolicyTypeType,
    SslProtocolType,
    SSLSupportMethodType,
    ViewerProtocolPolicyType,
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
    "ActiveTrustedKeyGroupsTypeDef",
    "ActiveTrustedSignersTypeDef",
    "AliasICPRecordalTypeDef",
    "AliasesTypeDef",
    "AllowedMethodsTypeDef",
    "AssociateAliasRequestRequestTypeDef",
    "CacheBehaviorTypeDef",
    "CacheBehaviorsTypeDef",
    "CachePolicyConfigTypeDef",
    "CachePolicyCookiesConfigTypeDef",
    "CachePolicyHeadersConfigTypeDef",
    "CachePolicyListTypeDef",
    "CachePolicyQueryStringsConfigTypeDef",
    "CachePolicySummaryTypeDef",
    "CachePolicyTypeDef",
    "CachedMethodsTypeDef",
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    "CloudFrontOriginAccessIdentityListTypeDef",
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    "CloudFrontOriginAccessIdentityTypeDef",
    "ConflictingAliasTypeDef",
    "ConflictingAliasesListTypeDef",
    "ContentTypeProfileConfigTypeDef",
    "ContentTypeProfileTypeDef",
    "ContentTypeProfilesTypeDef",
    "CookieNamesTypeDef",
    "CookiePreferenceTypeDef",
    "CreateCachePolicyRequestRequestTypeDef",
    "CreateCachePolicyResultTypeDef",
    "CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    "CreateDistributionRequestRequestTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDistributionWithTagsRequestRequestTypeDef",
    "CreateDistributionWithTagsResultTypeDef",
    "CreateFieldLevelEncryptionConfigRequestRequestTypeDef",
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    "CreateFieldLevelEncryptionProfileRequestRequestTypeDef",
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "CreateFunctionResultTypeDef",
    "CreateInvalidationRequestRequestTypeDef",
    "CreateInvalidationResultTypeDef",
    "CreateKeyGroupRequestRequestTypeDef",
    "CreateKeyGroupResultTypeDef",
    "CreateMonitoringSubscriptionRequestRequestTypeDef",
    "CreateMonitoringSubscriptionResultTypeDef",
    "CreateOriginRequestPolicyRequestRequestTypeDef",
    "CreateOriginRequestPolicyResultTypeDef",
    "CreatePublicKeyRequestRequestTypeDef",
    "CreatePublicKeyResultTypeDef",
    "CreateRealtimeLogConfigRequestRequestTypeDef",
    "CreateRealtimeLogConfigResultTypeDef",
    "CreateResponseHeadersPolicyRequestRequestTypeDef",
    "CreateResponseHeadersPolicyResultTypeDef",
    "CreateStreamingDistributionRequestRequestTypeDef",
    "CreateStreamingDistributionResultTypeDef",
    "CreateStreamingDistributionWithTagsRequestRequestTypeDef",
    "CreateStreamingDistributionWithTagsResultTypeDef",
    "CustomErrorResponseTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomHeadersTypeDef",
    "CustomOriginConfigTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "DeleteCachePolicyRequestRequestTypeDef",
    "DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "DeleteDistributionRequestRequestTypeDef",
    "DeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    "DeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteKeyGroupRequestRequestTypeDef",
    "DeleteMonitoringSubscriptionRequestRequestTypeDef",
    "DeleteOriginRequestPolicyRequestRequestTypeDef",
    "DeletePublicKeyRequestRequestTypeDef",
    "DeleteRealtimeLogConfigRequestRequestTypeDef",
    "DeleteResponseHeadersPolicyRequestRequestTypeDef",
    "DeleteStreamingDistributionRequestRequestTypeDef",
    "DescribeFunctionRequestRequestTypeDef",
    "DescribeFunctionResultTypeDef",
    "DistributionConfigTypeDef",
    "DistributionConfigWithTagsTypeDef",
    "DistributionIdListTypeDef",
    "DistributionListTypeDef",
    "DistributionSummaryTypeDef",
    "DistributionTypeDef",
    "EncryptionEntitiesTypeDef",
    "EncryptionEntityTypeDef",
    "EndPointTypeDef",
    "FieldLevelEncryptionConfigTypeDef",
    "FieldLevelEncryptionListTypeDef",
    "FieldLevelEncryptionProfileConfigTypeDef",
    "FieldLevelEncryptionProfileListTypeDef",
    "FieldLevelEncryptionProfileSummaryTypeDef",
    "FieldLevelEncryptionProfileTypeDef",
    "FieldLevelEncryptionSummaryTypeDef",
    "FieldLevelEncryptionTypeDef",
    "FieldPatternsTypeDef",
    "ForwardedValuesTypeDef",
    "FunctionAssociationTypeDef",
    "FunctionAssociationsTypeDef",
    "FunctionConfigTypeDef",
    "FunctionListTypeDef",
    "FunctionMetadataTypeDef",
    "FunctionSummaryTypeDef",
    "GeoRestrictionTypeDef",
    "GetCachePolicyConfigRequestRequestTypeDef",
    "GetCachePolicyConfigResultTypeDef",
    "GetCachePolicyRequestRequestTypeDef",
    "GetCachePolicyResultTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    "GetCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    "GetDistributionConfigRequestRequestTypeDef",
    "GetDistributionConfigResultTypeDef",
    "GetDistributionRequestRequestTypeDef",
    "GetDistributionResultTypeDef",
    "GetFieldLevelEncryptionConfigRequestRequestTypeDef",
    "GetFieldLevelEncryptionConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileRequestRequestTypeDef",
    "GetFieldLevelEncryptionProfileResultTypeDef",
    "GetFieldLevelEncryptionRequestRequestTypeDef",
    "GetFieldLevelEncryptionResultTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResultTypeDef",
    "GetInvalidationRequestRequestTypeDef",
    "GetInvalidationResultTypeDef",
    "GetKeyGroupConfigRequestRequestTypeDef",
    "GetKeyGroupConfigResultTypeDef",
    "GetKeyGroupRequestRequestTypeDef",
    "GetKeyGroupResultTypeDef",
    "GetMonitoringSubscriptionRequestRequestTypeDef",
    "GetMonitoringSubscriptionResultTypeDef",
    "GetOriginRequestPolicyConfigRequestRequestTypeDef",
    "GetOriginRequestPolicyConfigResultTypeDef",
    "GetOriginRequestPolicyRequestRequestTypeDef",
    "GetOriginRequestPolicyResultTypeDef",
    "GetPublicKeyConfigRequestRequestTypeDef",
    "GetPublicKeyConfigResultTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GetPublicKeyResultTypeDef",
    "GetRealtimeLogConfigRequestRequestTypeDef",
    "GetRealtimeLogConfigResultTypeDef",
    "GetResponseHeadersPolicyConfigRequestRequestTypeDef",
    "GetResponseHeadersPolicyConfigResultTypeDef",
    "GetResponseHeadersPolicyRequestRequestTypeDef",
    "GetResponseHeadersPolicyResultTypeDef",
    "GetStreamingDistributionConfigRequestRequestTypeDef",
    "GetStreamingDistributionConfigResultTypeDef",
    "GetStreamingDistributionRequestRequestTypeDef",
    "GetStreamingDistributionResultTypeDef",
    "HeadersTypeDef",
    "InvalidationBatchTypeDef",
    "InvalidationListTypeDef",
    "InvalidationSummaryTypeDef",
    "InvalidationTypeDef",
    "KGKeyPairIdsTypeDef",
    "KeyGroupConfigTypeDef",
    "KeyGroupListTypeDef",
    "KeyGroupSummaryTypeDef",
    "KeyGroupTypeDef",
    "KeyPairIdsTypeDef",
    "KinesisStreamConfigTypeDef",
    "LambdaFunctionAssociationTypeDef",
    "LambdaFunctionAssociationsTypeDef",
    "ListCachePoliciesRequestRequestTypeDef",
    "ListCachePoliciesResultTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    "ListConflictingAliasesRequestRequestTypeDef",
    "ListConflictingAliasesResultTypeDef",
    "ListDistributionsByCachePolicyIdRequestRequestTypeDef",
    "ListDistributionsByCachePolicyIdResultTypeDef",
    "ListDistributionsByKeyGroupRequestRequestTypeDef",
    "ListDistributionsByKeyGroupResultTypeDef",
    "ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    "ListDistributionsByRealtimeLogConfigRequestRequestTypeDef",
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    "ListDistributionsByWebACLIdRequestRequestTypeDef",
    "ListDistributionsByWebACLIdResultTypeDef",
    "ListDistributionsRequestRequestTypeDef",
    "ListDistributionsResultTypeDef",
    "ListFieldLevelEncryptionConfigsRequestRequestTypeDef",
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    "ListFieldLevelEncryptionProfilesRequestRequestTypeDef",
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListFunctionsResultTypeDef",
    "ListInvalidationsRequestRequestTypeDef",
    "ListInvalidationsResultTypeDef",
    "ListKeyGroupsRequestRequestTypeDef",
    "ListKeyGroupsResultTypeDef",
    "ListOriginRequestPoliciesRequestRequestTypeDef",
    "ListOriginRequestPoliciesResultTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListPublicKeysResultTypeDef",
    "ListRealtimeLogConfigsRequestRequestTypeDef",
    "ListRealtimeLogConfigsResultTypeDef",
    "ListResponseHeadersPoliciesRequestRequestTypeDef",
    "ListResponseHeadersPoliciesResultTypeDef",
    "ListStreamingDistributionsRequestRequestTypeDef",
    "ListStreamingDistributionsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LoggingConfigTypeDef",
    "MonitoringSubscriptionTypeDef",
    "OriginCustomHeaderTypeDef",
    "OriginGroupFailoverCriteriaTypeDef",
    "OriginGroupMemberTypeDef",
    "OriginGroupMembersTypeDef",
    "OriginGroupTypeDef",
    "OriginGroupsTypeDef",
    "OriginRequestPolicyConfigTypeDef",
    "OriginRequestPolicyCookiesConfigTypeDef",
    "OriginRequestPolicyHeadersConfigTypeDef",
    "OriginRequestPolicyListTypeDef",
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    "OriginRequestPolicySummaryTypeDef",
    "OriginRequestPolicyTypeDef",
    "OriginShieldTypeDef",
    "OriginSslProtocolsTypeDef",
    "OriginTypeDef",
    "OriginsTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    "PathsTypeDef",
    "PublicKeyConfigTypeDef",
    "PublicKeyListTypeDef",
    "PublicKeySummaryTypeDef",
    "PublicKeyTypeDef",
    "PublishFunctionRequestRequestTypeDef",
    "PublishFunctionResultTypeDef",
    "QueryArgProfileConfigTypeDef",
    "QueryArgProfileTypeDef",
    "QueryArgProfilesTypeDef",
    "QueryStringCacheKeysTypeDef",
    "QueryStringNamesTypeDef",
    "RealtimeLogConfigTypeDef",
    "RealtimeLogConfigsTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    "ResponseHeadersPolicyConfigTypeDef",
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    "ResponseHeadersPolicyCorsConfigTypeDef",
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    "ResponseHeadersPolicyCustomHeadersConfigTypeDef",
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    "ResponseHeadersPolicyListTypeDef",
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    "ResponseHeadersPolicyStrictTransportSecurityTypeDef",
    "ResponseHeadersPolicySummaryTypeDef",
    "ResponseHeadersPolicyTypeDef",
    "ResponseHeadersPolicyXSSProtectionTypeDef",
    "ResponseMetadataTypeDef",
    "RestrictionsTypeDef",
    "S3OriginConfigTypeDef",
    "S3OriginTypeDef",
    "SignerTypeDef",
    "StatusCodesTypeDef",
    "StreamingDistributionConfigTypeDef",
    "StreamingDistributionConfigWithTagsTypeDef",
    "StreamingDistributionListTypeDef",
    "StreamingDistributionSummaryTypeDef",
    "StreamingDistributionTypeDef",
    "StreamingLoggingConfigTypeDef",
    "TagKeysTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TagsTypeDef",
    "TestFunctionRequestRequestTypeDef",
    "TestFunctionResultTypeDef",
    "TestResultTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedSignersTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCachePolicyRequestRequestTypeDef",
    "UpdateCachePolicyResultTypeDef",
    "UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    "UpdateDistributionRequestRequestTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    "UpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "UpdateFunctionResultTypeDef",
    "UpdateKeyGroupRequestRequestTypeDef",
    "UpdateKeyGroupResultTypeDef",
    "UpdateOriginRequestPolicyRequestRequestTypeDef",
    "UpdateOriginRequestPolicyResultTypeDef",
    "UpdatePublicKeyRequestRequestTypeDef",
    "UpdatePublicKeyResultTypeDef",
    "UpdateRealtimeLogConfigRequestRequestTypeDef",
    "UpdateRealtimeLogConfigResultTypeDef",
    "UpdateResponseHeadersPolicyRequestRequestTypeDef",
    "UpdateResponseHeadersPolicyResultTypeDef",
    "UpdateStreamingDistributionRequestRequestTypeDef",
    "UpdateStreamingDistributionResultTypeDef",
    "ViewerCertificateTypeDef",
    "WaiterConfigTypeDef",
)

ActiveTrustedKeyGroupsTypeDef = TypedDict(
    "ActiveTrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[List["KGKeyPairIdsTypeDef"]],
    },
)

ActiveTrustedSignersTypeDef = TypedDict(
    "ActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[List["SignerTypeDef"]],
    },
)

AliasICPRecordalTypeDef = TypedDict(
    "AliasICPRecordalTypeDef",
    {
        "CNAME": NotRequired[str],
        "ICPRecordalStatus": NotRequired[ICPRecordalStatusType],
    },
)

AliasesTypeDef = TypedDict(
    "AliasesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

AllowedMethodsTypeDef = TypedDict(
    "AllowedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[MethodType],
        "CachedMethods": NotRequired["CachedMethodsTypeDef"],
    },
)

AssociateAliasRequestRequestTypeDef = TypedDict(
    "AssociateAliasRequestRequestTypeDef",
    {
        "TargetDistributionId": str,
        "Alias": str,
    },
)

CacheBehaviorTypeDef = TypedDict(
    "CacheBehaviorTypeDef",
    {
        "PathPattern": str,
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
        "TrustedSigners": NotRequired["TrustedSignersTypeDef"],
        "TrustedKeyGroups": NotRequired["TrustedKeyGroupsTypeDef"],
        "AllowedMethods": NotRequired["AllowedMethodsTypeDef"],
        "SmoothStreaming": NotRequired[bool],
        "Compress": NotRequired[bool],
        "LambdaFunctionAssociations": NotRequired["LambdaFunctionAssociationsTypeDef"],
        "FunctionAssociations": NotRequired["FunctionAssociationsTypeDef"],
        "FieldLevelEncryptionId": NotRequired[str],
        "RealtimeLogConfigArn": NotRequired[str],
        "CachePolicyId": NotRequired[str],
        "OriginRequestPolicyId": NotRequired[str],
        "ResponseHeadersPolicyId": NotRequired[str],
        "ForwardedValues": NotRequired["ForwardedValuesTypeDef"],
        "MinTTL": NotRequired[int],
        "DefaultTTL": NotRequired[int],
        "MaxTTL": NotRequired[int],
    },
)

CacheBehaviorsTypeDef = TypedDict(
    "CacheBehaviorsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["CacheBehaviorTypeDef"]],
    },
)

CachePolicyConfigTypeDef = TypedDict(
    "CachePolicyConfigTypeDef",
    {
        "Name": str,
        "MinTTL": int,
        "Comment": NotRequired[str],
        "DefaultTTL": NotRequired[int],
        "MaxTTL": NotRequired[int],
        "ParametersInCacheKeyAndForwardedToOrigin": NotRequired[
            "ParametersInCacheKeyAndForwardedToOriginTypeDef"
        ],
    },
)

CachePolicyCookiesConfigTypeDef = TypedDict(
    "CachePolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": CachePolicyCookieBehaviorType,
        "Cookies": NotRequired["CookieNamesTypeDef"],
    },
)

CachePolicyHeadersConfigTypeDef = TypedDict(
    "CachePolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": CachePolicyHeaderBehaviorType,
        "Headers": NotRequired["HeadersTypeDef"],
    },
)

CachePolicyListTypeDef = TypedDict(
    "CachePolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["CachePolicySummaryTypeDef"]],
    },
)

CachePolicyQueryStringsConfigTypeDef = TypedDict(
    "CachePolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": CachePolicyQueryStringBehaviorType,
        "QueryStrings": NotRequired["QueryStringNamesTypeDef"],
    },
)

CachePolicySummaryTypeDef = TypedDict(
    "CachePolicySummaryTypeDef",
    {
        "Type": CachePolicyTypeType,
        "CachePolicy": "CachePolicyTypeDef",
    },
)

CachePolicyTypeDef = TypedDict(
    "CachePolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
    },
)

CachedMethodsTypeDef = TypedDict(
    "CachedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[MethodType],
    },
)

CloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
    },
)

CloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["CloudFrontOriginAccessIdentitySummaryTypeDef"]],
    },
)

CloudFrontOriginAccessIdentitySummaryTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "Comment": str,
    },
)

CloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "CloudFrontOriginAccessIdentityConfig": NotRequired[
            "CloudFrontOriginAccessIdentityConfigTypeDef"
        ],
    },
)

ConflictingAliasTypeDef = TypedDict(
    "ConflictingAliasTypeDef",
    {
        "Alias": NotRequired[str],
        "DistributionId": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)

ConflictingAliasesListTypeDef = TypedDict(
    "ConflictingAliasesListTypeDef",
    {
        "NextMarker": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Quantity": NotRequired[int],
        "Items": NotRequired[List["ConflictingAliasTypeDef"]],
    },
)

ContentTypeProfileConfigTypeDef = TypedDict(
    "ContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": NotRequired["ContentTypeProfilesTypeDef"],
    },
)

ContentTypeProfileTypeDef = TypedDict(
    "ContentTypeProfileTypeDef",
    {
        "Format": Literal["URLEncoded"],
        "ContentType": str,
        "ProfileId": NotRequired[str],
    },
)

ContentTypeProfilesTypeDef = TypedDict(
    "ContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["ContentTypeProfileTypeDef"]],
    },
)

CookieNamesTypeDef = TypedDict(
    "CookieNamesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

CookiePreferenceTypeDef = TypedDict(
    "CookiePreferenceTypeDef",
    {
        "Forward": ItemSelectionType,
        "WhitelistedNames": NotRequired["CookieNamesTypeDef"],
    },
)

CreateCachePolicyRequestRequestTypeDef = TypedDict(
    "CreateCachePolicyRequestRequestTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
    },
)

CreateCachePolicyResultTypeDef = TypedDict(
    "CreateCachePolicyResultTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
    },
)

CreateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionRequestRequestTypeDef = TypedDict(
    "CreateDistributionRequestRequestTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
    },
)

CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionWithTagsRequestRequestTypeDef = TypedDict(
    "CreateDistributionWithTagsRequestRequestTypeDef",
    {
        "DistributionConfigWithTags": "DistributionConfigWithTagsTypeDef",
    },
)

CreateDistributionWithTagsResultTypeDef = TypedDict(
    "CreateDistributionWithTagsResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
    },
)

CreateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
    },
)

CreateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionRequestRequestTypeDef = TypedDict(
    "CreateFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "FunctionConfig": "FunctionConfigTypeDef",
        "FunctionCode": Union[bytes, IO[bytes], StreamingBody],
    },
)

CreateFunctionResultTypeDef = TypedDict(
    "CreateFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInvalidationRequestRequestTypeDef = TypedDict(
    "CreateInvalidationRequestRequestTypeDef",
    {
        "DistributionId": str,
        "InvalidationBatch": "InvalidationBatchTypeDef",
    },
)

CreateInvalidationResultTypeDef = TypedDict(
    "CreateInvalidationResultTypeDef",
    {
        "Location": str,
        "Invalidation": "InvalidationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyGroupRequestRequestTypeDef = TypedDict(
    "CreateKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
    },
)

CreateKeyGroupResultTypeDef = TypedDict(
    "CreateKeyGroupResultTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
    },
)

CreateMonitoringSubscriptionResultTypeDef = TypedDict(
    "CreateMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "CreateOriginRequestPolicyRequestRequestTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
    },
)

CreateOriginRequestPolicyResultTypeDef = TypedDict(
    "CreateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublicKeyRequestRequestTypeDef = TypedDict(
    "CreatePublicKeyRequestRequestTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
    },
)

CreatePublicKeyResultTypeDef = TypedDict(
    "CreatePublicKeyResultTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "CreateRealtimeLogConfigRequestRequestTypeDef",
    {
        "EndPoints": Sequence["EndPointTypeDef"],
        "Fields": Sequence[str],
        "Name": str,
        "SamplingRate": int,
    },
)

CreateRealtimeLogConfigResultTypeDef = TypedDict(
    "CreateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "CreateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyConfig": "ResponseHeadersPolicyConfigTypeDef",
    },
)

CreateResponseHeadersPolicyResultTypeDef = TypedDict(
    "CreateResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": "ResponseHeadersPolicyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "CreateStreamingDistributionRequestRequestTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
    },
)

CreateStreamingDistributionResultTypeDef = TypedDict(
    "CreateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionWithTagsRequestRequestTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsRequestRequestTypeDef",
    {
        "StreamingDistributionConfigWithTags": "StreamingDistributionConfigWithTagsTypeDef",
    },
)

CreateStreamingDistributionWithTagsResultTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomErrorResponseTypeDef = TypedDict(
    "CustomErrorResponseTypeDef",
    {
        "ErrorCode": int,
        "ResponsePagePath": NotRequired[str],
        "ResponseCode": NotRequired[str],
        "ErrorCachingMinTTL": NotRequired[int],
    },
)

CustomErrorResponsesTypeDef = TypedDict(
    "CustomErrorResponsesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["CustomErrorResponseTypeDef"]],
    },
)

CustomHeadersTypeDef = TypedDict(
    "CustomHeadersTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["OriginCustomHeaderTypeDef"]],
    },
)

CustomOriginConfigTypeDef = TypedDict(
    "CustomOriginConfigTypeDef",
    {
        "HTTPPort": int,
        "HTTPSPort": int,
        "OriginProtocolPolicy": OriginProtocolPolicyType,
        "OriginSslProtocols": NotRequired["OriginSslProtocolsTypeDef"],
        "OriginReadTimeout": NotRequired[int],
        "OriginKeepaliveTimeout": NotRequired[int],
    },
)

DefaultCacheBehaviorTypeDef = TypedDict(
    "DefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
        "TrustedSigners": NotRequired["TrustedSignersTypeDef"],
        "TrustedKeyGroups": NotRequired["TrustedKeyGroupsTypeDef"],
        "AllowedMethods": NotRequired["AllowedMethodsTypeDef"],
        "SmoothStreaming": NotRequired[bool],
        "Compress": NotRequired[bool],
        "LambdaFunctionAssociations": NotRequired["LambdaFunctionAssociationsTypeDef"],
        "FunctionAssociations": NotRequired["FunctionAssociationsTypeDef"],
        "FieldLevelEncryptionId": NotRequired[str],
        "RealtimeLogConfigArn": NotRequired[str],
        "CachePolicyId": NotRequired[str],
        "OriginRequestPolicyId": NotRequired[str],
        "ResponseHeadersPolicyId": NotRequired[str],
        "ForwardedValues": NotRequired["ForwardedValuesTypeDef"],
        "MinTTL": NotRequired[int],
        "DefaultTTL": NotRequired[int],
        "MaxTTL": NotRequired[int],
    },
)

DeleteCachePolicyRequestRequestTypeDef = TypedDict(
    "DeleteCachePolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteDistributionRequestRequestTypeDef = TypedDict(
    "DeleteDistributionRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "DeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "DeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)

DeleteKeyGroupRequestRequestTypeDef = TypedDict(
    "DeleteKeyGroupRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)

DeleteOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "DeleteOriginRequestPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeletePublicKeyRequestRequestTypeDef = TypedDict(
    "DeletePublicKeyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "DeleteRealtimeLogConfigRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

DeleteResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "DeleteResponseHeadersPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DeleteStreamingDistributionRequestRequestTypeDef = TypedDict(
    "DeleteStreamingDistributionRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

DescribeFunctionRequestRequestTypeDef = TypedDict(
    "DescribeFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "Stage": NotRequired[FunctionStageType],
    },
)

DescribeFunctionResultTypeDef = TypedDict(
    "DescribeFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DistributionConfigTypeDef = TypedDict(
    "DistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": "OriginsTypeDef",
        "DefaultCacheBehavior": "DefaultCacheBehaviorTypeDef",
        "Comment": str,
        "Enabled": bool,
        "Aliases": NotRequired["AliasesTypeDef"],
        "DefaultRootObject": NotRequired[str],
        "OriginGroups": NotRequired["OriginGroupsTypeDef"],
        "CacheBehaviors": NotRequired["CacheBehaviorsTypeDef"],
        "CustomErrorResponses": NotRequired["CustomErrorResponsesTypeDef"],
        "Logging": NotRequired["LoggingConfigTypeDef"],
        "PriceClass": NotRequired[PriceClassType],
        "ViewerCertificate": NotRequired["ViewerCertificateTypeDef"],
        "Restrictions": NotRequired["RestrictionsTypeDef"],
        "WebACLId": NotRequired[str],
        "HttpVersion": NotRequired[HttpVersionType],
        "IsIPV6Enabled": NotRequired[bool],
    },
)

DistributionConfigWithTagsTypeDef = TypedDict(
    "DistributionConfigWithTagsTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "Tags": "TagsTypeDef",
    },
)

DistributionIdListTypeDef = TypedDict(
    "DistributionIdListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[str]],
    },
)

DistributionListTypeDef = TypedDict(
    "DistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["DistributionSummaryTypeDef"]],
    },
)

DistributionSummaryTypeDef = TypedDict(
    "DistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "Aliases": "AliasesTypeDef",
        "Origins": "OriginsTypeDef",
        "DefaultCacheBehavior": "DefaultCacheBehaviorTypeDef",
        "CacheBehaviors": "CacheBehaviorsTypeDef",
        "CustomErrorResponses": "CustomErrorResponsesTypeDef",
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
        "ViewerCertificate": "ViewerCertificateTypeDef",
        "Restrictions": "RestrictionsTypeDef",
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
        "OriginGroups": NotRequired["OriginGroupsTypeDef"],
        "AliasICPRecordals": NotRequired[List["AliasICPRecordalTypeDef"]],
    },
)

DistributionTypeDef = TypedDict(
    "DistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "InProgressInvalidationBatches": int,
        "DomainName": str,
        "DistributionConfig": "DistributionConfigTypeDef",
        "ActiveTrustedSigners": NotRequired["ActiveTrustedSignersTypeDef"],
        "ActiveTrustedKeyGroups": NotRequired["ActiveTrustedKeyGroupsTypeDef"],
        "AliasICPRecordals": NotRequired[List["AliasICPRecordalTypeDef"]],
    },
)

EncryptionEntitiesTypeDef = TypedDict(
    "EncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["EncryptionEntityTypeDef"]],
    },
)

EncryptionEntityTypeDef = TypedDict(
    "EncryptionEntityTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": "FieldPatternsTypeDef",
    },
)

EndPointTypeDef = TypedDict(
    "EndPointTypeDef",
    {
        "StreamType": str,
        "KinesisStreamConfig": NotRequired["KinesisStreamConfigTypeDef"],
    },
)

FieldLevelEncryptionConfigTypeDef = TypedDict(
    "FieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": NotRequired[str],
        "QueryArgProfileConfig": NotRequired["QueryArgProfileConfigTypeDef"],
        "ContentTypeProfileConfig": NotRequired["ContentTypeProfileConfigTypeDef"],
    },
)

FieldLevelEncryptionListTypeDef = TypedDict(
    "FieldLevelEncryptionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["FieldLevelEncryptionSummaryTypeDef"]],
    },
)

FieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "FieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": "EncryptionEntitiesTypeDef",
        "Comment": NotRequired[str],
    },
)

FieldLevelEncryptionProfileListTypeDef = TypedDict(
    "FieldLevelEncryptionProfileListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["FieldLevelEncryptionProfileSummaryTypeDef"]],
    },
)

FieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "FieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "EncryptionEntities": "EncryptionEntitiesTypeDef",
        "Comment": NotRequired[str],
    },
)

FieldLevelEncryptionProfileTypeDef = TypedDict(
    "FieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
    },
)

FieldLevelEncryptionSummaryTypeDef = TypedDict(
    "FieldLevelEncryptionSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Comment": NotRequired[str],
        "QueryArgProfileConfig": NotRequired["QueryArgProfileConfigTypeDef"],
        "ContentTypeProfileConfig": NotRequired["ContentTypeProfileConfigTypeDef"],
    },
)

FieldLevelEncryptionTypeDef = TypedDict(
    "FieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
    },
)

FieldPatternsTypeDef = TypedDict(
    "FieldPatternsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

ForwardedValuesTypeDef = TypedDict(
    "ForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": "CookiePreferenceTypeDef",
        "Headers": NotRequired["HeadersTypeDef"],
        "QueryStringCacheKeys": NotRequired["QueryStringCacheKeysTypeDef"],
    },
)

FunctionAssociationTypeDef = TypedDict(
    "FunctionAssociationTypeDef",
    {
        "FunctionARN": str,
        "EventType": EventTypeType,
    },
)

FunctionAssociationsTypeDef = TypedDict(
    "FunctionAssociationsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["FunctionAssociationTypeDef"]],
    },
)

FunctionConfigTypeDef = TypedDict(
    "FunctionConfigTypeDef",
    {
        "Comment": str,
        "Runtime": Literal["cloudfront-js-1.0"],
    },
)

FunctionListTypeDef = TypedDict(
    "FunctionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["FunctionSummaryTypeDef"]],
    },
)

FunctionMetadataTypeDef = TypedDict(
    "FunctionMetadataTypeDef",
    {
        "FunctionARN": str,
        "LastModifiedTime": datetime,
        "Stage": NotRequired[FunctionStageType],
        "CreatedTime": NotRequired[datetime],
    },
)

FunctionSummaryTypeDef = TypedDict(
    "FunctionSummaryTypeDef",
    {
        "Name": str,
        "FunctionConfig": "FunctionConfigTypeDef",
        "FunctionMetadata": "FunctionMetadataTypeDef",
        "Status": NotRequired[str],
    },
)

GeoRestrictionTypeDef = TypedDict(
    "GeoRestrictionTypeDef",
    {
        "RestrictionType": GeoRestrictionTypeType,
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

GetCachePolicyConfigRequestRequestTypeDef = TypedDict(
    "GetCachePolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCachePolicyConfigResultTypeDef = TypedDict(
    "GetCachePolicyConfigResultTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCachePolicyRequestRequestTypeDef = TypedDict(
    "GetCachePolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCachePolicyResultTypeDef = TypedDict(
    "GetCachePolicyResultTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCloudFrontOriginAccessIdentityConfigResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionConfigRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetDistributionConfigResultTypeDef = TypedDict(
    "GetDistributionConfigResultTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionRequestRequestTypeDef = TypedDict(
    "GetDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetDistributionResultTypeDef = TypedDict(
    "GetDistributionResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionProfileConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionResultTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionRequestRequestTypeDef = TypedDict(
    "GetFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "Stage": NotRequired[FunctionStageType],
    },
)

GetFunctionResultTypeDef = TypedDict(
    "GetFunctionResultTypeDef",
    {
        "FunctionCode": StreamingBody,
        "ETag": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvalidationRequestRequestTypeDef = TypedDict(
    "GetInvalidationRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Id": str,
    },
)

GetInvalidationResultTypeDef = TypedDict(
    "GetInvalidationResultTypeDef",
    {
        "Invalidation": "InvalidationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyGroupConfigRequestRequestTypeDef = TypedDict(
    "GetKeyGroupConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetKeyGroupConfigResultTypeDef = TypedDict(
    "GetKeyGroupConfigResultTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyGroupRequestRequestTypeDef = TypedDict(
    "GetKeyGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetKeyGroupResultTypeDef = TypedDict(
    "GetKeyGroupResultTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "GetMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)

GetMonitoringSubscriptionResultTypeDef = TypedDict(
    "GetMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginRequestPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetOriginRequestPolicyConfigResultTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigResultTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetOriginRequestPolicyResultTypeDef = TypedDict(
    "GetOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyConfigRequestRequestTypeDef = TypedDict(
    "GetPublicKeyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetPublicKeyConfigResultTypeDef = TypedDict(
    "GetPublicKeyConfigResultTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetPublicKeyResultTypeDef = TypedDict(
    "GetPublicKeyResultTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "GetRealtimeLogConfigRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

GetRealtimeLogConfigResultTypeDef = TypedDict(
    "GetRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponseHeadersPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetResponseHeadersPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetResponseHeadersPolicyConfigResultTypeDef = TypedDict(
    "GetResponseHeadersPolicyConfigResultTypeDef",
    {
        "ResponseHeadersPolicyConfig": "ResponseHeadersPolicyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "GetResponseHeadersPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetResponseHeadersPolicyResultTypeDef = TypedDict(
    "GetResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": "ResponseHeadersPolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingDistributionConfigRequestRequestTypeDef = TypedDict(
    "GetStreamingDistributionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetStreamingDistributionConfigResultTypeDef = TypedDict(
    "GetStreamingDistributionConfigResultTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingDistributionRequestRequestTypeDef = TypedDict(
    "GetStreamingDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetStreamingDistributionResultTypeDef = TypedDict(
    "GetStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HeadersTypeDef = TypedDict(
    "HeadersTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

InvalidationBatchTypeDef = TypedDict(
    "InvalidationBatchTypeDef",
    {
        "Paths": "PathsTypeDef",
        "CallerReference": str,
    },
)

InvalidationListTypeDef = TypedDict(
    "InvalidationListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["InvalidationSummaryTypeDef"]],
    },
)

InvalidationSummaryTypeDef = TypedDict(
    "InvalidationSummaryTypeDef",
    {
        "Id": str,
        "CreateTime": datetime,
        "Status": str,
    },
)

InvalidationTypeDef = TypedDict(
    "InvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": "InvalidationBatchTypeDef",
    },
)

KGKeyPairIdsTypeDef = TypedDict(
    "KGKeyPairIdsTypeDef",
    {
        "KeyGroupId": NotRequired[str],
        "KeyPairIds": NotRequired["KeyPairIdsTypeDef"],
    },
)

KeyGroupConfigTypeDef = TypedDict(
    "KeyGroupConfigTypeDef",
    {
        "Name": str,
        "Items": Sequence[str],
        "Comment": NotRequired[str],
    },
)

KeyGroupListTypeDef = TypedDict(
    "KeyGroupListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["KeyGroupSummaryTypeDef"]],
    },
)

KeyGroupSummaryTypeDef = TypedDict(
    "KeyGroupSummaryTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
    },
)

KeyGroupTypeDef = TypedDict(
    "KeyGroupTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
    },
)

KeyPairIdsTypeDef = TypedDict(
    "KeyPairIdsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "RoleARN": str,
        "StreamARN": str,
    },
)

LambdaFunctionAssociationTypeDef = TypedDict(
    "LambdaFunctionAssociationTypeDef",
    {
        "LambdaFunctionARN": str,
        "EventType": EventTypeType,
        "IncludeBody": NotRequired[bool],
    },
)

LambdaFunctionAssociationsTypeDef = TypedDict(
    "LambdaFunctionAssociationsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["LambdaFunctionAssociationTypeDef"]],
    },
)

ListCachePoliciesRequestRequestTypeDef = TypedDict(
    "ListCachePoliciesRequestRequestTypeDef",
    {
        "Type": NotRequired[CachePolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListCachePoliciesResultTypeDef = TypedDict(
    "ListCachePoliciesResultTypeDef",
    {
        "CachePolicyList": "CachePolicyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListCloudFrontOriginAccessIdentitiesResultTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": "CloudFrontOriginAccessIdentityListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConflictingAliasesRequestRequestTypeDef = TypedDict(
    "ListConflictingAliasesRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Alias": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListConflictingAliasesResultTypeDef = TypedDict(
    "ListConflictingAliasesResultTypeDef",
    {
        "ConflictingAliasesList": "ConflictingAliasesListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByCachePolicyIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdRequestRequestTypeDef",
    {
        "CachePolicyId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListDistributionsByCachePolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByKeyGroupRequestRequestTypeDef = TypedDict(
    "ListDistributionsByKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListDistributionsByKeyGroupResultTypeDef = TypedDict(
    "ListDistributionsByKeyGroupResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    {
        "OriginRequestPolicyId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListDistributionsByOriginRequestPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "RealtimeLogConfigName": NotRequired[str],
        "RealtimeLogConfigArn": NotRequired[str],
    },
)

ListDistributionsByRealtimeLogConfigResultTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListDistributionsByResponseHeadersPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByWebACLIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByWebACLIdRequestRequestTypeDef",
    {
        "WebACLId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListDistributionsByWebACLIdResultTypeDef = TypedDict(
    "ListDistributionsByWebACLIdResultTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsRequestRequestTypeDef = TypedDict(
    "ListDistributionsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListDistributionsResultTypeDef = TypedDict(
    "ListDistributionsResultTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFieldLevelEncryptionConfigsRequestRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListFieldLevelEncryptionConfigsResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    {
        "FieldLevelEncryptionList": "FieldLevelEncryptionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFieldLevelEncryptionProfilesRequestRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListFieldLevelEncryptionProfilesResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    {
        "FieldLevelEncryptionProfileList": "FieldLevelEncryptionProfileListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsRequestRequestTypeDef = TypedDict(
    "ListFunctionsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "Stage": NotRequired[FunctionStageType],
    },
)

ListFunctionsResultTypeDef = TypedDict(
    "ListFunctionsResultTypeDef",
    {
        "FunctionList": "FunctionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvalidationsRequestRequestTypeDef = TypedDict(
    "ListInvalidationsRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListInvalidationsResultTypeDef = TypedDict(
    "ListInvalidationsResultTypeDef",
    {
        "InvalidationList": "InvalidationListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyGroupsRequestRequestTypeDef = TypedDict(
    "ListKeyGroupsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListKeyGroupsResultTypeDef = TypedDict(
    "ListKeyGroupsResultTypeDef",
    {
        "KeyGroupList": "KeyGroupListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginRequestPoliciesRequestRequestTypeDef = TypedDict(
    "ListOriginRequestPoliciesRequestRequestTypeDef",
    {
        "Type": NotRequired[OriginRequestPolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListOriginRequestPoliciesResultTypeDef = TypedDict(
    "ListOriginRequestPoliciesResultTypeDef",
    {
        "OriginRequestPolicyList": "OriginRequestPolicyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListPublicKeysResultTypeDef = TypedDict(
    "ListPublicKeysResultTypeDef",
    {
        "PublicKeyList": "PublicKeyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRealtimeLogConfigsRequestRequestTypeDef = TypedDict(
    "ListRealtimeLogConfigsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[str],
        "Marker": NotRequired[str],
    },
)

ListRealtimeLogConfigsResultTypeDef = TypedDict(
    "ListRealtimeLogConfigsResultTypeDef",
    {
        "RealtimeLogConfigs": "RealtimeLogConfigsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResponseHeadersPoliciesRequestRequestTypeDef = TypedDict(
    "ListResponseHeadersPoliciesRequestRequestTypeDef",
    {
        "Type": NotRequired[ResponseHeadersPolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListResponseHeadersPoliciesResultTypeDef = TypedDict(
    "ListResponseHeadersPoliciesResultTypeDef",
    {
        "ResponseHeadersPolicyList": "ResponseHeadersPolicyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamingDistributionsRequestRequestTypeDef = TypedDict(
    "ListStreamingDistributionsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListStreamingDistributionsResultTypeDef = TypedDict(
    "ListStreamingDistributionsResultTypeDef",
    {
        "StreamingDistributionList": "StreamingDistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": "TagsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "Enabled": bool,
        "IncludeCookies": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

MonitoringSubscriptionTypeDef = TypedDict(
    "MonitoringSubscriptionTypeDef",
    {
        "RealtimeMetricsSubscriptionConfig": NotRequired[
            "RealtimeMetricsSubscriptionConfigTypeDef"
        ],
    },
)

OriginCustomHeaderTypeDef = TypedDict(
    "OriginCustomHeaderTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

OriginGroupFailoverCriteriaTypeDef = TypedDict(
    "OriginGroupFailoverCriteriaTypeDef",
    {
        "StatusCodes": "StatusCodesTypeDef",
    },
)

OriginGroupMemberTypeDef = TypedDict(
    "OriginGroupMemberTypeDef",
    {
        "OriginId": str,
    },
)

OriginGroupMembersTypeDef = TypedDict(
    "OriginGroupMembersTypeDef",
    {
        "Quantity": int,
        "Items": Sequence["OriginGroupMemberTypeDef"],
    },
)

OriginGroupTypeDef = TypedDict(
    "OriginGroupTypeDef",
    {
        "Id": str,
        "FailoverCriteria": "OriginGroupFailoverCriteriaTypeDef",
        "Members": "OriginGroupMembersTypeDef",
    },
)

OriginGroupsTypeDef = TypedDict(
    "OriginGroupsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["OriginGroupTypeDef"]],
    },
)

OriginRequestPolicyConfigTypeDef = TypedDict(
    "OriginRequestPolicyConfigTypeDef",
    {
        "Name": str,
        "HeadersConfig": "OriginRequestPolicyHeadersConfigTypeDef",
        "CookiesConfig": "OriginRequestPolicyCookiesConfigTypeDef",
        "QueryStringsConfig": "OriginRequestPolicyQueryStringsConfigTypeDef",
        "Comment": NotRequired[str],
    },
)

OriginRequestPolicyCookiesConfigTypeDef = TypedDict(
    "OriginRequestPolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": OriginRequestPolicyCookieBehaviorType,
        "Cookies": NotRequired["CookieNamesTypeDef"],
    },
)

OriginRequestPolicyHeadersConfigTypeDef = TypedDict(
    "OriginRequestPolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": OriginRequestPolicyHeaderBehaviorType,
        "Headers": NotRequired["HeadersTypeDef"],
    },
)

OriginRequestPolicyListTypeDef = TypedDict(
    "OriginRequestPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["OriginRequestPolicySummaryTypeDef"]],
    },
)

OriginRequestPolicyQueryStringsConfigTypeDef = TypedDict(
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": OriginRequestPolicyQueryStringBehaviorType,
        "QueryStrings": NotRequired["QueryStringNamesTypeDef"],
    },
)

OriginRequestPolicySummaryTypeDef = TypedDict(
    "OriginRequestPolicySummaryTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
    },
)

OriginRequestPolicyTypeDef = TypedDict(
    "OriginRequestPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
    },
)

OriginShieldTypeDef = TypedDict(
    "OriginShieldTypeDef",
    {
        "Enabled": bool,
        "OriginShieldRegion": NotRequired[str],
    },
)

OriginSslProtocolsTypeDef = TypedDict(
    "OriginSslProtocolsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[SslProtocolType],
    },
)

OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "Id": str,
        "DomainName": str,
        "OriginPath": NotRequired[str],
        "CustomHeaders": NotRequired["CustomHeadersTypeDef"],
        "S3OriginConfig": NotRequired["S3OriginConfigTypeDef"],
        "CustomOriginConfig": NotRequired["CustomOriginConfigTypeDef"],
        "ConnectionAttempts": NotRequired[int],
        "ConnectionTimeout": NotRequired[int],
        "OriginShield": NotRequired["OriginShieldTypeDef"],
    },
)

OriginsTypeDef = TypedDict(
    "OriginsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence["OriginTypeDef"],
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

ParametersInCacheKeyAndForwardedToOriginTypeDef = TypedDict(
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    {
        "EnableAcceptEncodingGzip": bool,
        "HeadersConfig": "CachePolicyHeadersConfigTypeDef",
        "CookiesConfig": "CachePolicyCookiesConfigTypeDef",
        "QueryStringsConfig": "CachePolicyQueryStringsConfigTypeDef",
        "EnableAcceptEncodingBrotli": NotRequired[bool],
    },
)

PathsTypeDef = TypedDict(
    "PathsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

PublicKeyConfigTypeDef = TypedDict(
    "PublicKeyConfigTypeDef",
    {
        "CallerReference": str,
        "Name": str,
        "EncodedKey": str,
        "Comment": NotRequired[str],
    },
)

PublicKeyListTypeDef = TypedDict(
    "PublicKeyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["PublicKeySummaryTypeDef"]],
    },
)

PublicKeySummaryTypeDef = TypedDict(
    "PublicKeySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatedTime": datetime,
        "EncodedKey": str,
        "Comment": NotRequired[str],
    },
)

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
    },
)

PublishFunctionRequestRequestTypeDef = TypedDict(
    "PublishFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)

PublishFunctionResultTypeDef = TypedDict(
    "PublishFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryArgProfileConfigTypeDef = TypedDict(
    "QueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": NotRequired["QueryArgProfilesTypeDef"],
    },
)

QueryArgProfileTypeDef = TypedDict(
    "QueryArgProfileTypeDef",
    {
        "QueryArg": str,
        "ProfileId": str,
    },
)

QueryArgProfilesTypeDef = TypedDict(
    "QueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["QueryArgProfileTypeDef"]],
    },
)

QueryStringCacheKeysTypeDef = TypedDict(
    "QueryStringCacheKeysTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

QueryStringNamesTypeDef = TypedDict(
    "QueryStringNamesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

RealtimeLogConfigTypeDef = TypedDict(
    "RealtimeLogConfigTypeDef",
    {
        "ARN": str,
        "Name": str,
        "SamplingRate": int,
        "EndPoints": List["EndPointTypeDef"],
        "Fields": List[str],
    },
)

RealtimeLogConfigsTypeDef = TypedDict(
    "RealtimeLogConfigsTypeDef",
    {
        "MaxItems": int,
        "IsTruncated": bool,
        "Marker": str,
        "Items": NotRequired[List["RealtimeLogConfigTypeDef"]],
        "NextMarker": NotRequired[str],
    },
)

RealtimeMetricsSubscriptionConfigTypeDef = TypedDict(
    "RealtimeMetricsSubscriptionConfigTypeDef",
    {
        "RealtimeMetricsSubscriptionStatus": RealtimeMetricsSubscriptionStatusType,
    },
)

ResponseHeadersPolicyAccessControlAllowHeadersTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[str],
    },
)

ResponseHeadersPolicyAccessControlAllowMethodsTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[ResponseHeadersPolicyAccessControlAllowMethodsValuesType],
    },
)

ResponseHeadersPolicyAccessControlAllowOriginsTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[str],
    },
)

ResponseHeadersPolicyAccessControlExposeHeadersTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

ResponseHeadersPolicyConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyConfigTypeDef",
    {
        "Name": str,
        "Comment": NotRequired[str],
        "CorsConfig": NotRequired["ResponseHeadersPolicyCorsConfigTypeDef"],
        "SecurityHeadersConfig": NotRequired["ResponseHeadersPolicySecurityHeadersConfigTypeDef"],
        "CustomHeadersConfig": NotRequired["ResponseHeadersPolicyCustomHeadersConfigTypeDef"],
    },
)

ResponseHeadersPolicyContentSecurityPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    {
        "Override": bool,
        "ContentSecurityPolicy": str,
    },
)

ResponseHeadersPolicyContentTypeOptionsTypeDef = TypedDict(
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    {
        "Override": bool,
    },
)

ResponseHeadersPolicyCorsConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyCorsConfigTypeDef",
    {
        "AccessControlAllowOrigins": "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
        "AccessControlAllowHeaders": "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
        "AccessControlAllowMethods": "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
        "AccessControlAllowCredentials": bool,
        "OriginOverride": bool,
        "AccessControlExposeHeaders": NotRequired[
            "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef"
        ],
        "AccessControlMaxAgeSec": NotRequired[int],
    },
)

ResponseHeadersPolicyCustomHeaderTypeDef = TypedDict(
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    {
        "Header": str,
        "Value": str,
        "Override": bool,
    },
)

ResponseHeadersPolicyCustomHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyCustomHeadersConfigTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence["ResponseHeadersPolicyCustomHeaderTypeDef"]],
    },
)

ResponseHeadersPolicyFrameOptionsTypeDef = TypedDict(
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    {
        "Override": bool,
        "FrameOption": FrameOptionsListType,
    },
)

ResponseHeadersPolicyListTypeDef = TypedDict(
    "ResponseHeadersPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["ResponseHeadersPolicySummaryTypeDef"]],
    },
)

ResponseHeadersPolicyReferrerPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    {
        "Override": bool,
        "ReferrerPolicy": ReferrerPolicyListType,
    },
)

ResponseHeadersPolicySecurityHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    {
        "XSSProtection": NotRequired["ResponseHeadersPolicyXSSProtectionTypeDef"],
        "FrameOptions": NotRequired["ResponseHeadersPolicyFrameOptionsTypeDef"],
        "ReferrerPolicy": NotRequired["ResponseHeadersPolicyReferrerPolicyTypeDef"],
        "ContentSecurityPolicy": NotRequired["ResponseHeadersPolicyContentSecurityPolicyTypeDef"],
        "ContentTypeOptions": NotRequired["ResponseHeadersPolicyContentTypeOptionsTypeDef"],
        "StrictTransportSecurity": NotRequired[
            "ResponseHeadersPolicyStrictTransportSecurityTypeDef"
        ],
    },
)

ResponseHeadersPolicyStrictTransportSecurityTypeDef = TypedDict(
    "ResponseHeadersPolicyStrictTransportSecurityTypeDef",
    {
        "Override": bool,
        "AccessControlMaxAgeSec": int,
        "IncludeSubdomains": NotRequired[bool],
        "Preload": NotRequired[bool],
    },
)

ResponseHeadersPolicySummaryTypeDef = TypedDict(
    "ResponseHeadersPolicySummaryTypeDef",
    {
        "Type": ResponseHeadersPolicyTypeType,
        "ResponseHeadersPolicy": "ResponseHeadersPolicyTypeDef",
    },
)

ResponseHeadersPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "ResponseHeadersPolicyConfig": "ResponseHeadersPolicyConfigTypeDef",
    },
)

ResponseHeadersPolicyXSSProtectionTypeDef = TypedDict(
    "ResponseHeadersPolicyXSSProtectionTypeDef",
    {
        "Override": bool,
        "Protection": bool,
        "ModeBlock": NotRequired[bool],
        "ReportUri": NotRequired[str],
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

RestrictionsTypeDef = TypedDict(
    "RestrictionsTypeDef",
    {
        "GeoRestriction": "GeoRestrictionTypeDef",
    },
)

S3OriginConfigTypeDef = TypedDict(
    "S3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": str,
    },
)

S3OriginTypeDef = TypedDict(
    "S3OriginTypeDef",
    {
        "DomainName": str,
        "OriginAccessIdentity": str,
    },
)

SignerTypeDef = TypedDict(
    "SignerTypeDef",
    {
        "AwsAccountNumber": NotRequired[str],
        "KeyPairIds": NotRequired["KeyPairIdsTypeDef"],
    },
)

StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[int],
    },
)

StreamingDistributionConfigTypeDef = TypedDict(
    "StreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": "S3OriginTypeDef",
        "Comment": str,
        "TrustedSigners": "TrustedSignersTypeDef",
        "Enabled": bool,
        "Aliases": NotRequired["AliasesTypeDef"],
        "Logging": NotRequired["StreamingLoggingConfigTypeDef"],
        "PriceClass": NotRequired[PriceClassType],
    },
)

StreamingDistributionConfigWithTagsTypeDef = TypedDict(
    "StreamingDistributionConfigWithTagsTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "Tags": "TagsTypeDef",
    },
)

StreamingDistributionListTypeDef = TypedDict(
    "StreamingDistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List["StreamingDistributionSummaryTypeDef"]],
    },
)

StreamingDistributionSummaryTypeDef = TypedDict(
    "StreamingDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": "S3OriginTypeDef",
        "Aliases": "AliasesTypeDef",
        "TrustedSigners": "TrustedSignersTypeDef",
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
    },
)

StreamingDistributionTypeDef = TypedDict(
    "StreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "DomainName": str,
        "ActiveTrustedSigners": "ActiveTrustedSignersTypeDef",
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "LastModifiedTime": NotRequired[datetime],
    },
)

StreamingLoggingConfigTypeDef = TypedDict(
    "StreamingLoggingConfigTypeDef",
    {
        "Enabled": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

TagKeysTypeDef = TypedDict(
    "TagKeysTypeDef",
    {
        "Items": NotRequired[Sequence[str]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "Tags": "TagsTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

TagsTypeDef = TypedDict(
    "TagsTypeDef",
    {
        "Items": NotRequired[Sequence["TagTypeDef"]],
    },
)

TestFunctionRequestRequestTypeDef = TypedDict(
    "TestFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "EventObject": Union[bytes, IO[bytes], StreamingBody],
        "Stage": NotRequired[FunctionStageType],
    },
)

TestFunctionResultTypeDef = TypedDict(
    "TestFunctionResultTypeDef",
    {
        "TestResult": "TestResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "FunctionSummary": NotRequired["FunctionSummaryTypeDef"],
        "ComputeUtilization": NotRequired[str],
        "FunctionExecutionLogs": NotRequired[List[str]],
        "FunctionErrorMessage": NotRequired[str],
        "FunctionOutput": NotRequired[str],
    },
)

TrustedKeyGroupsTypeDef = TypedDict(
    "TrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

TrustedSignersTypeDef = TypedDict(
    "TrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": "TagKeysTypeDef",
    },
)

UpdateCachePolicyRequestRequestTypeDef = TypedDict(
    "UpdateCachePolicyRequestRequestTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateCachePolicyResultTypeDef = TypedDict(
    "UpdateCachePolicyResultTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionRequestRequestTypeDef = TypedDict(
    "UpdateDistributionRequestRequestTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFunctionRequestRequestTypeDef = TypedDict(
    "UpdateFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "FunctionConfig": "FunctionConfigTypeDef",
        "FunctionCode": Union[bytes, IO[bytes], StreamingBody],
    },
)

UpdateFunctionResultTypeDef = TypedDict(
    "UpdateFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateKeyGroupRequestRequestTypeDef = TypedDict(
    "UpdateKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateKeyGroupResultTypeDef = TypedDict(
    "UpdateKeyGroupResultTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "UpdateOriginRequestPolicyRequestRequestTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateOriginRequestPolicyResultTypeDef = TypedDict(
    "UpdateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePublicKeyRequestRequestTypeDef = TypedDict(
    "UpdatePublicKeyRequestRequestTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdatePublicKeyResultTypeDef = TypedDict(
    "UpdatePublicKeyResultTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "UpdateRealtimeLogConfigRequestRequestTypeDef",
    {
        "EndPoints": NotRequired[Sequence["EndPointTypeDef"]],
        "Fields": NotRequired[Sequence[str]],
        "Name": NotRequired[str],
        "ARN": NotRequired[str],
        "SamplingRate": NotRequired[int],
    },
)

UpdateRealtimeLogConfigResultTypeDef = TypedDict(
    "UpdateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "UpdateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyConfig": "ResponseHeadersPolicyConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateResponseHeadersPolicyResultTypeDef = TypedDict(
    "UpdateResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": "ResponseHeadersPolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "UpdateStreamingDistributionRequestRequestTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)

UpdateStreamingDistributionResultTypeDef = TypedDict(
    "UpdateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ViewerCertificateTypeDef = TypedDict(
    "ViewerCertificateTypeDef",
    {
        "CloudFrontDefaultCertificate": NotRequired[bool],
        "IAMCertificateId": NotRequired[str],
        "ACMCertificateArn": NotRequired[str],
        "SSLSupportMethod": NotRequired[SSLSupportMethodType],
        "MinimumProtocolVersion": NotRequired[MinimumProtocolVersionType],
        "Certificate": NotRequired[str],
        "CertificateSource": NotRequired[CertificateSourceType],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
