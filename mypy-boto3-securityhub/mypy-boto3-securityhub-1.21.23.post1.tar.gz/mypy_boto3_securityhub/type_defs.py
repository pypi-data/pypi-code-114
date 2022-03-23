"""
Type annotations for securityhub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdminStatusType,
    AwsIamAccessKeyStatusType,
    AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
    ComplianceStatusType,
    ControlStatusType,
    IntegrationTypeType,
    MalwareStateType,
    MalwareTypeType,
    MapFilterComparisonType,
    NetworkDirectionType,
    PartitionType,
    RecordStateType,
    SeverityLabelType,
    SeverityRatingType,
    SortOrderType,
    StandardsStatusType,
    StatusReasonCodeType,
    StringFilterComparisonType,
    ThreatIntelIndicatorCategoryType,
    ThreatIntelIndicatorTypeType,
    VerificationStateType,
    WorkflowStateType,
    WorkflowStatusType,
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
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "AdjustmentTypeDef",
    "AdminAccountTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiCallActionTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    "AwsEc2VpnConnectionDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsEcrRepositoryDetailsTypeDef",
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    "AwsEcsClusterConfigurationDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsClusterDetailsTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    "AwsEcsServiceDetailsTypeDef",
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    "AwsEcsTaskDefinitionDetailsTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    "AwsEksClusterDetailsTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    "AwsEksClusterLoggingDetailsTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbv2LoadBalancerAttributeTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRdsEventSubscriptionDetailsTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "AwsS3BucketLoggingConfigurationTypeDef",
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    "AwsS3BucketNotificationConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "AwsSecurityFindingTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsSsmComplianceSummaryTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsWafRateBasedRuleDetailsTypeDef",
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "AwsXrayEncryptionConfigDetailsTypeDef",
    "BatchDisableStandardsRequestRequestTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsRequestRequestTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "BatchImportFindingsRequestRequestTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateFindingsRequestRequestTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "BooleanFilterTypeDef",
    "CellTypeDef",
    "CidrBlockAssociationTypeDef",
    "CityTypeDef",
    "ClassificationResultTypeDef",
    "ClassificationStatusTypeDef",
    "ComplianceTypeDef",
    "ContainerDetailsTypeDef",
    "CountryTypeDef",
    "CreateActionTargetRequestRequestTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateFindingAggregatorRequestRequestTypeDef",
    "CreateFindingAggregatorResponseTypeDef",
    "CreateInsightRequestRequestTypeDef",
    "CreateInsightResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "CvssTypeDef",
    "DataClassificationDetailsTypeDef",
    "DateFilterTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteActionTargetRequestRequestTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteFindingAggregatorRequestRequestTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "DeleteInsightResponseTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeActionTargetsRequestRequestTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribeProductsRequestRequestTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsRequestRequestTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "DescribeStandardsRequestRequestTypeDef",
    "DescribeStandardsResponseTypeDef",
    "DisableImportFindingsForProductRequestRequestTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "DnsRequestActionTypeDef",
    "EnableImportFindingsForProductRequestRequestTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EnableSecurityHubRequestRequestTypeDef",
    "FindingAggregatorTypeDef",
    "FindingProviderFieldsTypeDef",
    "FindingProviderSeverityTypeDef",
    "FirewallPolicyDetailsTypeDef",
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetEnabledStandardsRequestRequestTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "GetFindingAggregatorRequestRequestTypeDef",
    "GetFindingAggregatorResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInsightResultsRequestRequestTypeDef",
    "GetInsightResultsResponseTypeDef",
    "GetInsightsRequestRequestTypeDef",
    "GetInsightsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "IcmpTypeCodeTypeDef",
    "ImportFindingsErrorTypeDef",
    "InsightResultValueTypeDef",
    "InsightResultsTypeDef",
    "InsightTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "InviteMembersResponseTypeDef",
    "IpFilterTypeDef",
    "IpOrganizationDetailsTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "KeywordFilterTypeDef",
    "ListEnabledProductsForImportRequestRequestTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListFindingAggregatorsRequestRequestTypeDef",
    "ListFindingAggregatorsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoadBalancerStateTypeDef",
    "MalwareTypeDef",
    "MapFilterTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkHeaderTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkPathComponentTypeDef",
    "NetworkTypeDef",
    "NoteTypeDef",
    "NoteUpdateTypeDef",
    "NumberFilterTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PatchSummaryTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PortRangeFromToTypeDef",
    "PortRangeTypeDef",
    "ProcessDetailsTypeDef",
    "ProductTypeDef",
    "RangeTypeDef",
    "RecommendationTypeDef",
    "RecordTypeDef",
    "RelatedFindingTypeDef",
    "RemediationTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ResultTypeDef",
    "RuleGroupDetailsTypeDef",
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    "RuleGroupSourceListDetailsTypeDef",
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    "RuleGroupSourceTypeDef",
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    "RuleGroupVariablesTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "SensitiveDataResultTypeDef",
    "SeverityTypeDef",
    "SeverityUpdateTypeDef",
    "SoftwarePackageTypeDef",
    "SortCriterionTypeDef",
    "StandardTypeDef",
    "StandardsControlTypeDef",
    "StandardsStatusReasonTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatelessCustomActionDefinitionTypeDef",
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    "StatelessCustomPublishMetricActionTypeDef",
    "StatusReasonTypeDef",
    "StringFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateActionTargetRequestRequestTypeDef",
    "UpdateFindingAggregatorRequestRequestTypeDef",
    "UpdateFindingAggregatorResponseTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "UpdateInsightRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    "UpdateStandardsControlRequestRequestTypeDef",
    "VulnerabilityTypeDef",
    "VulnerabilityVendorTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "WorkflowTypeDef",
    "WorkflowUpdateTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "AdministratorId": str,
        "InvitationId": str,
    },
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "MasterId": str,
        "InvitationId": str,
    },
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "AccountId": str,
        "Email": NotRequired[str],
    },
)

ActionLocalIpDetailsTypeDef = TypedDict(
    "ActionLocalIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
    },
)

ActionLocalPortDetailsTypeDef = TypedDict(
    "ActionLocalPortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)

ActionRemoteIpDetailsTypeDef = TypedDict(
    "ActionRemoteIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
        "Organization": NotRequired["IpOrganizationDetailsTypeDef"],
        "Country": NotRequired["CountryTypeDef"],
        "City": NotRequired["CityTypeDef"],
        "GeoLocation": NotRequired["GeoLocationTypeDef"],
    },
)

ActionRemotePortDetailsTypeDef = TypedDict(
    "ActionRemotePortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ActionTargetArn": str,
        "Name": str,
        "Description": str,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": NotRequired[str],
        "NetworkConnectionAction": NotRequired["NetworkConnectionActionTypeDef"],
        "AwsApiCallAction": NotRequired["AwsApiCallActionTypeDef"],
        "DnsRequestAction": NotRequired["DnsRequestActionTypeDef"],
        "PortProbeAction": NotRequired["PortProbeActionTypeDef"],
    },
)

AdjustmentTypeDef = TypedDict(
    "AdjustmentTypeDef",
    {
        "Metric": NotRequired[str],
        "Reason": NotRequired[str],
    },
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AccountId": NotRequired[str],
        "Status": NotRequired[AdminStatusType],
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)

AwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "AwsApiCallActionDomainDetailsTypeDef",
    {
        "Domain": NotRequired[str],
    },
)

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired["ActionRemoteIpDetailsTypeDef"],
        "DomainDetails": NotRequired["AwsApiCallActionDomainDetailsTypeDef"],
        "AffectedResources": NotRequired[Mapping[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)

AwsApiGatewayAccessLogSettingsTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsTypeDef",
    {
        "Format": NotRequired[str],
        "DestinationArn": NotRequired[str],
    },
)

AwsApiGatewayCanarySettingsTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsTypeDef",
    {
        "PercentTraffic": NotRequired[float],
        "DeploymentId": NotRequired[str],
        "StageVariableOverrides": NotRequired[Mapping[str, str]],
        "UseStageCache": NotRequired[bool],
    },
)

AwsApiGatewayEndpointConfigurationTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationTypeDef",
    {
        "Types": NotRequired[Sequence[str]],
    },
)

AwsApiGatewayMethodSettingsTypeDef = TypedDict(
    "AwsApiGatewayMethodSettingsTypeDef",
    {
        "MetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[str],
        "DataTraceEnabled": NotRequired[bool],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
        "CachingEnabled": NotRequired[bool],
        "CacheTtlInSeconds": NotRequired[int],
        "CacheDataEncrypted": NotRequired[bool],
        "RequireAuthorizationForCacheControl": NotRequired[bool],
        "UnauthorizedCacheControlHeaderStrategy": NotRequired[str],
        "HttpMethod": NotRequired[str],
        "ResourcePath": NotRequired[str],
    },
)

AwsApiGatewayRestApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Version": NotRequired[str],
        "BinaryMediaTypes": NotRequired[Sequence[str]],
        "MinimumCompressionSize": NotRequired[int],
        "ApiKeySource": NotRequired[str],
        "EndpointConfiguration": NotRequired["AwsApiGatewayEndpointConfigurationTypeDef"],
    },
)

AwsApiGatewayStageDetailsTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "ClientCertificateId": NotRequired[str],
        "StageName": NotRequired[str],
        "Description": NotRequired[str],
        "CacheClusterEnabled": NotRequired[bool],
        "CacheClusterSize": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "MethodSettings": NotRequired[Sequence["AwsApiGatewayMethodSettingsTypeDef"]],
        "Variables": NotRequired[Mapping[str, str]],
        "DocumentationVersion": NotRequired[str],
        "AccessLogSettings": NotRequired["AwsApiGatewayAccessLogSettingsTypeDef"],
        "CanarySettings": NotRequired["AwsApiGatewayCanarySettingsTypeDef"],
        "TracingEnabled": NotRequired[bool],
        "CreatedDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "WebAclArn": NotRequired[str],
    },
)

AwsApiGatewayV2ApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsTypeDef",
    {
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKeySelectionExpression": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "Version": NotRequired[str],
        "Name": NotRequired[str],
        "ProtocolType": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired["AwsCorsConfigurationTypeDef"],
    },
)

AwsApiGatewayV2RouteSettingsTypeDef = TypedDict(
    "AwsApiGatewayV2RouteSettingsTypeDef",
    {
        "DetailedMetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[str],
        "DataTraceEnabled": NotRequired[bool],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
    },
)

AwsApiGatewayV2StageDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsTypeDef",
    {
        "ClientCertificateId": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteSettings": NotRequired["AwsApiGatewayV2RouteSettingsTypeDef"],
        "DeploymentId": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "RouteSettings": NotRequired["AwsApiGatewayV2RouteSettingsTypeDef"],
        "StageName": NotRequired[str],
        "StageVariables": NotRequired[Mapping[str, str]],
        "AccessLogSettings": NotRequired["AwsApiGatewayAccessLogSettingsTypeDef"],
        "AutoDeploy": NotRequired[bool],
        "LastDeploymentStatusMessage": NotRequired[str],
        "ApiGatewayManaged": NotRequired[bool],
    },
)

AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    {
        "Value": NotRequired[str],
    },
)

AwsAutoScalingAutoScalingGroupDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    {
        "LaunchConfigurationName": NotRequired[str],
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "CreatedTime": NotRequired[str],
        "MixedInstancesPolicy": NotRequired[
            "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef"
        ],
        "AvailabilityZones": NotRequired[
            Sequence["AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef"]
        ],
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    {
        "InstancesDistribution": NotRequired[
            "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef"
        ],
        "LaunchTemplate": NotRequired[
            "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef"
        ],
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    {
        "OnDemandAllocationStrategy": NotRequired[str],
        "OnDemandBaseCapacity": NotRequired[int],
        "OnDemandPercentageAboveBaseCapacity": NotRequired[int],
        "SpotAllocationStrategy": NotRequired[str],
        "SpotInstancePools": NotRequired[int],
        "SpotMaxPrice": NotRequired[str],
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[
            "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef"
        ],
        "Overrides": NotRequired[
            Sequence[
                "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef"
            ]
        ],
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[str],
    },
)

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired["AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef"],
        "NoDevice": NotRequired[bool],
        "VirtualName": NotRequired[str],
    },
)

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)

AwsAutoScalingLaunchConfigurationDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BlockDeviceMappings": NotRequired[
            Sequence["AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef"]
        ],
        "ClassicLinkVpcId": NotRequired[str],
        "ClassicLinkVpcSecurityGroups": NotRequired[Sequence[str]],
        "CreatedTime": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceMonitoring": NotRequired[
            "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef"
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "PlacementTenancy": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SpotPrice": NotRequired[str],
        "UserData": NotRequired[str],
        "MetadataOptions": NotRequired["AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef"],
    },
)

AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpTokens": NotRequired[str],
    },
)

AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            Sequence["AwsCertificateManagerCertificateDomainValidationOptionTypeDef"]
        ],
        "ExtendedKeyUsages": NotRequired[
            Sequence["AwsCertificateManagerCertificateExtendedKeyUsageTypeDef"]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[Sequence[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[Sequence["AwsCertificateManagerCertificateKeyUsageTypeDef"]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired["AwsCertificateManagerCertificateOptionsTypeDef"],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired["AwsCertificateManagerCertificateRenewalSummaryTypeDef"],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[Sequence[str]],
        "Type": NotRequired[str],
    },
)

AwsCertificateManagerCertificateDomainValidationOptionTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    {
        "DomainName": NotRequired[str],
        "ResourceRecord": NotRequired["AwsCertificateManagerCertificateResourceRecordTypeDef"],
        "ValidationDomain": NotRequired[str],
        "ValidationEmails": NotRequired[Sequence[str]],
        "ValidationMethod": NotRequired[str],
        "ValidationStatus": NotRequired[str],
    },
)

AwsCertificateManagerCertificateExtendedKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    {
        "Name": NotRequired[str],
        "OId": NotRequired[str],
    },
)

AwsCertificateManagerCertificateKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    {
        "Name": NotRequired[str],
    },
)

AwsCertificateManagerCertificateOptionsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": NotRequired[str],
    },
)

AwsCertificateManagerCertificateRenewalSummaryTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    {
        "DomainValidationOptions": NotRequired[
            Sequence["AwsCertificateManagerCertificateDomainValidationOptionTypeDef"]
        ],
        "RenewalStatus": NotRequired[str],
        "RenewalStatusReason": NotRequired[str],
        "UpdatedAt": NotRequired[str],
    },
)

AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsCloudFrontDistributionCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": NotRequired[str],
    },
)

AwsCloudFrontDistributionCacheBehaviorsTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    {
        "Items": NotRequired[Sequence["AwsCloudFrontDistributionCacheBehaviorTypeDef"]],
    },
)

AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": NotRequired[str],
    },
)

AwsCloudFrontDistributionDetailsTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsTypeDef",
    {
        "CacheBehaviors": NotRequired["AwsCloudFrontDistributionCacheBehaviorsTypeDef"],
        "DefaultCacheBehavior": NotRequired["AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef"],
        "DefaultRootObject": NotRequired[str],
        "DomainName": NotRequired[str],
        "ETag": NotRequired[str],
        "LastModifiedTime": NotRequired[str],
        "Logging": NotRequired["AwsCloudFrontDistributionLoggingTypeDef"],
        "Origins": NotRequired["AwsCloudFrontDistributionOriginsTypeDef"],
        "OriginGroups": NotRequired["AwsCloudFrontDistributionOriginGroupsTypeDef"],
        "ViewerCertificate": NotRequired["AwsCloudFrontDistributionViewerCertificateTypeDef"],
        "Status": NotRequired[str],
        "WebAclId": NotRequired[str],
    },
)

AwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingTypeDef",
    {
        "Bucket": NotRequired[str],
        "Enabled": NotRequired[bool],
        "IncludeCookies": NotRequired[bool],
        "Prefix": NotRequired[str],
    },
)

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    {
        "Items": NotRequired[Sequence[int]],
        "Quantity": NotRequired[int],
    },
)

AwsCloudFrontDistributionOriginGroupFailoverTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    {
        "StatusCodes": NotRequired[
            "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef"
        ],
    },
)

AwsCloudFrontDistributionOriginGroupTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    {
        "FailoverCriteria": NotRequired["AwsCloudFrontDistributionOriginGroupFailoverTypeDef"],
    },
)

AwsCloudFrontDistributionOriginGroupsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    {
        "Items": NotRequired[Sequence["AwsCloudFrontDistributionOriginGroupTypeDef"]],
    },
)

AwsCloudFrontDistributionOriginItemTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemTypeDef",
    {
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "OriginPath": NotRequired[str],
        "S3OriginConfig": NotRequired["AwsCloudFrontDistributionOriginS3OriginConfigTypeDef"],
    },
)

AwsCloudFrontDistributionOriginS3OriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": NotRequired[str],
    },
)

AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": NotRequired[Sequence["AwsCloudFrontDistributionOriginItemTypeDef"]],
    },
)

AwsCloudFrontDistributionViewerCertificateTypeDef = TypedDict(
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    {
        "AcmCertificateArn": NotRequired[str],
        "Certificate": NotRequired[str],
        "CertificateSource": NotRequired[str],
        "CloudFrontDefaultCertificate": NotRequired[bool],
        "IamCertificateId": NotRequired[str],
        "MinimumProtocolVersion": NotRequired[str],
        "SslSupportMethod": NotRequired[str],
    },
)

AwsCloudTrailTrailDetailsTypeDef = TypedDict(
    "AwsCloudTrailTrailDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "HasCustomEventSelectors": NotRequired[bool],
        "HomeRegion": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "IsOrganizationTrail": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "LogFileValidationEnabled": NotRequired[bool],
        "Name": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "TrailArn": NotRequired[str],
    },
)

AwsCodeBuildProjectArtifactsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    {
        "ArtifactIdentifier": NotRequired[str],
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceType": NotRequired[str],
        "OverrideArtifactName": NotRequired[bool],
        "Packaging": NotRequired[str],
        "Path": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsCodeBuildProjectDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsTypeDef",
    {
        "EncryptionKey": NotRequired[str],
        "Artifacts": NotRequired[Sequence["AwsCodeBuildProjectArtifactsDetailsTypeDef"]],
        "Environment": NotRequired["AwsCodeBuildProjectEnvironmentTypeDef"],
        "Name": NotRequired[str],
        "Source": NotRequired["AwsCodeBuildProjectSourceTypeDef"],
        "ServiceRole": NotRequired[str],
        "LogsConfig": NotRequired["AwsCodeBuildProjectLogsConfigDetailsTypeDef"],
        "VpcConfig": NotRequired["AwsCodeBuildProjectVpcConfigTypeDef"],
    },
)

AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {
        "Credential": NotRequired[str],
        "CredentialProvider": NotRequired[str],
    },
)

AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            Sequence["AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef"]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[
            "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef"
        ],
        "Type": NotRequired[str],
    },
)

AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    {
        "GroupName": NotRequired[str],
        "Status": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)

AwsCodeBuildProjectLogsConfigDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    {
        "CloudWatchLogs": NotRequired["AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef"],
        "S3Logs": NotRequired["AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef"],
    },
)

AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    {
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Location": NotRequired[str],
        "GitCloneDepth": NotRequired[int],
        "InsecureSsl": NotRequired[bool],
    },
)

AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

AwsCorsConfigurationTypeDef = TypedDict(
    "AwsCorsConfigurationTypeDef",
    {
        "AllowOrigins": NotRequired[Sequence[str]],
        "AllowCredentials": NotRequired[bool],
        "ExposeHeaders": NotRequired[Sequence[str]],
        "MaxAge": NotRequired[int],
        "AllowMethods": NotRequired[Sequence[str]],
        "AllowHeaders": NotRequired[Sequence[str]],
    },
)

AwsDynamoDbTableAttributeDefinitionTypeDef = TypedDict(
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeType": NotRequired[str],
    },
)

AwsDynamoDbTableBillingModeSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    {
        "BillingMode": NotRequired[str],
        "LastUpdateToPayPerRequestDateTime": NotRequired[str],
    },
)

AwsDynamoDbTableDetailsTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsTypeDef",
    {
        "AttributeDefinitions": NotRequired[Sequence["AwsDynamoDbTableAttributeDefinitionTypeDef"]],
        "BillingModeSummary": NotRequired["AwsDynamoDbTableBillingModeSummaryTypeDef"],
        "CreationDateTime": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            Sequence["AwsDynamoDbTableGlobalSecondaryIndexTypeDef"]
        ],
        "GlobalTableVersion": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[Sequence["AwsDynamoDbTableKeySchemaTypeDef"]],
        "LatestStreamArn": NotRequired[str],
        "LatestStreamLabel": NotRequired[str],
        "LocalSecondaryIndexes": NotRequired[
            Sequence["AwsDynamoDbTableLocalSecondaryIndexTypeDef"]
        ],
        "ProvisionedThroughput": NotRequired["AwsDynamoDbTableProvisionedThroughputTypeDef"],
        "Replicas": NotRequired[Sequence["AwsDynamoDbTableReplicaTypeDef"]],
        "RestoreSummary": NotRequired["AwsDynamoDbTableRestoreSummaryTypeDef"],
        "SseDescription": NotRequired["AwsDynamoDbTableSseDescriptionTypeDef"],
        "StreamSpecification": NotRequired["AwsDynamoDbTableStreamSpecificationTypeDef"],
        "TableId": NotRequired[str],
        "TableName": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "TableStatus": NotRequired[str],
    },
)

AwsDynamoDbTableGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    {
        "Backfilling": NotRequired[bool],
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "IndexSizeBytes": NotRequired[int],
        "IndexStatus": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[Sequence["AwsDynamoDbTableKeySchemaTypeDef"]],
        "Projection": NotRequired["AwsDynamoDbTableProjectionTypeDef"],
        "ProvisionedThroughput": NotRequired["AwsDynamoDbTableProvisionedThroughputTypeDef"],
    },
)

AwsDynamoDbTableKeySchemaTypeDef = TypedDict(
    "AwsDynamoDbTableKeySchemaTypeDef",
    {
        "AttributeName": NotRequired[str],
        "KeyType": NotRequired[str],
    },
)

AwsDynamoDbTableLocalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    {
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[Sequence["AwsDynamoDbTableKeySchemaTypeDef"]],
        "Projection": NotRequired["AwsDynamoDbTableProjectionTypeDef"],
    },
)

AwsDynamoDbTableProjectionTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionTypeDef",
    {
        "NonKeyAttributes": NotRequired[Sequence[str]],
        "ProjectionType": NotRequired[str],
    },
)

AwsDynamoDbTableProvisionedThroughputOverrideTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": NotRequired[int],
    },
)

AwsDynamoDbTableProvisionedThroughputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    {
        "LastDecreaseDateTime": NotRequired[str],
        "LastIncreaseDateTime": NotRequired[str],
        "NumberOfDecreasesToday": NotRequired[int],
        "ReadCapacityUnits": NotRequired[int],
        "WriteCapacityUnits": NotRequired[int],
    },
)

AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef"
        ],
    },
)

AwsDynamoDbTableReplicaTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            Sequence["AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef"]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef"
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)

AwsDynamoDbTableRestoreSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    {
        "SourceBackupArn": NotRequired[str],
        "SourceTableArn": NotRequired[str],
        "RestoreDateTime": NotRequired[str],
        "RestoreInProgress": NotRequired[bool],
    },
)

AwsDynamoDbTableSseDescriptionTypeDef = TypedDict(
    "AwsDynamoDbTableSseDescriptionTypeDef",
    {
        "InaccessibleEncryptionDateTime": NotRequired[str],
        "Status": NotRequired[str],
        "SseType": NotRequired[str],
        "KmsMasterKeyArn": NotRequired[str],
    },
)

AwsDynamoDbTableStreamSpecificationTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": NotRequired[bool],
        "StreamViewType": NotRequired[str],
    },
)

AwsEc2EipDetailsTypeDef = TypedDict(
    "AwsEc2EipDetailsTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "Domain": NotRequired[str],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfaceOwnerId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[Sequence[str]],
        "IpV6Addresses": NotRequired[Sequence[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[Sequence["AwsEc2InstanceNetworkInterfacesDetailsTypeDef"]],
    },
)

AwsEc2InstanceNetworkInterfacesDetailsTypeDef = TypedDict(
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
    },
)

AwsEc2NetworkAclAssociationTypeDef = TypedDict(
    "AwsEc2NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": NotRequired[str],
        "NetworkAclId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)

AwsEc2NetworkAclDetailsTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsTypeDef",
    {
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Associations": NotRequired[Sequence["AwsEc2NetworkAclAssociationTypeDef"]],
        "Entries": NotRequired[Sequence["AwsEc2NetworkAclEntryTypeDef"]],
    },
)

AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Egress": NotRequired[bool],
        "IcmpTypeCode": NotRequired["IcmpTypeCodeTypeDef"],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired["PortRangeFromToTypeDef"],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "RuleNumber": NotRequired[int],
    },
)

AwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsEc2NetworkInterfaceDetailsTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    {
        "Attachment": NotRequired["AwsEc2NetworkInterfaceAttachmentTypeDef"],
        "NetworkInterfaceId": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence["AwsEc2NetworkInterfaceSecurityGroupTypeDef"]],
        "SourceDestCheck": NotRequired[bool],
        "IpV6Addresses": NotRequired[Sequence["AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef"]],
        "PrivateIpAddresses": NotRequired[
            Sequence["AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef"]
        ],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)

AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    {
        "IpV6Address": NotRequired[str],
    },
)

AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    {
        "PrivateIpAddress": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
    },
)

AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)

AwsEc2SecurityGroupDetailsTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["AwsEc2SecurityGroupIpPermissionTypeDef"]],
        "IpPermissionsEgress": NotRequired[Sequence["AwsEc2SecurityGroupIpPermissionTypeDef"]],
    },
)

AwsEc2SecurityGroupIpPermissionTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[Sequence["AwsEc2SecurityGroupUserIdGroupPairTypeDef"]],
        "IpRanges": NotRequired[Sequence["AwsEc2SecurityGroupIpRangeTypeDef"]],
        "Ipv6Ranges": NotRequired[Sequence["AwsEc2SecurityGroupIpv6RangeTypeDef"]],
        "PrefixListIds": NotRequired[Sequence["AwsEc2SecurityGroupPrefixListIdTypeDef"]],
    },
)

AwsEc2SecurityGroupIpRangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
    },
)

AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    {
        "CidrIpv6": NotRequired[str],
    },
)

AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    {
        "PrefixListId": NotRequired[str],
    },
)

AwsEc2SecurityGroupUserIdGroupPairTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

AwsEc2SubnetDetailsTypeDef = TypedDict(
    "AwsEc2SubnetDetailsTypeDef",
    {
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "SubnetArn": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Ipv6CidrBlockAssociationSet": NotRequired[Sequence["Ipv6CidrBlockAssociationTypeDef"]],
    },
)

AwsEc2VolumeAttachmentTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentTypeDef",
    {
        "AttachTime": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsEc2VolumeDetailsTypeDef = TypedDict(
    "AwsEc2VolumeDetailsTypeDef",
    {
        "CreateTime": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Attachments": NotRequired[Sequence["AwsEc2VolumeAttachmentTypeDef"]],
    },
)

AwsEc2VpcDetailsTypeDef = TypedDict(
    "AwsEc2VpcDetailsTypeDef",
    {
        "CidrBlockAssociationSet": NotRequired[Sequence["CidrBlockAssociationTypeDef"]],
        "Ipv6CidrBlockAssociationSet": NotRequired[Sequence["Ipv6CidrBlockAssociationTypeDef"]],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[str],
    },
)

AwsEc2VpcEndpointServiceDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BaseEndpointDnsNames": NotRequired[Sequence[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "NetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[Sequence["AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef"]],
    },
)

AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    {
        "ServiceType": NotRequired[str],
    },
)

AwsEc2VpnConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[Sequence["AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef"]],
        "Options": NotRequired["AwsEc2VpnConnectionOptionsDetailsTypeDef"],
        "Routes": NotRequired[Sequence["AwsEc2VpnConnectionRoutesDetailsTypeDef"]],
        "TransitGatewayId": NotRequired[str],
    },
)

AwsEc2VpnConnectionOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    {
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelOptions": NotRequired[
            Sequence["AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef"]
        ],
    },
)

AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    {
        "DpdTimeoutSeconds": NotRequired[int],
        "IkeVersions": NotRequired[Sequence[str]],
        "OutsideIpAddress": NotRequired[str],
        "Phase1DhGroupNumbers": NotRequired[Sequence[int]],
        "Phase1EncryptionAlgorithms": NotRequired[Sequence[str]],
        "Phase1IntegrityAlgorithms": NotRequired[Sequence[str]],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2DhGroupNumbers": NotRequired[Sequence[int]],
        "Phase2EncryptionAlgorithms": NotRequired[Sequence[str]],
        "Phase2IntegrityAlgorithms": NotRequired[Sequence[str]],
        "Phase2LifetimeSeconds": NotRequired[int],
        "PreSharedKey": NotRequired[str],
        "RekeyFuzzPercentage": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "TunnelInsideCidr": NotRequired[str],
    },
)

AwsEc2VpnConnectionRoutesDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "State": NotRequired[str],
    },
)

AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    {
        "AcceptedRouteCount": NotRequired[int],
        "CertificateArn": NotRequired[str],
        "LastStatusChange": NotRequired[str],
        "OutsideIpAddress": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)

AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "RegistryId": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Architecture": NotRequired[str],
        "ImageDigest": NotRequired[str],
        "ImageTags": NotRequired[Sequence[str]],
        "ImagePublishedAt": NotRequired[str],
    },
)

AwsEcrRepositoryDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "ImageScanningConfiguration": NotRequired[
            "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef"
        ],
        "ImageTagMutability": NotRequired[str],
        "LifecyclePolicy": NotRequired["AwsEcrRepositoryLifecyclePolicyDetailsTypeDef"],
        "RepositoryName": NotRequired[str],
        "RepositoryPolicyText": NotRequired[str],
    },
)

AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    {
        "ScanOnPush": NotRequired[bool],
    },
)

AwsEcrRepositoryLifecyclePolicyDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    {
        "LifecyclePolicyText": NotRequired[str],
        "RegistryId": NotRequired[str],
    },
)

AwsEcsClusterClusterSettingsDetailsTypeDef = TypedDict(
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsEcsClusterConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationDetailsTypeDef",
    {
        "ExecuteCommandConfiguration": NotRequired[
            "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef"
        ],
    },
)

AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    {
        "KmsKeyId": NotRequired[str],
        "LogConfiguration": NotRequired[
            "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef"
        ],
        "Logging": NotRequired[str],
    },
)

AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    {
        "CloudWatchEncryptionEnabled": NotRequired[bool],
        "CloudWatchLogGroupName": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3EncryptionEnabled": NotRequired[bool],
        "S3KeyPrefix": NotRequired[str],
    },
)

AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": NotRequired[int],
        "CapacityProvider": NotRequired[str],
        "Weight": NotRequired[int],
    },
)

AwsEcsClusterDetailsTypeDef = TypedDict(
    "AwsEcsClusterDetailsTypeDef",
    {
        "CapacityProviders": NotRequired[Sequence[str]],
        "ClusterSettings": NotRequired[Sequence["AwsEcsClusterClusterSettingsDetailsTypeDef"]],
        "Configuration": NotRequired["AwsEcsClusterConfigurationDetailsTypeDef"],
        "DefaultCapacityProviderStrategy": NotRequired[
            Sequence["AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef"]
        ],
    },
)

AwsEcsServiceCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": NotRequired[int],
        "CapacityProvider": NotRequired[str],
        "Weight": NotRequired[int],
    },
)

AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    {
        "Enable": NotRequired[bool],
        "Rollback": NotRequired[bool],
    },
)

AwsEcsServiceDeploymentConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    {
        "DeploymentCircuitBreaker": NotRequired[
            "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef"
        ],
        "MaximumPercent": NotRequired[int],
        "MinimumHealthyPercent": NotRequired[int],
    },
)

AwsEcsServiceDeploymentControllerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)

AwsEcsServiceDetailsTypeDef = TypedDict(
    "AwsEcsServiceDetailsTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            Sequence["AwsEcsServiceCapacityProviderStrategyDetailsTypeDef"]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[
            "AwsEcsServiceDeploymentConfigurationDetailsTypeDef"
        ],
        "DeploymentController": NotRequired["AwsEcsServiceDeploymentControllerDetailsTypeDef"],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[Sequence["AwsEcsServiceLoadBalancersDetailsTypeDef"]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired["AwsEcsServiceNetworkConfigurationDetailsTypeDef"],
        "PlacementConstraints": NotRequired[
            Sequence["AwsEcsServicePlacementConstraintsDetailsTypeDef"]
        ],
        "PlacementStrategies": NotRequired[
            Sequence["AwsEcsServicePlacementStrategiesDetailsTypeDef"]
        ],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[Sequence["AwsEcsServiceServiceRegistriesDetailsTypeDef"]],
        "TaskDefinition": NotRequired[str],
    },
)

AwsEcsServiceLoadBalancersDetailsTypeDef = TypedDict(
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ContainerPort": NotRequired[int],
        "LoadBalancerName": NotRequired[str],
        "TargetGroupArn": NotRequired[str],
    },
)

AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    {
        "AssignPublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Subnets": NotRequired[Sequence[str]],
    },
)

AwsEcsServiceNetworkConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    {
        "AwsVpcConfiguration": NotRequired[
            "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef"
        ],
    },
)

AwsEcsServicePlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsEcsServicePlacementStrategiesDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    {
        "Field": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsEcsServiceServiceRegistriesDetailsTypeDef = TypedDict(
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ContainerPort": NotRequired[int],
        "Port": NotRequired[int],
        "RegistryArn": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    {
        "Condition": NotRequired[str],
        "ContainerName": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Cpu": NotRequired[int],
        "DependsOn": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef"]
        ],
        "DisableNetworking": NotRequired[bool],
        "DnsSearchDomains": NotRequired[Sequence[str]],
        "DnsServers": NotRequired[Sequence[str]],
        "DockerLabels": NotRequired[Mapping[str, str]],
        "DockerSecurityOptions": NotRequired[Sequence[str]],
        "EntryPoint": NotRequired[Sequence[str]],
        "Environment": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef"]
        ],
        "EnvironmentFiles": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef"]
        ],
        "Essential": NotRequired[bool],
        "ExtraHosts": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef"]
        ],
        "FirelensConfiguration": NotRequired[
            "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef"
        ],
        "HealthCheck": NotRequired[
            "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef"
        ],
        "Hostname": NotRequired[str],
        "Image": NotRequired[str],
        "Interactive": NotRequired[bool],
        "Links": NotRequired[Sequence[str]],
        "LinuxParameters": NotRequired[
            "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef"
        ],
        "LogConfiguration": NotRequired[
            "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef"
        ],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "MountPoints": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef"]
        ],
        "Name": NotRequired[str],
        "PortMappings": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef"]
        ],
        "Privileged": NotRequired[bool],
        "PseudoTerminal": NotRequired[bool],
        "ReadonlyRootFilesystem": NotRequired[bool],
        "RepositoryCredentials": NotRequired[
            "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef"
        ],
        "ResourceRequirements": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef"]
        ],
        "Secrets": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef"]
        ],
        "StartTimeout": NotRequired[int],
        "StopTimeout": NotRequired[int],
        "SystemControls": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef"]
        ],
        "Ulimits": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef"]
        ],
        "User": NotRequired[str],
        "VolumesFrom": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef"]
        ],
        "WorkingDirectory": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    {
        "Hostname": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    {
        "Options": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Interval": NotRequired[int],
        "Retries": NotRequired[int],
        "StartPeriod": NotRequired[int],
        "Timeout": NotRequired[int],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    {
        "Add": NotRequired[Sequence[str]],
        "Drop": NotRequired[Sequence[str]],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    {
        "Capabilities": NotRequired[
            "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef"
        ],
        "Devices": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef"]
        ],
        "InitProcessEnabled": NotRequired[bool],
        "MaxSwap": NotRequired[int],
        "SharedMemorySize": NotRequired[int],
        "Swappiness": NotRequired[int],
        "Tmpfs": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef"]
        ],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "HostPath": NotRequired[str],
        "Permissions": NotRequired[Sequence[str]],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "MountOptions": NotRequired[Sequence[str]],
        "Size": NotRequired[int],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    {
        "LogDriver": NotRequired[str],
        "Options": NotRequired[Mapping[str, str]],
        "SecretOptions": NotRequired[
            Sequence[
                "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef"
            ]
        ],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ValueFrom": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "SourceVolume": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    {
        "ContainerPort": NotRequired[int],
        "HostPort": NotRequired[int],
        "Protocol": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    {
        "CredentialsParameter": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ValueFrom": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    {
        "Namespace": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    {
        "HardLimit": NotRequired[int],
        "Name": NotRequired[str],
        "SoftLimit": NotRequired[int],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    {
        "ReadOnly": NotRequired[bool],
        "SourceContainer": NotRequired[str],
    },
)

AwsEcsTaskDefinitionDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsTypeDef",
    {
        "ContainerDefinitions": NotRequired[
            Sequence["AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef"]
        ],
        "Cpu": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "Family": NotRequired[str],
        "InferenceAccelerators": NotRequired[
            Sequence["AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef"]
        ],
        "IpcMode": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkMode": NotRequired[str],
        "PidMode": NotRequired[str],
        "PlacementConstraints": NotRequired[
            Sequence["AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef"]
        ],
        "ProxyConfiguration": NotRequired["AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef"],
        "RequiresCompatibilities": NotRequired[Sequence[str]],
        "TaskRoleArn": NotRequired[str],
        "Volumes": NotRequired[Sequence["AwsEcsTaskDefinitionVolumesDetailsTypeDef"]],
    },
)

AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "DeviceType": NotRequired[str],
    },
)

AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            Sequence[
                "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef"
            ]
        ],
        "Type": NotRequired[str],
    },
)

AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsEcsTaskDefinitionVolumesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    {
        "DockerVolumeConfiguration": NotRequired[
            "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef"
        ],
        "EfsVolumeConfiguration": NotRequired[
            "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef"
        ],
        "Host": NotRequired["AwsEcsTaskDefinitionVolumesHostDetailsTypeDef"],
        "Name": NotRequired[str],
    },
)

AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    {
        "Autoprovision": NotRequired[bool],
        "Driver": NotRequired[str],
        "DriverOpts": NotRequired[Mapping[str, str]],
        "Labels": NotRequired[Mapping[str, str]],
        "Scope": NotRequired[str],
    },
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Iam": NotRequired[str],
    },
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    {
        "AuthorizationConfig": NotRequired[
            "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef"
        ],
        "FilesystemId": NotRequired[str],
        "RootDirectory": NotRequired[str],
        "TransitEncryption": NotRequired[str],
        "TransitEncryptionPort": NotRequired[int],
    },
)

AwsEcsTaskDefinitionVolumesHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    {
        "SourcePath": NotRequired[str],
    },
)

AwsEksClusterDetailsTypeDef = TypedDict(
    "AwsEksClusterDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityData": NotRequired[str],
        "ClusterStatus": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Name": NotRequired[str],
        "ResourcesVpcConfig": NotRequired["AwsEksClusterResourcesVpcConfigDetailsTypeDef"],
        "RoleArn": NotRequired[str],
        "Version": NotRequired[str],
        "Logging": NotRequired["AwsEksClusterLoggingDetailsTypeDef"],
    },
)

AwsEksClusterLoggingClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Types": NotRequired[Sequence[str]],
    },
)

AwsEksClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsTypeDef",
    {
        "ClusterLogging": NotRequired[Sequence["AwsEksClusterLoggingClusterLoggingDetailsTypeDef"]],
    },
)

AwsEksClusterResourcesVpcConfigDetailsTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)

AwsElasticBeanstalkEnvironmentDetailsTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "Cname": NotRequired[str],
        "DateCreated": NotRequired[str],
        "DateUpdated": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EnvironmentArn": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentLinks": NotRequired[
            Sequence["AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef"]
        ],
        "EnvironmentName": NotRequired[str],
        "OptionSettings": NotRequired[
            Sequence["AwsElasticBeanstalkEnvironmentOptionSettingTypeDef"]
        ],
        "PlatformArn": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "Status": NotRequired[str],
        "Tier": NotRequired["AwsElasticBeanstalkEnvironmentTierTypeDef"],
        "VersionLabel": NotRequired[str],
    },
)

AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "LinkName": NotRequired[str],
    },
)

AwsElasticBeanstalkEnvironmentOptionSettingTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    {
        "Namespace": NotRequired[str],
        "OptionName": NotRequired[str],
        "ResourceName": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Version": NotRequired[str],
    },
)

AwsElasticsearchDomainDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsTypeDef",
    {
        "AccessPolicies": NotRequired[str],
        "DomainEndpointOptions": NotRequired["AwsElasticsearchDomainDomainEndpointOptionsTypeDef"],
        "DomainId": NotRequired[str],
        "DomainName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Mapping[str, str]],
        "ElasticsearchVersion": NotRequired[str],
        "ElasticsearchClusterConfig": NotRequired[
            "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef"
        ],
        "EncryptionAtRestOptions": NotRequired[
            "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef"
        ],
        "LogPublishingOptions": NotRequired["AwsElasticsearchDomainLogPublishingOptionsTypeDef"],
        "NodeToNodeEncryptionOptions": NotRequired[
            "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef"
        ],
        "ServiceSoftwareOptions": NotRequired[
            "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef"
        ],
        "VPCOptions": NotRequired["AwsElasticsearchDomainVPCOptionsTypeDef"],
    },
)

AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": NotRequired[bool],
        "TLSSecurityPolicy": NotRequired[str],
    },
)

AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    {
        "DedicatedMasterCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "DedicatedMasterType": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "ZoneAwarenessConfig": NotRequired[
            "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef"
        ],
        "ZoneAwarenessEnabled": NotRequired[bool],
    },
)

AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)

AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)

AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)

AwsElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    {
        "IndexSlowLogs": NotRequired["AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef"],
        "SearchSlowLogs": NotRequired["AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef"],
        "AuditLogs": NotRequired["AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef"],
    },
)

AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

AwsElasticsearchDomainServiceSoftwareOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    {
        "AutomatedUpdateDate": NotRequired[str],
        "Cancellable": NotRequired[bool],
        "CurrentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "UpdateStatus": NotRequired[str],
    },
)

AwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VPCId": NotRequired[str],
    },
)

AwsElbAppCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbAppCookieStickinessPolicyTypeDef",
    {
        "CookieName": NotRequired[str],
        "PolicyName": NotRequired[str],
    },
)

AwsElbLbCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyTypeDef",
    {
        "CookieExpirationPeriod": NotRequired[int],
        "PolicyName": NotRequired[str],
    },
)

AwsElbLoadBalancerAccessLogTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogTypeDef",
    {
        "EmitInterval": NotRequired[int],
        "Enabled": NotRequired[bool],
        "S3BucketName": NotRequired[str],
        "S3BucketPrefix": NotRequired[str],
    },
)

AwsElbLoadBalancerAttributesTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesTypeDef",
    {
        "AccessLog": NotRequired["AwsElbLoadBalancerAccessLogTypeDef"],
        "ConnectionDraining": NotRequired["AwsElbLoadBalancerConnectionDrainingTypeDef"],
        "ConnectionSettings": NotRequired["AwsElbLoadBalancerConnectionSettingsTypeDef"],
        "CrossZoneLoadBalancing": NotRequired["AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef"],
    },
)

AwsElbLoadBalancerBackendServerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)

AwsElbLoadBalancerConnectionDrainingTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Timeout": NotRequired[int],
    },
)

AwsElbLoadBalancerConnectionSettingsTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    {
        "IdleTimeout": NotRequired[int],
    },
)

AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

AwsElbLoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackendServerDescriptions": NotRequired[
            Sequence["AwsElbLoadBalancerBackendServerDescriptionTypeDef"]
        ],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "HealthCheck": NotRequired["AwsElbLoadBalancerHealthCheckTypeDef"],
        "Instances": NotRequired[Sequence["AwsElbLoadBalancerInstanceTypeDef"]],
        "ListenerDescriptions": NotRequired[
            Sequence["AwsElbLoadBalancerListenerDescriptionTypeDef"]
        ],
        "LoadBalancerAttributes": NotRequired["AwsElbLoadBalancerAttributesTypeDef"],
        "LoadBalancerName": NotRequired[str],
        "Policies": NotRequired["AwsElbLoadBalancerPoliciesTypeDef"],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SourceSecurityGroup": NotRequired["AwsElbLoadBalancerSourceSecurityGroupTypeDef"],
        "Subnets": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
    },
)

AwsElbLoadBalancerHealthCheckTypeDef = TypedDict(
    "AwsElbLoadBalancerHealthCheckTypeDef",
    {
        "HealthyThreshold": NotRequired[int],
        "Interval": NotRequired[int],
        "Target": NotRequired[str],
        "Timeout": NotRequired[int],
        "UnhealthyThreshold": NotRequired[int],
    },
)

AwsElbLoadBalancerInstanceTypeDef = TypedDict(
    "AwsElbLoadBalancerInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
    },
)

AwsElbLoadBalancerListenerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    {
        "Listener": NotRequired["AwsElbLoadBalancerListenerTypeDef"],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)

AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": NotRequired[int],
        "InstanceProtocol": NotRequired[str],
        "LoadBalancerPort": NotRequired[int],
        "Protocol": NotRequired[str],
        "SslCertificateId": NotRequired[str],
    },
)

AwsElbLoadBalancerPoliciesTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[
            Sequence["AwsElbAppCookieStickinessPolicyTypeDef"]
        ],
        "LbCookieStickinessPolicies": NotRequired[
            Sequence["AwsElbLbCookieStickinessPolicyTypeDef"]
        ],
        "OtherPolicies": NotRequired[Sequence[str]],
    },
)

AwsElbLoadBalancerSourceSecurityGroupTypeDef = TypedDict(
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "OwnerAlias": NotRequired[str],
    },
)

AwsElbv2LoadBalancerAttributeTypeDef = TypedDict(
    "AwsElbv2LoadBalancerAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence["AvailabilityZoneTypeDef"]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "State": NotRequired["LoadBalancerStateTypeDef"],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[Sequence["AwsElbv2LoadBalancerAttributeTypeDef"]],
    },
)

AwsIamAccessKeyDetailsTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsTypeDef",
    {
        "UserName": NotRequired[str],
        "Status": NotRequired[AwsIamAccessKeyStatusType],
        "CreatedAt": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[str],
        "PrincipalName": NotRequired[str],
        "AccountId": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "SessionContext": NotRequired["AwsIamAccessKeySessionContextTypeDef"],
    },
)

AwsIamAccessKeySessionContextAttributesTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    {
        "MfaAuthenticated": NotRequired[bool],
        "CreationDate": NotRequired[str],
    },
)

AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {
        "Type": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "Arn": NotRequired[str],
        "AccountId": NotRequired[str],
        "UserName": NotRequired[str],
    },
)

AwsIamAccessKeySessionContextTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextTypeDef",
    {
        "Attributes": NotRequired["AwsIamAccessKeySessionContextAttributesTypeDef"],
        "SessionIssuer": NotRequired["AwsIamAccessKeySessionContextSessionIssuerTypeDef"],
    },
)

AwsIamAttachedManagedPolicyTypeDef = TypedDict(
    "AwsIamAttachedManagedPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)

AwsIamGroupDetailsTypeDef = TypedDict(
    "AwsIamGroupDetailsTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[Sequence["AwsIamAttachedManagedPolicyTypeDef"]],
        "CreateDate": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupPolicyList": NotRequired[Sequence["AwsIamGroupPolicyTypeDef"]],
        "Path": NotRequired[str],
    },
)

AwsIamGroupPolicyTypeDef = TypedDict(
    "AwsIamGroupPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)

AwsIamInstanceProfileRoleTypeDef = TypedDict(
    "AwsIamInstanceProfileRoleTypeDef",
    {
        "Arn": NotRequired[str],
        "AssumeRolePolicyDocument": NotRequired[str],
        "CreateDate": NotRequired[str],
        "Path": NotRequired[str],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
    },
)

AwsIamInstanceProfileTypeDef = TypedDict(
    "AwsIamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[str],
        "InstanceProfileId": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Path": NotRequired[str],
        "Roles": NotRequired[Sequence["AwsIamInstanceProfileRoleTypeDef"]],
    },
)

AwsIamPermissionsBoundaryTypeDef = TypedDict(
    "AwsIamPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryArn": NotRequired[str],
        "PermissionsBoundaryType": NotRequired[str],
    },
)

AwsIamPolicyDetailsTypeDef = TypedDict(
    "AwsIamPolicyDetailsTypeDef",
    {
        "AttachmentCount": NotRequired[int],
        "CreateDate": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "Description": NotRequired[str],
        "IsAttachable": NotRequired[bool],
        "Path": NotRequired[str],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyVersionList": NotRequired[Sequence["AwsIamPolicyVersionTypeDef"]],
        "UpdateDate": NotRequired[str],
    },
)

AwsIamPolicyVersionTypeDef = TypedDict(
    "AwsIamPolicyVersionTypeDef",
    {
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "CreateDate": NotRequired[str],
    },
)

AwsIamRoleDetailsTypeDef = TypedDict(
    "AwsIamRoleDetailsTypeDef",
    {
        "AssumeRolePolicyDocument": NotRequired[str],
        "AttachedManagedPolicies": NotRequired[Sequence["AwsIamAttachedManagedPolicyTypeDef"]],
        "CreateDate": NotRequired[str],
        "InstanceProfileList": NotRequired[Sequence["AwsIamInstanceProfileTypeDef"]],
        "PermissionsBoundary": NotRequired["AwsIamPermissionsBoundaryTypeDef"],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
        "RolePolicyList": NotRequired[Sequence["AwsIamRolePolicyTypeDef"]],
        "MaxSessionDuration": NotRequired[int],
        "Path": NotRequired[str],
    },
)

AwsIamRolePolicyTypeDef = TypedDict(
    "AwsIamRolePolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)

AwsIamUserDetailsTypeDef = TypedDict(
    "AwsIamUserDetailsTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[Sequence["AwsIamAttachedManagedPolicyTypeDef"]],
        "CreateDate": NotRequired[str],
        "GroupList": NotRequired[Sequence[str]],
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired["AwsIamPermissionsBoundaryTypeDef"],
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserPolicyList": NotRequired[Sequence["AwsIamUserPolicyTypeDef"]],
    },
)

AwsIamUserPolicyTypeDef = TypedDict(
    "AwsIamUserPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)

AwsKmsKeyDetailsTypeDef = TypedDict(
    "AwsKmsKeyDetailsTypeDef",
    {
        "AWSAccountId": NotRequired[str],
        "CreationDate": NotRequired[float],
        "KeyId": NotRequired[str],
        "KeyManager": NotRequired[str],
        "KeyState": NotRequired[str],
        "Origin": NotRequired[str],
        "Description": NotRequired[str],
        "KeyRotationStatus": NotRequired[bool],
    },
)

AwsLambdaFunctionCodeTypeDef = TypedDict(
    "AwsLambdaFunctionCodeTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "ZipFile": NotRequired[str],
    },
)

AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    {
        "TargetArn": NotRequired[str],
    },
)

AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "Code": NotRequired["AwsLambdaFunctionCodeTypeDef"],
        "CodeSha256": NotRequired[str],
        "DeadLetterConfig": NotRequired["AwsLambdaFunctionDeadLetterConfigTypeDef"],
        "Environment": NotRequired["AwsLambdaFunctionEnvironmentTypeDef"],
        "FunctionName": NotRequired[str],
        "Handler": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "LastModified": NotRequired[str],
        "Layers": NotRequired[Sequence["AwsLambdaFunctionLayerTypeDef"]],
        "MasterArn": NotRequired[str],
        "MemorySize": NotRequired[int],
        "RevisionId": NotRequired[str],
        "Role": NotRequired[str],
        "Runtime": NotRequired[str],
        "Timeout": NotRequired[int],
        "TracingConfig": NotRequired["AwsLambdaFunctionTracingConfigTypeDef"],
        "VpcConfig": NotRequired["AwsLambdaFunctionVpcConfigTypeDef"],
        "Version": NotRequired[str],
    },
)

AwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)

AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": NotRequired[Mapping[str, str]],
        "Error": NotRequired["AwsLambdaFunctionEnvironmentErrorTypeDef"],
    },
)

AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef",
    {
        "Arn": NotRequired[str],
        "CodeSize": NotRequired[int],
    },
)

AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef",
    {
        "Mode": NotRequired[str],
    },
)

AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
    },
)

AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {
        "Version": NotRequired[int],
        "CompatibleRuntimes": NotRequired[Sequence[str]],
        "CreatedDate": NotRequired[str],
    },
)

AwsNetworkFirewallFirewallDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    {
        "DeleteProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallId": NotRequired[str],
        "FirewallName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "SubnetMappings": NotRequired[
            Sequence["AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef"]
        ],
        "VpcId": NotRequired[str],
    },
)

AwsNetworkFirewallFirewallPolicyDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    {
        "FirewallPolicy": NotRequired["FirewallPolicyDetailsTypeDef"],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
        "Description": NotRequired[str],
    },
)

AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    {
        "SubnetId": NotRequired[str],
    },
)

AwsNetworkFirewallRuleGroupDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired["RuleGroupDetailsTypeDef"],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "WarmEnabled": NotRequired[bool],
        "WarmCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "ZoneAwarenessConfig": NotRequired[
            "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef"
        ],
        "DedicatedMasterCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "WarmType": NotRequired[str],
        "ZoneAwarenessEnabled": NotRequired[bool],
        "DedicatedMasterType": NotRequired[str],
    },
)

AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)

AwsOpenSearchServiceDomainDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "AccessPolicies": NotRequired[str],
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "DomainEndpoint": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EncryptionAtRestOptions": NotRequired[
            "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef"
        ],
        "NodeToNodeEncryptionOptions": NotRequired[
            "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef"
        ],
        "ServiceSoftwareOptions": NotRequired[
            "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef"
        ],
        "ClusterConfig": NotRequired["AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef"],
        "DomainEndpointOptions": NotRequired[
            "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef"
        ],
        "VpcOptions": NotRequired["AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef"],
        "LogPublishingOptions": NotRequired[
            "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef"
        ],
        "DomainEndpoints": NotRequired[Mapping[str, str]],
    },
)

AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    {
        "CustomEndpointCertificateArn": NotRequired[str],
        "CustomEndpointEnabled": NotRequired[bool],
        "EnforceHTTPS": NotRequired[bool],
        "CustomEndpoint": NotRequired[str],
        "TLSSecurityPolicy": NotRequired[str],
    },
)

AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)

AwsOpenSearchServiceDomainLogPublishingOptionTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)

AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    {
        "IndexSlowLogs": NotRequired["AwsOpenSearchServiceDomainLogPublishingOptionTypeDef"],
        "SearchSlowLogs": NotRequired["AwsOpenSearchServiceDomainLogPublishingOptionTypeDef"],
        "AuditLogs": NotRequired["AwsOpenSearchServiceDomainLogPublishingOptionTypeDef"],
    },
)

AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    {
        "AutomatedUpdateDate": NotRequired[str],
        "Cancellable": NotRequired[bool],
        "CurrentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "UpdateStatus": NotRequired[str],
        "OptionalDeployment": NotRequired[bool],
    },
)

AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)

AwsRdsDbClusterAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRdsDbClusterDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "Status": NotRequired[str],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[Sequence[str]],
        "MultiAz": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[Sequence[str]],
        "VpcSecurityGroups": NotRequired[Sequence["AwsRdsDbInstanceVpcSecurityGroupTypeDef"]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "AssociatedRoles": NotRequired[Sequence["AwsRdsDbClusterAssociatedRoleTypeDef"]],
        "ClusterCreateTime": NotRequired[str],
        "EnabledCloudWatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamStatus": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[Sequence["AwsRdsDbDomainMembershipTypeDef"]],
        "DbClusterParameterGroup": NotRequired[str],
        "DbSubnetGroup": NotRequired[str],
        "DbClusterOptionGroupMemberships": NotRequired[
            Sequence["AwsRdsDbClusterOptionGroupMembershipTypeDef"]
        ],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterMembers": NotRequired[Sequence["AwsRdsDbClusterMemberTypeDef"]],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
    },
)

AwsRdsDbClusterMemberTypeDef = TypedDict(
    "AwsRdsDbClusterMemberTypeDef",
    {
        "IsClusterWriter": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "DbClusterParameterGroupStatus": NotRequired[str],
    },
)

AwsRdsDbClusterOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    {
        "DbClusterOptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRdsDbClusterSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterSnapshotIdentifier": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
    },
)

AwsRdsDbDomainMembershipTypeDef = TypedDict(
    "AwsRdsDbDomainMembershipTypeDef",
    {
        "Domain": NotRequired[str],
        "Status": NotRequired[str],
        "Fqdn": NotRequired[str],
        "IamRoleName": NotRequired[str],
    },
)

AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FeatureName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRdsDbInstanceDetailsTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsTypeDef",
    {
        "AssociatedRoles": NotRequired[Sequence["AwsRdsDbInstanceAssociatedRoleTypeDef"]],
        "CACertificateIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DbiResourceId": NotRequired[str],
        "DBName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "Endpoint": NotRequired["AwsRdsDbInstanceEndpointTypeDef"],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "InstanceCreateTime": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StorageEncrypted": NotRequired[bool],
        "TdeCredentialArn": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence["AwsRdsDbInstanceVpcSecurityGroupTypeDef"]],
        "MultiAz": NotRequired[bool],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "DbInstanceStatus": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DbSecurityGroups": NotRequired[Sequence[str]],
        "DbParameterGroups": NotRequired[Sequence["AwsRdsDbParameterGroupTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "DbSubnetGroup": NotRequired["AwsRdsDbSubnetGroupTypeDef"],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired["AwsRdsDbPendingModifiedValuesTypeDef"],
        "LatestRestorableTime": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[Sequence[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[Sequence[str]],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[Sequence["AwsRdsDbOptionGroupMembershipTypeDef"]],
        "CharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "StatusInfos": NotRequired[Sequence["AwsRdsDbStatusInfoTypeDef"]],
        "StorageType": NotRequired[str],
        "DomainMemberships": NotRequired[Sequence["AwsRdsDbDomainMembershipTypeDef"]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKmsKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudWatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence["AwsRdsDbProcessorFeatureTypeDef"]],
        "ListenerEndpoint": NotRequired["AwsRdsDbInstanceEndpointTypeDef"],
        "MaxAllocatedStorage": NotRequired[int],
    },
)

AwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "HostedZoneId": NotRequired[str],
    },
)

AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRdsDbOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRdsDbParameterGroupTypeDef = TypedDict(
    "AwsRdsDbParameterGroupTypeDef",
    {
        "DbParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
    },
)

AwsRdsDbPendingModifiedValuesTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesTypeDef",
    {
        "DbInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CaCertificateIdentifier": NotRequired[str],
        "DbSubnetGroupName": NotRequired[str],
        "PendingCloudWatchLogsExports": NotRequired["AwsRdsPendingCloudWatchLogsExportsTypeDef"],
        "ProcessorFeatures": NotRequired[Sequence["AwsRdsDbProcessorFeatureTypeDef"]],
    },
)

AwsRdsDbProcessorFeatureTypeDef = TypedDict(
    "AwsRdsDbProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsRdsDbSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsTypeDef",
    {
        "DbSnapshotIdentifier": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDbSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[Sequence["AwsRdsDbProcessorFeatureTypeDef"]],
        "DbiResourceId": NotRequired[str],
    },
)

AwsRdsDbStatusInfoTypeDef = TypedDict(
    "AwsRdsDbStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)

AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)

AwsRdsDbSubnetGroupSubnetTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired["AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef"],
        "SubnetStatus": NotRequired[str],
    },
)

AwsRdsDbSubnetGroupTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupTypeDef",
    {
        "DbSubnetGroupName": NotRequired[str],
        "DbSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[Sequence["AwsRdsDbSubnetGroupSubnetTypeDef"]],
        "DbSubnetGroupArn": NotRequired[str],
    },
)

AwsRdsEventSubscriptionDetailsTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsTypeDef",
    {
        "CustSubscriptionId": NotRequired[str],
        "CustomerAwsId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "EventCategoriesList": NotRequired[Sequence[str]],
        "EventSubscriptionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SourceIdsList": NotRequired[Sequence[str]],
        "SourceType": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
    },
)

AwsRdsPendingCloudWatchLogsExportsTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": NotRequired[Sequence[str]],
        "LogTypesToDisable": NotRequired[Sequence[str]],
    },
)

AwsRedshiftClusterClusterNodeTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeTypeDef",
    {
        "NodeRole": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
    },
)

AwsRedshiftClusterClusterParameterGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    {
        "ClusterParameterStatusList": NotRequired[
            Sequence["AwsRedshiftClusterClusterParameterStatusTypeDef"]
        ],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
    },
)

AwsRedshiftClusterClusterParameterStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterApplyErrorDescription": NotRequired[str],
    },
)

AwsRedshiftClusterClusterSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "RetentionPeriod": NotRequired[int],
        "SnapshotCopyGrantName": NotRequired[str],
    },
)

AwsRedshiftClusterDeferredMaintenanceWindowTypeDef = TypedDict(
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceEndTime": NotRequired[str],
        "DeferMaintenanceIdentifier": NotRequired[str],
        "DeferMaintenanceStartTime": NotRequired[str],
    },
)

AwsRedshiftClusterDetailsTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsTypeDef",
    {
        "AllowVersionUpgrade": NotRequired[bool],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "ClusterAvailabilityStatus": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "ClusterNodes": NotRequired[Sequence["AwsRedshiftClusterClusterNodeTypeDef"]],
        "ClusterParameterGroups": NotRequired[
            Sequence["AwsRedshiftClusterClusterParameterGroupTypeDef"]
        ],
        "ClusterPublicKey": NotRequired[str],
        "ClusterRevisionNumber": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[
            Sequence["AwsRedshiftClusterClusterSecurityGroupTypeDef"]
        ],
        "ClusterSnapshotCopyStatus": NotRequired[
            "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef"
        ],
        "ClusterStatus": NotRequired[str],
        "ClusterSubnetGroupName": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "DBName": NotRequired[str],
        "DeferredMaintenanceWindows": NotRequired[
            Sequence["AwsRedshiftClusterDeferredMaintenanceWindowTypeDef"]
        ],
        "ElasticIpStatus": NotRequired["AwsRedshiftClusterElasticIpStatusTypeDef"],
        "ElasticResizeNumberOfNodeOptions": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Endpoint": NotRequired["AwsRedshiftClusterEndpointTypeDef"],
        "EnhancedVpcRouting": NotRequired[bool],
        "ExpectedNextSnapshotScheduleTime": NotRequired[str],
        "ExpectedNextSnapshotScheduleTimeStatus": NotRequired[str],
        "HsmStatus": NotRequired["AwsRedshiftClusterHsmStatusTypeDef"],
        "IamRoles": NotRequired[Sequence["AwsRedshiftClusterIamRoleTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "MaintenanceTrackName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "NextMaintenanceWindowStartTime": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PendingActions": NotRequired[Sequence[str]],
        "PendingModifiedValues": NotRequired["AwsRedshiftClusterPendingModifiedValuesTypeDef"],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ResizeInfo": NotRequired["AwsRedshiftClusterResizeInfoTypeDef"],
        "RestoreStatus": NotRequired["AwsRedshiftClusterRestoreStatusTypeDef"],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "SnapshotScheduleState": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence["AwsRedshiftClusterVpcSecurityGroupTypeDef"]],
    },
)

AwsRedshiftClusterElasticIpStatusTypeDef = TypedDict(
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    {
        "ElasticIp": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRedshiftClusterEndpointTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)

AwsRedshiftClusterHsmStatusTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "Status": NotRequired[str],
    },
)

AwsRedshiftClusterIamRoleTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleTypeDef",
    {
        "ApplyStatus": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)

AwsRedshiftClusterPendingModifiedValuesTypeDef = TypedDict(
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    {
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ClusterIdentifier": NotRequired[str],
        "ClusterType": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "EncryptionType": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "MaintenanceTrackName": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
    },
)

AwsRedshiftClusterResizeInfoTypeDef = TypedDict(
    "AwsRedshiftClusterResizeInfoTypeDef",
    {
        "AllowCancelResize": NotRequired[bool],
        "ResizeType": NotRequired[str],
    },
)

AwsRedshiftClusterRestoreStatusTypeDef = TypedDict(
    "AwsRedshiftClusterRestoreStatusTypeDef",
    {
        "CurrentRestoreRateInMegaBytesPerSecond": NotRequired[float],
        "ElapsedTimeInSeconds": NotRequired[int],
        "EstimatedTimeToCompletionInSeconds": NotRequired[int],
        "ProgressInMegaBytes": NotRequired[int],
        "SnapshotSizeInMegaBytes": NotRequired[int],
        "Status": NotRequired[str],
    },
)

AwsRedshiftClusterVpcSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "VpcSecurityGroupId": NotRequired[str],
    },
)

AwsS3AccountPublicAccessBlockDetailsTypeDef = TypedDict(
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    {
        "BlockPublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
        "IgnorePublicAcls": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
    },
)

AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    {
        "Rules": NotRequired[
            Sequence["AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef"]
        ],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef = (
    TypedDict(
        "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
        {
            "DaysAfterInitiation": NotRequired[int],
        },
    )
)

AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    {
        "AbortIncompleteMultipartUpload": NotRequired[
            "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef"
        ],
        "ExpirationDate": NotRequired[str],
        "ExpirationInDays": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
        "Filter": NotRequired["AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef"],
        "ID": NotRequired[str],
        "NoncurrentVersionExpirationInDays": NotRequired[int],
        "NoncurrentVersionTransitions": NotRequired[
            Sequence[
                "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef"
            ]
        ],
        "Prefix": NotRequired[str],
        "Status": NotRequired[str],
        "Transitions": NotRequired[
            Sequence["AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef"]
        ],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    {
        "Predicate": NotRequired[
            "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef"
        ],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    {
        "Operands": NotRequired[
            Sequence[
                "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef"
            ]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef"
        ],
        "Type": NotRequired[str],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef"
        ],
        "Type": NotRequired[str],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    {
        "Days": NotRequired[int],
        "StorageClass": NotRequired[str],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    {
        "Date": NotRequired[str],
        "Days": NotRequired[int],
        "StorageClass": NotRequired[str],
    },
)

AwsS3BucketBucketVersioningConfigurationTypeDef = TypedDict(
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    {
        "IsMfaDeleteEnabled": NotRequired[bool],
        "Status": NotRequired[str],
    },
)

AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef",
    {
        "OwnerId": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            "AwsS3BucketServerSideEncryptionConfigurationTypeDef"
        ],
        "BucketLifecycleConfiguration": NotRequired[
            "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef"
        ],
        "PublicAccessBlockConfiguration": NotRequired[
            "AwsS3AccountPublicAccessBlockDetailsTypeDef"
        ],
        "AccessControlList": NotRequired[str],
        "BucketLoggingConfiguration": NotRequired["AwsS3BucketLoggingConfigurationTypeDef"],
        "BucketWebsiteConfiguration": NotRequired["AwsS3BucketWebsiteConfigurationTypeDef"],
        "BucketNotificationConfiguration": NotRequired[
            "AwsS3BucketNotificationConfigurationTypeDef"
        ],
        "BucketVersioningConfiguration": NotRequired[
            "AwsS3BucketBucketVersioningConfigurationTypeDef"
        ],
    },
)

AwsS3BucketLoggingConfigurationTypeDef = TypedDict(
    "AwsS3BucketLoggingConfigurationTypeDef",
    {
        "DestinationBucketName": NotRequired[str],
        "LogFilePrefix": NotRequired[str],
    },
)

AwsS3BucketNotificationConfigurationDetailTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    {
        "Events": NotRequired[Sequence[str]],
        "Filter": NotRequired["AwsS3BucketNotificationConfigurationFilterTypeDef"],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsS3BucketNotificationConfigurationFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    {
        "S3KeyFilter": NotRequired["AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef"],
    },
)

AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    {
        "Name": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType],
        "Value": NotRequired[str],
    },
)

AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    {
        "FilterRules": NotRequired[
            Sequence["AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef"]
        ],
    },
)

AwsS3BucketNotificationConfigurationTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationTypeDef",
    {
        "Configurations": NotRequired[
            Sequence["AwsS3BucketNotificationConfigurationDetailTypeDef"]
        ],
    },
)

AwsS3BucketServerSideEncryptionByDefaultTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": NotRequired[str],
        "KMSMasterKeyID": NotRequired[str],
    },
)

AwsS3BucketServerSideEncryptionConfigurationTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": NotRequired[Sequence["AwsS3BucketServerSideEncryptionRuleTypeDef"]],
    },
)

AwsS3BucketServerSideEncryptionRuleTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": NotRequired[
            "AwsS3BucketServerSideEncryptionByDefaultTypeDef"
        ],
    },
)

AwsS3BucketWebsiteConfigurationRedirectToTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    {
        "Hostname": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)

AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": NotRequired[str],
        "KeyPrefixEquals": NotRequired[str],
    },
)

AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    {
        "Hostname": NotRequired[str],
        "HttpRedirectCode": NotRequired[str],
        "Protocol": NotRequired[str],
        "ReplaceKeyPrefixWith": NotRequired[str],
        "ReplaceKeyWith": NotRequired[str],
    },
)

AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    {
        "Condition": NotRequired["AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef"],
        "Redirect": NotRequired["AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef"],
    },
)

AwsS3BucketWebsiteConfigurationTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": NotRequired[str],
        "IndexDocumentSuffix": NotRequired[str],
        "RedirectAllRequestsTo": NotRequired["AwsS3BucketWebsiteConfigurationRedirectToTypeDef"],
        "RoutingRules": NotRequired[Sequence["AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef"]],
    },
)

AwsS3ObjectDetailsTypeDef = TypedDict(
    "AwsS3ObjectDetailsTypeDef",
    {
        "LastModified": NotRequired[str],
        "ETag": NotRequired[str],
        "VersionId": NotRequired[str],
        "ContentType": NotRequired[str],
        "ServerSideEncryption": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
    },
)

AwsSecretsManagerSecretDetailsTypeDef = TypedDict(
    "AwsSecretsManagerSecretDetailsTypeDef",
    {
        "RotationRules": NotRequired["AwsSecretsManagerSecretRotationRulesTypeDef"],
        "RotationOccurredWithinFrequency": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "RotationEnabled": NotRequired[bool],
        "RotationLambdaArn": NotRequired[str],
        "Deleted": NotRequired[bool],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

AwsSecretsManagerSecretRotationRulesTypeDef = TypedDict(
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    {
        "AutomaticallyAfterDays": NotRequired[int],
    },
)

AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[Sequence["StringFilterTypeDef"]],
        "AwsAccountId": NotRequired[Sequence["StringFilterTypeDef"]],
        "Id": NotRequired[Sequence["StringFilterTypeDef"]],
        "GeneratorId": NotRequired[Sequence["StringFilterTypeDef"]],
        "Region": NotRequired[Sequence["StringFilterTypeDef"]],
        "Type": NotRequired[Sequence["StringFilterTypeDef"]],
        "FirstObservedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "LastObservedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "CreatedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "UpdatedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "SeverityProduct": NotRequired[Sequence["NumberFilterTypeDef"]],
        "SeverityNormalized": NotRequired[Sequence["NumberFilterTypeDef"]],
        "SeverityLabel": NotRequired[Sequence["StringFilterTypeDef"]],
        "Confidence": NotRequired[Sequence["NumberFilterTypeDef"]],
        "Criticality": NotRequired[Sequence["NumberFilterTypeDef"]],
        "Title": NotRequired[Sequence["StringFilterTypeDef"]],
        "Description": NotRequired[Sequence["StringFilterTypeDef"]],
        "RecommendationText": NotRequired[Sequence["StringFilterTypeDef"]],
        "SourceUrl": NotRequired[Sequence["StringFilterTypeDef"]],
        "ProductFields": NotRequired[Sequence["MapFilterTypeDef"]],
        "ProductName": NotRequired[Sequence["StringFilterTypeDef"]],
        "CompanyName": NotRequired[Sequence["StringFilterTypeDef"]],
        "UserDefinedFields": NotRequired[Sequence["MapFilterTypeDef"]],
        "MalwareName": NotRequired[Sequence["StringFilterTypeDef"]],
        "MalwareType": NotRequired[Sequence["StringFilterTypeDef"]],
        "MalwarePath": NotRequired[Sequence["StringFilterTypeDef"]],
        "MalwareState": NotRequired[Sequence["StringFilterTypeDef"]],
        "NetworkDirection": NotRequired[Sequence["StringFilterTypeDef"]],
        "NetworkProtocol": NotRequired[Sequence["StringFilterTypeDef"]],
        "NetworkSourceIpV4": NotRequired[Sequence["IpFilterTypeDef"]],
        "NetworkSourceIpV6": NotRequired[Sequence["IpFilterTypeDef"]],
        "NetworkSourcePort": NotRequired[Sequence["NumberFilterTypeDef"]],
        "NetworkSourceDomain": NotRequired[Sequence["StringFilterTypeDef"]],
        "NetworkSourceMac": NotRequired[Sequence["StringFilterTypeDef"]],
        "NetworkDestinationIpV4": NotRequired[Sequence["IpFilterTypeDef"]],
        "NetworkDestinationIpV6": NotRequired[Sequence["IpFilterTypeDef"]],
        "NetworkDestinationPort": NotRequired[Sequence["NumberFilterTypeDef"]],
        "NetworkDestinationDomain": NotRequired[Sequence["StringFilterTypeDef"]],
        "ProcessName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ProcessPath": NotRequired[Sequence["StringFilterTypeDef"]],
        "ProcessPid": NotRequired[Sequence["NumberFilterTypeDef"]],
        "ProcessParentPid": NotRequired[Sequence["NumberFilterTypeDef"]],
        "ProcessLaunchedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ProcessTerminatedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ThreatIntelIndicatorType": NotRequired[Sequence["StringFilterTypeDef"]],
        "ThreatIntelIndicatorValue": NotRequired[Sequence["StringFilterTypeDef"]],
        "ThreatIntelIndicatorCategory": NotRequired[Sequence["StringFilterTypeDef"]],
        "ThreatIntelIndicatorLastObservedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ThreatIntelIndicatorSource": NotRequired[Sequence["StringFilterTypeDef"]],
        "ThreatIntelIndicatorSourceUrl": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceType": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourcePartition": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceRegion": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceTags": NotRequired[Sequence["MapFilterTypeDef"]],
        "ResourceAwsEc2InstanceType": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsEc2InstanceImageId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsEc2InstanceIpV4Addresses": NotRequired[Sequence["IpFilterTypeDef"]],
        "ResourceAwsEc2InstanceIpV6Addresses": NotRequired[Sequence["IpFilterTypeDef"]],
        "ResourceAwsEc2InstanceKeyName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsEc2InstanceVpcId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsEc2InstanceSubnetId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsEc2InstanceLaunchedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ResourceAwsS3BucketOwnerId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsS3BucketOwnerName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsIamAccessKeyUserName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsIamAccessKeyPrincipalName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsIamAccessKeyStatus": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceAwsIamAccessKeyCreatedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ResourceAwsIamUserUserName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceContainerName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceContainerImageId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceContainerImageName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ResourceContainerLaunchedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ResourceDetailsOther": NotRequired[Sequence["MapFilterTypeDef"]],
        "ComplianceStatus": NotRequired[Sequence["StringFilterTypeDef"]],
        "VerificationState": NotRequired[Sequence["StringFilterTypeDef"]],
        "WorkflowState": NotRequired[Sequence["StringFilterTypeDef"]],
        "WorkflowStatus": NotRequired[Sequence["StringFilterTypeDef"]],
        "RecordState": NotRequired[Sequence["StringFilterTypeDef"]],
        "RelatedFindingsProductArn": NotRequired[Sequence["StringFilterTypeDef"]],
        "RelatedFindingsId": NotRequired[Sequence["StringFilterTypeDef"]],
        "NoteText": NotRequired[Sequence["StringFilterTypeDef"]],
        "NoteUpdatedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "NoteUpdatedBy": NotRequired[Sequence["StringFilterTypeDef"]],
        "Keyword": NotRequired[Sequence["KeywordFilterTypeDef"]],
        "FindingProviderFieldsConfidence": NotRequired[Sequence["NumberFilterTypeDef"]],
        "FindingProviderFieldsCriticality": NotRequired[Sequence["NumberFilterTypeDef"]],
        "FindingProviderFieldsRelatedFindingsId": NotRequired[Sequence["StringFilterTypeDef"]],
        "FindingProviderFieldsRelatedFindingsProductArn": NotRequired[
            Sequence["StringFilterTypeDef"]
        ],
        "FindingProviderFieldsSeverityLabel": NotRequired[Sequence["StringFilterTypeDef"]],
        "FindingProviderFieldsSeverityOriginal": NotRequired[Sequence["StringFilterTypeDef"]],
        "FindingProviderFieldsTypes": NotRequired[Sequence["StringFilterTypeDef"]],
        "Sample": NotRequired[Sequence["BooleanFilterTypeDef"]],
    },
)

AwsSecurityFindingIdentifierTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierTypeDef",
    {
        "Id": str,
        "ProductArn": str,
    },
)

AwsSecurityFindingTypeDef = TypedDict(
    "AwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": Sequence["ResourceTypeDef"],
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Region": NotRequired[str],
        "Types": NotRequired[Sequence[str]],
        "FirstObservedAt": NotRequired[str],
        "LastObservedAt": NotRequired[str],
        "Severity": NotRequired["SeverityTypeDef"],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Remediation": NotRequired["RemediationTypeDef"],
        "SourceUrl": NotRequired[str],
        "ProductFields": NotRequired[Mapping[str, str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Malware": NotRequired[Sequence["MalwareTypeDef"]],
        "Network": NotRequired["NetworkTypeDef"],
        "NetworkPath": NotRequired[Sequence["NetworkPathComponentTypeDef"]],
        "Process": NotRequired["ProcessDetailsTypeDef"],
        "ThreatIntelIndicators": NotRequired[Sequence["ThreatIntelIndicatorTypeDef"]],
        "Compliance": NotRequired["ComplianceTypeDef"],
        "VerificationState": NotRequired[VerificationStateType],
        "WorkflowState": NotRequired[WorkflowStateType],
        "Workflow": NotRequired["WorkflowTypeDef"],
        "RecordState": NotRequired[RecordStateType],
        "RelatedFindings": NotRequired[Sequence["RelatedFindingTypeDef"]],
        "Note": NotRequired["NoteTypeDef"],
        "Vulnerabilities": NotRequired[Sequence["VulnerabilityTypeDef"]],
        "PatchSummary": NotRequired["PatchSummaryTypeDef"],
        "Action": NotRequired["ActionTypeDef"],
        "FindingProviderFields": NotRequired["FindingProviderFieldsTypeDef"],
        "Sample": NotRequired[bool],
    },
)

AwsSnsTopicDetailsTypeDef = TypedDict(
    "AwsSnsTopicDetailsTypeDef",
    {
        "KmsMasterKeyId": NotRequired[str],
        "Subscription": NotRequired[Sequence["AwsSnsTopicSubscriptionTypeDef"]],
        "TopicName": NotRequired[str],
        "Owner": NotRequired[str],
    },
)

AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef",
    {
        "Endpoint": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)

AwsSqsQueueDetailsTypeDef = TypedDict(
    "AwsSqsQueueDetailsTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": NotRequired[int],
        "KmsMasterKeyId": NotRequired[str],
        "QueueName": NotRequired[str],
        "DeadLetterTargetArn": NotRequired[str],
    },
)

AwsSsmComplianceSummaryTypeDef = TypedDict(
    "AwsSsmComplianceSummaryTypeDef",
    {
        "Status": NotRequired[str],
        "CompliantCriticalCount": NotRequired[int],
        "CompliantHighCount": NotRequired[int],
        "CompliantMediumCount": NotRequired[int],
        "ExecutionType": NotRequired[str],
        "NonCompliantCriticalCount": NotRequired[int],
        "CompliantInformationalCount": NotRequired[int],
        "NonCompliantInformationalCount": NotRequired[int],
        "CompliantUnspecifiedCount": NotRequired[int],
        "NonCompliantLowCount": NotRequired[int],
        "NonCompliantHighCount": NotRequired[int],
        "CompliantLowCount": NotRequired[int],
        "ComplianceType": NotRequired[str],
        "PatchBaselineId": NotRequired[str],
        "OverallSeverity": NotRequired[str],
        "NonCompliantMediumCount": NotRequired[int],
        "NonCompliantUnspecifiedCount": NotRequired[int],
        "PatchGroup": NotRequired[str],
    },
)

AwsSsmPatchComplianceDetailsTypeDef = TypedDict(
    "AwsSsmPatchComplianceDetailsTypeDef",
    {
        "Patch": NotRequired["AwsSsmPatchTypeDef"],
    },
)

AwsSsmPatchTypeDef = TypedDict(
    "AwsSsmPatchTypeDef",
    {
        "ComplianceSummary": NotRequired["AwsSsmComplianceSummaryTypeDef"],
    },
)

AwsWafRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[Sequence["AwsWafRateBasedRuleMatchPredicateTypeDef"]],
    },
)

AwsWafRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)

AwsWafRegionalRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[
            Sequence["AwsWafRegionalRateBasedRuleMatchPredicateTypeDef"]
        ],
    },
)

AwsWafRegionalRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)

AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "Rules": NotRequired[Sequence["AwsWafWebAclRuleTypeDef"]],
        "WebAclId": NotRequired[str],
    },
)

AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": NotRequired["WafActionTypeDef"],
        "ExcludedRules": NotRequired[Sequence["WafExcludedRuleTypeDef"]],
        "OverrideAction": NotRequired["WafOverrideActionTypeDef"],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AwsXrayEncryptionConfigDetailsTypeDef = TypedDict(
    "AwsXrayEncryptionConfigDetailsTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[str],
        "Type": NotRequired[str],
    },
)

BatchDisableStandardsRequestRequestTypeDef = TypedDict(
    "BatchDisableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": Sequence[str],
    },
)

BatchDisableStandardsResponseTypeDef = TypedDict(
    "BatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List["StandardsSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEnableStandardsRequestRequestTypeDef = TypedDict(
    "BatchEnableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionRequests": Sequence["StandardsSubscriptionRequestTypeDef"],
    },
)

BatchEnableStandardsResponseTypeDef = TypedDict(
    "BatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List["StandardsSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchImportFindingsRequestRequestTypeDef = TypedDict(
    "BatchImportFindingsRequestRequestTypeDef",
    {
        "Findings": Sequence["AwsSecurityFindingTypeDef"],
    },
)

BatchImportFindingsResponseTypeDef = TypedDict(
    "BatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List["ImportFindingsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "BatchUpdateFindingsRequestRequestTypeDef",
    {
        "FindingIdentifiers": Sequence["AwsSecurityFindingIdentifierTypeDef"],
        "Note": NotRequired["NoteUpdateTypeDef"],
        "Severity": NotRequired["SeverityUpdateTypeDef"],
        "VerificationState": NotRequired[VerificationStateType],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Types": NotRequired[Sequence[str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Workflow": NotRequired["WorkflowUpdateTypeDef"],
        "RelatedFindings": NotRequired[Sequence["RelatedFindingTypeDef"]],
    },
)

BatchUpdateFindingsResponseTypeDef = TypedDict(
    "BatchUpdateFindingsResponseTypeDef",
    {
        "ProcessedFindings": List["AwsSecurityFindingIdentifierTypeDef"],
        "UnprocessedFindings": List["BatchUpdateFindingsUnprocessedFindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateFindingsUnprocessedFindingTypeDef = TypedDict(
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    {
        "FindingIdentifier": "AwsSecurityFindingIdentifierTypeDef",
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

BooleanFilterTypeDef = TypedDict(
    "BooleanFilterTypeDef",
    {
        "Value": NotRequired[bool],
    },
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "Column": NotRequired[int],
        "Row": NotRequired[int],
        "ColumnName": NotRequired[str],
        "CellReference": NotRequired[str],
    },
)

CidrBlockAssociationTypeDef = TypedDict(
    "CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[str],
    },
)

CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": NotRequired[str],
    },
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "MimeType": NotRequired[str],
        "SizeClassified": NotRequired[int],
        "AdditionalOccurrences": NotRequired[bool],
        "Status": NotRequired["ClassificationStatusTypeDef"],
        "SensitiveData": NotRequired[Sequence["SensitiveDataResultTypeDef"]],
        "CustomDataIdentifiers": NotRequired["CustomDataIdentifiersResultTypeDef"],
    },
)

ClassificationStatusTypeDef = TypedDict(
    "ClassificationStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Reason": NotRequired[str],
    },
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": NotRequired[ComplianceStatusType],
        "RelatedRequirements": NotRequired[Sequence[str]],
        "StatusReasons": NotRequired[Sequence["StatusReasonTypeDef"]],
    },
)

ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageName": NotRequired[str],
        "LaunchedAt": NotRequired[str],
    },
)

CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
    },
)

CreateActionTargetRequestRequestTypeDef = TypedDict(
    "CreateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Id": str,
    },
)

CreateActionTargetResponseTypeDef = TypedDict(
    "CreateActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "CreateFindingAggregatorRequestRequestTypeDef",
    {
        "RegionLinkingMode": str,
        "Regions": NotRequired[Sequence[str]],
    },
)

CreateFindingAggregatorResponseTypeDef = TypedDict(
    "CreateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInsightRequestRequestTypeDef = TypedDict(
    "CreateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "GroupByAttribute": str,
    },
)

CreateInsightResponseTypeDef = TypedDict(
    "CreateInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "AccountDetails": Sequence["AccountDetailsTypeDef"],
    },
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDataIdentifiersDetectionsTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Occurrences": NotRequired["OccurrencesTypeDef"],
    },
)

CustomDataIdentifiersResultTypeDef = TypedDict(
    "CustomDataIdentifiersResultTypeDef",
    {
        "Detections": NotRequired[Sequence["CustomDataIdentifiersDetectionsTypeDef"]],
        "TotalCount": NotRequired[int],
    },
)

CvssTypeDef = TypedDict(
    "CvssTypeDef",
    {
        "Version": NotRequired[str],
        "BaseScore": NotRequired[float],
        "BaseVector": NotRequired[str],
        "Source": NotRequired[str],
        "Adjustments": NotRequired[Sequence["AdjustmentTypeDef"]],
    },
)

DataClassificationDetailsTypeDef = TypedDict(
    "DataClassificationDetailsTypeDef",
    {
        "DetailedResultsLocation": NotRequired[str],
        "Result": NotRequired["ClassificationResultTypeDef"],
    },
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "Start": NotRequired[str],
        "End": NotRequired[str],
        "DateRange": NotRequired["DateRangeTypeDef"],
    },
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "Value": NotRequired[int],
        "Unit": NotRequired[Literal["DAYS"]],
    },
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteActionTargetRequestRequestTypeDef = TypedDict(
    "DeleteActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)

DeleteActionTargetResponseTypeDef = TypedDict(
    "DeleteActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFindingAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)

DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)

DeleteInsightResponseTypeDef = TypedDict(
    "DeleteInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeActionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeActionTargetsRequestRequestTypeDef",
    {
        "ActionTargetArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeActionTargetsResponseTypeDef = TypedDict(
    "DescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List["ActionTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubArn": NotRequired[str],
    },
)

DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubArn": str,
        "SubscribedAt": str,
        "AutoEnableControls": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductsRequestRequestTypeDef = TypedDict(
    "DescribeProductsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ProductArn": NotRequired[str],
    },
)

DescribeProductsResponseTypeDef = TypedDict(
    "DescribeProductsResponseTypeDef",
    {
        "Products": List["ProductTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsControlsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeStandardsControlsResponseTypeDef = TypedDict(
    "DescribeStandardsControlsResponseTypeDef",
    {
        "Controls": List["StandardsControlTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStandardsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeStandardsResponseTypeDef = TypedDict(
    "DescribeStandardsResponseTypeDef",
    {
        "Standards": List["StandardTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "DisableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductSubscriptionArn": str,
    },
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)

EnableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "EnableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductArn": str,
    },
)

EnableImportFindingsForProductResponseTypeDef = TypedDict(
    "EnableImportFindingsForProductResponseTypeDef",
    {
        "ProductSubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

EnableSecurityHubRequestRequestTypeDef = TypedDict(
    "EnableSecurityHubRequestRequestTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
        "EnableDefaultStandards": NotRequired[bool],
    },
)

FindingAggregatorTypeDef = TypedDict(
    "FindingAggregatorTypeDef",
    {
        "FindingAggregatorArn": NotRequired[str],
    },
)

FindingProviderFieldsTypeDef = TypedDict(
    "FindingProviderFieldsTypeDef",
    {
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "RelatedFindings": NotRequired[Sequence["RelatedFindingTypeDef"]],
        "Severity": NotRequired["FindingProviderSeverityTypeDef"],
        "Types": NotRequired[Sequence[str]],
    },
)

FindingProviderSeverityTypeDef = TypedDict(
    "FindingProviderSeverityTypeDef",
    {
        "Label": NotRequired[SeverityLabelType],
        "Original": NotRequired[str],
    },
)

FirewallPolicyDetailsTypeDef = TypedDict(
    "FirewallPolicyDetailsTypeDef",
    {
        "StatefulRuleGroupReferences": NotRequired[
            Sequence["FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef"]
        ],
        "StatelessCustomActions": NotRequired[
            Sequence["FirewallPolicyStatelessCustomActionsDetailsTypeDef"]
        ],
        "StatelessDefaultActions": NotRequired[Sequence[str]],
        "StatelessFragmentDefaultActions": NotRequired[Sequence[str]],
        "StatelessRuleGroupReferences": NotRequired[
            Sequence["FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef"]
        ],
    },
)

FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)

FirewallPolicyStatelessCustomActionsDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": NotRequired["StatelessCustomActionDefinitionTypeDef"],
        "ActionName": NotRequired[str],
    },
)

FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    {
        "Priority": NotRequired[int],
        "ResourceArn": NotRequired[str],
    },
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lon": NotRequired[float],
        "Lat": NotRequired[float],
    },
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnabledStandardsRequestRequestTypeDef = TypedDict(
    "GetEnabledStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List["StandardsSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingAggregatorRequestRequestTypeDef = TypedDict(
    "GetFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)

GetFindingAggregatorResponseTypeDef = TypedDict(
    "GetFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "Filters": NotRequired["AwsSecurityFindingFiltersTypeDef"],
        "SortCriteria": NotRequired[Sequence["SortCriterionTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List["AwsSecurityFindingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightResultsRequestRequestTypeDef = TypedDict(
    "GetInsightResultsRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)

GetInsightResultsResponseTypeDef = TypedDict(
    "GetInsightResultsResponseTypeDef",
    {
        "InsightResults": "InsightResultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightsRequestRequestTypeDef = TypedDict(
    "GetInsightsRequestRequestTypeDef",
    {
        "InsightArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "Insights": List["InsightTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)

ImportFindingsErrorTypeDef = TypedDict(
    "ImportFindingsErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

InsightResultValueTypeDef = TypedDict(
    "InsightResultValueTypeDef",
    {
        "GroupByAttributeValue": str,
        "Count": int,
    },
)

InsightResultsTypeDef = TypedDict(
    "InsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List["InsightResultValueTypeDef"],
    },
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "GroupByAttribute": str,
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "InvitedAt": NotRequired[datetime],
        "MemberStatus": NotRequired[str],
    },
)

InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpFilterTypeDef = TypedDict(
    "IpFilterTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)

IpOrganizationDetailsTypeDef = TypedDict(
    "IpOrganizationDetailsTypeDef",
    {
        "Asn": NotRequired[int],
        "AsnOrg": NotRequired[str],
        "Isp": NotRequired[str],
        "Org": NotRequired[str],
    },
)

Ipv6CidrBlockAssociationTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[str],
    },
)

KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Value": NotRequired[str],
    },
)

ListEnabledProductsForImportRequestRequestTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {
        "ProductSubscriptions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingAggregatorsRequestRequestTypeDef = TypedDict(
    "ListFindingAggregatorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFindingAggregatorsResponseTypeDef = TypedDict(
    "ListFindingAggregatorsResponseTypeDef",
    {
        "FindingAggregators": List["FindingAggregatorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "OnlyAssociated": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountTypeDef"],
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

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": NotRequired[str],
        "Reason": NotRequired[str],
    },
)

MalwareTypeDef = TypedDict(
    "MalwareTypeDef",
    {
        "Name": str,
        "Type": NotRequired[MalwareTypeType],
        "Path": NotRequired[str],
        "State": NotRequired[MalwareStateType],
    },
)

MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Comparison": NotRequired[MapFilterComparisonType],
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": NotRequired[str],
        "Email": NotRequired[str],
        "MasterId": NotRequired[str],
        "AdministratorId": NotRequired[str],
        "MemberStatus": NotRequired[str],
        "InvitedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": NotRequired[str],
        "RemoteIpDetails": NotRequired["ActionRemoteIpDetailsTypeDef"],
        "RemotePortDetails": NotRequired["ActionRemotePortDetailsTypeDef"],
        "LocalPortDetails": NotRequired["ActionLocalPortDetailsTypeDef"],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)

NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired["NetworkPathComponentDetailsTypeDef"],
        "Source": NotRequired["NetworkPathComponentDetailsTypeDef"],
    },
)

NetworkPathComponentDetailsTypeDef = TypedDict(
    "NetworkPathComponentDetailsTypeDef",
    {
        "Address": NotRequired[Sequence[str]],
        "PortRanges": NotRequired[Sequence["PortRangeTypeDef"]],
    },
)

NetworkPathComponentTypeDef = TypedDict(
    "NetworkPathComponentTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentType": NotRequired[str],
        "Egress": NotRequired["NetworkHeaderTypeDef"],
        "Ingress": NotRequired["NetworkHeaderTypeDef"],
    },
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": NotRequired[NetworkDirectionType],
        "Protocol": NotRequired[str],
        "OpenPortRange": NotRequired["PortRangeTypeDef"],
        "SourceIpV4": NotRequired[str],
        "SourceIpV6": NotRequired[str],
        "SourcePort": NotRequired[int],
        "SourceDomain": NotRequired[str],
        "SourceMac": NotRequired[str],
        "DestinationIpV4": NotRequired[str],
        "DestinationIpV6": NotRequired[str],
        "DestinationPort": NotRequired[int],
        "DestinationDomain": NotRequired[str],
    },
)

NoteTypeDef = TypedDict(
    "NoteTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)

NoteUpdateTypeDef = TypedDict(
    "NoteUpdateTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "Gte": NotRequired[float],
        "Lte": NotRequired[float],
        "Eq": NotRequired[float],
    },
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "LineRanges": NotRequired[Sequence["RangeTypeDef"]],
        "OffsetRanges": NotRequired[Sequence["RangeTypeDef"]],
        "Pages": NotRequired[Sequence["PageTypeDef"]],
        "Records": NotRequired[Sequence["RecordTypeDef"]],
        "Cells": NotRequired[Sequence["CellTypeDef"]],
    },
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageNumber": NotRequired[int],
        "LineRange": NotRequired["RangeTypeDef"],
        "OffsetRange": NotRequired["RangeTypeDef"],
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

PatchSummaryTypeDef = TypedDict(
    "PatchSummaryTypeDef",
    {
        "Id": str,
        "InstalledCount": NotRequired[int],
        "MissingCount": NotRequired[int],
        "FailedCount": NotRequired[int],
        "InstalledOtherCount": NotRequired[int],
        "InstalledRejectedCount": NotRequired[int],
        "InstalledPendingReboot": NotRequired[int],
        "OperationStartTime": NotRequired[str],
        "OperationEndTime": NotRequired[str],
        "RebootOption": NotRequired[str],
        "Operation": NotRequired[str],
    },
)

PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "PortProbeDetails": NotRequired[Sequence["PortProbeDetailTypeDef"]],
        "Blocked": NotRequired[bool],
    },
)

PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": NotRequired["ActionLocalPortDetailsTypeDef"],
        "LocalIpDetails": NotRequired["ActionLocalIpDetailsTypeDef"],
        "RemoteIpDetails": NotRequired["ActionRemoteIpDetailsTypeDef"],
    },
)

PortRangeFromToTypeDef = TypedDict(
    "PortRangeFromToTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "Begin": NotRequired[int],
        "End": NotRequired[int],
    },
)

ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Path": NotRequired[str],
        "Pid": NotRequired[int],
        "ParentPid": NotRequired[int],
        "LaunchedAt": NotRequired[str],
        "TerminatedAt": NotRequired[str],
    },
)

ProductTypeDef = TypedDict(
    "ProductTypeDef",
    {
        "ProductArn": str,
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Description": NotRequired[str],
        "Categories": NotRequired[List[str]],
        "IntegrationTypes": NotRequired[List[IntegrationTypeType]],
        "MarketplaceUrl": NotRequired[str],
        "ActivationUrl": NotRequired[str],
        "ProductSubscriptionResourcePolicy": NotRequired[str],
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Start": NotRequired[int],
        "End": NotRequired[int],
        "StartColumn": NotRequired[int],
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Text": NotRequired[str],
        "Url": NotRequired[str],
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "JsonPath": NotRequired[str],
        "RecordIndex": NotRequired[int],
    },
)

RelatedFindingTypeDef = TypedDict(
    "RelatedFindingTypeDef",
    {
        "ProductArn": str,
        "Id": str,
    },
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "Recommendation": NotRequired["RecommendationTypeDef"],
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[
            "AwsAutoScalingAutoScalingGroupDetailsTypeDef"
        ],
        "AwsCodeBuildProject": NotRequired["AwsCodeBuildProjectDetailsTypeDef"],
        "AwsCloudFrontDistribution": NotRequired["AwsCloudFrontDistributionDetailsTypeDef"],
        "AwsEc2Instance": NotRequired["AwsEc2InstanceDetailsTypeDef"],
        "AwsEc2NetworkInterface": NotRequired["AwsEc2NetworkInterfaceDetailsTypeDef"],
        "AwsEc2SecurityGroup": NotRequired["AwsEc2SecurityGroupDetailsTypeDef"],
        "AwsEc2Volume": NotRequired["AwsEc2VolumeDetailsTypeDef"],
        "AwsEc2Vpc": NotRequired["AwsEc2VpcDetailsTypeDef"],
        "AwsEc2Eip": NotRequired["AwsEc2EipDetailsTypeDef"],
        "AwsEc2Subnet": NotRequired["AwsEc2SubnetDetailsTypeDef"],
        "AwsEc2NetworkAcl": NotRequired["AwsEc2NetworkAclDetailsTypeDef"],
        "AwsElbv2LoadBalancer": NotRequired["AwsElbv2LoadBalancerDetailsTypeDef"],
        "AwsElasticBeanstalkEnvironment": NotRequired[
            "AwsElasticBeanstalkEnvironmentDetailsTypeDef"
        ],
        "AwsElasticsearchDomain": NotRequired["AwsElasticsearchDomainDetailsTypeDef"],
        "AwsS3Bucket": NotRequired["AwsS3BucketDetailsTypeDef"],
        "AwsS3AccountPublicAccessBlock": NotRequired["AwsS3AccountPublicAccessBlockDetailsTypeDef"],
        "AwsS3Object": NotRequired["AwsS3ObjectDetailsTypeDef"],
        "AwsSecretsManagerSecret": NotRequired["AwsSecretsManagerSecretDetailsTypeDef"],
        "AwsIamAccessKey": NotRequired["AwsIamAccessKeyDetailsTypeDef"],
        "AwsIamUser": NotRequired["AwsIamUserDetailsTypeDef"],
        "AwsIamPolicy": NotRequired["AwsIamPolicyDetailsTypeDef"],
        "AwsApiGatewayV2Stage": NotRequired["AwsApiGatewayV2StageDetailsTypeDef"],
        "AwsApiGatewayV2Api": NotRequired["AwsApiGatewayV2ApiDetailsTypeDef"],
        "AwsDynamoDbTable": NotRequired["AwsDynamoDbTableDetailsTypeDef"],
        "AwsApiGatewayStage": NotRequired["AwsApiGatewayStageDetailsTypeDef"],
        "AwsApiGatewayRestApi": NotRequired["AwsApiGatewayRestApiDetailsTypeDef"],
        "AwsCloudTrailTrail": NotRequired["AwsCloudTrailTrailDetailsTypeDef"],
        "AwsSsmPatchCompliance": NotRequired["AwsSsmPatchComplianceDetailsTypeDef"],
        "AwsCertificateManagerCertificate": NotRequired[
            "AwsCertificateManagerCertificateDetailsTypeDef"
        ],
        "AwsRedshiftCluster": NotRequired["AwsRedshiftClusterDetailsTypeDef"],
        "AwsElbLoadBalancer": NotRequired["AwsElbLoadBalancerDetailsTypeDef"],
        "AwsIamGroup": NotRequired["AwsIamGroupDetailsTypeDef"],
        "AwsIamRole": NotRequired["AwsIamRoleDetailsTypeDef"],
        "AwsKmsKey": NotRequired["AwsKmsKeyDetailsTypeDef"],
        "AwsLambdaFunction": NotRequired["AwsLambdaFunctionDetailsTypeDef"],
        "AwsLambdaLayerVersion": NotRequired["AwsLambdaLayerVersionDetailsTypeDef"],
        "AwsRdsDbInstance": NotRequired["AwsRdsDbInstanceDetailsTypeDef"],
        "AwsSnsTopic": NotRequired["AwsSnsTopicDetailsTypeDef"],
        "AwsSqsQueue": NotRequired["AwsSqsQueueDetailsTypeDef"],
        "AwsWafWebAcl": NotRequired["AwsWafWebAclDetailsTypeDef"],
        "AwsRdsDbSnapshot": NotRequired["AwsRdsDbSnapshotDetailsTypeDef"],
        "AwsRdsDbClusterSnapshot": NotRequired["AwsRdsDbClusterSnapshotDetailsTypeDef"],
        "AwsRdsDbCluster": NotRequired["AwsRdsDbClusterDetailsTypeDef"],
        "AwsEcsCluster": NotRequired["AwsEcsClusterDetailsTypeDef"],
        "AwsEcsTaskDefinition": NotRequired["AwsEcsTaskDefinitionDetailsTypeDef"],
        "Container": NotRequired["ContainerDetailsTypeDef"],
        "Other": NotRequired[Mapping[str, str]],
        "AwsRdsEventSubscription": NotRequired["AwsRdsEventSubscriptionDetailsTypeDef"],
        "AwsEcsService": NotRequired["AwsEcsServiceDetailsTypeDef"],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            "AwsAutoScalingLaunchConfigurationDetailsTypeDef"
        ],
        "AwsEc2VpnConnection": NotRequired["AwsEc2VpnConnectionDetailsTypeDef"],
        "AwsEcrContainerImage": NotRequired["AwsEcrContainerImageDetailsTypeDef"],
        "AwsOpenSearchServiceDomain": NotRequired["AwsOpenSearchServiceDomainDetailsTypeDef"],
        "AwsEc2VpcEndpointService": NotRequired["AwsEc2VpcEndpointServiceDetailsTypeDef"],
        "AwsXrayEncryptionConfig": NotRequired["AwsXrayEncryptionConfigDetailsTypeDef"],
        "AwsWafRateBasedRule": NotRequired["AwsWafRateBasedRuleDetailsTypeDef"],
        "AwsWafRegionalRateBasedRule": NotRequired["AwsWafRegionalRateBasedRuleDetailsTypeDef"],
        "AwsEcrRepository": NotRequired["AwsEcrRepositoryDetailsTypeDef"],
        "AwsEksCluster": NotRequired["AwsEksClusterDetailsTypeDef"],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            "AwsNetworkFirewallFirewallPolicyDetailsTypeDef"
        ],
        "AwsNetworkFirewallFirewall": NotRequired["AwsNetworkFirewallFirewallDetailsTypeDef"],
        "AwsNetworkFirewallRuleGroup": NotRequired["AwsNetworkFirewallRuleGroupDetailsTypeDef"],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "DataClassification": NotRequired["DataClassificationDetailsTypeDef"],
        "Details": NotRequired["ResourceDetailsTypeDef"],
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

ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "AccountId": NotRequired[str],
        "ProcessingResult": NotRequired[str],
    },
)

RuleGroupDetailsTypeDef = TypedDict(
    "RuleGroupDetailsTypeDef",
    {
        "RuleVariables": NotRequired["RuleGroupVariablesTypeDef"],
        "RulesSource": NotRequired["RuleGroupSourceTypeDef"],
    },
)

RuleGroupSourceCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": NotRequired["StatelessCustomActionDefinitionTypeDef"],
        "ActionName": NotRequired[str],
    },
)

RuleGroupSourceListDetailsTypeDef = TypedDict(
    "RuleGroupSourceListDetailsTypeDef",
    {
        "GeneratedRulesType": NotRequired[str],
        "TargetTypes": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence[str]],
    },
)

RuleGroupSourceStatefulRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    {
        "Action": NotRequired[str],
        "Header": NotRequired["RuleGroupSourceStatefulRulesHeaderDetailsTypeDef"],
        "RuleOptions": NotRequired[Sequence["RuleGroupSourceStatefulRulesOptionsDetailsTypeDef"]],
    },
)

RuleGroupSourceStatefulRulesHeaderDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    {
        "Destination": NotRequired[str],
        "DestinationPort": NotRequired[str],
        "Direction": NotRequired[str],
        "Protocol": NotRequired[str],
        "Source": NotRequired[str],
        "SourcePort": NotRequired[str],
    },
)

RuleGroupSourceStatefulRulesOptionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    {
        "Keyword": NotRequired[str],
        "Settings": NotRequired[Sequence[str]],
    },
)

RuleGroupSourceStatelessRuleDefinitionTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    {
        "Actions": NotRequired[Sequence[str]],
        "MatchAttributes": NotRequired["RuleGroupSourceStatelessRuleMatchAttributesTypeDef"],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    {
        "AddressDefinition": NotRequired[str],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    {
        "AddressDefinition": NotRequired[str],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    {
        "Flags": NotRequired[Sequence[str]],
        "Masks": NotRequired[Sequence[str]],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    {
        "DestinationPorts": NotRequired[
            Sequence["RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef"]
        ],
        "Destinations": NotRequired[
            Sequence["RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef"]
        ],
        "Protocols": NotRequired[Sequence[int]],
        "SourcePorts": NotRequired[
            Sequence["RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef"]
        ],
        "Sources": NotRequired[
            Sequence["RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef"]
        ],
        "TcpFlags": NotRequired[
            Sequence["RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef"]
        ],
    },
)

RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    {
        "CustomActions": NotRequired[Sequence["RuleGroupSourceCustomActionsDetailsTypeDef"]],
        "StatelessRules": NotRequired[Sequence["RuleGroupSourceStatelessRulesDetailsTypeDef"]],
    },
)

RuleGroupSourceStatelessRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    {
        "Priority": NotRequired[int],
        "RuleDefinition": NotRequired["RuleGroupSourceStatelessRuleDefinitionTypeDef"],
    },
)

RuleGroupSourceTypeDef = TypedDict(
    "RuleGroupSourceTypeDef",
    {
        "RulesSourceList": NotRequired["RuleGroupSourceListDetailsTypeDef"],
        "RulesString": NotRequired[str],
        "StatefulRules": NotRequired[Sequence["RuleGroupSourceStatefulRulesDetailsTypeDef"]],
        "StatelessRulesAndCustomActions": NotRequired[
            "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef"
        ],
    },
)

RuleGroupVariablesIpSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)

RuleGroupVariablesPortSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)

RuleGroupVariablesTypeDef = TypedDict(
    "RuleGroupVariablesTypeDef",
    {
        "IpSets": NotRequired["RuleGroupVariablesIpSetsDetailsTypeDef"],
        "PortSets": NotRequired["RuleGroupVariablesPortSetsDetailsTypeDef"],
    },
)

SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired["OccurrencesTypeDef"],
    },
)

SensitiveDataResultTypeDef = TypedDict(
    "SensitiveDataResultTypeDef",
    {
        "Category": NotRequired[str],
        "Detections": NotRequired[Sequence["SensitiveDataDetectionsTypeDef"]],
        "TotalCount": NotRequired[int],
    },
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "Product": NotRequired[float],
        "Label": NotRequired[SeverityLabelType],
        "Normalized": NotRequired[int],
        "Original": NotRequired[str],
    },
)

SeverityUpdateTypeDef = TypedDict(
    "SeverityUpdateTypeDef",
    {
        "Normalized": NotRequired[int],
        "Product": NotRequired[float],
        "Label": NotRequired[SeverityLabelType],
    },
)

SoftwarePackageTypeDef = TypedDict(
    "SoftwarePackageTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Epoch": NotRequired[str],
        "Release": NotRequired[str],
        "Architecture": NotRequired[str],
        "PackageManager": NotRequired[str],
        "FilePath": NotRequired[str],
    },
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "Field": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)

StandardTypeDef = TypedDict(
    "StandardTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EnabledByDefault": NotRequired[bool],
    },
)

StandardsControlTypeDef = TypedDict(
    "StandardsControlTypeDef",
    {
        "StandardsControlArn": NotRequired[str],
        "ControlStatus": NotRequired[ControlStatusType],
        "DisabledReason": NotRequired[str],
        "ControlStatusUpdatedAt": NotRequired[datetime],
        "ControlId": NotRequired[str],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "RemediationUrl": NotRequired[str],
        "SeverityRating": NotRequired[SeverityRatingType],
        "RelatedRequirements": NotRequired[List[str]],
    },
)

StandardsStatusReasonTypeDef = TypedDict(
    "StandardsStatusReasonTypeDef",
    {
        "StatusReasonCode": StatusReasonCodeType,
    },
)

StandardsSubscriptionRequestTypeDef = TypedDict(
    "StandardsSubscriptionRequestTypeDef",
    {
        "StandardsArn": str,
        "StandardsInput": NotRequired[Mapping[str, str]],
    },
)

StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": StandardsStatusType,
        "StandardsStatusReason": NotRequired["StandardsStatusReasonTypeDef"],
    },
)

StatelessCustomActionDefinitionTypeDef = TypedDict(
    "StatelessCustomActionDefinitionTypeDef",
    {
        "PublishMetricAction": NotRequired["StatelessCustomPublishMetricActionTypeDef"],
    },
)

StatelessCustomPublishMetricActionDimensionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    {
        "Value": NotRequired[str],
    },
)

StatelessCustomPublishMetricActionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionTypeDef",
    {
        "Dimensions": NotRequired[Sequence["StatelessCustomPublishMetricActionDimensionTypeDef"]],
    },
)

StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "ReasonCode": str,
        "Description": NotRequired[str],
    },
)

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": NotRequired[str],
        "Comparison": NotRequired[StringFilterComparisonType],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": NotRequired[ThreatIntelIndicatorTypeType],
        "Value": NotRequired[str],
        "Category": NotRequired[ThreatIntelIndicatorCategoryType],
        "LastObservedAt": NotRequired[str],
        "Source": NotRequired[str],
        "SourceUrl": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateActionTargetRequestRequestTypeDef = TypedDict(
    "UpdateActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "UpdateFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
        "RegionLinkingMode": str,
        "Regions": NotRequired[Sequence[str]],
    },
)

UpdateFindingAggregatorResponseTypeDef = TypedDict(
    "UpdateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFindingsRequestRequestTypeDef = TypedDict(
    "UpdateFindingsRequestRequestTypeDef",
    {
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "Note": NotRequired["NoteUpdateTypeDef"],
        "RecordState": NotRequired[RecordStateType],
    },
)

UpdateInsightRequestRequestTypeDef = TypedDict(
    "UpdateInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
        "Name": NotRequired[str],
        "Filters": NotRequired["AwsSecurityFindingFiltersTypeDef"],
        "GroupByAttribute": NotRequired[str],
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
    },
)

UpdateSecurityHubConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    {
        "AutoEnableControls": NotRequired[bool],
    },
)

UpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "UpdateStandardsControlRequestRequestTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": NotRequired[ControlStatusType],
        "DisabledReason": NotRequired[str],
    },
)

VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "Id": str,
        "VulnerablePackages": NotRequired[Sequence["SoftwarePackageTypeDef"]],
        "Cvss": NotRequired[Sequence["CvssTypeDef"]],
        "RelatedVulnerabilities": NotRequired[Sequence[str]],
        "Vendor": NotRequired["VulnerabilityVendorTypeDef"],
        "ReferenceUrls": NotRequired[Sequence[str]],
    },
)

VulnerabilityVendorTypeDef = TypedDict(
    "VulnerabilityVendorTypeDef",
    {
        "Name": str,
        "Url": NotRequired[str],
        "VendorSeverity": NotRequired[str],
        "VendorCreatedAt": NotRequired[str],
        "VendorUpdatedAt": NotRequired[str],
    },
)

WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)

WafExcludedRuleTypeDef = TypedDict(
    "WafExcludedRuleTypeDef",
    {
        "RuleId": NotRequired[str],
    },
)

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Status": NotRequired[WorkflowStatusType],
    },
)

WorkflowUpdateTypeDef = TypedDict(
    "WorkflowUpdateTypeDef",
    {
        "Status": NotRequired[WorkflowStatusType],
    },
)
