"""
Type annotations for ec2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ec2.type_defs import AcceleratorCountRequestTypeDef

    data: AcceleratorCountRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Optional, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AcceleratorManufacturerType,
    AcceleratorNameType,
    AcceleratorTypeType,
    AccountAttributeNameType,
    ActivityStatusType,
    AddressFamilyType,
    AffinityType,
    AllocationStateType,
    AllocationStrategyType,
    AllowsMultipleInstanceTypesType,
    AnalysisStatusType,
    ApplianceModeSupportValueType,
    ArchitectureTypeType,
    ArchitectureValuesType,
    AssociationStatusCodeType,
    AttachmentStatusType,
    AutoAcceptSharedAssociationsValueType,
    AutoAcceptSharedAttachmentsValueType,
    AutoPlacementType,
    AvailabilityZoneOptInStatusType,
    AvailabilityZoneStateType,
    BareMetalType,
    BatchStateType,
    BgpStatusType,
    BootModeTypeType,
    BootModeValuesType,
    BundleTaskStateType,
    BurstablePerformanceType,
    ByoipCidrStateType,
    CancelBatchErrorCodeType,
    CancelSpotInstanceRequestStateType,
    CapacityReservationFleetStateType,
    CapacityReservationInstancePlatformType,
    CapacityReservationPreferenceType,
    CapacityReservationStateType,
    CapacityReservationTenancyType,
    CarrierGatewayStateType,
    ClientCertificateRevocationListStatusCodeType,
    ClientVpnAuthenticationTypeType,
    ClientVpnAuthorizationRuleStatusCodeType,
    ClientVpnConnectionStatusCodeType,
    ClientVpnEndpointAttributeStatusCodeType,
    ClientVpnEndpointStatusCodeType,
    ClientVpnRouteStatusCodeType,
    ConnectionNotificationStateType,
    ConnectivityTypeType,
    ConversionTaskStateType,
    CpuManufacturerType,
    DatafeedSubscriptionStateType,
    DefaultRouteTableAssociationValueType,
    DefaultRouteTablePropagationValueType,
    DefaultTargetCapacityTypeType,
    DeleteFleetErrorCodeType,
    DeleteQueuedReservedInstancesErrorCodeType,
    DestinationFileFormatType,
    DeviceTypeType,
    DiskImageFormatType,
    DiskTypeType,
    DnsNameStateType,
    DnsSupportValueType,
    DomainTypeType,
    EbsEncryptionSupportType,
    EbsNvmeSupportType,
    EbsOptimizedSupportType,
    ElasticGpuStatusType,
    EnaSupportType,
    EndDateTypeType,
    EphemeralNvmeSupportType,
    EventCodeType,
    EventTypeType,
    ExcessCapacityTerminationPolicyType,
    ExportEnvironmentType,
    ExportTaskStateType,
    FastLaunchStateCodeType,
    FastSnapshotRestoreStateCodeType,
    FindingsFoundType,
    FleetActivityStatusType,
    FleetEventTypeType,
    FleetExcessCapacityTerminationPolicyType,
    FleetOnDemandAllocationStrategyType,
    FleetReplacementStrategyType,
    FleetStateCodeType,
    FleetTypeType,
    FlowLogsResourceTypeType,
    FpgaImageAttributeNameType,
    FpgaImageStateCodeType,
    GatewayAssociationStateType,
    HostnameTypeType,
    HostRecoveryType,
    HostTenancyType,
    HttpTokensStateType,
    HypervisorTypeType,
    IamInstanceProfileAssociationStateType,
    Igmpv2SupportValueType,
    ImageAttributeNameType,
    ImageStateType,
    ImageTypeValuesType,
    InstanceAttributeNameType,
    InstanceEventWindowStateType,
    InstanceGenerationType,
    InstanceHealthStatusType,
    InstanceInterruptionBehaviorType,
    InstanceLifecycleType,
    InstanceLifecycleTypeType,
    InstanceMatchCriteriaType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataOptionsStateType,
    InstanceMetadataProtocolStateType,
    InstanceMetadataTagsStateType,
    InstanceStateNameType,
    InstanceStorageEncryptionSupportType,
    InstanceTypeHypervisorType,
    InstanceTypeType,
    InterfacePermissionTypeType,
    InterfaceProtocolTypeType,
    IpamAddressHistoryResourceTypeType,
    IpamComplianceStatusType,
    IpamManagementStateType,
    IpamOverlapStatusType,
    IpamPoolAllocationResourceTypeType,
    IpamPoolCidrStateType,
    IpamPoolStateType,
    IpamResourceTypeType,
    IpamScopeStateType,
    IpamScopeTypeType,
    IpamStateType,
    Ipv6SupportValueType,
    KeyTypeType,
    LaunchTemplateErrorCodeType,
    LaunchTemplateHttpTokensStateType,
    LaunchTemplateInstanceMetadataEndpointStateType,
    LaunchTemplateInstanceMetadataOptionsStateType,
    LaunchTemplateInstanceMetadataProtocolIpv6Type,
    LaunchTemplateInstanceMetadataTagsStateType,
    ListingStateType,
    ListingStatusType,
    LocalGatewayRouteStateType,
    LocalGatewayRouteTypeType,
    LocalStorageType,
    LocalStorageTypeType,
    LocationTypeType,
    LogDestinationTypeType,
    MembershipTypeType,
    ModifyAvailabilityZoneOptInStatusType,
    MonitoringStateType,
    MoveStatusType,
    MulticastSupportValueType,
    NatGatewayStateType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    NetworkInterfacePermissionStateCodeType,
    NetworkInterfaceStatusType,
    NetworkInterfaceTypeType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    OnDemandAllocationStrategyType,
    OperationTypeType,
    PartitionLoadFrequencyType,
    PaymentOptionType,
    PlacementGroupStateType,
    PlacementGroupStrategyType,
    PlacementStrategyType,
    PrefixListStateType,
    PrincipalTypeType,
    ProductCodeValuesType,
    ProtocolType,
    ReplacementStrategyType,
    ReplaceRootVolumeTaskStateType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    ReservationStateType,
    ReservedInstanceStateType,
    ResourceTypeType,
    RIProductDescriptionType,
    RootDeviceTypeType,
    RouteOriginType,
    RouteStateType,
    RouteTableAssociationStateCodeType,
    RuleActionType,
    SelfServicePortalType,
    ServiceStateType,
    ServiceTypeType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotStateType,
    SpotAllocationStrategyType,
    SpotInstanceInterruptionBehaviorType,
    SpotInstanceStateType,
    SpotInstanceTypeType,
    StateType,
    StaticSourcesSupportValueType,
    StatusType,
    StatusTypeType,
    StorageTierType,
    SubnetCidrBlockStateCodeType,
    SubnetCidrReservationTypeType,
    SubnetStateType,
    SummaryStatusType,
    TargetCapacityUnitTypeType,
    TelemetryStatusType,
    TenancyType,
    TieringOperationStatusType,
    TrafficDirectionType,
    TrafficMirrorFilterRuleFieldType,
    TrafficMirrorRuleActionType,
    TrafficMirrorSessionFieldType,
    TrafficMirrorTargetTypeType,
    TrafficTypeType,
    TransitGatewayAssociationStateType,
    TransitGatewayAttachmentResourceTypeType,
    TransitGatewayAttachmentStateType,
    TransitGatewayConnectPeerStateType,
    TransitGatewayMulitcastDomainAssociationStateType,
    TransitGatewayMulticastDomainStateType,
    TransitGatewayPrefixListReferenceStateType,
    TransitGatewayPropagationStateType,
    TransitGatewayRouteStateType,
    TransitGatewayRouteTableStateType,
    TransitGatewayRouteTypeType,
    TransitGatewayStateType,
    TransportProtocolType,
    TunnelInsideIpVersionType,
    UnlimitedSupportedInstanceFamilyType,
    UnsuccessfulInstanceCreditSpecificationErrorCodeType,
    UsageClassTypeType,
    VirtualizationTypeType,
    VolumeAttachmentStateType,
    VolumeAttributeNameType,
    VolumeModificationStateType,
    VolumeStateType,
    VolumeStatusInfoStatusType,
    VolumeStatusNameType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcCidrBlockStateCodeType,
    VpcEndpointTypeType,
    VpcPeeringConnectionStateReasonCodeType,
    VpcStateType,
    VpnEcmpSupportValueType,
    VpnStateType,
    WeekDayType,
    scopeType,
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
    "AcceleratorCountRequestTypeDef",
    "AcceleratorCountTypeDef",
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    "AcceleratorTotalMemoryMiBTypeDef",
    "AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    "AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    "AcceptVpcEndpointConnectionsRequestRequestTypeDef",
    "AcceptVpcEndpointConnectionsResultTypeDef",
    "AcceptVpcPeeringConnectionRequestRequestTypeDef",
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef",
    "AcceptVpcPeeringConnectionResultTypeDef",
    "AccessScopeAnalysisFindingTypeDef",
    "AccessScopePathRequestTypeDef",
    "AccessScopePathTypeDef",
    "AccountAttributeTypeDef",
    "AccountAttributeValueTypeDef",
    "ActiveInstanceTypeDef",
    "AddIpamOperatingRegionTypeDef",
    "AddPrefixListEntryTypeDef",
    "AddressAttributeTypeDef",
    "AddressTypeDef",
    "AdvertiseByoipCidrRequestRequestTypeDef",
    "AdvertiseByoipCidrResultTypeDef",
    "AllocateAddressRequestRequestTypeDef",
    "AllocateAddressResultTypeDef",
    "AllocateHostsRequestRequestTypeDef",
    "AllocateHostsResultTypeDef",
    "AllocateIpamPoolCidrRequestRequestTypeDef",
    "AllocateIpamPoolCidrResultTypeDef",
    "AllowedPrincipalTypeDef",
    "AlternatePathHintTypeDef",
    "AnalysisAclRuleTypeDef",
    "AnalysisComponentTypeDef",
    "AnalysisLoadBalancerListenerTypeDef",
    "AnalysisLoadBalancerTargetTypeDef",
    "AnalysisPacketHeaderTypeDef",
    "AnalysisRouteTableRouteTypeDef",
    "AnalysisSecurityGroupRuleTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    "AssignIpv6AddressesRequestRequestTypeDef",
    "AssignIpv6AddressesResultTypeDef",
    "AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef",
    "AssignPrivateIpAddressesRequestRequestTypeDef",
    "AssignPrivateIpAddressesResultTypeDef",
    "AssignedPrivateIpAddressTypeDef",
    "AssociateAddressRequestClassicAddressAssociateTypeDef",
    "AssociateAddressRequestRequestTypeDef",
    "AssociateAddressRequestVpcAddressAssociateTypeDef",
    "AssociateAddressResultTypeDef",
    "AssociateClientVpnTargetNetworkRequestRequestTypeDef",
    "AssociateClientVpnTargetNetworkResultTypeDef",
    "AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef",
    "AssociateDhcpOptionsRequestRequestTypeDef",
    "AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef",
    "AssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    "AssociateIamInstanceProfileRequestRequestTypeDef",
    "AssociateIamInstanceProfileResultTypeDef",
    "AssociateInstanceEventWindowRequestRequestTypeDef",
    "AssociateInstanceEventWindowResultTypeDef",
    "AssociateRouteTableRequestRequestTypeDef",
    "AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef",
    "AssociateRouteTableResultTypeDef",
    "AssociateSubnetCidrBlockRequestRequestTypeDef",
    "AssociateSubnetCidrBlockResultTypeDef",
    "AssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    "AssociateTransitGatewayRouteTableRequestRequestTypeDef",
    "AssociateTransitGatewayRouteTableResultTypeDef",
    "AssociateTrunkInterfaceRequestRequestTypeDef",
    "AssociateTrunkInterfaceResultTypeDef",
    "AssociateVpcCidrBlockRequestRequestTypeDef",
    "AssociateVpcCidrBlockResultTypeDef",
    "AssociatedRoleTypeDef",
    "AssociatedTargetNetworkTypeDef",
    "AssociationStatusTypeDef",
    "AthenaIntegrationTypeDef",
    "AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef",
    "AttachClassicLinkVpcRequestRequestTypeDef",
    "AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef",
    "AttachClassicLinkVpcResultTypeDef",
    "AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef",
    "AttachInternetGatewayRequestRequestTypeDef",
    "AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef",
    "AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef",
    "AttachNetworkInterfaceRequestRequestTypeDef",
    "AttachNetworkInterfaceResultTypeDef",
    "AttachVolumeRequestInstanceAttachVolumeTypeDef",
    "AttachVolumeRequestRequestTypeDef",
    "AttachVolumeRequestVolumeAttachToInstanceTypeDef",
    "AttachVpnGatewayRequestRequestTypeDef",
    "AttachVpnGatewayResultTypeDef",
    "AttributeBooleanValueTypeDef",
    "AttributeValueTypeDef",
    "AuthorizationRuleTypeDef",
    "AuthorizeClientVpnIngressRequestRequestTypeDef",
    "AuthorizeClientVpnIngressResultTypeDef",
    "AuthorizeSecurityGroupEgressRequestRequestTypeDef",
    "AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef",
    "AuthorizeSecurityGroupEgressResultTypeDef",
    "AuthorizeSecurityGroupIngressRequestRequestTypeDef",
    "AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef",
    "AuthorizeSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneMessageTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableCapacityTypeDef",
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    "BaselineEbsBandwidthMbpsTypeDef",
    "BlobAttributeValueTypeDef",
    "BlockDeviceMappingTypeDef",
    "BundleInstanceRequestRequestTypeDef",
    "BundleInstanceResultTypeDef",
    "BundleTaskErrorTypeDef",
    "BundleTaskTypeDef",
    "ByoipCidrTypeDef",
    "CancelBundleTaskRequestRequestTypeDef",
    "CancelBundleTaskResultTypeDef",
    "CancelCapacityReservationFleetErrorTypeDef",
    "CancelCapacityReservationFleetsRequestRequestTypeDef",
    "CancelCapacityReservationFleetsResultTypeDef",
    "CancelCapacityReservationRequestRequestTypeDef",
    "CancelCapacityReservationResultTypeDef",
    "CancelConversionRequestRequestTypeDef",
    "CancelExportTaskRequestRequestTypeDef",
    "CancelImportTaskRequestRequestTypeDef",
    "CancelImportTaskResultTypeDef",
    "CancelReservedInstancesListingRequestRequestTypeDef",
    "CancelReservedInstancesListingResultTypeDef",
    "CancelSpotFleetRequestsErrorItemTypeDef",
    "CancelSpotFleetRequestsErrorTypeDef",
    "CancelSpotFleetRequestsRequestRequestTypeDef",
    "CancelSpotFleetRequestsResponseTypeDef",
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    "CancelSpotInstanceRequestsRequestRequestTypeDef",
    "CancelSpotInstanceRequestsResultTypeDef",
    "CancelledSpotInstanceRequestTypeDef",
    "CapacityReservationFleetCancellationStateTypeDef",
    "CapacityReservationFleetTypeDef",
    "CapacityReservationGroupTypeDef",
    "CapacityReservationOptionsRequestTypeDef",
    "CapacityReservationOptionsTypeDef",
    "CapacityReservationSpecificationResponseResponseMetadataTypeDef",
    "CapacityReservationSpecificationResponseTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CapacityReservationTargetResponseTypeDef",
    "CapacityReservationTargetTypeDef",
    "CapacityReservationTypeDef",
    "CarrierGatewayTypeDef",
    "CertificateAuthenticationRequestTypeDef",
    "CertificateAuthenticationTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CidrBlockTypeDef",
    "ClassicLinkDnsSupportTypeDef",
    "ClassicLinkInstanceTypeDef",
    "ClassicLoadBalancerTypeDef",
    "ClassicLoadBalancersConfigTypeDef",
    "ClientCertificateRevocationListStatusTypeDef",
    "ClientConnectOptionsTypeDef",
    "ClientConnectResponseOptionsTypeDef",
    "ClientDataTypeDef",
    "ClientLoginBannerOptionsTypeDef",
    "ClientLoginBannerResponseOptionsTypeDef",
    "ClientVpnAuthenticationRequestTypeDef",
    "ClientVpnAuthenticationTypeDef",
    "ClientVpnAuthorizationRuleStatusTypeDef",
    "ClientVpnConnectionStatusTypeDef",
    "ClientVpnConnectionTypeDef",
    "ClientVpnEndpointAttributeStatusTypeDef",
    "ClientVpnEndpointStatusTypeDef",
    "ClientVpnEndpointTypeDef",
    "ClientVpnRouteStatusTypeDef",
    "ClientVpnRouteTypeDef",
    "CoipAddressUsageTypeDef",
    "CoipPoolTypeDef",
    "ConfirmProductInstanceRequestRequestTypeDef",
    "ConfirmProductInstanceResultTypeDef",
    "ConnectionLogOptionsTypeDef",
    "ConnectionLogResponseOptionsTypeDef",
    "ConnectionNotificationTypeDef",
    "ConversionTaskTypeDef",
    "CopyFpgaImageRequestRequestTypeDef",
    "CopyFpgaImageResultTypeDef",
    "CopyImageRequestRequestTypeDef",
    "CopyImageResultTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotRequestSnapshotCopyTypeDef",
    "CopySnapshotResultTypeDef",
    "CpuOptionsRequestTypeDef",
    "CpuOptionsResponseMetadataTypeDef",
    "CpuOptionsTypeDef",
    "CreateCapacityReservationFleetRequestRequestTypeDef",
    "CreateCapacityReservationFleetResultTypeDef",
    "CreateCapacityReservationRequestRequestTypeDef",
    "CreateCapacityReservationResultTypeDef",
    "CreateCarrierGatewayRequestRequestTypeDef",
    "CreateCarrierGatewayResultTypeDef",
    "CreateClientVpnEndpointRequestRequestTypeDef",
    "CreateClientVpnEndpointResultTypeDef",
    "CreateClientVpnRouteRequestRequestTypeDef",
    "CreateClientVpnRouteResultTypeDef",
    "CreateCustomerGatewayRequestRequestTypeDef",
    "CreateCustomerGatewayResultTypeDef",
    "CreateDefaultSubnetRequestRequestTypeDef",
    "CreateDefaultSubnetResultTypeDef",
    "CreateDefaultVpcRequestRequestTypeDef",
    "CreateDefaultVpcResultTypeDef",
    "CreateDhcpOptionsRequestRequestTypeDef",
    "CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef",
    "CreateDhcpOptionsResultTypeDef",
    "CreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    "CreateFleetErrorTypeDef",
    "CreateFleetInstanceTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResultTypeDef",
    "CreateFlowLogsRequestRequestTypeDef",
    "CreateFlowLogsResultTypeDef",
    "CreateFpgaImageRequestRequestTypeDef",
    "CreateFpgaImageResultTypeDef",
    "CreateImageRequestInstanceCreateImageTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateImageResultTypeDef",
    "CreateInstanceEventWindowRequestRequestTypeDef",
    "CreateInstanceEventWindowResultTypeDef",
    "CreateInstanceExportTaskRequestRequestTypeDef",
    "CreateInstanceExportTaskResultTypeDef",
    "CreateInternetGatewayRequestRequestTypeDef",
    "CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef",
    "CreateInternetGatewayResultTypeDef",
    "CreateIpamPoolRequestRequestTypeDef",
    "CreateIpamPoolResultTypeDef",
    "CreateIpamRequestRequestTypeDef",
    "CreateIpamResultTypeDef",
    "CreateIpamScopeRequestRequestTypeDef",
    "CreateIpamScopeResultTypeDef",
    "CreateKeyPairRequestRequestTypeDef",
    "CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef",
    "CreateLaunchTemplateRequestRequestTypeDef",
    "CreateLaunchTemplateResultTypeDef",
    "CreateLaunchTemplateVersionRequestRequestTypeDef",
    "CreateLaunchTemplateVersionResultTypeDef",
    "CreateLocalGatewayRouteRequestRequestTypeDef",
    "CreateLocalGatewayRouteResultTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "CreateManagedPrefixListRequestRequestTypeDef",
    "CreateManagedPrefixListResultTypeDef",
    "CreateNatGatewayRequestRequestTypeDef",
    "CreateNatGatewayResultTypeDef",
    "CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef",
    "CreateNetworkAclEntryRequestRequestTypeDef",
    "CreateNetworkAclRequestRequestTypeDef",
    "CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef",
    "CreateNetworkAclRequestVpcCreateNetworkAclTypeDef",
    "CreateNetworkAclResultTypeDef",
    "CreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    "CreateNetworkInsightsAccessScopeResultTypeDef",
    "CreateNetworkInsightsPathRequestRequestTypeDef",
    "CreateNetworkInsightsPathResultTypeDef",
    "CreateNetworkInterfacePermissionRequestRequestTypeDef",
    "CreateNetworkInterfacePermissionResultTypeDef",
    "CreateNetworkInterfaceRequestRequestTypeDef",
    "CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef",
    "CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef",
    "CreateNetworkInterfaceResultTypeDef",
    "CreatePlacementGroupRequestRequestTypeDef",
    "CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef",
    "CreatePlacementGroupResultTypeDef",
    "CreatePublicIpv4PoolRequestRequestTypeDef",
    "CreatePublicIpv4PoolResultTypeDef",
    "CreateReplaceRootVolumeTaskRequestRequestTypeDef",
    "CreateReplaceRootVolumeTaskResultTypeDef",
    "CreateReservedInstancesListingRequestRequestTypeDef",
    "CreateReservedInstancesListingResultTypeDef",
    "CreateRestoreImageTaskRequestRequestTypeDef",
    "CreateRestoreImageTaskResultTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteRequestRouteTableCreateRouteTypeDef",
    "CreateRouteResultTypeDef",
    "CreateRouteTableRequestRequestTypeDef",
    "CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef",
    "CreateRouteTableRequestVpcCreateRouteTableTypeDef",
    "CreateRouteTableResultTypeDef",
    "CreateSecurityGroupRequestRequestTypeDef",
    "CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef",
    "CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef",
    "CreateSecurityGroupResultTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef",
    "CreateSnapshotRequestVolumeCreateSnapshotTypeDef",
    "CreateSnapshotsRequestRequestTypeDef",
    "CreateSnapshotsResultTypeDef",
    "CreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    "CreateStoreImageTaskRequestRequestTypeDef",
    "CreateStoreImageTaskResultTypeDef",
    "CreateSubnetCidrReservationRequestRequestTypeDef",
    "CreateSubnetCidrReservationResultTypeDef",
    "CreateSubnetRequestRequestTypeDef",
    "CreateSubnetRequestServiceResourceCreateSubnetTypeDef",
    "CreateSubnetRequestVpcCreateSubnetTypeDef",
    "CreateSubnetResultTypeDef",
    "CreateTagsRequestDhcpOptionsCreateTagsTypeDef",
    "CreateTagsRequestImageCreateTagsTypeDef",
    "CreateTagsRequestInstanceCreateTagsTypeDef",
    "CreateTagsRequestInternetGatewayCreateTagsTypeDef",
    "CreateTagsRequestNetworkAclCreateTagsTypeDef",
    "CreateTagsRequestNetworkInterfaceCreateTagsTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateTagsRequestRouteTableCreateTagsTypeDef",
    "CreateTagsRequestSecurityGroupCreateTagsTypeDef",
    "CreateTagsRequestServiceResourceCreateTagsTypeDef",
    "CreateTagsRequestSnapshotCreateTagsTypeDef",
    "CreateTagsRequestSubnetCreateTagsTypeDef",
    "CreateTagsRequestVolumeCreateTagsTypeDef",
    "CreateTagsRequestVpcCreateTagsTypeDef",
    "CreateTrafficMirrorFilterRequestRequestTypeDef",
    "CreateTrafficMirrorFilterResultTypeDef",
    "CreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    "CreateTrafficMirrorSessionRequestRequestTypeDef",
    "CreateTrafficMirrorSessionResultTypeDef",
    "CreateTrafficMirrorTargetRequestRequestTypeDef",
    "CreateTrafficMirrorTargetResultTypeDef",
    "CreateTransitGatewayConnectPeerRequestRequestTypeDef",
    "CreateTransitGatewayConnectPeerResultTypeDef",
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    "CreateTransitGatewayConnectRequestRequestTypeDef",
    "CreateTransitGatewayConnectResultTypeDef",
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    "CreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    "CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    "CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    "CreateTransitGatewayRequestRequestTypeDef",
    "CreateTransitGatewayResultTypeDef",
    "CreateTransitGatewayRouteRequestRequestTypeDef",
    "CreateTransitGatewayRouteResultTypeDef",
    "CreateTransitGatewayRouteTableRequestRequestTypeDef",
    "CreateTransitGatewayRouteTableResultTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    "CreateVolumePermissionModificationsTypeDef",
    "CreateVolumePermissionTypeDef",
    "CreateVolumeRequestRequestTypeDef",
    "CreateVolumeRequestServiceResourceCreateVolumeTypeDef",
    "CreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    "CreateVpcEndpointRequestRequestTypeDef",
    "CreateVpcEndpointResultTypeDef",
    "CreateVpcEndpointServiceConfigurationRequestRequestTypeDef",
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    "CreateVpcPeeringConnectionRequestRequestTypeDef",
    "CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef",
    "CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef",
    "CreateVpcPeeringConnectionResultTypeDef",
    "CreateVpcRequestRequestTypeDef",
    "CreateVpcRequestServiceResourceCreateVpcTypeDef",
    "CreateVpcResultTypeDef",
    "CreateVpnConnectionRequestRequestTypeDef",
    "CreateVpnConnectionResultTypeDef",
    "CreateVpnConnectionRouteRequestRequestTypeDef",
    "CreateVpnGatewayRequestRequestTypeDef",
    "CreateVpnGatewayResultTypeDef",
    "CreditSpecificationRequestTypeDef",
    "CreditSpecificationTypeDef",
    "CustomerGatewayTypeDef",
    "DeleteCarrierGatewayRequestRequestTypeDef",
    "DeleteCarrierGatewayResultTypeDef",
    "DeleteClientVpnEndpointRequestRequestTypeDef",
    "DeleteClientVpnEndpointResultTypeDef",
    "DeleteClientVpnRouteRequestRequestTypeDef",
    "DeleteClientVpnRouteResultTypeDef",
    "DeleteCustomerGatewayRequestRequestTypeDef",
    "DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef",
    "DeleteDhcpOptionsRequestRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    "DeleteFleetErrorItemTypeDef",
    "DeleteFleetErrorTypeDef",
    "DeleteFleetSuccessItemTypeDef",
    "DeleteFleetsRequestRequestTypeDef",
    "DeleteFleetsResultTypeDef",
    "DeleteFlowLogsRequestRequestTypeDef",
    "DeleteFlowLogsResultTypeDef",
    "DeleteFpgaImageRequestRequestTypeDef",
    "DeleteFpgaImageResultTypeDef",
    "DeleteInstanceEventWindowRequestRequestTypeDef",
    "DeleteInstanceEventWindowResultTypeDef",
    "DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef",
    "DeleteInternetGatewayRequestRequestTypeDef",
    "DeleteIpamPoolRequestRequestTypeDef",
    "DeleteIpamPoolResultTypeDef",
    "DeleteIpamRequestRequestTypeDef",
    "DeleteIpamResultTypeDef",
    "DeleteIpamScopeRequestRequestTypeDef",
    "DeleteIpamScopeResultTypeDef",
    "DeleteKeyPairRequestKeyPairDeleteTypeDef",
    "DeleteKeyPairRequestKeyPairInfoDeleteTypeDef",
    "DeleteKeyPairRequestRequestTypeDef",
    "DeleteLaunchTemplateRequestRequestTypeDef",
    "DeleteLaunchTemplateResultTypeDef",
    "DeleteLaunchTemplateVersionsRequestRequestTypeDef",
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    "DeleteLaunchTemplateVersionsResultTypeDef",
    "DeleteLocalGatewayRouteRequestRequestTypeDef",
    "DeleteLocalGatewayRouteResultTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "DeleteManagedPrefixListRequestRequestTypeDef",
    "DeleteManagedPrefixListResultTypeDef",
    "DeleteNatGatewayRequestRequestTypeDef",
    "DeleteNatGatewayResultTypeDef",
    "DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef",
    "DeleteNetworkAclEntryRequestRequestTypeDef",
    "DeleteNetworkAclRequestNetworkAclDeleteTypeDef",
    "DeleteNetworkAclRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    "DeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeResultTypeDef",
    "DeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    "DeleteNetworkInsightsPathRequestRequestTypeDef",
    "DeleteNetworkInsightsPathResultTypeDef",
    "DeleteNetworkInterfacePermissionRequestRequestTypeDef",
    "DeleteNetworkInterfacePermissionResultTypeDef",
    "DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef",
    "DeleteNetworkInterfaceRequestRequestTypeDef",
    "DeletePlacementGroupRequestPlacementGroupDeleteTypeDef",
    "DeletePlacementGroupRequestRequestTypeDef",
    "DeletePublicIpv4PoolRequestRequestTypeDef",
    "DeletePublicIpv4PoolResultTypeDef",
    "DeleteQueuedReservedInstancesErrorTypeDef",
    "DeleteQueuedReservedInstancesRequestRequestTypeDef",
    "DeleteQueuedReservedInstancesResultTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteRequestRouteDeleteTypeDef",
    "DeleteRouteTableRequestRequestTypeDef",
    "DeleteRouteTableRequestRouteTableDeleteTypeDef",
    "DeleteSecurityGroupRequestRequestTypeDef",
    "DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotRequestSnapshotDeleteTypeDef",
    "DeleteSpotDatafeedSubscriptionRequestRequestTypeDef",
    "DeleteSubnetCidrReservationRequestRequestTypeDef",
    "DeleteSubnetCidrReservationResultTypeDef",
    "DeleteSubnetRequestRequestTypeDef",
    "DeleteSubnetRequestSubnetDeleteTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteTagsRequestTagDeleteTypeDef",
    "DeleteTrafficMirrorFilterRequestRequestTypeDef",
    "DeleteTrafficMirrorFilterResultTypeDef",
    "DeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    "DeleteTrafficMirrorSessionRequestRequestTypeDef",
    "DeleteTrafficMirrorSessionResultTypeDef",
    "DeleteTrafficMirrorTargetRequestRequestTypeDef",
    "DeleteTrafficMirrorTargetResultTypeDef",
    "DeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    "DeleteTransitGatewayConnectRequestRequestTypeDef",
    "DeleteTransitGatewayConnectResultTypeDef",
    "DeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    "DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    "DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    "DeleteTransitGatewayRequestRequestTypeDef",
    "DeleteTransitGatewayResultTypeDef",
    "DeleteTransitGatewayRouteRequestRequestTypeDef",
    "DeleteTransitGatewayRouteResultTypeDef",
    "DeleteTransitGatewayRouteTableRequestRequestTypeDef",
    "DeleteTransitGatewayRouteTableResultTypeDef",
    "DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    "DeleteVolumeRequestRequestTypeDef",
    "DeleteVolumeRequestVolumeDeleteTypeDef",
    "DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    "DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    "DeleteVpcEndpointsRequestRequestTypeDef",
    "DeleteVpcEndpointsResultTypeDef",
    "DeleteVpcPeeringConnectionRequestRequestTypeDef",
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef",
    "DeleteVpcPeeringConnectionResultTypeDef",
    "DeleteVpcRequestRequestTypeDef",
    "DeleteVpcRequestVpcDeleteTypeDef",
    "DeleteVpnConnectionRequestRequestTypeDef",
    "DeleteVpnConnectionRouteRequestRequestTypeDef",
    "DeleteVpnGatewayRequestRequestTypeDef",
    "DeprovisionByoipCidrRequestRequestTypeDef",
    "DeprovisionByoipCidrResultTypeDef",
    "DeprovisionIpamPoolCidrRequestRequestTypeDef",
    "DeprovisionIpamPoolCidrResultTypeDef",
    "DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    "DeprovisionPublicIpv4PoolCidrResultTypeDef",
    "DeregisterImageRequestImageDeregisterTypeDef",
    "DeregisterImageRequestRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    "DeregisterInstanceTagAttributeRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "DescribeAccountAttributesRequestRequestTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAddressesAttributeRequestRequestTypeDef",
    "DescribeAddressesAttributeResultTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeAggregateIdFormatRequestRequestTypeDef",
    "DescribeAggregateIdFormatResultTypeDef",
    "DescribeAvailabilityZonesRequestRequestTypeDef",
    "DescribeAvailabilityZonesResultTypeDef",
    "DescribeBundleTasksRequestRequestTypeDef",
    "DescribeBundleTasksResultTypeDef",
    "DescribeByoipCidrsRequestRequestTypeDef",
    "DescribeByoipCidrsResultTypeDef",
    "DescribeCapacityReservationFleetsRequestRequestTypeDef",
    "DescribeCapacityReservationFleetsResultTypeDef",
    "DescribeCapacityReservationsRequestRequestTypeDef",
    "DescribeCapacityReservationsResultTypeDef",
    "DescribeCarrierGatewaysRequestRequestTypeDef",
    "DescribeCarrierGatewaysResultTypeDef",
    "DescribeClassicLinkInstancesRequestRequestTypeDef",
    "DescribeClassicLinkInstancesResultTypeDef",
    "DescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    "DescribeClientVpnConnectionsRequestRequestTypeDef",
    "DescribeClientVpnConnectionsResultTypeDef",
    "DescribeClientVpnEndpointsRequestRequestTypeDef",
    "DescribeClientVpnEndpointsResultTypeDef",
    "DescribeClientVpnRoutesRequestRequestTypeDef",
    "DescribeClientVpnRoutesResultTypeDef",
    "DescribeClientVpnTargetNetworksRequestRequestTypeDef",
    "DescribeClientVpnTargetNetworksResultTypeDef",
    "DescribeCoipPoolsRequestRequestTypeDef",
    "DescribeCoipPoolsResultTypeDef",
    "DescribeConversionTasksRequestRequestTypeDef",
    "DescribeConversionTasksResultTypeDef",
    "DescribeCustomerGatewaysRequestRequestTypeDef",
    "DescribeCustomerGatewaysResultTypeDef",
    "DescribeDhcpOptionsRequestRequestTypeDef",
    "DescribeDhcpOptionsResultTypeDef",
    "DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef",
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    "DescribeElasticGpusRequestRequestTypeDef",
    "DescribeElasticGpusResultTypeDef",
    "DescribeExportImageTasksRequestRequestTypeDef",
    "DescribeExportImageTasksResultTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeExportTasksResultTypeDef",
    "DescribeFastLaunchImagesRequestRequestTypeDef",
    "DescribeFastLaunchImagesResultTypeDef",
    "DescribeFastLaunchImagesSuccessItemTypeDef",
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    "DescribeFastSnapshotRestoresRequestRequestTypeDef",
    "DescribeFastSnapshotRestoresResultTypeDef",
    "DescribeFleetErrorTypeDef",
    "DescribeFleetHistoryRequestRequestTypeDef",
    "DescribeFleetHistoryResultTypeDef",
    "DescribeFleetInstancesRequestRequestTypeDef",
    "DescribeFleetInstancesResultTypeDef",
    "DescribeFleetsInstancesTypeDef",
    "DescribeFleetsRequestRequestTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeFlowLogsRequestRequestTypeDef",
    "DescribeFlowLogsResultTypeDef",
    "DescribeFpgaImageAttributeRequestRequestTypeDef",
    "DescribeFpgaImageAttributeResultTypeDef",
    "DescribeFpgaImagesRequestRequestTypeDef",
    "DescribeFpgaImagesResultTypeDef",
    "DescribeHostReservationOfferingsRequestRequestTypeDef",
    "DescribeHostReservationOfferingsResultTypeDef",
    "DescribeHostReservationsRequestRequestTypeDef",
    "DescribeHostReservationsResultTypeDef",
    "DescribeHostsRequestRequestTypeDef",
    "DescribeHostsResultTypeDef",
    "DescribeIamInstanceProfileAssociationsRequestRequestTypeDef",
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    "DescribeIdFormatRequestRequestTypeDef",
    "DescribeIdFormatResultTypeDef",
    "DescribeIdentityIdFormatRequestRequestTypeDef",
    "DescribeIdentityIdFormatResultTypeDef",
    "DescribeImageAttributeRequestImageDescribeAttributeTypeDef",
    "DescribeImageAttributeRequestRequestTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeImportImageTasksRequestRequestTypeDef",
    "DescribeImportImageTasksResultTypeDef",
    "DescribeImportSnapshotTasksRequestRequestTypeDef",
    "DescribeImportSnapshotTasksResultTypeDef",
    "DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "DescribeInstanceCreditSpecificationsRequestRequestTypeDef",
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    "DescribeInstanceEventNotificationAttributesRequestRequestTypeDef",
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    "DescribeInstanceEventWindowsRequestRequestTypeDef",
    "DescribeInstanceEventWindowsResultTypeDef",
    "DescribeInstanceStatusRequestRequestTypeDef",
    "DescribeInstanceStatusResultTypeDef",
    "DescribeInstanceTypeOfferingsRequestRequestTypeDef",
    "DescribeInstanceTypeOfferingsResultTypeDef",
    "DescribeInstanceTypesRequestRequestTypeDef",
    "DescribeInstanceTypesResultTypeDef",
    "DescribeInstancesRequestRequestTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeInternetGatewaysRequestRequestTypeDef",
    "DescribeInternetGatewaysResultTypeDef",
    "DescribeIpamPoolsRequestRequestTypeDef",
    "DescribeIpamPoolsResultTypeDef",
    "DescribeIpamScopesRequestRequestTypeDef",
    "DescribeIpamScopesResultTypeDef",
    "DescribeIpamsRequestRequestTypeDef",
    "DescribeIpamsResultTypeDef",
    "DescribeIpv6PoolsRequestRequestTypeDef",
    "DescribeIpv6PoolsResultTypeDef",
    "DescribeKeyPairsRequestRequestTypeDef",
    "DescribeKeyPairsResultTypeDef",
    "DescribeLaunchTemplateVersionsRequestRequestTypeDef",
    "DescribeLaunchTemplateVersionsResultTypeDef",
    "DescribeLaunchTemplatesRequestRequestTypeDef",
    "DescribeLaunchTemplatesResultTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTablesRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    "DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    "DescribeLocalGatewaysRequestRequestTypeDef",
    "DescribeLocalGatewaysResultTypeDef",
    "DescribeManagedPrefixListsRequestRequestTypeDef",
    "DescribeManagedPrefixListsResultTypeDef",
    "DescribeMovingAddressesRequestRequestTypeDef",
    "DescribeMovingAddressesResultTypeDef",
    "DescribeNatGatewaysRequestRequestTypeDef",
    "DescribeNatGatewaysResultTypeDef",
    "DescribeNetworkAclsRequestRequestTypeDef",
    "DescribeNetworkAclsResultTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    "DescribeNetworkInsightsAccessScopesRequestRequestTypeDef",
    "DescribeNetworkInsightsAccessScopesResultTypeDef",
    "DescribeNetworkInsightsAnalysesRequestRequestTypeDef",
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    "DescribeNetworkInsightsPathsRequestRequestTypeDef",
    "DescribeNetworkInsightsPathsResultTypeDef",
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef",
    "DescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    "DescribeNetworkInterfacePermissionsRequestRequestTypeDef",
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    "DescribeNetworkInterfacesRequestRequestTypeDef",
    "DescribeNetworkInterfacesResultTypeDef",
    "DescribePlacementGroupsRequestRequestTypeDef",
    "DescribePlacementGroupsResultTypeDef",
    "DescribePrefixListsRequestRequestTypeDef",
    "DescribePrefixListsResultTypeDef",
    "DescribePrincipalIdFormatRequestRequestTypeDef",
    "DescribePrincipalIdFormatResultTypeDef",
    "DescribePublicIpv4PoolsRequestRequestTypeDef",
    "DescribePublicIpv4PoolsResultTypeDef",
    "DescribeRegionsRequestRequestTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeReplaceRootVolumeTasksRequestRequestTypeDef",
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    "DescribeReservedInstancesListingsRequestRequestTypeDef",
    "DescribeReservedInstancesListingsResultTypeDef",
    "DescribeReservedInstancesModificationsRequestRequestTypeDef",
    "DescribeReservedInstancesModificationsResultTypeDef",
    "DescribeReservedInstancesOfferingsRequestRequestTypeDef",
    "DescribeReservedInstancesOfferingsResultTypeDef",
    "DescribeReservedInstancesRequestRequestTypeDef",
    "DescribeReservedInstancesResultTypeDef",
    "DescribeRouteTablesRequestRequestTypeDef",
    "DescribeRouteTablesResultTypeDef",
    "DescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    "DescribeScheduledInstancesRequestRequestTypeDef",
    "DescribeScheduledInstancesResultTypeDef",
    "DescribeSecurityGroupReferencesRequestRequestTypeDef",
    "DescribeSecurityGroupReferencesResultTypeDef",
    "DescribeSecurityGroupRulesRequestRequestTypeDef",
    "DescribeSecurityGroupRulesResultTypeDef",
    "DescribeSecurityGroupsRequestRequestTypeDef",
    "DescribeSecurityGroupsResultTypeDef",
    "DescribeSnapshotAttributeRequestRequestTypeDef",
    "DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef",
    "DescribeSnapshotAttributeResultTypeDef",
    "DescribeSnapshotTierStatusRequestRequestTypeDef",
    "DescribeSnapshotTierStatusResultTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeSpotDatafeedSubscriptionRequestRequestTypeDef",
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    "DescribeSpotFleetInstancesRequestRequestTypeDef",
    "DescribeSpotFleetInstancesResponseTypeDef",
    "DescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    "DescribeSpotFleetRequestsRequestRequestTypeDef",
    "DescribeSpotFleetRequestsResponseTypeDef",
    "DescribeSpotInstanceRequestsRequestRequestTypeDef",
    "DescribeSpotInstanceRequestsResultTypeDef",
    "DescribeSpotPriceHistoryRequestRequestTypeDef",
    "DescribeSpotPriceHistoryResultTypeDef",
    "DescribeStaleSecurityGroupsRequestRequestTypeDef",
    "DescribeStaleSecurityGroupsResultTypeDef",
    "DescribeStoreImageTasksRequestRequestTypeDef",
    "DescribeStoreImageTasksResultTypeDef",
    "DescribeSubnetsRequestRequestTypeDef",
    "DescribeSubnetsResultTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeTrafficMirrorFiltersRequestRequestTypeDef",
    "DescribeTrafficMirrorFiltersResultTypeDef",
    "DescribeTrafficMirrorSessionsRequestRequestTypeDef",
    "DescribeTrafficMirrorSessionsResultTypeDef",
    "DescribeTrafficMirrorTargetsRequestRequestTypeDef",
    "DescribeTrafficMirrorTargetsResultTypeDef",
    "DescribeTransitGatewayAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    "DescribeTransitGatewayConnectPeersRequestRequestTypeDef",
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    "DescribeTransitGatewayConnectsRequestRequestTypeDef",
    "DescribeTransitGatewayConnectsResultTypeDef",
    "DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef",
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    "DescribeTransitGatewayRouteTablesRequestRequestTypeDef",
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    "DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    "DescribeTransitGatewaysRequestRequestTypeDef",
    "DescribeTransitGatewaysResultTypeDef",
    "DescribeTrunkInterfaceAssociationsRequestRequestTypeDef",
    "DescribeTrunkInterfaceAssociationsResultTypeDef",
    "DescribeVolumeAttributeRequestRequestTypeDef",
    "DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef",
    "DescribeVolumeAttributeResultTypeDef",
    "DescribeVolumeStatusRequestRequestTypeDef",
    "DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef",
    "DescribeVolumeStatusResultTypeDef",
    "DescribeVolumesModificationsRequestRequestTypeDef",
    "DescribeVolumesModificationsResultTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVolumesResultTypeDef",
    "DescribeVpcAttributeRequestRequestTypeDef",
    "DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef",
    "DescribeVpcAttributeResultTypeDef",
    "DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    "DescribeVpcClassicLinkRequestRequestTypeDef",
    "DescribeVpcClassicLinkResultTypeDef",
    "DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    "DescribeVpcEndpointConnectionsRequestRequestTypeDef",
    "DescribeVpcEndpointConnectionsResultTypeDef",
    "DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    "DescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    "DescribeVpcEndpointServicesRequestRequestTypeDef",
    "DescribeVpcEndpointServicesResultTypeDef",
    "DescribeVpcEndpointsRequestRequestTypeDef",
    "DescribeVpcEndpointsResultTypeDef",
    "DescribeVpcPeeringConnectionsRequestRequestTypeDef",
    "DescribeVpcPeeringConnectionsResultTypeDef",
    "DescribeVpcsRequestRequestTypeDef",
    "DescribeVpcsResultTypeDef",
    "DescribeVpnConnectionsRequestRequestTypeDef",
    "DescribeVpnConnectionsResultTypeDef",
    "DescribeVpnGatewaysRequestRequestTypeDef",
    "DescribeVpnGatewaysResultTypeDef",
    "DestinationOptionsRequestTypeDef",
    "DestinationOptionsResponseTypeDef",
    "DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef",
    "DetachClassicLinkVpcRequestRequestTypeDef",
    "DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef",
    "DetachClassicLinkVpcResultTypeDef",
    "DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef",
    "DetachInternetGatewayRequestRequestTypeDef",
    "DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef",
    "DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef",
    "DetachNetworkInterfaceRequestRequestTypeDef",
    "DetachVolumeRequestInstanceDetachVolumeTypeDef",
    "DetachVolumeRequestRequestTypeDef",
    "DetachVolumeRequestVolumeDetachFromInstanceTypeDef",
    "DetachVpnGatewayRequestRequestTypeDef",
    "DhcpConfigurationTypeDef",
    "DhcpOptionsTypeDef",
    "DirectoryServiceAuthenticationRequestTypeDef",
    "DirectoryServiceAuthenticationTypeDef",
    "DisableEbsEncryptionByDefaultRequestRequestTypeDef",
    "DisableEbsEncryptionByDefaultResultTypeDef",
    "DisableFastLaunchRequestRequestTypeDef",
    "DisableFastLaunchResultTypeDef",
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    "DisableFastSnapshotRestoresRequestRequestTypeDef",
    "DisableFastSnapshotRestoresResultTypeDef",
    "DisableImageDeprecationRequestRequestTypeDef",
    "DisableImageDeprecationResultTypeDef",
    "DisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    "DisableIpamOrganizationAdminAccountResultTypeDef",
    "DisableSerialConsoleAccessRequestRequestTypeDef",
    "DisableSerialConsoleAccessResultTypeDef",
    "DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    "DisableVgwRoutePropagationRequestRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    "DisableVpcClassicLinkRequestRequestTypeDef",
    "DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef",
    "DisableVpcClassicLinkResultTypeDef",
    "DisassociateAddressRequestClassicAddressDisassociateTypeDef",
    "DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef",
    "DisassociateAddressRequestRequestTypeDef",
    "DisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    "DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    "DisassociateIamInstanceProfileRequestRequestTypeDef",
    "DisassociateIamInstanceProfileResultTypeDef",
    "DisassociateInstanceEventWindowRequestRequestTypeDef",
    "DisassociateInstanceEventWindowResultTypeDef",
    "DisassociateRouteTableRequestRequestTypeDef",
    "DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef",
    "DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef",
    "DisassociateSubnetCidrBlockRequestRequestTypeDef",
    "DisassociateSubnetCidrBlockResultTypeDef",
    "DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    "DisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    "DisassociateTrunkInterfaceRequestRequestTypeDef",
    "DisassociateTrunkInterfaceResultTypeDef",
    "DisassociateVpcCidrBlockRequestRequestTypeDef",
    "DisassociateVpcCidrBlockResultTypeDef",
    "DiskImageDescriptionTypeDef",
    "DiskImageDetailTypeDef",
    "DiskImageTypeDef",
    "DiskImageVolumeDescriptionTypeDef",
    "DiskInfoTypeDef",
    "DnsEntryTypeDef",
    "DnsServersOptionsModifyStructureTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsInfoTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "EbsOptimizedInfoTypeDef",
    "EfaInfoTypeDef",
    "EgressOnlyInternetGatewayTypeDef",
    "ElasticGpuAssociationTypeDef",
    "ElasticGpuHealthTypeDef",
    "ElasticGpuSpecificationResponseTypeDef",
    "ElasticGpuSpecificationTypeDef",
    "ElasticGpusTypeDef",
    "ElasticInferenceAcceleratorAssociationTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "EnableEbsEncryptionByDefaultRequestRequestTypeDef",
    "EnableEbsEncryptionByDefaultResultTypeDef",
    "EnableFastLaunchRequestRequestTypeDef",
    "EnableFastLaunchResultTypeDef",
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    "EnableFastSnapshotRestoresRequestRequestTypeDef",
    "EnableFastSnapshotRestoresResultTypeDef",
    "EnableImageDeprecationRequestRequestTypeDef",
    "EnableImageDeprecationResultTypeDef",
    "EnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    "EnableIpamOrganizationAdminAccountResultTypeDef",
    "EnableSerialConsoleAccessRequestRequestTypeDef",
    "EnableSerialConsoleAccessResultTypeDef",
    "EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    "EnableVgwRoutePropagationRequestRequestTypeDef",
    "EnableVolumeIORequestRequestTypeDef",
    "EnableVolumeIORequestVolumeEnableIoTypeDef",
    "EnableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    "EnableVpcClassicLinkRequestRequestTypeDef",
    "EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef",
    "EnableVpcClassicLinkResultTypeDef",
    "EnclaveOptionsRequestTypeDef",
    "EnclaveOptionsResponseMetadataTypeDef",
    "EnclaveOptionsTypeDef",
    "EventInformationTypeDef",
    "ExplanationTypeDef",
    "ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    "ExportClientVpnClientConfigurationRequestRequestTypeDef",
    "ExportClientVpnClientConfigurationResultTypeDef",
    "ExportImageRequestRequestTypeDef",
    "ExportImageResultTypeDef",
    "ExportImageTaskTypeDef",
    "ExportTaskS3LocationRequestTypeDef",
    "ExportTaskS3LocationTypeDef",
    "ExportTaskTypeDef",
    "ExportToS3TaskSpecificationTypeDef",
    "ExportToS3TaskTypeDef",
    "ExportTransitGatewayRoutesRequestRequestTypeDef",
    "ExportTransitGatewayRoutesResultTypeDef",
    "FailedCapacityReservationFleetCancellationResultTypeDef",
    "FailedQueuedPurchaseDeletionTypeDef",
    "FastLaunchLaunchTemplateSpecificationRequestTypeDef",
    "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
    "FastLaunchSnapshotConfigurationRequestTypeDef",
    "FastLaunchSnapshotConfigurationResponseTypeDef",
    "FederatedAuthenticationRequestTypeDef",
    "FederatedAuthenticationTypeDef",
    "FilterTypeDef",
    "FleetCapacityReservationTypeDef",
    "FleetDataTypeDef",
    "FleetLaunchTemplateConfigRequestTypeDef",
    "FleetLaunchTemplateConfigTypeDef",
    "FleetLaunchTemplateOverridesRequestTypeDef",
    "FleetLaunchTemplateOverridesTypeDef",
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    "FleetLaunchTemplateSpecificationTypeDef",
    "FleetSpotCapacityRebalanceRequestTypeDef",
    "FleetSpotCapacityRebalanceTypeDef",
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    "FleetSpotMaintenanceStrategiesTypeDef",
    "FlowLogTypeDef",
    "FpgaDeviceInfoTypeDef",
    "FpgaDeviceMemoryInfoTypeDef",
    "FpgaImageAttributeTypeDef",
    "FpgaImageStateTypeDef",
    "FpgaImageTypeDef",
    "FpgaInfoTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    "GetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    "GetCapacityReservationUsageRequestRequestTypeDef",
    "GetCapacityReservationUsageResultTypeDef",
    "GetCoipPoolUsageRequestRequestTypeDef",
    "GetCoipPoolUsageResultTypeDef",
    "GetConsoleOutputRequestInstanceConsoleOutputTypeDef",
    "GetConsoleOutputRequestRequestTypeDef",
    "GetConsoleOutputResultTypeDef",
    "GetConsoleScreenshotRequestRequestTypeDef",
    "GetConsoleScreenshotResultTypeDef",
    "GetDefaultCreditSpecificationRequestRequestTypeDef",
    "GetDefaultCreditSpecificationResultTypeDef",
    "GetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    "GetEbsEncryptionByDefaultRequestRequestTypeDef",
    "GetEbsEncryptionByDefaultResultTypeDef",
    "GetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    "GetGroupsForCapacityReservationRequestRequestTypeDef",
    "GetGroupsForCapacityReservationResultTypeDef",
    "GetHostReservationPurchasePreviewRequestRequestTypeDef",
    "GetHostReservationPurchasePreviewResultTypeDef",
    "GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    "GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    "GetIpamAddressHistoryRequestRequestTypeDef",
    "GetIpamAddressHistoryResultTypeDef",
    "GetIpamPoolAllocationsRequestRequestTypeDef",
    "GetIpamPoolAllocationsResultTypeDef",
    "GetIpamPoolCidrsRequestRequestTypeDef",
    "GetIpamPoolCidrsResultTypeDef",
    "GetIpamResourceCidrsRequestRequestTypeDef",
    "GetIpamResourceCidrsResultTypeDef",
    "GetLaunchTemplateDataRequestRequestTypeDef",
    "GetLaunchTemplateDataResultTypeDef",
    "GetManagedPrefixListAssociationsRequestRequestTypeDef",
    "GetManagedPrefixListAssociationsResultTypeDef",
    "GetManagedPrefixListEntriesRequestRequestTypeDef",
    "GetManagedPrefixListEntriesResultTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    "GetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    "GetNetworkInsightsAccessScopeContentResultTypeDef",
    "GetPasswordDataRequestInstancePasswordDataTypeDef",
    "GetPasswordDataRequestRequestTypeDef",
    "GetPasswordDataResultTypeDef",
    "GetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    "GetSerialConsoleAccessStatusRequestRequestTypeDef",
    "GetSerialConsoleAccessStatusResultTypeDef",
    "GetSpotPlacementScoresRequestRequestTypeDef",
    "GetSpotPlacementScoresResultTypeDef",
    "GetSubnetCidrReservationsRequestRequestTypeDef",
    "GetSubnetCidrReservationsResultTypeDef",
    "GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "GetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    "GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    "GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    "GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    "GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    "GetVpnConnectionDeviceTypesRequestRequestTypeDef",
    "GetVpnConnectionDeviceTypesResultTypeDef",
    "GpuDeviceInfoTypeDef",
    "GpuDeviceMemoryInfoTypeDef",
    "GpuInfoTypeDef",
    "GroupIdentifierTypeDef",
    "HibernationOptionsRequestTypeDef",
    "HibernationOptionsResponseMetadataTypeDef",
    "HibernationOptionsTypeDef",
    "HistoryRecordEntryTypeDef",
    "HistoryRecordTypeDef",
    "HostInstanceTypeDef",
    "HostOfferingTypeDef",
    "HostPropertiesTypeDef",
    "HostReservationTypeDef",
    "HostTypeDef",
    "IKEVersionsListValueTypeDef",
    "IKEVersionsRequestListValueTypeDef",
    "IamInstanceProfileAssociationTypeDef",
    "IamInstanceProfileResponseMetadataTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "IamInstanceProfileTypeDef",
    "IcmpTypeCodeTypeDef",
    "IdFormatTypeDef",
    "ImageAttributeTypeDef",
    "ImageDiskContainerTypeDef",
    "ImageRecycleBinInfoTypeDef",
    "ImageTypeDef",
    "ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    "ImportImageLicenseConfigurationRequestTypeDef",
    "ImportImageLicenseConfigurationResponseTypeDef",
    "ImportImageRequestRequestTypeDef",
    "ImportImageResultTypeDef",
    "ImportImageTaskTypeDef",
    "ImportInstanceLaunchSpecificationTypeDef",
    "ImportInstanceRequestRequestTypeDef",
    "ImportInstanceResultTypeDef",
    "ImportInstanceTaskDetailsTypeDef",
    "ImportInstanceVolumeDetailItemTypeDef",
    "ImportKeyPairRequestRequestTypeDef",
    "ImportKeyPairRequestServiceResourceImportKeyPairTypeDef",
    "ImportKeyPairResultTypeDef",
    "ImportSnapshotRequestRequestTypeDef",
    "ImportSnapshotResultTypeDef",
    "ImportSnapshotTaskTypeDef",
    "ImportVolumeRequestRequestTypeDef",
    "ImportVolumeResultTypeDef",
    "ImportVolumeTaskDetailsTypeDef",
    "InferenceAcceleratorInfoTypeDef",
    "InferenceDeviceInfoTypeDef",
    "InstanceAttributeTypeDef",
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceCapacityTypeDef",
    "InstanceCountTypeDef",
    "InstanceCreditSpecificationRequestTypeDef",
    "InstanceCreditSpecificationTypeDef",
    "InstanceDeleteTagsRequestTypeDef",
    "InstanceEventWindowAssociationRequestTypeDef",
    "InstanceEventWindowAssociationTargetTypeDef",
    "InstanceEventWindowDisassociationRequestTypeDef",
    "InstanceEventWindowStateChangeTypeDef",
    "InstanceEventWindowTimeRangeRequestTypeDef",
    "InstanceEventWindowTimeRangeTypeDef",
    "InstanceEventWindowTypeDef",
    "InstanceExportDetailsTypeDef",
    "InstanceFamilyCreditSpecificationTypeDef",
    "InstanceIpv4PrefixTypeDef",
    "InstanceIpv6AddressRequestTypeDef",
    "InstanceIpv6AddressTypeDef",
    "InstanceIpv6PrefixTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceMetadataOptionsResponseResponseMetadataTypeDef",
    "InstanceMetadataOptionsResponseTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceNetworkInterfaceAssociationTypeDef",
    "InstanceNetworkInterfaceAttachmentTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "InstanceNetworkInterfaceTypeDef",
    "InstancePrivateIpAddressTypeDef",
    "InstanceRequirementsRequestTypeDef",
    "InstanceRequirementsTypeDef",
    "InstanceRequirementsWithMetadataRequestTypeDef",
    "InstanceSpecificationTypeDef",
    "InstanceStateChangeTypeDef",
    "InstanceStateResponseMetadataTypeDef",
    "InstanceStateTypeDef",
    "InstanceStatusDetailsTypeDef",
    "InstanceStatusEventTypeDef",
    "InstanceStatusSummaryTypeDef",
    "InstanceStatusTypeDef",
    "InstanceStorageInfoTypeDef",
    "InstanceTagNotificationAttributeTypeDef",
    "InstanceTypeDef",
    "InstanceTypeInfoFromInstanceRequirementsTypeDef",
    "InstanceTypeInfoTypeDef",
    "InstanceTypeOfferingTypeDef",
    "InstanceUsageTypeDef",
    "IntegrateServicesTypeDef",
    "InternetGatewayAttachmentTypeDef",
    "InternetGatewayTypeDef",
    "IpPermissionTypeDef",
    "IpRangeTypeDef",
    "IpamAddressHistoryRecordTypeDef",
    "IpamCidrAuthorizationContextTypeDef",
    "IpamOperatingRegionTypeDef",
    "IpamPoolAllocationTypeDef",
    "IpamPoolCidrFailureReasonTypeDef",
    "IpamPoolCidrTypeDef",
    "IpamPoolTypeDef",
    "IpamResourceCidrTypeDef",
    "IpamResourceTagTypeDef",
    "IpamScopeTypeDef",
    "IpamTypeDef",
    "Ipv4PrefixSpecificationRequestTypeDef",
    "Ipv4PrefixSpecificationResponseTypeDef",
    "Ipv4PrefixSpecificationTypeDef",
    "Ipv6CidrAssociationTypeDef",
    "Ipv6CidrBlockTypeDef",
    "Ipv6PoolTypeDef",
    "Ipv6PrefixSpecificationRequestTypeDef",
    "Ipv6PrefixSpecificationResponseTypeDef",
    "Ipv6PrefixSpecificationTypeDef",
    "Ipv6RangeTypeDef",
    "KeyPairInfoTypeDef",
    "KeyPairTypeDef",
    "LastErrorTypeDef",
    "LaunchPermissionModificationsTypeDef",
    "LaunchPermissionTypeDef",
    "LaunchSpecificationTypeDef",
    "LaunchTemplateAndOverridesResponseTypeDef",
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    "LaunchTemplateBlockDeviceMappingTypeDef",
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    "LaunchTemplateConfigTypeDef",
    "LaunchTemplateCpuOptionsRequestTypeDef",
    "LaunchTemplateCpuOptionsTypeDef",
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    "LaunchTemplateEbsBlockDeviceTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    "LaunchTemplateEnclaveOptionsTypeDef",
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    "LaunchTemplateHibernationOptionsTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    "LaunchTemplateLicenseConfigurationTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplatePlacementRequestTypeDef",
    "LaunchTemplatePlacementTypeDef",
    "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
    "LaunchTemplatePrivateDnsNameOptionsTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    "LaunchTemplateSpotMarketOptionsTypeDef",
    "LaunchTemplateTagSpecificationRequestTypeDef",
    "LaunchTemplateTagSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LaunchTemplateVersionTypeDef",
    "LaunchTemplatesMonitoringRequestTypeDef",
    "LaunchTemplatesMonitoringTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "LicenseConfigurationTypeDef",
    "ListImagesInRecycleBinRequestRequestTypeDef",
    "ListImagesInRecycleBinResultTypeDef",
    "ListSnapshotsInRecycleBinRequestRequestTypeDef",
    "ListSnapshotsInRecycleBinResultTypeDef",
    "LoadBalancersConfigTypeDef",
    "LoadPermissionModificationsTypeDef",
    "LoadPermissionRequestTypeDef",
    "LoadPermissionTypeDef",
    "LocalGatewayRouteTableTypeDef",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    "LocalGatewayRouteTypeDef",
    "LocalGatewayTypeDef",
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    "LocalGatewayVirtualInterfaceTypeDef",
    "ManagedPrefixListTypeDef",
    "MemoryGiBPerVCpuRequestTypeDef",
    "MemoryGiBPerVCpuTypeDef",
    "MemoryInfoTypeDef",
    "MemoryMiBRequestTypeDef",
    "MemoryMiBTypeDef",
    "ModifyAddressAttributeRequestRequestTypeDef",
    "ModifyAddressAttributeResultTypeDef",
    "ModifyAvailabilityZoneGroupRequestRequestTypeDef",
    "ModifyAvailabilityZoneGroupResultTypeDef",
    "ModifyCapacityReservationFleetRequestRequestTypeDef",
    "ModifyCapacityReservationFleetResultTypeDef",
    "ModifyCapacityReservationRequestRequestTypeDef",
    "ModifyCapacityReservationResultTypeDef",
    "ModifyClientVpnEndpointRequestRequestTypeDef",
    "ModifyClientVpnEndpointResultTypeDef",
    "ModifyDefaultCreditSpecificationRequestRequestTypeDef",
    "ModifyDefaultCreditSpecificationResultTypeDef",
    "ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    "ModifyFleetRequestRequestTypeDef",
    "ModifyFleetResultTypeDef",
    "ModifyFpgaImageAttributeRequestRequestTypeDef",
    "ModifyFpgaImageAttributeResultTypeDef",
    "ModifyHostsRequestRequestTypeDef",
    "ModifyHostsResultTypeDef",
    "ModifyIdFormatRequestRequestTypeDef",
    "ModifyIdentityIdFormatRequestRequestTypeDef",
    "ModifyImageAttributeRequestImageModifyAttributeTypeDef",
    "ModifyImageAttributeRequestRequestTypeDef",
    "ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef",
    "ModifyInstanceAttributeRequestRequestTypeDef",
    "ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    "ModifyInstanceCreditSpecificationRequestRequestTypeDef",
    "ModifyInstanceCreditSpecificationResultTypeDef",
    "ModifyInstanceEventStartTimeRequestRequestTypeDef",
    "ModifyInstanceEventStartTimeResultTypeDef",
    "ModifyInstanceEventWindowRequestRequestTypeDef",
    "ModifyInstanceEventWindowResultTypeDef",
    "ModifyInstanceMetadataOptionsRequestRequestTypeDef",
    "ModifyInstanceMetadataOptionsResultTypeDef",
    "ModifyInstancePlacementRequestRequestTypeDef",
    "ModifyInstancePlacementResultTypeDef",
    "ModifyIpamPoolRequestRequestTypeDef",
    "ModifyIpamPoolResultTypeDef",
    "ModifyIpamRequestRequestTypeDef",
    "ModifyIpamResourceCidrRequestRequestTypeDef",
    "ModifyIpamResourceCidrResultTypeDef",
    "ModifyIpamResultTypeDef",
    "ModifyIpamScopeRequestRequestTypeDef",
    "ModifyIpamScopeResultTypeDef",
    "ModifyLaunchTemplateRequestRequestTypeDef",
    "ModifyLaunchTemplateResultTypeDef",
    "ModifyManagedPrefixListRequestRequestTypeDef",
    "ModifyManagedPrefixListResultTypeDef",
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef",
    "ModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    "ModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    "ModifyPrivateDnsNameOptionsResultTypeDef",
    "ModifyReservedInstancesRequestRequestTypeDef",
    "ModifyReservedInstancesResultTypeDef",
    "ModifySecurityGroupRulesRequestRequestTypeDef",
    "ModifySecurityGroupRulesResultTypeDef",
    "ModifySnapshotAttributeRequestRequestTypeDef",
    "ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef",
    "ModifySnapshotTierRequestRequestTypeDef",
    "ModifySnapshotTierResultTypeDef",
    "ModifySpotFleetRequestRequestRequestTypeDef",
    "ModifySpotFleetRequestResponseTypeDef",
    "ModifySubnetAttributeRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    "ModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    "ModifyTrafficMirrorSessionRequestRequestTypeDef",
    "ModifyTrafficMirrorSessionResultTypeDef",
    "ModifyTransitGatewayOptionsTypeDef",
    "ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    "ModifyTransitGatewayRequestRequestTypeDef",
    "ModifyTransitGatewayResultTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    "ModifyVolumeAttributeRequestRequestTypeDef",
    "ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef",
    "ModifyVolumeRequestRequestTypeDef",
    "ModifyVolumeResultTypeDef",
    "ModifyVpcAttributeRequestRequestTypeDef",
    "ModifyVpcAttributeRequestVpcModifyAttributeTypeDef",
    "ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    "ModifyVpcEndpointRequestRequestTypeDef",
    "ModifyVpcEndpointResultTypeDef",
    "ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    "ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    "ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    "ModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    "ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    "ModifyVpcTenancyRequestRequestTypeDef",
    "ModifyVpcTenancyResultTypeDef",
    "ModifyVpnConnectionOptionsRequestRequestTypeDef",
    "ModifyVpnConnectionOptionsResultTypeDef",
    "ModifyVpnConnectionRequestRequestTypeDef",
    "ModifyVpnConnectionResultTypeDef",
    "ModifyVpnTunnelCertificateRequestRequestTypeDef",
    "ModifyVpnTunnelCertificateResultTypeDef",
    "ModifyVpnTunnelOptionsRequestRequestTypeDef",
    "ModifyVpnTunnelOptionsResultTypeDef",
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    "MonitorInstancesRequestInstanceMonitorTypeDef",
    "MonitorInstancesRequestRequestTypeDef",
    "MonitorInstancesResultTypeDef",
    "MonitoringResponseMetadataTypeDef",
    "MonitoringTypeDef",
    "MoveAddressToVpcRequestRequestTypeDef",
    "MoveAddressToVpcResultTypeDef",
    "MoveByoipCidrToIpamRequestRequestTypeDef",
    "MoveByoipCidrToIpamResultTypeDef",
    "MovingAddressStatusTypeDef",
    "NatGatewayAddressTypeDef",
    "NatGatewayTypeDef",
    "NetworkAclAssociationTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkAclTypeDef",
    "NetworkCardInfoTypeDef",
    "NetworkInfoTypeDef",
    "NetworkInsightsAccessScopeAnalysisTypeDef",
    "NetworkInsightsAccessScopeContentTypeDef",
    "NetworkInsightsAccessScopeTypeDef",
    "NetworkInsightsAnalysisTypeDef",
    "NetworkInsightsPathTypeDef",
    "NetworkInterfaceAssociationResponseMetadataTypeDef",
    "NetworkInterfaceAssociationTypeDef",
    "NetworkInterfaceAttachmentChangesTypeDef",
    "NetworkInterfaceAttachmentResponseMetadataTypeDef",
    "NetworkInterfaceAttachmentTypeDef",
    "NetworkInterfaceCountRequestTypeDef",
    "NetworkInterfaceCountTypeDef",
    "NetworkInterfaceIpv6AddressTypeDef",
    "NetworkInterfacePermissionStateTypeDef",
    "NetworkInterfacePermissionTypeDef",
    "NetworkInterfacePrivateIpAddressTypeDef",
    "NetworkInterfaceTypeDef",
    "NewDhcpConfigurationTypeDef",
    "OnDemandOptionsRequestTypeDef",
    "OnDemandOptionsTypeDef",
    "PacketHeaderStatementRequestTypeDef",
    "PacketHeaderStatementTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "PathStatementRequestTypeDef",
    "PathStatementTypeDef",
    "PciIdTypeDef",
    "PeeringAttachmentStatusTypeDef",
    "PeeringConnectionOptionsRequestTypeDef",
    "PeeringConnectionOptionsTypeDef",
    "PeeringTgwInfoTypeDef",
    "Phase1DHGroupNumbersListValueTypeDef",
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    "Phase2DHGroupNumbersListValueTypeDef",
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    "PlacementGroupInfoTypeDef",
    "PlacementGroupTypeDef",
    "PlacementResponseMetadataTypeDef",
    "PlacementResponseTypeDef",
    "PlacementTypeDef",
    "PoolCidrBlockTypeDef",
    "PortRangeTypeDef",
    "PrefixListAssociationTypeDef",
    "PrefixListEntryTypeDef",
    "PrefixListIdTypeDef",
    "PrefixListTypeDef",
    "PriceScheduleSpecificationTypeDef",
    "PriceScheduleTypeDef",
    "PricingDetailTypeDef",
    "PrincipalIdFormatTypeDef",
    "PrivateDnsDetailsTypeDef",
    "PrivateDnsNameConfigurationTypeDef",
    "PrivateDnsNameOptionsOnLaunchResponseMetadataTypeDef",
    "PrivateDnsNameOptionsOnLaunchTypeDef",
    "PrivateDnsNameOptionsRequestTypeDef",
    "PrivateDnsNameOptionsResponseResponseMetadataTypeDef",
    "PrivateDnsNameOptionsResponseTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "ProcessorInfoTypeDef",
    "ProductCodeTypeDef",
    "PropagatingVgwTypeDef",
    "ProvisionByoipCidrRequestRequestTypeDef",
    "ProvisionByoipCidrResultTypeDef",
    "ProvisionIpamPoolCidrRequestRequestTypeDef",
    "ProvisionIpamPoolCidrResultTypeDef",
    "ProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    "ProvisionPublicIpv4PoolCidrResultTypeDef",
    "ProvisionedBandwidthTypeDef",
    "PtrUpdateStatusTypeDef",
    "PublicIpv4PoolRangeTypeDef",
    "PublicIpv4PoolTypeDef",
    "PurchaseHostReservationRequestRequestTypeDef",
    "PurchaseHostReservationResultTypeDef",
    "PurchaseRequestTypeDef",
    "PurchaseReservedInstancesOfferingRequestRequestTypeDef",
    "PurchaseReservedInstancesOfferingResultTypeDef",
    "PurchaseScheduledInstancesRequestRequestTypeDef",
    "PurchaseScheduledInstancesResultTypeDef",
    "PurchaseTypeDef",
    "RebootInstancesRequestInstanceRebootTypeDef",
    "RebootInstancesRequestRequestTypeDef",
    "RecurringChargeTypeDef",
    "ReferencedSecurityGroupTypeDef",
    "RegionTypeDef",
    "RegisterImageRequestRequestTypeDef",
    "RegisterImageRequestServiceResourceRegisterImageTypeDef",
    "RegisterImageResultTypeDef",
    "RegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    "RegisterInstanceTagAttributeRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    "RejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    "RejectVpcEndpointConnectionsRequestRequestTypeDef",
    "RejectVpcEndpointConnectionsResultTypeDef",
    "RejectVpcPeeringConnectionRequestRequestTypeDef",
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef",
    "RejectVpcPeeringConnectionResultTypeDef",
    "ReleaseAddressRequestClassicAddressReleaseTypeDef",
    "ReleaseAddressRequestRequestTypeDef",
    "ReleaseAddressRequestVpcAddressReleaseTypeDef",
    "ReleaseHostsRequestRequestTypeDef",
    "ReleaseHostsResultTypeDef",
    "ReleaseIpamPoolAllocationRequestRequestTypeDef",
    "ReleaseIpamPoolAllocationResultTypeDef",
    "RemoveIpamOperatingRegionTypeDef",
    "RemovePrefixListEntryTypeDef",
    "ReplaceIamInstanceProfileAssociationRequestRequestTypeDef",
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    "ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef",
    "ReplaceNetworkAclAssociationRequestRequestTypeDef",
    "ReplaceNetworkAclAssociationResultTypeDef",
    "ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef",
    "ReplaceNetworkAclEntryRequestRequestTypeDef",
    "ReplaceRootVolumeTaskTypeDef",
    "ReplaceRouteRequestRequestTypeDef",
    "ReplaceRouteRequestRouteReplaceTypeDef",
    "ReplaceRouteTableAssociationRequestRequestTypeDef",
    "ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef",
    "ReplaceRouteTableAssociationResultTypeDef",
    "ReplaceTransitGatewayRouteRequestRequestTypeDef",
    "ReplaceTransitGatewayRouteResultTypeDef",
    "ReportInstanceStatusRequestInstanceReportStatusTypeDef",
    "ReportInstanceStatusRequestRequestTypeDef",
    "RequestIpamResourceTagTypeDef",
    "RequestLaunchTemplateDataTypeDef",
    "RequestSpotFleetRequestRequestTypeDef",
    "RequestSpotFleetResponseTypeDef",
    "RequestSpotInstancesRequestRequestTypeDef",
    "RequestSpotInstancesResultTypeDef",
    "RequestSpotLaunchSpecificationTypeDef",
    "ReservationFleetInstanceSpecificationTypeDef",
    "ReservationResponseMetadataTypeDef",
    "ReservationTypeDef",
    "ReservationValueTypeDef",
    "ReservedInstanceLimitPriceTypeDef",
    "ReservedInstanceReservationValueTypeDef",
    "ReservedInstancesConfigurationTypeDef",
    "ReservedInstancesIdTypeDef",
    "ReservedInstancesListingTypeDef",
    "ReservedInstancesModificationResultTypeDef",
    "ReservedInstancesModificationTypeDef",
    "ReservedInstancesOfferingTypeDef",
    "ReservedInstancesTypeDef",
    "ResetAddressAttributeRequestRequestTypeDef",
    "ResetAddressAttributeResultTypeDef",
    "ResetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    "ResetFpgaImageAttributeRequestRequestTypeDef",
    "ResetFpgaImageAttributeResultTypeDef",
    "ResetImageAttributeRequestImageResetAttributeTypeDef",
    "ResetImageAttributeRequestRequestTypeDef",
    "ResetInstanceAttributeRequestInstanceResetAttributeTypeDef",
    "ResetInstanceAttributeRequestInstanceResetKernelTypeDef",
    "ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef",
    "ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef",
    "ResetInstanceAttributeRequestRequestTypeDef",
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef",
    "ResetNetworkInterfaceAttributeRequestRequestTypeDef",
    "ResetSnapshotAttributeRequestRequestTypeDef",
    "ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef",
    "ResourceStatementRequestTypeDef",
    "ResourceStatementTypeDef",
    "ResponseErrorTypeDef",
    "ResponseLaunchTemplateDataTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreAddressToClassicRequestRequestTypeDef",
    "RestoreAddressToClassicResultTypeDef",
    "RestoreImageFromRecycleBinRequestRequestTypeDef",
    "RestoreImageFromRecycleBinResultTypeDef",
    "RestoreManagedPrefixListVersionRequestRequestTypeDef",
    "RestoreManagedPrefixListVersionResultTypeDef",
    "RestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    "RestoreSnapshotFromRecycleBinResultTypeDef",
    "RestoreSnapshotTierRequestRequestTypeDef",
    "RestoreSnapshotTierResultTypeDef",
    "RevokeClientVpnIngressRequestRequestTypeDef",
    "RevokeClientVpnIngressResultTypeDef",
    "RevokeSecurityGroupEgressRequestRequestTypeDef",
    "RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef",
    "RevokeSecurityGroupEgressResultTypeDef",
    "RevokeSecurityGroupIngressRequestRequestTypeDef",
    "RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef",
    "RevokeSecurityGroupIngressResultTypeDef",
    "RouteTableAssociationStateResponseMetadataTypeDef",
    "RouteTableAssociationStateTypeDef",
    "RouteTableAssociationTypeDef",
    "RouteTableTypeDef",
    "RouteTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "RunInstancesRequestRequestTypeDef",
    "RunInstancesRequestServiceResourceCreateInstancesTypeDef",
    "RunInstancesRequestSubnetCreateInstancesTypeDef",
    "RunScheduledInstancesRequestRequestTypeDef",
    "RunScheduledInstancesResultTypeDef",
    "S3ObjectTagTypeDef",
    "S3StorageTypeDef",
    "ScheduledInstanceAvailabilityTypeDef",
    "ScheduledInstanceRecurrenceRequestTypeDef",
    "ScheduledInstanceRecurrenceTypeDef",
    "ScheduledInstanceTypeDef",
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    "ScheduledInstancesEbsTypeDef",
    "ScheduledInstancesIamInstanceProfileTypeDef",
    "ScheduledInstancesIpv6AddressTypeDef",
    "ScheduledInstancesLaunchSpecificationTypeDef",
    "ScheduledInstancesMonitoringTypeDef",
    "ScheduledInstancesNetworkInterfaceTypeDef",
    "ScheduledInstancesPlacementTypeDef",
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    "SearchLocalGatewayRoutesRequestRequestTypeDef",
    "SearchLocalGatewayRoutesResultTypeDef",
    "SearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    "SearchTransitGatewayRoutesRequestRequestTypeDef",
    "SearchTransitGatewayRoutesResultTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SecurityGroupReferenceTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityGroupRuleRequestTypeDef",
    "SecurityGroupRuleTypeDef",
    "SecurityGroupRuleUpdateTypeDef",
    "SecurityGroupTypeDef",
    "SendDiagnosticInterruptRequestRequestTypeDef",
    "ServiceConfigurationTypeDef",
    "ServiceDetailTypeDef",
    "ServiceResourceClassicAddressRequestTypeDef",
    "ServiceResourceDhcpOptionsRequestTypeDef",
    "ServiceResourceImageRequestTypeDef",
    "ServiceResourceInstanceRequestTypeDef",
    "ServiceResourceInternetGatewayRequestTypeDef",
    "ServiceResourceKeyPairRequestTypeDef",
    "ServiceResourceNetworkAclRequestTypeDef",
    "ServiceResourceNetworkInterfaceAssociationRequestTypeDef",
    "ServiceResourceNetworkInterfaceRequestTypeDef",
    "ServiceResourcePlacementGroupRequestTypeDef",
    "ServiceResourceRouteRequestTypeDef",
    "ServiceResourceRouteTableAssociationRequestTypeDef",
    "ServiceResourceRouteTableRequestTypeDef",
    "ServiceResourceSecurityGroupRequestTypeDef",
    "ServiceResourceSnapshotRequestTypeDef",
    "ServiceResourceSubnetRequestTypeDef",
    "ServiceResourceTagRequestTypeDef",
    "ServiceResourceVolumeRequestTypeDef",
    "ServiceResourceVpcAddressRequestTypeDef",
    "ServiceResourceVpcPeeringConnectionRequestTypeDef",
    "ServiceResourceVpcRequestTypeDef",
    "ServiceTypeDetailTypeDef",
    "SlotDateTimeRangeRequestTypeDef",
    "SlotStartTimeRangeRequestTypeDef",
    "SnapshotDetailTypeDef",
    "SnapshotDiskContainerTypeDef",
    "SnapshotInfoTypeDef",
    "SnapshotRecycleBinInfoTypeDef",
    "SnapshotResponseMetadataTypeDef",
    "SnapshotTaskDetailTypeDef",
    "SnapshotTierStatusTypeDef",
    "SnapshotTypeDef",
    "SpotCapacityRebalanceTypeDef",
    "SpotDatafeedSubscriptionTypeDef",
    "SpotFleetLaunchSpecificationTypeDef",
    "SpotFleetMonitoringTypeDef",
    "SpotFleetRequestConfigDataTypeDef",
    "SpotFleetRequestConfigTypeDef",
    "SpotFleetTagSpecificationTypeDef",
    "SpotInstanceRequestTypeDef",
    "SpotInstanceStateFaultTypeDef",
    "SpotInstanceStatusTypeDef",
    "SpotMaintenanceStrategiesTypeDef",
    "SpotMarketOptionsTypeDef",
    "SpotOptionsRequestTypeDef",
    "SpotOptionsTypeDef",
    "SpotPlacementScoreTypeDef",
    "SpotPlacementTypeDef",
    "SpotPriceTypeDef",
    "StaleIpPermissionTypeDef",
    "StaleSecurityGroupTypeDef",
    "StartInstancesRequestInstanceStartTypeDef",
    "StartInstancesRequestRequestTypeDef",
    "StartInstancesResultTypeDef",
    "StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    "StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    "StartNetworkInsightsAnalysisRequestRequestTypeDef",
    "StartNetworkInsightsAnalysisResultTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    "StateReasonResponseMetadataTypeDef",
    "StateReasonTypeDef",
    "StopInstancesRequestInstanceStopTypeDef",
    "StopInstancesRequestRequestTypeDef",
    "StopInstancesResultTypeDef",
    "StorageLocationTypeDef",
    "StorageTypeDef",
    "StoreImageTaskResultTypeDef",
    "SubnetAssociationTypeDef",
    "SubnetCidrBlockStateTypeDef",
    "SubnetCidrReservationTypeDef",
    "SubnetIpv6CidrBlockAssociationTypeDef",
    "SubnetTypeDef",
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    "TagDescriptionTypeDef",
    "TagSpecificationTypeDef",
    "TagTypeDef",
    "TargetCapacitySpecificationRequestTypeDef",
    "TargetCapacitySpecificationTypeDef",
    "TargetConfigurationRequestTypeDef",
    "TargetConfigurationTypeDef",
    "TargetGroupTypeDef",
    "TargetGroupsConfigTypeDef",
    "TargetNetworkTypeDef",
    "TargetReservationValueTypeDef",
    "TerminateClientVpnConnectionsRequestRequestTypeDef",
    "TerminateClientVpnConnectionsResultTypeDef",
    "TerminateConnectionStatusTypeDef",
    "TerminateInstancesRequestInstanceTerminateTypeDef",
    "TerminateInstancesRequestRequestTypeDef",
    "TerminateInstancesResultTypeDef",
    "ThroughResourcesStatementRequestTypeDef",
    "ThroughResourcesStatementTypeDef",
    "TotalLocalStorageGBRequestTypeDef",
    "TotalLocalStorageGBTypeDef",
    "TrafficMirrorFilterRuleTypeDef",
    "TrafficMirrorFilterTypeDef",
    "TrafficMirrorPortRangeRequestTypeDef",
    "TrafficMirrorPortRangeTypeDef",
    "TrafficMirrorSessionTypeDef",
    "TrafficMirrorTargetTypeDef",
    "TransitGatewayAssociationTypeDef",
    "TransitGatewayAttachmentAssociationTypeDef",
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    "TransitGatewayAttachmentPropagationTypeDef",
    "TransitGatewayAttachmentTypeDef",
    "TransitGatewayConnectOptionsTypeDef",
    "TransitGatewayConnectPeerConfigurationTypeDef",
    "TransitGatewayConnectPeerTypeDef",
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    "TransitGatewayConnectTypeDef",
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    "TransitGatewayMulticastDomainAssociationTypeDef",
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    "TransitGatewayMulticastDomainOptionsTypeDef",
    "TransitGatewayMulticastDomainTypeDef",
    "TransitGatewayMulticastGroupTypeDef",
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    "TransitGatewayOptionsTypeDef",
    "TransitGatewayPeeringAttachmentTypeDef",
    "TransitGatewayPrefixListAttachmentTypeDef",
    "TransitGatewayPrefixListReferenceTypeDef",
    "TransitGatewayPropagationTypeDef",
    "TransitGatewayRequestOptionsTypeDef",
    "TransitGatewayRouteAttachmentTypeDef",
    "TransitGatewayRouteTableAssociationTypeDef",
    "TransitGatewayRouteTablePropagationTypeDef",
    "TransitGatewayRouteTableTypeDef",
    "TransitGatewayRouteTypeDef",
    "TransitGatewayTypeDef",
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    "TransitGatewayVpcAttachmentTypeDef",
    "TrunkInterfaceAssociationTypeDef",
    "TunnelOptionTypeDef",
    "UnassignIpv6AddressesRequestRequestTypeDef",
    "UnassignIpv6AddressesResultTypeDef",
    "UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef",
    "UnassignPrivateIpAddressesRequestRequestTypeDef",
    "UnmonitorInstancesRequestInstanceUnmonitorTypeDef",
    "UnmonitorInstancesRequestRequestTypeDef",
    "UnmonitorInstancesResultTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    "UnsuccessfulItemErrorTypeDef",
    "UnsuccessfulItemTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    "UserBucketDetailsTypeDef",
    "UserBucketTypeDef",
    "UserDataTypeDef",
    "UserIdGroupPairTypeDef",
    "VCpuCountRangeRequestTypeDef",
    "VCpuCountRangeTypeDef",
    "VCpuInfoTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "VgwTelemetryTypeDef",
    "VolumeAttachmentResponseMetadataTypeDef",
    "VolumeAttachmentTypeDef",
    "VolumeDetailTypeDef",
    "VolumeModificationTypeDef",
    "VolumeResponseMetadataTypeDef",
    "VolumeStatusActionTypeDef",
    "VolumeStatusAttachmentStatusTypeDef",
    "VolumeStatusDetailsTypeDef",
    "VolumeStatusEventTypeDef",
    "VolumeStatusInfoTypeDef",
    "VolumeStatusItemTypeDef",
    "VolumeTypeDef",
    "VpcAttachmentTypeDef",
    "VpcCidrBlockAssociationTypeDef",
    "VpcCidrBlockStateTypeDef",
    "VpcClassicLinkTypeDef",
    "VpcEndpointConnectionTypeDef",
    "VpcEndpointTypeDef",
    "VpcIpv6CidrBlockAssociationTypeDef",
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    "VpcPeeringConnectionStateReasonResponseMetadataTypeDef",
    "VpcPeeringConnectionStateReasonTypeDef",
    "VpcPeeringConnectionTypeDef",
    "VpcPeeringConnectionVpcInfoResponseMetadataTypeDef",
    "VpcPeeringConnectionVpcInfoTypeDef",
    "VpcTypeDef",
    "VpnConnectionDeviceTypeTypeDef",
    "VpnConnectionOptionsSpecificationTypeDef",
    "VpnConnectionOptionsTypeDef",
    "VpnConnectionTypeDef",
    "VpnGatewayTypeDef",
    "VpnStaticRouteTypeDef",
    "VpnTunnelOptionsSpecificationTypeDef",
    "WaiterConfigTypeDef",
    "WithdrawByoipCidrRequestRequestTypeDef",
    "WithdrawByoipCidrResultTypeDef",
)

AcceleratorCountRequestTypeDef = TypedDict(
    "AcceleratorCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AcceleratorCountTypeDef = TypedDict(
    "AcceleratorCountTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AcceleratorTotalMemoryMiBRequestTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AcceleratorTotalMemoryMiBTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "ReservedInstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
        "TargetConfigurations": NotRequired[Sequence["TargetConfigurationRequestTypeDef"]],
    },
)

AcceptReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    {
        "ExchangeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

AcceptTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

AcceptTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

AcceptVpcEndpointConnectionsResultTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

AcceptVpcPeeringConnectionResultTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionResultTypeDef",
    {
        "VpcPeeringConnection": "VpcPeeringConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessScopeAnalysisFindingTypeDef = TypedDict(
    "AccessScopeAnalysisFindingTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": NotRequired[str],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "FindingId": NotRequired[str],
        "FindingComponents": NotRequired[List["PathComponentTypeDef"]],
    },
)

AccessScopePathRequestTypeDef = TypedDict(
    "AccessScopePathRequestTypeDef",
    {
        "Source": NotRequired["PathStatementRequestTypeDef"],
        "Destination": NotRequired["PathStatementRequestTypeDef"],
        "ThroughResources": NotRequired[Sequence["ThroughResourcesStatementRequestTypeDef"]],
    },
)

AccessScopePathTypeDef = TypedDict(
    "AccessScopePathTypeDef",
    {
        "Source": NotRequired["PathStatementTypeDef"],
        "Destination": NotRequired["PathStatementTypeDef"],
        "ThroughResources": NotRequired[List["ThroughResourcesStatementTypeDef"]],
    },
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List["AccountAttributeValueTypeDef"]],
    },
)

AccountAttributeValueTypeDef = TypedDict(
    "AccountAttributeValueTypeDef",
    {
        "AttributeValue": NotRequired[str],
    },
)

ActiveInstanceTypeDef = TypedDict(
    "ActiveInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "SpotInstanceRequestId": NotRequired[str],
        "InstanceHealth": NotRequired[InstanceHealthStatusType],
    },
)

AddIpamOperatingRegionTypeDef = TypedDict(
    "AddIpamOperatingRegionTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)

AddPrefixListEntryTypeDef = TypedDict(
    "AddPrefixListEntryTypeDef",
    {
        "Cidr": str,
        "Description": NotRequired[str],
    },
)

AddressAttributeTypeDef = TypedDict(
    "AddressAttributeTypeDef",
    {
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "PtrRecord": NotRequired[str],
        "PtrRecordUpdate": NotRequired["PtrUpdateStatusTypeDef"],
    },
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "Domain": NotRequired[DomainTypeType],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfaceOwnerId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "CustomerOwnedIp": NotRequired[str],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "CarrierIp": NotRequired[str],
    },
)

AdvertiseByoipCidrRequestRequestTypeDef = TypedDict(
    "AdvertiseByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)

AdvertiseByoipCidrResultTypeDef = TypedDict(
    "AdvertiseByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateAddressRequestRequestTypeDef = TypedDict(
    "AllocateAddressRequestRequestTypeDef",
    {
        "Domain": NotRequired[DomainTypeType],
        "Address": NotRequired[str],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

AllocateAddressResultTypeDef = TypedDict(
    "AllocateAddressResultTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "Domain": DomainTypeType,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateHostsRequestRequestTypeDef = TypedDict(
    "AllocateHostsRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Quantity": int,
        "AutoPlacement": NotRequired[AutoPlacementType],
        "ClientToken": NotRequired[str],
        "InstanceType": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "HostRecovery": NotRequired[HostRecoveryType],
    },
)

AllocateHostsResultTypeDef = TypedDict(
    "AllocateHostsResultTypeDef",
    {
        "HostIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "AllocateIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cidr": NotRequired[str],
        "NetmaskLength": NotRequired[int],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "PreviewNextCidr": NotRequired[bool],
        "DisallowedCidrs": NotRequired[Sequence[str]],
    },
)

AllocateIpamPoolCidrResultTypeDef = TypedDict(
    "AllocateIpamPoolCidrResultTypeDef",
    {
        "IpamPoolAllocation": "IpamPoolAllocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllowedPrincipalTypeDef = TypedDict(
    "AllowedPrincipalTypeDef",
    {
        "PrincipalType": NotRequired[PrincipalTypeType],
        "Principal": NotRequired[str],
    },
)

AlternatePathHintTypeDef = TypedDict(
    "AlternatePathHintTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentArn": NotRequired[str],
    },
)

AnalysisAclRuleTypeDef = TypedDict(
    "AnalysisAclRuleTypeDef",
    {
        "Cidr": NotRequired[str],
        "Egress": NotRequired[bool],
        "PortRange": NotRequired["PortRangeTypeDef"],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "RuleNumber": NotRequired[int],
    },
)

AnalysisComponentTypeDef = TypedDict(
    "AnalysisComponentTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

AnalysisLoadBalancerListenerTypeDef = TypedDict(
    "AnalysisLoadBalancerListenerTypeDef",
    {
        "LoadBalancerPort": NotRequired[int],
        "InstancePort": NotRequired[int],
    },
)

AnalysisLoadBalancerTargetTypeDef = TypedDict(
    "AnalysisLoadBalancerTargetTypeDef",
    {
        "Address": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Instance": NotRequired["AnalysisComponentTypeDef"],
        "Port": NotRequired[int],
    },
)

AnalysisPacketHeaderTypeDef = TypedDict(
    "AnalysisPacketHeaderTypeDef",
    {
        "DestinationAddresses": NotRequired[List[str]],
        "DestinationPortRanges": NotRequired[List["PortRangeTypeDef"]],
        "Protocol": NotRequired[str],
        "SourceAddresses": NotRequired[List[str]],
        "SourcePortRanges": NotRequired[List["PortRangeTypeDef"]],
    },
)

AnalysisRouteTableRouteTypeDef = TypedDict(
    "AnalysisRouteTableRouteTypeDef",
    {
        "DestinationCidr": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "Origin": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

AnalysisSecurityGroupRuleTypeDef = TypedDict(
    "AnalysisSecurityGroupRuleTypeDef",
    {
        "Cidr": NotRequired[str],
        "Direction": NotRequired[str],
        "SecurityGroupId": NotRequired[str],
        "PortRange": NotRequired["PortRangeTypeDef"],
        "PrefixListId": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)

ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "AssignIpv6AddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[str]],
        "Ipv6PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[str]],
    },
)

AssignIpv6AddressesResultTypeDef = TypedDict(
    "AssignIpv6AddressesResultTypeDef",
    {
        "AssignedIpv6Addresses": List[str],
        "AssignedIpv6Prefixes": List[str],
        "NetworkInterfaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef = TypedDict(
    "AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef",
    {
        "AllowReassignment": NotRequired[bool],
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
        "Ipv4PrefixCount": NotRequired[int],
    },
)

AssignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "AssignPrivateIpAddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "AllowReassignment": NotRequired[bool],
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
        "Ipv4PrefixCount": NotRequired[int],
    },
)

AssignPrivateIpAddressesResultTypeDef = TypedDict(
    "AssignPrivateIpAddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "AssignedPrivateIpAddresses": List["AssignedPrivateIpAddressTypeDef"],
        "AssignedIpv4Prefixes": List["Ipv4PrefixSpecificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignedPrivateIpAddressTypeDef = TypedDict(
    "AssignedPrivateIpAddressTypeDef",
    {
        "PrivateIpAddress": NotRequired[str],
    },
)

AssociateAddressRequestClassicAddressAssociateTypeDef = TypedDict(
    "AssociateAddressRequestClassicAddressAssociateTypeDef",
    {
        "AllocationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AllowReassociation": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

AssociateAddressRequestRequestTypeDef = TypedDict(
    "AssociateAddressRequestRequestTypeDef",
    {
        "AllocationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllowReassociation": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

AssociateAddressRequestVpcAddressAssociateTypeDef = TypedDict(
    "AssociateAddressRequestVpcAddressAssociateTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllowReassociation": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

AssociateAddressResultTypeDef = TypedDict(
    "AssociateAddressResultTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "SubnetId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

AssociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkResultTypeDef",
    {
        "AssociationId": str,
        "Status": "AssociationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef = TypedDict(
    "AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

AssociateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "AssociateDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef = TypedDict(
    "AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef",
    {
        "DhcpOptionsId": str,
        "DryRun": NotRequired[bool],
    },
)

AssociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

AssociateEnclaveCertificateIamRoleResultTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    {
        "CertificateS3BucketName": str,
        "CertificateS3ObjectKey": str,
        "EncryptionKmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIamInstanceProfileRequestRequestTypeDef = TypedDict(
    "AssociateIamInstanceProfileRequestRequestTypeDef",
    {
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceId": str,
    },
)

AssociateIamInstanceProfileResultTypeDef = TypedDict(
    "AssociateIamInstanceProfileResultTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "AssociateInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "AssociationTarget": "InstanceEventWindowAssociationRequestTypeDef",
        "DryRun": NotRequired[bool],
    },
)

AssociateInstanceEventWindowResultTypeDef = TypedDict(
    "AssociateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateRouteTableRequestRequestTypeDef = TypedDict(
    "AssociateRouteTableRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
        "SubnetId": NotRequired[str],
        "GatewayId": NotRequired[str],
    },
)

AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef = TypedDict(
    "AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef",
    {
        "DryRun": NotRequired[bool],
        "SubnetId": NotRequired[str],
        "GatewayId": NotRequired[str],
    },
)

AssociateRouteTableResultTypeDef = TypedDict(
    "AssociateRouteTableResultTypeDef",
    {
        "AssociationId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSubnetCidrBlockRequestRequestTypeDef = TypedDict(
    "AssociateSubnetCidrBlockRequestRequestTypeDef",
    {
        "Ipv6CidrBlock": str,
        "SubnetId": str,
    },
)

AssociateSubnetCidrBlockResultTypeDef = TypedDict(
    "AssociateSubnetCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef",
        "SubnetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

AssociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

AssociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableResultTypeDef",
    {
        "Association": "TransitGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "AssociateTrunkInterfaceRequestRequestTypeDef",
    {
        "BranchInterfaceId": str,
        "TrunkInterfaceId": str,
        "VlanId": NotRequired[int],
        "GreKey": NotRequired[int],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

AssociateTrunkInterfaceResultTypeDef = TypedDict(
    "AssociateTrunkInterfaceResultTypeDef",
    {
        "InterfaceAssociation": "TrunkInterfaceAssociationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "AssociateVpcCidrBlockRequestRequestTypeDef",
    {
        "VpcId": str,
        "AmazonProvidedIpv6CidrBlock": NotRequired[bool],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlockNetworkBorderGroup": NotRequired[str],
        "Ipv6Pool": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
    },
)

AssociateVpcCidrBlockResultTypeDef = TypedDict(
    "AssociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatedRoleTypeDef = TypedDict(
    "AssociatedRoleTypeDef",
    {
        "AssociatedRoleArn": NotRequired[str],
        "CertificateS3BucketName": NotRequired[str],
        "CertificateS3ObjectKey": NotRequired[str],
        "EncryptionKmsKeyId": NotRequired[str],
    },
)

AssociatedTargetNetworkTypeDef = TypedDict(
    "AssociatedTargetNetworkTypeDef",
    {
        "NetworkId": NotRequired[str],
        "NetworkType": NotRequired[Literal["vpc"]],
    },
)

AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Code": NotRequired[AssociationStatusCodeType],
        "Message": NotRequired[str],
    },
)

AthenaIntegrationTypeDef = TypedDict(
    "AthenaIntegrationTypeDef",
    {
        "IntegrationResultS3DestinationArn": str,
        "PartitionLoadFrequency": PartitionLoadFrequencyType,
        "PartitionStartDate": NotRequired[Union[datetime, str]],
        "PartitionEndDate": NotRequired[Union[datetime, str]],
    },
)

AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef = TypedDict(
    "AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef",
    {
        "Groups": Sequence[str],
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "AttachClassicLinkVpcRequestRequestTypeDef",
    {
        "Groups": Sequence[str],
        "InstanceId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef = TypedDict(
    "AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef",
    {
        "Groups": Sequence[str],
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachClassicLinkVpcResultTypeDef = TypedDict(
    "AttachClassicLinkVpcResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef = TypedDict(
    "AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachInternetGatewayRequestRequestTypeDef = TypedDict(
    "AttachInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef = TypedDict(
    "AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef",
    {
        "InternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef = TypedDict(
    "AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "NetworkCardIndex": NotRequired[int],
    },
)

AttachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "AttachNetworkInterfaceRequestRequestTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
        "NetworkInterfaceId": str,
        "DryRun": NotRequired[bool],
        "NetworkCardIndex": NotRequired[int],
    },
)

AttachNetworkInterfaceResultTypeDef = TypedDict(
    "AttachNetworkInterfaceResultTypeDef",
    {
        "AttachmentId": str,
        "NetworkCardIndex": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachVolumeRequestInstanceAttachVolumeTypeDef = TypedDict(
    "AttachVolumeRequestInstanceAttachVolumeTypeDef",
    {
        "Device": str,
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachVolumeRequestRequestTypeDef = TypedDict(
    "AttachVolumeRequestRequestTypeDef",
    {
        "Device": str,
        "InstanceId": str,
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachVolumeRequestVolumeAttachToInstanceTypeDef = TypedDict(
    "AttachVolumeRequestVolumeAttachToInstanceTypeDef",
    {
        "Device": str,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachVpnGatewayRequestRequestTypeDef = TypedDict(
    "AttachVpnGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

AttachVpnGatewayResultTypeDef = TypedDict(
    "AttachVpnGatewayResultTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeBooleanValueTypeDef = TypedDict(
    "AttributeBooleanValueTypeDef",
    {
        "Value": NotRequired[bool],
    },
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

AuthorizationRuleTypeDef = TypedDict(
    "AuthorizationRuleTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "GroupId": NotRequired[str],
        "AccessAll": NotRequired[bool],
        "DestinationCidr": NotRequired[str],
        "Status": NotRequired["ClientVpnAuthorizationRuleStatusTypeDef"],
    },
)

AuthorizeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "AuthorizeClientVpnIngressRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
        "AccessGroupId": NotRequired[str],
        "AuthorizeAllGroups": NotRequired[bool],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

AuthorizeClientVpnIngressResultTypeDef = TypedDict(
    "AuthorizeClientVpnIngressResultTypeDef",
    {
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressRequestRequestTypeDef",
    {
        "GroupId": str,
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)

AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)

AuthorizeSecurityGroupEgressResultTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressResultTypeDef",
    {
        "Return": bool,
        "SecurityGroupRules": List["SecurityGroupRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeSecurityGroupIngressRequestRequestTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestRequestTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

AuthorizeSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressResultTypeDef",
    {
        "Return": bool,
        "SecurityGroupRules": List["SecurityGroupRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneMessageTypeDef = TypedDict(
    "AvailabilityZoneMessageTypeDef",
    {
        "Message": NotRequired[str],
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "State": NotRequired[AvailabilityZoneStateType],
        "OptInStatus": NotRequired[AvailabilityZoneOptInStatusType],
        "Messages": NotRequired[List["AvailabilityZoneMessageTypeDef"]],
        "RegionName": NotRequired[str],
        "ZoneName": NotRequired[str],
        "ZoneId": NotRequired[str],
        "GroupName": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "ZoneType": NotRequired[str],
        "ParentZoneName": NotRequired[str],
        "ParentZoneId": NotRequired[str],
    },
)

AvailableCapacityTypeDef = TypedDict(
    "AvailableCapacityTypeDef",
    {
        "AvailableInstanceCapacity": NotRequired[List["InstanceCapacityTypeDef"]],
        "AvailableVCpus": NotRequired[int],
    },
)

BaselineEbsBandwidthMbpsRequestTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

BaselineEbsBandwidthMbpsTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

BlobAttributeValueTypeDef = TypedDict(
    "BlobAttributeValueTypeDef",
    {
        "Value": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired["EbsBlockDeviceTypeDef"],
        "NoDevice": NotRequired[str],
    },
)

BundleInstanceRequestRequestTypeDef = TypedDict(
    "BundleInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Storage": "StorageTypeDef",
        "DryRun": NotRequired[bool],
    },
)

BundleInstanceResultTypeDef = TypedDict(
    "BundleInstanceResultTypeDef",
    {
        "BundleTask": "BundleTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BundleTaskErrorTypeDef = TypedDict(
    "BundleTaskErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

BundleTaskTypeDef = TypedDict(
    "BundleTaskTypeDef",
    {
        "BundleId": NotRequired[str],
        "BundleTaskError": NotRequired["BundleTaskErrorTypeDef"],
        "InstanceId": NotRequired[str],
        "Progress": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "State": NotRequired[BundleTaskStateType],
        "Storage": NotRequired["StorageTypeDef"],
        "UpdateTime": NotRequired[datetime],
    },
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": NotRequired[str],
        "Description": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "State": NotRequired[ByoipCidrStateType],
    },
)

CancelBundleTaskRequestRequestTypeDef = TypedDict(
    "CancelBundleTaskRequestRequestTypeDef",
    {
        "BundleId": str,
        "DryRun": NotRequired[bool],
    },
)

CancelBundleTaskResultTypeDef = TypedDict(
    "CancelBundleTaskResultTypeDef",
    {
        "BundleTask": "BundleTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelCapacityReservationFleetErrorTypeDef = TypedDict(
    "CancelCapacityReservationFleetErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

CancelCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "CancelCapacityReservationFleetsRequestRequestTypeDef",
    {
        "CapacityReservationFleetIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

CancelCapacityReservationFleetsResultTypeDef = TypedDict(
    "CancelCapacityReservationFleetsResultTypeDef",
    {
        "SuccessfulFleetCancellations": List["CapacityReservationFleetCancellationStateTypeDef"],
        "FailedFleetCancellations": List["FailedCapacityReservationFleetCancellationResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelCapacityReservationRequestRequestTypeDef = TypedDict(
    "CancelCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "DryRun": NotRequired[bool],
    },
)

CancelCapacityReservationResultTypeDef = TypedDict(
    "CancelCapacityReservationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelConversionRequestRequestTypeDef = TypedDict(
    "CancelConversionRequestRequestTypeDef",
    {
        "ConversionTaskId": str,
        "DryRun": NotRequired[bool],
        "ReasonMessage": NotRequired[str],
    },
)

CancelExportTaskRequestRequestTypeDef = TypedDict(
    "CancelExportTaskRequestRequestTypeDef",
    {
        "ExportTaskId": str,
    },
)

CancelImportTaskRequestRequestTypeDef = TypedDict(
    "CancelImportTaskRequestRequestTypeDef",
    {
        "CancelReason": NotRequired[str],
        "DryRun": NotRequired[bool],
        "ImportTaskId": NotRequired[str],
    },
)

CancelImportTaskResultTypeDef = TypedDict(
    "CancelImportTaskResultTypeDef",
    {
        "ImportTaskId": str,
        "PreviousState": str,
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelReservedInstancesListingRequestRequestTypeDef = TypedDict(
    "CancelReservedInstancesListingRequestRequestTypeDef",
    {
        "ReservedInstancesListingId": str,
    },
)

CancelReservedInstancesListingResultTypeDef = TypedDict(
    "CancelReservedInstancesListingResultTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSpotFleetRequestsErrorItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorItemTypeDef",
    {
        "Error": NotRequired["CancelSpotFleetRequestsErrorTypeDef"],
        "SpotFleetRequestId": NotRequired[str],
    },
)

CancelSpotFleetRequestsErrorTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorTypeDef",
    {
        "Code": NotRequired[CancelBatchErrorCodeType],
        "Message": NotRequired[str],
    },
)

CancelSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "CancelSpotFleetRequestsRequestRequestTypeDef",
    {
        "SpotFleetRequestIds": Sequence[str],
        "TerminateInstances": bool,
        "DryRun": NotRequired[bool],
    },
)

CancelSpotFleetRequestsResponseTypeDef = TypedDict(
    "CancelSpotFleetRequestsResponseTypeDef",
    {
        "SuccessfulFleetRequests": List["CancelSpotFleetRequestsSuccessItemTypeDef"],
        "UnsuccessfulFleetRequests": List["CancelSpotFleetRequestsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSpotFleetRequestsSuccessItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    {
        "CurrentSpotFleetRequestState": NotRequired[BatchStateType],
        "PreviousSpotFleetRequestState": NotRequired[BatchStateType],
        "SpotFleetRequestId": NotRequired[str],
    },
)

CancelSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "CancelSpotInstanceRequestsRequestRequestTypeDef",
    {
        "SpotInstanceRequestIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

CancelSpotInstanceRequestsResultTypeDef = TypedDict(
    "CancelSpotInstanceRequestsResultTypeDef",
    {
        "CancelledSpotInstanceRequests": List["CancelledSpotInstanceRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelledSpotInstanceRequestTypeDef = TypedDict(
    "CancelledSpotInstanceRequestTypeDef",
    {
        "SpotInstanceRequestId": NotRequired[str],
        "State": NotRequired[CancelSpotInstanceRequestStateType],
    },
)

CapacityReservationFleetCancellationStateTypeDef = TypedDict(
    "CapacityReservationFleetCancellationStateTypeDef",
    {
        "CurrentFleetState": NotRequired[CapacityReservationFleetStateType],
        "PreviousFleetState": NotRequired[CapacityReservationFleetStateType],
        "CapacityReservationFleetId": NotRequired[str],
    },
)

CapacityReservationFleetTypeDef = TypedDict(
    "CapacityReservationFleetTypeDef",
    {
        "CapacityReservationFleetId": NotRequired[str],
        "CapacityReservationFleetArn": NotRequired[str],
        "State": NotRequired[CapacityReservationFleetStateType],
        "TotalTargetCapacity": NotRequired[int],
        "TotalFulfilledCapacity": NotRequired[float],
        "Tenancy": NotRequired[Literal["default"]],
        "EndDate": NotRequired[datetime],
        "CreateTime": NotRequired[datetime],
        "InstanceMatchCriteria": NotRequired[Literal["open"]],
        "AllocationStrategy": NotRequired[str],
        "InstanceTypeSpecifications": NotRequired[List["FleetCapacityReservationTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

CapacityReservationGroupTypeDef = TypedDict(
    "CapacityReservationGroupTypeDef",
    {
        "GroupArn": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)

CapacityReservationOptionsRequestTypeDef = TypedDict(
    "CapacityReservationOptionsRequestTypeDef",
    {
        "UsageStrategy": NotRequired[Literal["use-capacity-reservations-first"]],
    },
)

CapacityReservationOptionsTypeDef = TypedDict(
    "CapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": NotRequired[Literal["use-capacity-reservations-first"]],
    },
)

CapacityReservationSpecificationResponseResponseMetadataTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseResponseMetadataTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityReservationSpecificationResponseTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired["CapacityReservationTargetResponseTypeDef"],
    },
)

CapacityReservationSpecificationTypeDef = TypedDict(
    "CapacityReservationSpecificationTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired["CapacityReservationTargetTypeDef"],
    },
)

CapacityReservationTargetResponseTypeDef = TypedDict(
    "CapacityReservationTargetResponseTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)

CapacityReservationTargetTypeDef = TypedDict(
    "CapacityReservationTargetTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)

CapacityReservationTypeDef = TypedDict(
    "CapacityReservationTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "CapacityReservationArn": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "InstancePlatform": NotRequired[CapacityReservationInstancePlatformType],
        "AvailabilityZone": NotRequired[str],
        "Tenancy": NotRequired[CapacityReservationTenancyType],
        "TotalInstanceCount": NotRequired[int],
        "AvailableInstanceCount": NotRequired[int],
        "EbsOptimized": NotRequired[bool],
        "EphemeralStorage": NotRequired[bool],
        "State": NotRequired[CapacityReservationStateType],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "EndDateType": NotRequired[EndDateTypeType],
        "InstanceMatchCriteria": NotRequired[InstanceMatchCriteriaType],
        "CreateDate": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
        "OutpostArn": NotRequired[str],
        "CapacityReservationFleetId": NotRequired[str],
        "PlacementGroupArn": NotRequired[str],
    },
)

CarrierGatewayTypeDef = TypedDict(
    "CarrierGatewayTypeDef",
    {
        "CarrierGatewayId": NotRequired[str],
        "VpcId": NotRequired[str],
        "State": NotRequired[CarrierGatewayStateType],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

CertificateAuthenticationRequestTypeDef = TypedDict(
    "CertificateAuthenticationRequestTypeDef",
    {
        "ClientRootCertificateChainArn": NotRequired[str],
    },
)

CertificateAuthenticationTypeDef = TypedDict(
    "CertificateAuthenticationTypeDef",
    {
        "ClientRootCertificateChain": NotRequired[str],
    },
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)

CidrBlockTypeDef = TypedDict(
    "CidrBlockTypeDef",
    {
        "CidrBlock": NotRequired[str],
    },
)

ClassicLinkDnsSupportTypeDef = TypedDict(
    "ClassicLinkDnsSupportTypeDef",
    {
        "ClassicLinkDnsSupported": NotRequired[bool],
        "VpcId": NotRequired[str],
    },
)

ClassicLinkInstanceTypeDef = TypedDict(
    "ClassicLinkInstanceTypeDef",
    {
        "Groups": NotRequired[List["GroupIdentifierTypeDef"]],
        "InstanceId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

ClassicLoadBalancerTypeDef = TypedDict(
    "ClassicLoadBalancerTypeDef",
    {
        "Name": NotRequired[str],
    },
)

ClassicLoadBalancersConfigTypeDef = TypedDict(
    "ClassicLoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancers": NotRequired[List["ClassicLoadBalancerTypeDef"]],
    },
)

ClientCertificateRevocationListStatusTypeDef = TypedDict(
    "ClientCertificateRevocationListStatusTypeDef",
    {
        "Code": NotRequired[ClientCertificateRevocationListStatusCodeType],
        "Message": NotRequired[str],
    },
)

ClientConnectOptionsTypeDef = TypedDict(
    "ClientConnectOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LambdaFunctionArn": NotRequired[str],
    },
)

ClientConnectResponseOptionsTypeDef = TypedDict(
    "ClientConnectResponseOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LambdaFunctionArn": NotRequired[str],
        "Status": NotRequired["ClientVpnEndpointAttributeStatusTypeDef"],
    },
)

ClientDataTypeDef = TypedDict(
    "ClientDataTypeDef",
    {
        "Comment": NotRequired[str],
        "UploadEnd": NotRequired[Union[datetime, str]],
        "UploadSize": NotRequired[float],
        "UploadStart": NotRequired[Union[datetime, str]],
    },
)

ClientLoginBannerOptionsTypeDef = TypedDict(
    "ClientLoginBannerOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "BannerText": NotRequired[str],
    },
)

ClientLoginBannerResponseOptionsTypeDef = TypedDict(
    "ClientLoginBannerResponseOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "BannerText": NotRequired[str],
    },
)

ClientVpnAuthenticationRequestTypeDef = TypedDict(
    "ClientVpnAuthenticationRequestTypeDef",
    {
        "Type": NotRequired[ClientVpnAuthenticationTypeType],
        "ActiveDirectory": NotRequired["DirectoryServiceAuthenticationRequestTypeDef"],
        "MutualAuthentication": NotRequired["CertificateAuthenticationRequestTypeDef"],
        "FederatedAuthentication": NotRequired["FederatedAuthenticationRequestTypeDef"],
    },
)

ClientVpnAuthenticationTypeDef = TypedDict(
    "ClientVpnAuthenticationTypeDef",
    {
        "Type": NotRequired[ClientVpnAuthenticationTypeType],
        "ActiveDirectory": NotRequired["DirectoryServiceAuthenticationTypeDef"],
        "MutualAuthentication": NotRequired["CertificateAuthenticationTypeDef"],
        "FederatedAuthentication": NotRequired["FederatedAuthenticationTypeDef"],
    },
)

ClientVpnAuthorizationRuleStatusTypeDef = TypedDict(
    "ClientVpnAuthorizationRuleStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnAuthorizationRuleStatusCodeType],
        "Message": NotRequired[str],
    },
)

ClientVpnConnectionStatusTypeDef = TypedDict(
    "ClientVpnConnectionStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnConnectionStatusCodeType],
        "Message": NotRequired[str],
    },
)

ClientVpnConnectionTypeDef = TypedDict(
    "ClientVpnConnectionTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Timestamp": NotRequired[str],
        "ConnectionId": NotRequired[str],
        "Username": NotRequired[str],
        "ConnectionEstablishedTime": NotRequired[str],
        "IngressBytes": NotRequired[str],
        "EgressBytes": NotRequired[str],
        "IngressPackets": NotRequired[str],
        "EgressPackets": NotRequired[str],
        "ClientIp": NotRequired[str],
        "CommonName": NotRequired[str],
        "Status": NotRequired["ClientVpnConnectionStatusTypeDef"],
        "ConnectionEndTime": NotRequired[str],
        "PostureComplianceStatuses": NotRequired[List[str]],
    },
)

ClientVpnEndpointAttributeStatusTypeDef = TypedDict(
    "ClientVpnEndpointAttributeStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnEndpointAttributeStatusCodeType],
        "Message": NotRequired[str],
    },
)

ClientVpnEndpointStatusTypeDef = TypedDict(
    "ClientVpnEndpointStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnEndpointStatusCodeType],
        "Message": NotRequired[str],
    },
)

ClientVpnEndpointTypeDef = TypedDict(
    "ClientVpnEndpointTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired["ClientVpnEndpointStatusTypeDef"],
        "CreationTime": NotRequired[str],
        "DeletionTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "ClientCidrBlock": NotRequired[str],
        "DnsServers": NotRequired[List[str]],
        "SplitTunnel": NotRequired[bool],
        "VpnProtocol": NotRequired[Literal["openvpn"]],
        "TransportProtocol": NotRequired[TransportProtocolType],
        "VpnPort": NotRequired[int],
        "AssociatedTargetNetworks": NotRequired[List["AssociatedTargetNetworkTypeDef"]],
        "ServerCertificateArn": NotRequired[str],
        "AuthenticationOptions": NotRequired[List["ClientVpnAuthenticationTypeDef"]],
        "ConnectionLogOptions": NotRequired["ConnectionLogResponseOptionsTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "SecurityGroupIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortalUrl": NotRequired[str],
        "ClientConnectOptions": NotRequired["ClientConnectResponseOptionsTypeDef"],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired["ClientLoginBannerResponseOptionsTypeDef"],
    },
)

ClientVpnRouteStatusTypeDef = TypedDict(
    "ClientVpnRouteStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnRouteStatusCodeType],
        "Message": NotRequired[str],
    },
)

ClientVpnRouteTypeDef = TypedDict(
    "ClientVpnRouteTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "DestinationCidr": NotRequired[str],
        "TargetSubnet": NotRequired[str],
        "Type": NotRequired[str],
        "Origin": NotRequired[str],
        "Status": NotRequired["ClientVpnRouteStatusTypeDef"],
        "Description": NotRequired[str],
    },
)

CoipAddressUsageTypeDef = TypedDict(
    "CoipAddressUsageTypeDef",
    {
        "AllocationId": NotRequired[str],
        "AwsAccountId": NotRequired[str],
        "AwsService": NotRequired[str],
        "CoIp": NotRequired[str],
    },
)

CoipPoolTypeDef = TypedDict(
    "CoipPoolTypeDef",
    {
        "PoolId": NotRequired[str],
        "PoolCidrs": NotRequired[List[str]],
        "LocalGatewayRouteTableId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "PoolArn": NotRequired[str],
    },
)

ConfirmProductInstanceRequestRequestTypeDef = TypedDict(
    "ConfirmProductInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ProductCode": str,
        "DryRun": NotRequired[bool],
    },
)

ConfirmProductInstanceResultTypeDef = TypedDict(
    "ConfirmProductInstanceResultTypeDef",
    {
        "OwnerId": str,
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionLogOptionsTypeDef = TypedDict(
    "ConnectionLogOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "CloudwatchLogGroup": NotRequired[str],
        "CloudwatchLogStream": NotRequired[str],
    },
)

ConnectionLogResponseOptionsTypeDef = TypedDict(
    "ConnectionLogResponseOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "CloudwatchLogGroup": NotRequired[str],
        "CloudwatchLogStream": NotRequired[str],
    },
)

ConnectionNotificationTypeDef = TypedDict(
    "ConnectionNotificationTypeDef",
    {
        "ConnectionNotificationId": NotRequired[str],
        "ServiceId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
        "ConnectionNotificationType": NotRequired[Literal["Topic"]],
        "ConnectionNotificationArn": NotRequired[str],
        "ConnectionEvents": NotRequired[List[str]],
        "ConnectionNotificationState": NotRequired[ConnectionNotificationStateType],
    },
)

ConversionTaskTypeDef = TypedDict(
    "ConversionTaskTypeDef",
    {
        "ConversionTaskId": NotRequired[str],
        "ExpirationTime": NotRequired[str],
        "ImportInstance": NotRequired["ImportInstanceTaskDetailsTypeDef"],
        "ImportVolume": NotRequired["ImportVolumeTaskDetailsTypeDef"],
        "State": NotRequired[ConversionTaskStateType],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

CopyFpgaImageRequestRequestTypeDef = TypedDict(
    "CopyFpgaImageRequestRequestTypeDef",
    {
        "SourceFpgaImageId": str,
        "SourceRegion": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

CopyFpgaImageResultTypeDef = TypedDict(
    "CopyFpgaImageResultTypeDef",
    {
        "FpgaImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyImageRequestRequestTypeDef = TypedDict(
    "CopyImageRequestRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DestinationOutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

CopyImageResultTypeDef = TypedDict(
    "CopyImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopySnapshotRequestRequestTypeDef = TypedDict(
    "CopySnapshotRequestRequestTypeDef",
    {
        "SourceRegion": str,
        "SourceSnapshotId": str,
        "Description": NotRequired[str],
        "DestinationOutpostArn": NotRequired[str],
        "DestinationRegion": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PresignedUrl": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CopySnapshotRequestSnapshotCopyTypeDef = TypedDict(
    "CopySnapshotRequestSnapshotCopyTypeDef",
    {
        "SourceRegion": str,
        "Description": NotRequired[str],
        "DestinationOutpostArn": NotRequired[str],
        "DestinationRegion": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PresignedUrl": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CpuOptionsRequestTypeDef = TypedDict(
    "CpuOptionsRequestTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
    },
)

CpuOptionsResponseMetadataTypeDef = TypedDict(
    "CpuOptionsResponseMetadataTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
    },
)

CreateCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "CreateCapacityReservationFleetRequestRequestTypeDef",
    {
        "InstanceTypeSpecifications": Sequence["ReservationFleetInstanceSpecificationTypeDef"],
        "TotalTargetCapacity": int,
        "AllocationStrategy": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tenancy": NotRequired[Literal["default"]],
        "EndDate": NotRequired[Union[datetime, str]],
        "InstanceMatchCriteria": NotRequired[Literal["open"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateCapacityReservationFleetResultTypeDef = TypedDict(
    "CreateCapacityReservationFleetResultTypeDef",
    {
        "CapacityReservationFleetId": str,
        "State": CapacityReservationFleetStateType,
        "TotalTargetCapacity": int,
        "TotalFulfilledCapacity": float,
        "InstanceMatchCriteria": Literal["open"],
        "AllocationStrategy": str,
        "CreateTime": datetime,
        "EndDate": datetime,
        "Tenancy": Literal["default"],
        "FleetCapacityReservations": List["FleetCapacityReservationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCapacityReservationRequestRequestTypeDef = TypedDict(
    "CreateCapacityReservationRequestRequestTypeDef",
    {
        "InstanceType": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "InstanceCount": int,
        "ClientToken": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Tenancy": NotRequired[CapacityReservationTenancyType],
        "EbsOptimized": NotRequired[bool],
        "EphemeralStorage": NotRequired[bool],
        "EndDate": NotRequired[Union[datetime, str]],
        "EndDateType": NotRequired[EndDateTypeType],
        "InstanceMatchCriteria": NotRequired[InstanceMatchCriteriaType],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
        "OutpostArn": NotRequired[str],
        "PlacementGroupArn": NotRequired[str],
    },
)

CreateCapacityReservationResultTypeDef = TypedDict(
    "CreateCapacityReservationResultTypeDef",
    {
        "CapacityReservation": "CapacityReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCarrierGatewayRequestRequestTypeDef = TypedDict(
    "CreateCarrierGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

CreateCarrierGatewayResultTypeDef = TypedDict(
    "CreateCarrierGatewayResultTypeDef",
    {
        "CarrierGateway": "CarrierGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "CreateClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientCidrBlock": str,
        "ServerCertificateArn": str,
        "AuthenticationOptions": Sequence["ClientVpnAuthenticationRequestTypeDef"],
        "ConnectionLogOptions": "ConnectionLogOptionsTypeDef",
        "DnsServers": NotRequired[Sequence[str]],
        "TransportProtocol": NotRequired[TransportProtocolType],
        "VpnPort": NotRequired[int],
        "Description": NotRequired[str],
        "SplitTunnel": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortal": NotRequired[SelfServicePortalType],
        "ClientConnectOptions": NotRequired["ClientConnectOptionsTypeDef"],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired["ClientLoginBannerOptionsTypeDef"],
    },
)

CreateClientVpnEndpointResultTypeDef = TypedDict(
    "CreateClientVpnEndpointResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Status": "ClientVpnEndpointStatusTypeDef",
        "DnsName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClientVpnRouteRequestRequestTypeDef = TypedDict(
    "CreateClientVpnRouteRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
        "TargetVpcSubnetId": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

CreateClientVpnRouteResultTypeDef = TypedDict(
    "CreateClientVpnRouteResultTypeDef",
    {
        "Status": "ClientVpnRouteStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "CreateCustomerGatewayRequestRequestTypeDef",
    {
        "BgpAsn": int,
        "Type": Literal["ipsec.1"],
        "PublicIp": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DeviceName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

CreateCustomerGatewayResultTypeDef = TypedDict(
    "CreateCustomerGatewayResultTypeDef",
    {
        "CustomerGateway": "CustomerGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDefaultSubnetRequestRequestTypeDef = TypedDict(
    "CreateDefaultSubnetRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
    },
)

CreateDefaultSubnetResultTypeDef = TypedDict(
    "CreateDefaultSubnetResultTypeDef",
    {
        "Subnet": "SubnetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDefaultVpcRequestRequestTypeDef = TypedDict(
    "CreateDefaultVpcRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

CreateDefaultVpcResultTypeDef = TypedDict(
    "CreateDefaultVpcResultTypeDef",
    {
        "Vpc": "VpcTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "CreateDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpConfigurations": Sequence["NewDhcpConfigurationTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef = TypedDict(
    "CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef",
    {
        "DhcpConfigurations": Sequence["NewDhcpConfigurationTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateDhcpOptionsResultTypeDef = TypedDict(
    "CreateDhcpOptionsResultTypeDef",
    {
        "DhcpOptions": "DhcpOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    {
        "ClientToken": str,
        "EgressOnlyInternetGateway": "EgressOnlyInternetGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetErrorTypeDef = TypedDict(
    "CreateFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired["LaunchTemplateAndOverridesResponseTypeDef"],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

CreateFleetInstanceTypeDef = TypedDict(
    "CreateFleetInstanceTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired["LaunchTemplateAndOverridesResponseTypeDef"],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "InstanceIds": NotRequired[List[str]],
        "InstanceType": NotRequired[InstanceTypeType],
        "Platform": NotRequired[Literal["Windows"]],
    },
)

CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "LaunchTemplateConfigs": Sequence["FleetLaunchTemplateConfigRequestTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationRequestTypeDef",
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "SpotOptions": NotRequired["SpotOptionsRequestTypeDef"],
        "OnDemandOptions": NotRequired["OnDemandOptionsRequestTypeDef"],
        "ExcessCapacityTerminationPolicy": NotRequired[FleetExcessCapacityTerminationPolicyType],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[Union[datetime, str]],
        "ValidUntil": NotRequired[Union[datetime, str]],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "Context": NotRequired[str],
    },
)

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "FleetId": str,
        "Errors": List["CreateFleetErrorTypeDef"],
        "Instances": List["CreateFleetInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFlowLogsRequestRequestTypeDef = TypedDict(
    "CreateFlowLogsRequestRequestTypeDef",
    {
        "ResourceIds": Sequence[str],
        "ResourceType": FlowLogsResourceTypeType,
        "TrafficType": TrafficTypeType,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "DeliverLogsPermissionArn": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "LogDestinationType": NotRequired[LogDestinationTypeType],
        "LogDestination": NotRequired[str],
        "LogFormat": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "MaxAggregationInterval": NotRequired[int],
        "DestinationOptions": NotRequired["DestinationOptionsRequestTypeDef"],
    },
)

CreateFlowLogsResultTypeDef = TypedDict(
    "CreateFlowLogsResultTypeDef",
    {
        "ClientToken": str,
        "FlowLogIds": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFpgaImageRequestRequestTypeDef = TypedDict(
    "CreateFpgaImageRequestRequestTypeDef",
    {
        "InputStorageLocation": "StorageLocationTypeDef",
        "DryRun": NotRequired[bool],
        "LogsStorageLocation": NotRequired["StorageLocationTypeDef"],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateFpgaImageResultTypeDef = TypedDict(
    "CreateFpgaImageResultTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageRequestInstanceCreateImageTypeDef = TypedDict(
    "CreateImageRequestInstanceCreateImageTypeDef",
    {
        "Name": str,
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "NoReboot": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateImageRequestRequestTypeDef = TypedDict(
    "CreateImageRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "NoReboot": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateImageResultTypeDef = TypedDict(
    "CreateImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "CreateInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Name": NotRequired[str],
        "TimeRanges": NotRequired[Sequence["InstanceEventWindowTimeRangeRequestTypeDef"]],
        "CronExpression": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateInstanceEventWindowResultTypeDef = TypedDict(
    "CreateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceExportTaskRequestRequestTypeDef = TypedDict(
    "CreateInstanceExportTaskRequestRequestTypeDef",
    {
        "ExportToS3Task": "ExportToS3TaskSpecificationTypeDef",
        "InstanceId": str,
        "TargetEnvironment": ExportEnvironmentType,
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateInstanceExportTaskResultTypeDef = TypedDict(
    "CreateInstanceExportTaskResultTypeDef",
    {
        "ExportTask": "ExportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInternetGatewayRequestRequestTypeDef = TypedDict(
    "CreateInternetGatewayRequestRequestTypeDef",
    {
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef = TypedDict(
    "CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef",
    {
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateInternetGatewayResultTypeDef = TypedDict(
    "CreateInternetGatewayResultTypeDef",
    {
        "InternetGateway": "InternetGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIpamPoolRequestRequestTypeDef = TypedDict(
    "CreateIpamPoolRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "AddressFamily": AddressFamilyType,
        "DryRun": NotRequired[bool],
        "Locale": NotRequired[str],
        "SourceIpamPoolId": NotRequired[str],
        "Description": NotRequired[str],
        "AutoImport": NotRequired[bool],
        "PubliclyAdvertisable": NotRequired[bool],
        "AllocationMinNetmaskLength": NotRequired[int],
        "AllocationMaxNetmaskLength": NotRequired[int],
        "AllocationDefaultNetmaskLength": NotRequired[int],
        "AllocationResourceTags": NotRequired[Sequence["RequestIpamResourceTagTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
        "AwsService": NotRequired[Literal["ec2"]],
    },
)

CreateIpamPoolResultTypeDef = TypedDict(
    "CreateIpamPoolResultTypeDef",
    {
        "IpamPool": "IpamPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIpamRequestRequestTypeDef = TypedDict(
    "CreateIpamRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "OperatingRegions": NotRequired[Sequence["AddIpamOperatingRegionTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateIpamResultTypeDef = TypedDict(
    "CreateIpamResultTypeDef",
    {
        "Ipam": "IpamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIpamScopeRequestRequestTypeDef = TypedDict(
    "CreateIpamScopeRequestRequestTypeDef",
    {
        "IpamId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateIpamScopeResultTypeDef = TypedDict(
    "CreateIpamScopeResultTypeDef",
    {
        "IpamScope": "IpamScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyPairRequestRequestTypeDef = TypedDict(
    "CreateKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
        "DryRun": NotRequired[bool],
        "KeyType": NotRequired[KeyTypeType],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef = TypedDict(
    "CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef",
    {
        "KeyName": str,
        "DryRun": NotRequired[bool],
        "KeyType": NotRequired[KeyTypeType],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateLaunchTemplateRequestRequestTypeDef = TypedDict(
    "CreateLaunchTemplateRequestRequestTypeDef",
    {
        "LaunchTemplateName": str,
        "LaunchTemplateData": "RequestLaunchTemplateDataTypeDef",
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateLaunchTemplateResultTypeDef = TypedDict(
    "CreateLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "Warning": "ValidationWarningTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLaunchTemplateVersionRequestRequestTypeDef = TypedDict(
    "CreateLaunchTemplateVersionRequestRequestTypeDef",
    {
        "LaunchTemplateData": "RequestLaunchTemplateDataTypeDef",
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "SourceVersion": NotRequired[str],
        "VersionDescription": NotRequired[str],
    },
)

CreateLaunchTemplateVersionResultTypeDef = TypedDict(
    "CreateLaunchTemplateVersionResultTypeDef",
    {
        "LaunchTemplateVersion": "LaunchTemplateVersionTypeDef",
        "Warning": "ValidationWarningTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "CreateLocalGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "DryRun": NotRequired[bool],
    },
)

CreateLocalGatewayRouteResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteResultTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateManagedPrefixListRequestRequestTypeDef = TypedDict(
    "CreateManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListName": str,
        "MaxEntries": int,
        "AddressFamily": str,
        "DryRun": NotRequired[bool],
        "Entries": NotRequired[Sequence["AddPrefixListEntryTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateManagedPrefixListResultTypeDef = TypedDict(
    "CreateManagedPrefixListResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNatGatewayRequestRequestTypeDef = TypedDict(
    "CreateNatGatewayRequestRequestTypeDef",
    {
        "SubnetId": str,
        "AllocationId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ConnectivityType": NotRequired[ConnectivityTypeType],
    },
)

CreateNatGatewayResultTypeDef = TypedDict(
    "CreateNatGatewayResultTypeDef",
    {
        "ClientToken": str,
        "NatGateway": "NatGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef = TypedDict(
    "CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired["IcmpTypeCodeTypeDef"],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired["PortRangeTypeDef"],
    },
)

CreateNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "CreateNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired["IcmpTypeCodeTypeDef"],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired["PortRangeTypeDef"],
    },
)

CreateNetworkAclRequestRequestTypeDef = TypedDict(
    "CreateNetworkAclRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef = TypedDict(
    "CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateNetworkAclRequestVpcCreateNetworkAclTypeDef = TypedDict(
    "CreateNetworkAclRequestVpcCreateNetworkAclTypeDef",
    {
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateNetworkAclResultTypeDef = TypedDict(
    "CreateNetworkAclResultTypeDef",
    {
        "NetworkAcl": "NetworkAclTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "CreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "ClientToken": str,
        "MatchPaths": NotRequired[Sequence["AccessScopePathRequestTypeDef"]],
        "ExcludePaths": NotRequired[Sequence["AccessScopePathRequestTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateNetworkInsightsAccessScopeResultTypeDef = TypedDict(
    "CreateNetworkInsightsAccessScopeResultTypeDef",
    {
        "NetworkInsightsAccessScope": "NetworkInsightsAccessScopeTypeDef",
        "NetworkInsightsAccessScopeContent": "NetworkInsightsAccessScopeContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "CreateNetworkInsightsPathRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": str,
        "Protocol": ProtocolType,
        "ClientToken": str,
        "SourceIp": NotRequired[str],
        "DestinationIp": NotRequired[str],
        "DestinationPort": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateNetworkInsightsPathResultTypeDef = TypedDict(
    "CreateNetworkInsightsPathResultTypeDef",
    {
        "NetworkInsightsPath": "NetworkInsightsPathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Permission": InterfacePermissionTypeType,
        "AwsAccountId": NotRequired[str],
        "AwsService": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

CreateNetworkInterfacePermissionResultTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionResultTypeDef",
    {
        "InterfacePermission": "NetworkInterfacePermissionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressTypeDef"]],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence["PrivateIpAddressSpecificationTypeDef"]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence["Ipv4PrefixSpecificationRequestTypeDef"]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence["Ipv6PrefixSpecificationRequestTypeDef"]],
        "Ipv6PrefixCount": NotRequired[int],
        "InterfaceType": NotRequired[NetworkInterfaceCreationTypeType],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef",
    {
        "SubnetId": str,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressTypeDef"]],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence["PrivateIpAddressSpecificationTypeDef"]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence["Ipv4PrefixSpecificationRequestTypeDef"]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence["Ipv6PrefixSpecificationRequestTypeDef"]],
        "Ipv6PrefixCount": NotRequired[int],
        "InterfaceType": NotRequired[NetworkInterfaceCreationTypeType],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef",
    {
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressTypeDef"]],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence["PrivateIpAddressSpecificationTypeDef"]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence["Ipv4PrefixSpecificationRequestTypeDef"]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence["Ipv6PrefixSpecificationRequestTypeDef"]],
        "Ipv6PrefixCount": NotRequired[int],
        "InterfaceType": NotRequired[NetworkInterfaceCreationTypeType],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateNetworkInterfaceResultTypeDef = TypedDict(
    "CreateNetworkInterfaceResultTypeDef",
    {
        "NetworkInterface": "NetworkInterfaceTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlacementGroupRequestRequestTypeDef = TypedDict(
    "CreatePlacementGroupRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupName": NotRequired[str],
        "Strategy": NotRequired[PlacementStrategyType],
        "PartitionCount": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef = TypedDict(
    "CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupName": NotRequired[str],
        "Strategy": NotRequired[PlacementStrategyType],
        "PartitionCount": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreatePlacementGroupResultTypeDef = TypedDict(
    "CreatePlacementGroupResultTypeDef",
    {
        "PlacementGroup": "PlacementGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "CreatePublicIpv4PoolRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreatePublicIpv4PoolResultTypeDef = TypedDict(
    "CreatePublicIpv4PoolResultTypeDef",
    {
        "PoolId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplaceRootVolumeTaskRequestRequestTypeDef = TypedDict(
    "CreateReplaceRootVolumeTaskRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateReplaceRootVolumeTaskResultTypeDef = TypedDict(
    "CreateReplaceRootVolumeTaskResultTypeDef",
    {
        "ReplaceRootVolumeTask": "ReplaceRootVolumeTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReservedInstancesListingRequestRequestTypeDef = TypedDict(
    "CreateReservedInstancesListingRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceCount": int,
        "PriceSchedules": Sequence["PriceScheduleSpecificationTypeDef"],
        "ReservedInstancesId": str,
    },
)

CreateReservedInstancesListingResultTypeDef = TypedDict(
    "CreateReservedInstancesListingResultTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRestoreImageTaskRequestRequestTypeDef = TypedDict(
    "CreateRestoreImageTaskRequestRequestTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
        "Name": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateRestoreImageTaskResultTypeDef = TypedDict(
    "CreateRestoreImageTaskResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteRequestRequestTypeDef = TypedDict(
    "CreateRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)

CreateRouteRequestRouteTableCreateRouteTypeDef = TypedDict(
    "CreateRouteRequestRouteTableCreateRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)

CreateRouteResultTypeDef = TypedDict(
    "CreateRouteResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteTableRequestRequestTypeDef = TypedDict(
    "CreateRouteTableRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef = TypedDict(
    "CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateRouteTableRequestVpcCreateRouteTableTypeDef = TypedDict(
    "CreateRouteTableRequestVpcCreateRouteTableTypeDef",
    {
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateRouteTableResultTypeDef = TypedDict(
    "CreateRouteTableResultTypeDef",
    {
        "RouteTable": "RouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecurityGroupRequestRequestTypeDef = TypedDict(
    "CreateSecurityGroupRequestRequestTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "VpcId": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef = TypedDict(
    "CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "VpcId": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef = TypedDict(
    "CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateSecurityGroupResultTypeDef = TypedDict(
    "CreateSecurityGroupResultTypeDef",
    {
        "GroupId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "VolumeId": str,
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef = TypedDict(
    "CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef",
    {
        "VolumeId": str,
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateSnapshotRequestVolumeCreateSnapshotTypeDef = TypedDict(
    "CreateSnapshotRequestVolumeCreateSnapshotTypeDef",
    {
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateSnapshotsRequestRequestTypeDef = TypedDict(
    "CreateSnapshotsRequestRequestTypeDef",
    {
        "InstanceSpecification": "InstanceSpecificationTypeDef",
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
        "CopyTagsFromSource": NotRequired[Literal["volume"]],
    },
)

CreateSnapshotsResultTypeDef = TypedDict(
    "CreateSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "Bucket": str,
        "DryRun": NotRequired[bool],
        "Prefix": NotRequired[str],
    },
)

CreateSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    {
        "SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStoreImageTaskRequestRequestTypeDef = TypedDict(
    "CreateStoreImageTaskRequestRequestTypeDef",
    {
        "ImageId": str,
        "Bucket": str,
        "S3ObjectTags": NotRequired[Sequence["S3ObjectTagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateStoreImageTaskResultTypeDef = TypedDict(
    "CreateStoreImageTaskResultTypeDef",
    {
        "ObjectKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "CreateSubnetCidrReservationRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Cidr": str,
        "ReservationType": SubnetCidrReservationTypeType,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

CreateSubnetCidrReservationResultTypeDef = TypedDict(
    "CreateSubnetCidrReservationResultTypeDef",
    {
        "SubnetCidrReservation": "SubnetCidrReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubnetRequestRequestTypeDef = TypedDict(
    "CreateSubnetRequestRequestTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
    },
)

CreateSubnetRequestServiceResourceCreateSubnetTypeDef = TypedDict(
    "CreateSubnetRequestServiceResourceCreateSubnetTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
    },
)

CreateSubnetRequestVpcCreateSubnetTypeDef = TypedDict(
    "CreateSubnetRequestVpcCreateSubnetTypeDef",
    {
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
    },
)

CreateSubnetResultTypeDef = TypedDict(
    "CreateSubnetResultTypeDef",
    {
        "Subnet": "SubnetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestDhcpOptionsCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestDhcpOptionsCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestImageCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestImageCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestInstanceCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestInstanceCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestInternetGatewayCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestInternetGatewayCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestNetworkAclCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestNetworkAclCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestNetworkInterfaceCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestNetworkInterfaceCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "Resources": Sequence[Any],
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestRouteTableCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestRouteTableCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestSecurityGroupCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestSecurityGroupCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestServiceResourceCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestServiceResourceCreateTagsTypeDef",
    {
        "Resources": Sequence[str],
        "Tags": Sequence["TagTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestSnapshotCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestSnapshotCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestSubnetCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestSubnetCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestVolumeCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestVolumeCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTagsRequestVpcCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestVpcCreateTagsTypeDef",
    {
        "Tags": Optional[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

CreateTrafficMirrorFilterResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterResultTypeDef",
    {
        "TrafficMirrorFilter": "TrafficMirrorFilterTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "DestinationPortRange": NotRequired["TrafficMirrorPortRangeRequestTypeDef"],
        "SourcePortRange": NotRequired["TrafficMirrorPortRangeRequestTypeDef"],
        "Protocol": NotRequired[int],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

CreateTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorSessionRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "SessionNumber": int,
        "PacketLength": NotRequired[int],
        "VirtualNetworkId": NotRequired[int],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

CreateTrafficMirrorSessionResultTypeDef = TypedDict(
    "CreateTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSession": "TrafficMirrorSessionTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorTargetRequestRequestTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
        "NetworkLoadBalancerArn": NotRequired[str],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

CreateTrafficMirrorTargetResultTypeDef = TypedDict(
    "CreateTrafficMirrorTargetResultTypeDef",
    {
        "TrafficMirrorTarget": "TrafficMirrorTargetTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "PeerAddress": str,
        "InsideCidrBlocks": Sequence[str],
        "TransitGatewayAddress": NotRequired[str],
        "BgpOptions": NotRequired["TransitGatewayConnectRequestBgpOptionsTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayConnectPeerResultTypeDef = TypedDict(
    "CreateTransitGatewayConnectPeerResultTypeDef",
    {
        "TransitGatewayConnectPeer": "TransitGatewayConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayConnectRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    {
        "Protocol": Literal["gre"],
    },
)

CreateTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestRequestTypeDef",
    {
        "TransportTransitGatewayAttachmentId": str,
        "Options": "CreateTransitGatewayConnectRequestOptionsTypeDef",
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayConnectResultTypeDef = TypedDict(
    "CreateTransitGatewayConnectResultTypeDef",
    {
        "TransitGatewayConnect": "TransitGatewayConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    {
        "Igmpv2Support": NotRequired[Igmpv2SupportValueType],
        "StaticSourcesSupport": NotRequired[StaticSourcesSupportValueType],
        "AutoAcceptSharedAssociations": NotRequired[AutoAcceptSharedAssociationsValueType],
    },
)

CreateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "Options": NotRequired["CreateTransitGatewayMulticastDomainRequestOptionsTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    {
        "TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "PeerTransitGatewayId": str,
        "PeerAccountId": str,
        "PeerRegion": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "Options": NotRequired["TransitGatewayRequestOptionsTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayResultTypeDef = TypedDict(
    "CreateTransitGatewayResultTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayRouteResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteResultTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableResultTypeDef",
    {
        "TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": NotRequired[DnsSupportValueType],
        "Ipv6Support": NotRequired[Ipv6SupportValueType],
        "ApplianceModeSupport": NotRequired[ApplianceModeSupportValueType],
    },
)

CreateTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "Options": NotRequired["CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVolumePermissionModificationsTypeDef = TypedDict(
    "CreateVolumePermissionModificationsTypeDef",
    {
        "Add": NotRequired[Sequence["CreateVolumePermissionTypeDef"]],
        "Remove": NotRequired[Sequence["CreateVolumePermissionTypeDef"]],
    },
)

CreateVolumePermissionTypeDef = TypedDict(
    "CreateVolumePermissionTypeDef",
    {
        "Group": NotRequired[Literal["all"]],
        "UserId": NotRequired[str],
    },
)

CreateVolumeRequestRequestTypeDef = TypedDict(
    "CreateVolumeRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeType": NotRequired[VolumeTypeType],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "MultiAttachEnabled": NotRequired[bool],
        "Throughput": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)

CreateVolumeRequestServiceResourceCreateVolumeTypeDef = TypedDict(
    "CreateVolumeRequestServiceResourceCreateVolumeTypeDef",
    {
        "AvailabilityZone": str,
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeType": NotRequired[VolumeTypeType],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "MultiAttachEnabled": NotRequired[bool],
        "Throughput": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)

CreateVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "ConnectionNotificationArn": str,
        "ConnectionEvents": Sequence[str],
        "DryRun": NotRequired[bool],
        "ServiceId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

CreateVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    {
        "ConnectionNotification": "ConnectionNotificationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointRequestRequestTypeDef",
    {
        "VpcId": str,
        "ServiceName": str,
        "DryRun": NotRequired[bool],
        "VpcEndpointType": NotRequired[VpcEndpointTypeType],
        "PolicyDocument": NotRequired[str],
        "RouteTableIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "ClientToken": NotRequired[str],
        "PrivateDnsEnabled": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcEndpointResultTypeDef = TypedDict(
    "CreateVpcEndpointResultTypeDef",
    {
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "AcceptanceRequired": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "NetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "GatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    {
        "ServiceConfiguration": "ServiceConfigurationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "PeerOwnerId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "VpcId": NotRequired[str],
        "PeerRegion": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef",
    {
        "DryRun": NotRequired[bool],
        "PeerOwnerId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "VpcId": NotRequired[str],
        "PeerRegion": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": NotRequired[bool],
        "PeerOwnerId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "PeerRegion": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcPeeringConnectionResultTypeDef = TypedDict(
    "CreateVpcPeeringConnectionResultTypeDef",
    {
        "VpcPeeringConnection": "VpcPeeringConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcRequestRequestTypeDef = TypedDict(
    "CreateVpcRequestRequestTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "AmazonProvidedIpv6CidrBlock": NotRequired[bool],
        "Ipv6Pool": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "Ipv6CidrBlockNetworkBorderGroup": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcRequestServiceResourceCreateVpcTypeDef = TypedDict(
    "CreateVpcRequestServiceResourceCreateVpcTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "AmazonProvidedIpv6CidrBlock": NotRequired[bool],
        "Ipv6Pool": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "Ipv6CidrBlockNetworkBorderGroup": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpcResultTypeDef = TypedDict(
    "CreateVpcResultTypeDef",
    {
        "Vpc": "VpcTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpnConnectionRequestRequestTypeDef = TypedDict(
    "CreateVpnConnectionRequestRequestTypeDef",
    {
        "CustomerGatewayId": str,
        "Type": str,
        "VpnGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Options": NotRequired["VpnConnectionOptionsSpecificationTypeDef"],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

CreateVpnConnectionResultTypeDef = TypedDict(
    "CreateVpnConnectionResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpnConnectionRouteRequestRequestTypeDef = TypedDict(
    "CreateVpnConnectionRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)

CreateVpnGatewayRequestRequestTypeDef = TypedDict(
    "CreateVpnGatewayRequestRequestTypeDef",
    {
        "Type": Literal["ipsec.1"],
        "AvailabilityZone": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "AmazonSideAsn": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

CreateVpnGatewayResultTypeDef = TypedDict(
    "CreateVpnGatewayResultTypeDef",
    {
        "VpnGateway": "VpnGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreditSpecificationRequestTypeDef = TypedDict(
    "CreditSpecificationRequestTypeDef",
    {
        "CpuCredits": str,
    },
)

CreditSpecificationTypeDef = TypedDict(
    "CreditSpecificationTypeDef",
    {
        "CpuCredits": NotRequired[str],
    },
)

CustomerGatewayTypeDef = TypedDict(
    "CustomerGatewayTypeDef",
    {
        "BgpAsn": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "State": NotRequired[str],
        "Type": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

DeleteCarrierGatewayRequestRequestTypeDef = TypedDict(
    "DeleteCarrierGatewayRequestRequestTypeDef",
    {
        "CarrierGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteCarrierGatewayResultTypeDef = TypedDict(
    "DeleteCarrierGatewayResultTypeDef",
    {
        "CarrierGateway": "CarrierGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "DeleteClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteClientVpnEndpointResultTypeDef = TypedDict(
    "DeleteClientVpnEndpointResultTypeDef",
    {
        "Status": "ClientVpnEndpointStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClientVpnRouteRequestRequestTypeDef = TypedDict(
    "DeleteClientVpnRouteRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
        "TargetVpcSubnetId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteClientVpnRouteResultTypeDef = TypedDict(
    "DeleteClientVpnRouteResultTypeDef",
    {
        "Status": "ClientVpnRouteStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomerGatewayRequestRequestTypeDef = TypedDict(
    "DeleteCustomerGatewayRequestRequestTypeDef",
    {
        "CustomerGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef = TypedDict(
    "DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteDhcpOptionsRequestRequestTypeDef = TypedDict(
    "DeleteDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "EgressOnlyInternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    {
        "ReturnCode": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetErrorItemTypeDef = TypedDict(
    "DeleteFleetErrorItemTypeDef",
    {
        "Error": NotRequired["DeleteFleetErrorTypeDef"],
        "FleetId": NotRequired[str],
    },
)

DeleteFleetErrorTypeDef = TypedDict(
    "DeleteFleetErrorTypeDef",
    {
        "Code": NotRequired[DeleteFleetErrorCodeType],
        "Message": NotRequired[str],
    },
)

DeleteFleetSuccessItemTypeDef = TypedDict(
    "DeleteFleetSuccessItemTypeDef",
    {
        "CurrentFleetState": NotRequired[FleetStateCodeType],
        "PreviousFleetState": NotRequired[FleetStateCodeType],
        "FleetId": NotRequired[str],
    },
)

DeleteFleetsRequestRequestTypeDef = TypedDict(
    "DeleteFleetsRequestRequestTypeDef",
    {
        "FleetIds": Sequence[str],
        "TerminateInstances": bool,
        "DryRun": NotRequired[bool],
    },
)

DeleteFleetsResultTypeDef = TypedDict(
    "DeleteFleetsResultTypeDef",
    {
        "SuccessfulFleetDeletions": List["DeleteFleetSuccessItemTypeDef"],
        "UnsuccessfulFleetDeletions": List["DeleteFleetErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFlowLogsRequestRequestTypeDef = TypedDict(
    "DeleteFlowLogsRequestRequestTypeDef",
    {
        "FlowLogIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteFlowLogsResultTypeDef = TypedDict(
    "DeleteFlowLogsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFpgaImageRequestRequestTypeDef = TypedDict(
    "DeleteFpgaImageRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteFpgaImageResultTypeDef = TypedDict(
    "DeleteFpgaImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "DeleteInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "DryRun": NotRequired[bool],
        "ForceDelete": NotRequired[bool],
    },
)

DeleteInstanceEventWindowResultTypeDef = TypedDict(
    "DeleteInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindowState": "InstanceEventWindowStateChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef = TypedDict(
    "DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteInternetGatewayRequestRequestTypeDef = TypedDict(
    "DeleteInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteIpamPoolRequestRequestTypeDef = TypedDict(
    "DeleteIpamPoolRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteIpamPoolResultTypeDef = TypedDict(
    "DeleteIpamPoolResultTypeDef",
    {
        "IpamPool": "IpamPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIpamRequestRequestTypeDef = TypedDict(
    "DeleteIpamRequestRequestTypeDef",
    {
        "IpamId": str,
        "DryRun": NotRequired[bool],
        "Cascade": NotRequired[bool],
    },
)

DeleteIpamResultTypeDef = TypedDict(
    "DeleteIpamResultTypeDef",
    {
        "Ipam": "IpamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIpamScopeRequestRequestTypeDef = TypedDict(
    "DeleteIpamScopeRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteIpamScopeResultTypeDef = TypedDict(
    "DeleteIpamScopeResultTypeDef",
    {
        "IpamScope": "IpamScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeyPairRequestKeyPairDeleteTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairDeleteTypeDef",
    {
        "KeyPairId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteKeyPairRequestKeyPairInfoDeleteTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairInfoDeleteTypeDef",
    {
        "KeyPairId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteKeyPairRequestRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestRequestTypeDef",
    {
        "KeyName": NotRequired[str],
        "KeyPairId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteLaunchTemplateRequestRequestTypeDef = TypedDict(
    "DeleteLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
    },
)

DeleteLaunchTemplateResultTypeDef = TypedDict(
    "DeleteLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "Versions": Sequence[str],
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
    },
)

DeleteLaunchTemplateVersionsResponseErrorItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "ResponseError": NotRequired["ResponseErrorTypeDef"],
    },
)

DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "VersionNumber": NotRequired[int],
    },
)

DeleteLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResultTypeDef",
    {
        "SuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef"
        ],
        "UnsuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "DeleteLocalGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayRouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteLocalGatewayRouteResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteResultTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteManagedPrefixListRequestRequestTypeDef = TypedDict(
    "DeleteManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteManagedPrefixListResultTypeDef = TypedDict(
    "DeleteManagedPrefixListResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNatGatewayRequestRequestTypeDef = TypedDict(
    "DeleteNatGatewayRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteNatGatewayResultTypeDef = TypedDict(
    "DeleteNatGatewayResultTypeDef",
    {
        "NatGatewayId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef = TypedDict(
    "DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef",
    {
        "Egress": bool,
        "RuleNumber": int,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "DeleteNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "RuleNumber": int,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkAclRequestNetworkAclDeleteTypeDef = TypedDict(
    "DeleteNetworkAclRequestNetworkAclDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkAclRequestRequestTypeDef = TypedDict(
    "DeleteNetworkAclRequestRequestTypeDef",
    {
        "NetworkAclId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInsightsAccessScopeResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeResultTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInsightsAnalysisResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsPathRequestRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInsightsPathResultTypeDef = TypedDict(
    "DeleteNetworkInsightsPathResultTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "NetworkInterfacePermissionId": str,
        "Force": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInterfacePermissionResultTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef = TypedDict(
    "DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInterfaceRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "DryRun": NotRequired[bool],
    },
)

DeletePlacementGroupRequestPlacementGroupDeleteTypeDef = TypedDict(
    "DeletePlacementGroupRequestPlacementGroupDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeletePlacementGroupRequestRequestTypeDef = TypedDict(
    "DeletePlacementGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "DryRun": NotRequired[bool],
    },
)

DeletePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "DeletePublicIpv4PoolRequestRequestTypeDef",
    {
        "PoolId": str,
        "DryRun": NotRequired[bool],
    },
)

DeletePublicIpv4PoolResultTypeDef = TypedDict(
    "DeletePublicIpv4PoolResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteQueuedReservedInstancesErrorTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesErrorTypeDef",
    {
        "Code": NotRequired[DeleteQueuedReservedInstancesErrorCodeType],
        "Message": NotRequired[str],
    },
)

DeleteQueuedReservedInstancesRequestRequestTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstancesIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteQueuedReservedInstancesResultTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesResultTypeDef",
    {
        "SuccessfulQueuedPurchaseDeletions": List["SuccessfulQueuedPurchaseDeletionTypeDef"],
        "FailedQueuedPurchaseDeletions": List["FailedQueuedPurchaseDeletionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteRouteRequestRouteDeleteTypeDef = TypedDict(
    "DeleteRouteRequestRouteDeleteTypeDef",
    {
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteRouteTableRequestRequestTypeDef = TypedDict(
    "DeleteRouteTableRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteRouteTableRequestRouteTableDeleteTypeDef = TypedDict(
    "DeleteRouteTableRequestRouteTableDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteSecurityGroupRequestRequestTypeDef = TypedDict(
    "DeleteSecurityGroupRequestRequestTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef = TypedDict(
    "DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef",
    {
        "GroupName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteSnapshotRequestSnapshotDeleteTypeDef = TypedDict(
    "DeleteSnapshotRequestSnapshotDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "DeleteSubnetCidrReservationRequestRequestTypeDef",
    {
        "SubnetCidrReservationId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteSubnetCidrReservationResultTypeDef = TypedDict(
    "DeleteSubnetCidrReservationResultTypeDef",
    {
        "DeletedSubnetCidrReservation": "SubnetCidrReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSubnetRequestRequestTypeDef = TypedDict(
    "DeleteSubnetRequestRequestTypeDef",
    {
        "SubnetId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteSubnetRequestSubnetDeleteTypeDef = TypedDict(
    "DeleteSubnetRequestSubnetDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "Resources": Sequence[Any],
        "DryRun": NotRequired[bool],
        "Tags": NotRequired[Optional[Sequence["TagTypeDef"]]],
    },
)

DeleteTagsRequestTagDeleteTypeDef = TypedDict(
    "DeleteTagsRequestTagDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTrafficMirrorFilterResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterResultTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTrafficMirrorSessionResultTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetRequestRequestTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTrafficMirrorTargetResultTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetResultTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayConnectPeerResultTypeDef = TypedDict(
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    {
        "TransitGatewayConnectPeer": "TransitGatewayConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayConnectRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayConnectResultTypeDef = TypedDict(
    "DeleteTransitGatewayConnectResultTypeDef",
    {
        "TransitGatewayConnect": "TransitGatewayConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    {
        "TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayResultTypeDef = TypedDict(
    "DeleteTransitGatewayResultTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRouteRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "DestinationCidrBlock": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayRouteResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteResultTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableResultTypeDef",
    {
        "TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeRequestRequestTypeDef = TypedDict(
    "DeleteVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteVolumeRequestVolumeDeleteTypeDef = TypedDict(
    "DeleteVolumeRequestVolumeDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "ConnectionNotificationIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "ServiceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcEndpointsRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointsRequestRequestTypeDef",
    {
        "VpcEndpointIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcEndpointsResultTypeDef = TypedDict(
    "DeleteVpcEndpointsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcPeeringConnectionResultTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcRequestRequestTypeDef = TypedDict(
    "DeleteVpcRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteVpcRequestVpcDeleteTypeDef = TypedDict(
    "DeleteVpcRequestVpcDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeleteVpnConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpnConnectionRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)

DeleteVpnConnectionRouteRequestRequestTypeDef = TypedDict(
    "DeleteVpnConnectionRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)

DeleteVpnGatewayRequestRequestTypeDef = TypedDict(
    "DeleteVpnGatewayRequestRequestTypeDef",
    {
        "VpnGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DeprovisionByoipCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)

DeprovisionByoipCidrResultTypeDef = TypedDict(
    "DeprovisionByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeprovisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cidr": NotRequired[str],
    },
)

DeprovisionIpamPoolCidrResultTypeDef = TypedDict(
    "DeprovisionIpamPoolCidrResultTypeDef",
    {
        "IpamPoolCidr": "IpamPoolCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "PoolId": str,
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)

DeprovisionPublicIpv4PoolCidrResultTypeDef = TypedDict(
    "DeprovisionPublicIpv4PoolCidrResultTypeDef",
    {
        "PoolId": str,
        "DeprovisionedAddresses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterImageRequestImageDeregisterTypeDef = TypedDict(
    "DeregisterImageRequestImageDeregisterTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DeregisterImageRequestRequestTypeDef = TypedDict(
    "DeregisterImageRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)

DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceTagAttribute": NotRequired["DeregisterInstanceTagAttributeRequestTypeDef"],
    },
)

DeregisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "DeregisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": NotRequired[bool],
        "InstanceTagKeys": NotRequired[Sequence[str]],
    },
)

DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "GroupIpAddress": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DeregisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {
        "DeregisteredMulticastGroupMembers": (
            "TransitGatewayMulticastDeregisteredGroupMembersTypeDef"
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "GroupIpAddress": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {
        "DeregisteredMulticastGroupSources": (
            "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef"
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestRequestTypeDef",
    {
        "AttributeNames": NotRequired[Sequence[AccountAttributeNameType]],
        "DryRun": NotRequired[bool],
    },
)

DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesAttributeRequestRequestTypeDef = TypedDict(
    "DescribeAddressesAttributeRequestRequestTypeDef",
    {
        "AllocationIds": NotRequired[Sequence[str]],
        "Attribute": NotRequired[Literal["domain-name"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

DescribeAddressesAttributeResultTypeDef = TypedDict(
    "DescribeAddressesAttributeResultTypeDef",
    {
        "Addresses": List["AddressAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "PublicIps": NotRequired[Sequence[str]],
        "AllocationIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregateIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeAggregateIdFormatRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DescribeAggregateIdFormatResultTypeDef = TypedDict(
    "DescribeAggregateIdFormatResultTypeDef",
    {
        "UseLongIdsAggregated": bool,
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityZonesRequestRequestTypeDef = TypedDict(
    "DescribeAvailabilityZonesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ZoneNames": NotRequired[Sequence[str]],
        "ZoneIds": NotRequired[Sequence[str]],
        "AllAvailabilityZones": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

DescribeAvailabilityZonesResultTypeDef = TypedDict(
    "DescribeAvailabilityZonesResultTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBundleTasksRequestRequestTypeDef = TypedDict(
    "DescribeBundleTasksRequestRequestTypeDef",
    {
        "BundleIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

DescribeBundleTasksResultTypeDef = TypedDict(
    "DescribeBundleTasksResultTypeDef",
    {
        "BundleTasks": List["BundleTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeByoipCidrsRequestRequestTypeDef = TypedDict(
    "DescribeByoipCidrsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

DescribeByoipCidrsResultTypeDef = TypedDict(
    "DescribeByoipCidrsResultTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityReservationFleetsRequestRequestTypeDef",
    {
        "CapacityReservationFleetIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

DescribeCapacityReservationFleetsResultTypeDef = TypedDict(
    "DescribeCapacityReservationFleetsResultTypeDef",
    {
        "CapacityReservationFleets": List["CapacityReservationFleetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityReservationsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityReservationsRequestRequestTypeDef",
    {
        "CapacityReservationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

DescribeCapacityReservationsResultTypeDef = TypedDict(
    "DescribeCapacityReservationsResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservations": List["CapacityReservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCarrierGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeCarrierGatewaysRequestRequestTypeDef",
    {
        "CarrierGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeCarrierGatewaysResultTypeDef = TypedDict(
    "DescribeCarrierGatewaysResultTypeDef",
    {
        "CarrierGateways": List["CarrierGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClassicLinkInstancesRequestRequestTypeDef = TypedDict(
    "DescribeClassicLinkInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeClassicLinkInstancesResultTypeDef = TypedDict(
    "DescribeClassicLinkInstancesResultTypeDef",
    {
        "Instances": List["ClassicLinkInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnAuthorizationRulesRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
    },
)

DescribeClientVpnAuthorizationRulesResultTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    {
        "AuthorizationRules": List["AuthorizationRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnConnectionsRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

DescribeClientVpnConnectionsResultTypeDef = TypedDict(
    "DescribeClientVpnConnectionsResultTypeDef",
    {
        "Connections": List["ClientVpnConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnEndpointsRequestRequestTypeDef",
    {
        "ClientVpnEndpointIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

DescribeClientVpnEndpointsResultTypeDef = TypedDict(
    "DescribeClientVpnEndpointsResultTypeDef",
    {
        "ClientVpnEndpoints": List["ClientVpnEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnRoutesRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnRoutesRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeClientVpnRoutesResultTypeDef = TypedDict(
    "DescribeClientVpnRoutesResultTypeDef",
    {
        "Routes": List["ClientVpnRouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnTargetNetworksRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

DescribeClientVpnTargetNetworksResultTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksResultTypeDef",
    {
        "ClientVpnTargetNetworks": List["TargetNetworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCoipPoolsRequestRequestTypeDef = TypedDict(
    "DescribeCoipPoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeCoipPoolsResultTypeDef = TypedDict(
    "DescribeCoipPoolsResultTypeDef",
    {
        "CoipPools": List["CoipPoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConversionTasksRequestRequestTypeDef = TypedDict(
    "DescribeConversionTasksRequestRequestTypeDef",
    {
        "ConversionTaskIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeConversionTasksResultTypeDef = TypedDict(
    "DescribeConversionTasksResultTypeDef",
    {
        "ConversionTasks": List["ConversionTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomerGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeCustomerGatewaysRequestRequestTypeDef",
    {
        "CustomerGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

DescribeCustomerGatewaysResultTypeDef = TypedDict(
    "DescribeCustomerGatewaysResultTypeDef",
    {
        "CustomerGateways": List["CustomerGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDhcpOptionsRequestRequestTypeDef = TypedDict(
    "DescribeDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeDhcpOptionsResultTypeDef = TypedDict(
    "DescribeDhcpOptionsResultTypeDef",
    {
        "DhcpOptions": List["DhcpOptionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "EgressOnlyInternetGatewayIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeEgressOnlyInternetGatewaysResultTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    {
        "EgressOnlyInternetGateways": List["EgressOnlyInternetGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticGpusRequestRequestTypeDef = TypedDict(
    "DescribeElasticGpusRequestRequestTypeDef",
    {
        "ElasticGpuIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeElasticGpusResultTypeDef = TypedDict(
    "DescribeElasticGpusResultTypeDef",
    {
        "ElasticGpuSet": List["ElasticGpusTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportImageTasksRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ExportImageTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeExportImageTasksResultTypeDef = TypedDict(
    "DescribeExportImageTasksResultTypeDef",
    {
        "ExportImageTasks": List["ExportImageTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "ExportTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeExportTasksResultTypeDef = TypedDict(
    "DescribeExportTasksResultTypeDef",
    {
        "ExportTasks": List["ExportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFastLaunchImagesRequestRequestTypeDef = TypedDict(
    "DescribeFastLaunchImagesRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeFastLaunchImagesResultTypeDef = TypedDict(
    "DescribeFastLaunchImagesResultTypeDef",
    {
        "FastLaunchImages": List["DescribeFastLaunchImagesSuccessItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFastLaunchImagesSuccessItemTypeDef = TypedDict(
    "DescribeFastLaunchImagesSuccessItemTypeDef",
    {
        "ImageId": NotRequired[str],
        "ResourceType": NotRequired[Literal["snapshot"]],
        "SnapshotConfiguration": NotRequired["FastLaunchSnapshotConfigurationResponseTypeDef"],
        "LaunchTemplate": NotRequired["FastLaunchLaunchTemplateSpecificationResponseTypeDef"],
        "MaxParallelLaunches": NotRequired[int],
        "OwnerId": NotRequired[str],
        "State": NotRequired[FastLaunchStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "StateTransitionTime": NotRequired[datetime],
    },
)

DescribeFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[FastSnapshotRestoreStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "EnablingTime": NotRequired[datetime],
        "OptimizingTime": NotRequired[datetime],
        "EnabledTime": NotRequired[datetime],
        "DisablingTime": NotRequired[datetime],
        "DisabledTime": NotRequired[datetime],
    },
)

DescribeFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeFastSnapshotRestoresResultTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresResultTypeDef",
    {
        "FastSnapshotRestores": List["DescribeFastSnapshotRestoreSuccessItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetErrorTypeDef = TypedDict(
    "DescribeFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired["LaunchTemplateAndOverridesResponseTypeDef"],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

DescribeFleetHistoryRequestRequestTypeDef = TypedDict(
    "DescribeFleetHistoryRequestRequestTypeDef",
    {
        "FleetId": str,
        "StartTime": Union[datetime, str],
        "DryRun": NotRequired[bool],
        "EventType": NotRequired[FleetEventTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetHistoryResultTypeDef = TypedDict(
    "DescribeFleetHistoryResultTypeDef",
    {
        "HistoryRecords": List["HistoryRecordEntryTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "FleetId": str,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetInstancesRequestRequestTypeDef = TypedDict(
    "DescribeFleetInstancesRequestRequestTypeDef",
    {
        "FleetId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeFleetInstancesResultTypeDef = TypedDict(
    "DescribeFleetInstancesResultTypeDef",
    {
        "ActiveInstances": List["ActiveInstanceTypeDef"],
        "NextToken": str,
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetsInstancesTypeDef = TypedDict(
    "DescribeFleetsInstancesTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired["LaunchTemplateAndOverridesResponseTypeDef"],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "InstanceIds": NotRequired[List[str]],
        "InstanceType": NotRequired[InstanceTypeType],
        "Platform": NotRequired[Literal["Windows"]],
    },
)

DescribeFleetsRequestRequestTypeDef = TypedDict(
    "DescribeFleetsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "FleetIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {
        "NextToken": str,
        "Fleets": List["FleetDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowLogsRequestRequestTypeDef = TypedDict(
    "DescribeFlowLogsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "FlowLogIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFlowLogsResultTypeDef = TypedDict(
    "DescribeFlowLogsResultTypeDef",
    {
        "FlowLogs": List["FlowLogTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "DescribeFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "Attribute": FpgaImageAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

DescribeFpgaImageAttributeResultTypeDef = TypedDict(
    "DescribeFpgaImageAttributeResultTypeDef",
    {
        "FpgaImageAttribute": "FpgaImageAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFpgaImagesRequestRequestTypeDef = TypedDict(
    "DescribeFpgaImagesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "FpgaImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeFpgaImagesResultTypeDef = TypedDict(
    "DescribeFpgaImagesResultTypeDef",
    {
        "FpgaImages": List["FpgaImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostReservationOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeHostReservationOfferingsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxDuration": NotRequired[int],
        "MaxResults": NotRequired[int],
        "MinDuration": NotRequired[int],
        "NextToken": NotRequired[str],
        "OfferingId": NotRequired[str],
    },
)

DescribeHostReservationOfferingsResultTypeDef = TypedDict(
    "DescribeHostReservationOfferingsResultTypeDef",
    {
        "NextToken": str,
        "OfferingSet": List["HostOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostReservationsRequestRequestTypeDef = TypedDict(
    "DescribeHostReservationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "HostReservationIdSet": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeHostReservationsResultTypeDef = TypedDict(
    "DescribeHostReservationsResultTypeDef",
    {
        "HostReservationSet": List["HostReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostsRequestRequestTypeDef = TypedDict(
    "DescribeHostsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "HostIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeHostsResultTypeDef = TypedDict(
    "DescribeHostsResultTypeDef",
    {
        "Hosts": List["HostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIamInstanceProfileAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeIamInstanceProfileAssociationsResultTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    {
        "IamInstanceProfileAssociations": List["IamInstanceProfileAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeIdFormatRequestRequestTypeDef",
    {
        "Resource": NotRequired[str],
    },
)

DescribeIdFormatResultTypeDef = TypedDict(
    "DescribeIdFormatResultTypeDef",
    {
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeIdentityIdFormatRequestRequestTypeDef",
    {
        "PrincipalArn": str,
        "Resource": NotRequired[str],
    },
)

DescribeIdentityIdFormatResultTypeDef = TypedDict(
    "DescribeIdentityIdFormatResultTypeDef",
    {
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageAttributeRequestImageDescribeAttributeTypeDef = TypedDict(
    "DescribeImageAttributeRequestImageDescribeAttributeTypeDef",
    {
        "Attribute": ImageAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

DescribeImageAttributeRequestRequestTypeDef = TypedDict(
    "DescribeImageAttributeRequestRequestTypeDef",
    {
        "Attribute": ImageAttributeNameType,
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)

DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "ExecutableUsers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "IncludeDeprecated": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportImageTasksRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeImportImageTasksResultTypeDef = TypedDict(
    "DescribeImportImageTasksResultTypeDef",
    {
        "ImportImageTasks": List["ImportImageTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportSnapshotTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportSnapshotTasksRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeImportSnapshotTasksResultTypeDef = TypedDict(
    "DescribeImportSnapshotTasksResultTypeDef",
    {
        "ImportSnapshotTasks": List["ImportSnapshotTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

DescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

DescribeInstanceCreditSpecificationsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstanceCreditSpecificationsResultTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    {
        "InstanceCreditSpecifications": List["InstanceCreditSpecificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DescribeInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceEventWindowsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceEventWindowsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceEventWindowIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstanceEventWindowsResultTypeDef = TypedDict(
    "DescribeInstanceEventWindowsResultTypeDef",
    {
        "InstanceEventWindows": List["InstanceEventWindowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStatusRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStatusRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IncludeAllInstances": NotRequired[bool],
    },
)

DescribeInstanceStatusResultTypeDef = TypedDict(
    "DescribeInstanceStatusResultTypeDef",
    {
        "InstanceStatuses": List["InstanceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypeOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LocationType": NotRequired[LocationTypeType],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstanceTypeOfferingsResultTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsResultTypeDef",
    {
        "InstanceTypeOfferings": List["InstanceTypeOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypesRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceTypes": NotRequired[Sequence[InstanceTypeType]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstanceTypesResultTypeDef = TypedDict(
    "DescribeInstanceTypesResultTypeDef",
    {
        "InstanceTypes": List["InstanceTypeInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesRequestRequestTypeDef = TypedDict(
    "DescribeInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef",
    {
        "Reservations": List["ReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInternetGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeInternetGatewaysRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "InternetGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeInternetGatewaysResultTypeDef = TypedDict(
    "DescribeInternetGatewaysResultTypeDef",
    {
        "InternetGateways": List["InternetGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamPoolsRequestRequestTypeDef = TypedDict(
    "DescribeIpamPoolsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamPoolIds": NotRequired[Sequence[str]],
    },
)

DescribeIpamPoolsResultTypeDef = TypedDict(
    "DescribeIpamPoolsResultTypeDef",
    {
        "NextToken": str,
        "IpamPools": List["IpamPoolTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamScopesRequestRequestTypeDef = TypedDict(
    "DescribeIpamScopesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamScopeIds": NotRequired[Sequence[str]],
    },
)

DescribeIpamScopesResultTypeDef = TypedDict(
    "DescribeIpamScopesResultTypeDef",
    {
        "NextToken": str,
        "IpamScopes": List["IpamScopeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamsRequestRequestTypeDef = TypedDict(
    "DescribeIpamsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamIds": NotRequired[Sequence[str]],
    },
)

DescribeIpamsResultTypeDef = TypedDict(
    "DescribeIpamsResultTypeDef",
    {
        "NextToken": str,
        "Ipams": List["IpamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpv6PoolsRequestRequestTypeDef = TypedDict(
    "DescribeIpv6PoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeIpv6PoolsResultTypeDef = TypedDict(
    "DescribeIpv6PoolsResultTypeDef",
    {
        "Ipv6Pools": List["Ipv6PoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyPairsRequestRequestTypeDef = TypedDict(
    "DescribeKeyPairsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "KeyNames": NotRequired[Sequence[str]],
        "KeyPairIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeKeyPairsResultTypeDef = TypedDict(
    "DescribeKeyPairsResultTypeDef",
    {
        "KeyPairs": List["KeyPairInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Versions": NotRequired[Sequence[str]],
        "MinVersion": NotRequired[str],
        "MaxVersion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsResultTypeDef",
    {
        "LaunchTemplateVersions": List["LaunchTemplateVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeLaunchTemplatesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateIds": NotRequired[Sequence[str]],
        "LaunchTemplateNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeLaunchTemplatesResultTypeDef = TypedDict(
    "DescribeLaunchTemplatesResultTypeDef",
    {
        "LaunchTemplates": List["LaunchTemplateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociations": List[
            "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociations": List[
            "LocalGatewayRouteTableVpcAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeLocalGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    {
        "LocalGatewayRouteTables": List["LocalGatewayRouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroups": List["LocalGatewayVirtualInterfaceGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeLocalGatewayVirtualInterfacesResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    {
        "LocalGatewayVirtualInterfaces": List["LocalGatewayVirtualInterfaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewaysRequestRequestTypeDef",
    {
        "LocalGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeLocalGatewaysResultTypeDef = TypedDict(
    "DescribeLocalGatewaysResultTypeDef",
    {
        "LocalGateways": List["LocalGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedPrefixListsRequestRequestTypeDef = TypedDict(
    "DescribeManagedPrefixListsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PrefixListIds": NotRequired[Sequence[str]],
    },
)

DescribeManagedPrefixListsResultTypeDef = TypedDict(
    "DescribeManagedPrefixListsResultTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List["ManagedPrefixListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMovingAddressesRequestRequestTypeDef = TypedDict(
    "DescribeMovingAddressesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PublicIps": NotRequired[Sequence[str]],
    },
)

DescribeMovingAddressesResultTypeDef = TypedDict(
    "DescribeMovingAddressesResultTypeDef",
    {
        "MovingAddressStatuses": List["MovingAddressStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNatGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeNatGatewaysRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NatGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeNatGatewaysResultTypeDef = TypedDict(
    "DescribeNatGatewaysResultTypeDef",
    {
        "NatGateways": List["NatGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkAclsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkAclsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "NetworkAclIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeNetworkAclsResultTypeDef = TypedDict(
    "DescribeNetworkAclsResultTypeDef",
    {
        "NetworkAcls": List["NetworkAclTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisIds": NotRequired[Sequence[str]],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "AnalysisStartTimeBegin": NotRequired[Union[datetime, str]],
        "AnalysisStartTimeEnd": NotRequired[Union[datetime, str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalyses": List["NetworkInsightsAccessScopeAnalysisTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAccessScopesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

DescribeNetworkInsightsAccessScopesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesResultTypeDef",
    {
        "NetworkInsightsAccessScopes": List["NetworkInsightsAccessScopeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAnalysesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesRequestRequestTypeDef",
    {
        "NetworkInsightsAnalysisIds": NotRequired[Sequence[str]],
        "NetworkInsightsPathId": NotRequired[str],
        "AnalysisStartTime": NotRequired[Union[datetime, str]],
        "AnalysisEndTime": NotRequired[Union[datetime, str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

DescribeNetworkInsightsAnalysesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    {
        "NetworkInsightsAnalyses": List["NetworkInsightsAnalysisTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsPathsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsRequestRequestTypeDef",
    {
        "NetworkInsightsPathIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

DescribeNetworkInsightsPathsResultTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsResultTypeDef",
    {
        "NetworkInsightsPaths": List["NetworkInsightsPathTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef",
    {
        "Attribute": NotRequired[NetworkInterfaceAttributeType],
        "DryRun": NotRequired[bool],
    },
)

DescribeNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Attribute": NotRequired[NetworkInterfaceAttributeType],
        "DryRun": NotRequired[bool],
    },
)

DescribeNetworkInterfaceAttributeResultTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "Description": "AttributeValueTypeDef",
        "Groups": List["GroupIdentifierTypeDef"],
        "NetworkInterfaceId": str,
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfacePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsRequestRequestTypeDef",
    {
        "NetworkInterfacePermissionIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeNetworkInterfacePermissionsResultTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    {
        "NetworkInterfacePermissions": List["NetworkInterfacePermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeNetworkInterfacesResultTypeDef = TypedDict(
    "DescribeNetworkInterfacesResultTypeDef",
    {
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlacementGroupsRequestRequestTypeDef = TypedDict(
    "DescribePlacementGroupsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "GroupNames": NotRequired[Sequence[str]],
        "GroupIds": NotRequired[Sequence[str]],
    },
)

DescribePlacementGroupsResultTypeDef = TypedDict(
    "DescribePlacementGroupsResultTypeDef",
    {
        "PlacementGroups": List["PlacementGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrefixListsRequestRequestTypeDef = TypedDict(
    "DescribePrefixListsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PrefixListIds": NotRequired[Sequence[str]],
    },
)

DescribePrefixListsResultTypeDef = TypedDict(
    "DescribePrefixListsResultTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List["PrefixListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrincipalIdFormatRequestRequestTypeDef = TypedDict(
    "DescribePrincipalIdFormatRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Resources": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribePrincipalIdFormatResultTypeDef = TypedDict(
    "DescribePrincipalIdFormatResultTypeDef",
    {
        "Principals": List["PrincipalIdFormatTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublicIpv4PoolsRequestRequestTypeDef = TypedDict(
    "DescribePublicIpv4PoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribePublicIpv4PoolsResultTypeDef = TypedDict(
    "DescribePublicIpv4PoolsResultTypeDef",
    {
        "PublicIpv4Pools": List["PublicIpv4PoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionsRequestRequestTypeDef = TypedDict(
    "DescribeRegionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "RegionNames": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "AllRegions": NotRequired[bool],
    },
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "Regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplaceRootVolumeTasksRequestRequestTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksRequestRequestTypeDef",
    {
        "ReplaceRootVolumeTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeReplaceRootVolumeTasksResultTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    {
        "ReplaceRootVolumeTasks": List["ReplaceRootVolumeTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesListingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesListingsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ReservedInstancesId": NotRequired[str],
        "ReservedInstancesListingId": NotRequired[str],
    },
)

DescribeReservedInstancesListingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesListingsResultTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesModificationsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "ReservedInstancesModificationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeReservedInstancesModificationsResultTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsResultTypeDef",
    {
        "NextToken": str,
        "ReservedInstancesModifications": List["ReservedInstancesModificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsRequestRequestTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "IncludeMarketplace": NotRequired[bool],
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxDuration": NotRequired[int],
        "MaxInstanceCount": NotRequired[int],
        "MinDuration": NotRequired[int],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesOfferingIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OfferingType": NotRequired[OfferingTypeValuesType],
    },
)

DescribeReservedInstancesOfferingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsResultTypeDef",
    {
        "ReservedInstancesOfferings": List["ReservedInstancesOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "ReservedInstancesIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "OfferingType": NotRequired[OfferingTypeValuesType],
    },
)

DescribeReservedInstancesResultTypeDef = TypedDict(
    "DescribeReservedInstancesResultTypeDef",
    {
        "ReservedInstances": List["ReservedInstancesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeRouteTablesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "RouteTableIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeRouteTablesResultTypeDef = TypedDict(
    "DescribeRouteTablesResultTypeDef",
    {
        "RouteTables": List["RouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledInstanceAvailabilityRequestRequestTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    {
        "FirstSlotStartTimeRange": "SlotDateTimeRangeRequestTypeDef",
        "Recurrence": "ScheduledInstanceRecurrenceRequestTypeDef",
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "MaxSlotDurationInHours": NotRequired[int],
        "MinSlotDurationInHours": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScheduledInstanceAvailabilityResultTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceAvailabilitySet": List["ScheduledInstanceAvailabilityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledInstancesRequestRequestTypeDef = TypedDict(
    "DescribeScheduledInstancesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ScheduledInstanceIds": NotRequired[Sequence[str]],
        "SlotStartTimeRange": NotRequired["SlotStartTimeRangeRequestTypeDef"],
    },
)

DescribeScheduledInstancesResultTypeDef = TypedDict(
    "DescribeScheduledInstancesResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityGroupReferencesRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesRequestRequestTypeDef",
    {
        "GroupId": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeSecurityGroupReferencesResultTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesResultTypeDef",
    {
        "SecurityGroupReferenceSet": List["SecurityGroupReferenceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupRulesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeSecurityGroupRulesResultTypeDef = TypedDict(
    "DescribeSecurityGroupRulesResultTypeDef",
    {
        "SecurityGroupRules": List["SecurityGroupRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "GroupIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeSecurityGroupsResultTypeDef = TypedDict(
    "DescribeSecurityGroupsResultTypeDef",
    {
        "SecurityGroups": List["SecurityGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)

DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef = TypedDict(
    "DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

DescribeSnapshotAttributeResultTypeDef = TypedDict(
    "DescribeSnapshotAttributeResultTypeDef",
    {
        "CreateVolumePermissions": List["CreateVolumePermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotTierStatusRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotTierStatusRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeSnapshotTierStatusResultTypeDef = TypedDict(
    "DescribeSnapshotTierStatusResultTypeDef",
    {
        "SnapshotTierStatuses": List["SnapshotTierStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OwnerIds": NotRequired[Sequence[str]],
        "RestorableByUserIds": NotRequired[Sequence[str]],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DescribeSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    {
        "SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotFleetInstancesRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetInstancesRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeSpotFleetInstancesResponseTypeDef = TypedDict(
    "DescribeSpotFleetInstancesResponseTypeDef",
    {
        "ActiveInstances": List["ActiveInstanceTypeDef"],
        "NextToken": str,
        "SpotFleetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotFleetRequestHistoryRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "StartTime": Union[datetime, str],
        "DryRun": NotRequired[bool],
        "EventType": NotRequired[EventTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeSpotFleetRequestHistoryResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    {
        "HistoryRecords": List["HistoryRecordTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "SpotFleetRequestId": str,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetRequestsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SpotFleetRequestIds": NotRequired[Sequence[str]],
    },
)

DescribeSpotFleetRequestsResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestsResponseTypeDef",
    {
        "NextToken": str,
        "SpotFleetRequestConfigs": List["SpotFleetRequestConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "SpotInstanceRequestIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeSpotInstanceRequestsResultTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsResultTypeDef",
    {
        "SpotInstanceRequests": List["SpotInstanceRequestTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotPriceHistoryRequestRequestTypeDef = TypedDict(
    "DescribeSpotPriceHistoryRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[Union[datetime, str]],
        "InstanceTypes": NotRequired[Sequence[InstanceTypeType]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProductDescriptions": NotRequired[Sequence[str]],
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

DescribeSpotPriceHistoryResultTypeDef = TypedDict(
    "DescribeSpotPriceHistoryResultTypeDef",
    {
        "NextToken": str,
        "SpotPriceHistory": List["SpotPriceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStaleSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeStaleSecurityGroupsResultTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsResultTypeDef",
    {
        "NextToken": str,
        "StaleSecurityGroupSet": List["StaleSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStoreImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeStoreImageTasksRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeStoreImageTasksResultTypeDef = TypedDict(
    "DescribeStoreImageTasksResultTypeDef",
    {
        "StoreImageTaskResults": List["StoreImageTaskResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubnetsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeSubnetsResultTypeDef = TypedDict(
    "DescribeSubnetsResultTypeDef",
    {
        "Subnets": List["SubnetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorFiltersRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersRequestRequestTypeDef",
    {
        "TrafficMirrorFilterIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeTrafficMirrorFiltersResultTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersResultTypeDef",
    {
        "TrafficMirrorFilters": List["TrafficMirrorFilterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorSessionsRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsRequestRequestTypeDef",
    {
        "TrafficMirrorSessionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeTrafficMirrorSessionsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsResultTypeDef",
    {
        "TrafficMirrorSessions": List["TrafficMirrorSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorTargetsRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsRequestRequestTypeDef",
    {
        "TrafficMirrorTargetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeTrafficMirrorTargetsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsResultTypeDef",
    {
        "TrafficMirrorTargets": List["TrafficMirrorTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    {
        "TransitGatewayAttachments": List["TransitGatewayAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayConnectPeersRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayConnectPeersResultTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    {
        "TransitGatewayConnectPeers": List["TransitGatewayConnectPeerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayConnectsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayConnectsResultTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsResultTypeDef",
    {
        "TransitGatewayConnects": List["TransitGatewayConnectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayMulticastDomainsResultTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    {
        "TransitGatewayMulticastDomains": List["TransitGatewayMulticastDomainTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayPeeringAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    {
        "TransitGatewayPeeringAttachments": List["TransitGatewayPeeringAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    {
        "TransitGatewayRouteTables": List["TransitGatewayRouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewayVpcAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    {
        "TransitGatewayVpcAttachments": List["TransitGatewayVpcAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewaysRequestRequestTypeDef",
    {
        "TransitGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeTransitGatewaysResultTypeDef = TypedDict(
    "DescribeTransitGatewaysResultTypeDef",
    {
        "TransitGateways": List["TransitGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrunkInterfaceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeTrunkInterfaceAssociationsResultTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsResultTypeDef",
    {
        "InterfaceAssociations": List["TrunkInterfaceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumeAttributeRequestRequestTypeDef = TypedDict(
    "DescribeVolumeAttributeRequestRequestTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)

DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef = TypedDict(
    "DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

DescribeVolumeAttributeResultTypeDef = TypedDict(
    "DescribeVolumeAttributeResultTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "VolumeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumeStatusRequestRequestTypeDef = TypedDict(
    "DescribeVolumeStatusRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef = TypedDict(
    "DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DescribeVolumeStatusResultTypeDef = TypedDict(
    "DescribeVolumeStatusResultTypeDef",
    {
        "NextToken": str,
        "VolumeStatuses": List["VolumeStatusItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesModificationsRequestRequestTypeDef = TypedDict(
    "DescribeVolumesModificationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VolumeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeVolumesModificationsResultTypeDef = TypedDict(
    "DescribeVolumesModificationsResultTypeDef",
    {
        "VolumesModifications": List["VolumeModificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcAttributeRequestRequestTypeDef = TypedDict(
    "DescribeVpcAttributeRequestRequestTypeDef",
    {
        "Attribute": VpcAttributeNameType,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef = TypedDict(
    "DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef",
    {
        "Attribute": VpcAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

DescribeVpcAttributeResultTypeDef = TypedDict(
    "DescribeVpcAttributeResultTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "VpcIds": NotRequired[Sequence[str]],
    },
)

DescribeVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    {
        "NextToken": str,
        "Vpcs": List["ClassicLinkDnsSupportTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "VpcIds": NotRequired[Sequence[str]],
    },
)

DescribeVpcClassicLinkResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkResultTypeDef",
    {
        "Vpcs": List["VpcClassicLinkTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ConnectionNotificationId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    {
        "ConnectionNotificationSet": List["ConnectionNotificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVpcEndpointConnectionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsResultTypeDef",
    {
        "VpcEndpointConnections": List["VpcEndpointConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ServiceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    {
        "ServiceConfigurations": List["ServiceConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    {
        "AllowedPrincipals": List["AllowedPrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServicesRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServicesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ServiceNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVpcEndpointServicesResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicesResultTypeDef",
    {
        "ServiceNames": List[str],
        "ServiceDetails": List["ServiceDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VpcEndpointIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVpcEndpointsResultTypeDef = TypedDict(
    "DescribeVpcEndpointsResultTypeDef",
    {
        "VpcEndpoints": List["VpcEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "VpcPeeringConnectionIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeVpcPeeringConnectionsResultTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsResultTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcsRequestRequestTypeDef = TypedDict(
    "DescribeVpcsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "VpcIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeVpcsResultTypeDef = TypedDict(
    "DescribeVpcsResultTypeDef",
    {
        "Vpcs": List["VpcTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpnConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpnConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "VpnConnectionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeVpnConnectionsResultTypeDef = TypedDict(
    "DescribeVpnConnectionsResultTypeDef",
    {
        "VpnConnections": List["VpnConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpnGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeVpnGatewaysRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "VpnGatewayIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DescribeVpnGatewaysResultTypeDef = TypedDict(
    "DescribeVpnGatewaysResultTypeDef",
    {
        "VpnGateways": List["VpnGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationOptionsRequestTypeDef = TypedDict(
    "DestinationOptionsRequestTypeDef",
    {
        "FileFormat": NotRequired[DestinationFileFormatType],
        "HiveCompatiblePartitions": NotRequired[bool],
        "PerHourPartition": NotRequired[bool],
    },
)

DestinationOptionsResponseTypeDef = TypedDict(
    "DestinationOptionsResponseTypeDef",
    {
        "FileFormat": NotRequired[DestinationFileFormatType],
        "HiveCompatiblePartitions": NotRequired[bool],
        "PerHourPartition": NotRequired[bool],
    },
)

DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef = TypedDict(
    "DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DetachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "DetachClassicLinkVpcRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef = TypedDict(
    "DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

DetachClassicLinkVpcResultTypeDef = TypedDict(
    "DetachClassicLinkVpcResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef = TypedDict(
    "DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DetachInternetGatewayRequestRequestTypeDef = TypedDict(
    "DetachInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef = TypedDict(
    "DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef",
    {
        "InternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef = TypedDict(
    "DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef",
    {
        "AttachmentId": str,
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)

DetachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "DetachNetworkInterfaceRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)

DetachVolumeRequestInstanceDetachVolumeTypeDef = TypedDict(
    "DetachVolumeRequestInstanceDetachVolumeTypeDef",
    {
        "VolumeId": str,
        "Device": NotRequired[str],
        "Force": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

DetachVolumeRequestRequestTypeDef = TypedDict(
    "DetachVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "Device": NotRequired[str],
        "Force": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DetachVolumeRequestVolumeDetachFromInstanceTypeDef = TypedDict(
    "DetachVolumeRequestVolumeDetachFromInstanceTypeDef",
    {
        "Device": NotRequired[str],
        "Force": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DetachVpnGatewayRequestRequestTypeDef = TypedDict(
    "DetachVpnGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)

DhcpConfigurationTypeDef = TypedDict(
    "DhcpConfigurationTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List["AttributeValueTypeDef"]],
    },
)

DhcpOptionsTypeDef = TypedDict(
    "DhcpOptionsTypeDef",
    {
        "DhcpConfigurations": NotRequired[List["DhcpConfigurationTypeDef"]],
        "DhcpOptionsId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

DirectoryServiceAuthenticationRequestTypeDef = TypedDict(
    "DirectoryServiceAuthenticationRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
    },
)

DirectoryServiceAuthenticationTypeDef = TypedDict(
    "DirectoryServiceAuthenticationTypeDef",
    {
        "DirectoryId": NotRequired[str],
    },
)

DisableEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DisableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableFastLaunchRequestRequestTypeDef = TypedDict(
    "DisableFastLaunchRequestRequestTypeDef",
    {
        "ImageId": str,
        "Force": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

DisableFastLaunchResultTypeDef = TypedDict(
    "DisableFastLaunchResultTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": "FastLaunchSnapshotConfigurationResponseTypeDef",
        "LaunchTemplate": "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "FastSnapshotRestoreStateErrors": NotRequired[
            List["DisableFastSnapshotRestoreStateErrorItemTypeDef"]
        ],
    },
)

DisableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Error": NotRequired["DisableFastSnapshotRestoreStateErrorTypeDef"],
    },
)

DisableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

DisableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[FastSnapshotRestoreStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "EnablingTime": NotRequired[datetime],
        "OptimizingTime": NotRequired[datetime],
        "EnabledTime": NotRequired[datetime],
        "DisablingTime": NotRequired[datetime],
        "DisabledTime": NotRequired[datetime],
    },
)

DisableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "DisableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "SourceSnapshotIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

DisableFastSnapshotRestoresResultTypeDef = TypedDict(
    "DisableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List["DisableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["DisableFastSnapshotRestoreErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableImageDeprecationRequestRequestTypeDef = TypedDict(
    "DisableImageDeprecationRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)

DisableImageDeprecationResultTypeDef = TypedDict(
    "DisableImageDeprecationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
        "DryRun": NotRequired[bool],
    },
)

DisableIpamOrganizationAdminAccountResultTypeDef = TypedDict(
    "DisableIpamOrganizationAdminAccountResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableSerialConsoleAccessRequestRequestTypeDef = TypedDict(
    "DisableSerialConsoleAccessRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DisableSerialConsoleAccessResultTypeDef = TypedDict(
    "DisableSerialConsoleAccessResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

DisableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    {
        "Propagation": "TransitGatewayPropagationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "DisableVgwRoutePropagationRequestRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

DisableVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "VpcId": NotRequired[str],
    },
)

DisableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "DisableVpcClassicLinkRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef = TypedDict(
    "DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DisableVpcClassicLinkResultTypeDef = TypedDict(
    "DisableVpcClassicLinkResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAddressRequestClassicAddressDisassociateTypeDef = TypedDict(
    "DisassociateAddressRequestClassicAddressDisassociateTypeDef",
    {
        "AssociationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef = TypedDict(
    "DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef",
    {
        "PublicIp": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DisassociateAddressRequestRequestTypeDef = TypedDict(
    "DisassociateAddressRequestRequestTypeDef",
    {
        "AssociationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DisassociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)

DisassociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    {
        "AssociationId": str,
        "Status": "AssociationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DisassociateEnclaveCertificateIamRoleResultTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateIamInstanceProfileRequestRequestTypeDef = TypedDict(
    "DisassociateIamInstanceProfileRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateIamInstanceProfileResultTypeDef = TypedDict(
    "DisassociateIamInstanceProfileResultTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "DisassociateInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "AssociationTarget": "InstanceEventWindowDisassociationRequestTypeDef",
        "DryRun": NotRequired[bool],
    },
)

DisassociateInstanceEventWindowResultTypeDef = TypedDict(
    "DisassociateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRouteTableRequestRequestTypeDef = TypedDict(
    "DisassociateRouteTableRequestRequestTypeDef",
    {
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)

DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef = TypedDict(
    "DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef = TypedDict(
    "DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef",
    {
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)

DisassociateSubnetCidrBlockRequestRequestTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateSubnetCidrBlockResultTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef",
        "SubnetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

DisassociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

DisassociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    {
        "Association": "TransitGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "DisassociateTrunkInterfaceRequestRequestTypeDef",
    {
        "AssociationId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

DisassociateTrunkInterfaceResultTypeDef = TypedDict(
    "DisassociateTrunkInterfaceResultTypeDef",
    {
        "Return": bool,
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "DisassociateVpcCidrBlockRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateVpcCidrBlockResultTypeDef = TypedDict(
    "DisassociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskImageDescriptionTypeDef = TypedDict(
    "DiskImageDescriptionTypeDef",
    {
        "Checksum": NotRequired[str],
        "Format": NotRequired[DiskImageFormatType],
        "ImportManifestUrl": NotRequired[str],
        "Size": NotRequired[int],
    },
)

DiskImageDetailTypeDef = TypedDict(
    "DiskImageDetailTypeDef",
    {
        "Bytes": int,
        "Format": DiskImageFormatType,
        "ImportManifestUrl": str,
    },
)

DiskImageTypeDef = TypedDict(
    "DiskImageTypeDef",
    {
        "Description": NotRequired[str],
        "Image": NotRequired["DiskImageDetailTypeDef"],
        "Volume": NotRequired["VolumeDetailTypeDef"],
    },
)

DiskImageVolumeDescriptionTypeDef = TypedDict(
    "DiskImageVolumeDescriptionTypeDef",
    {
        "Id": NotRequired[str],
        "Size": NotRequired[int],
    },
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "SizeInGB": NotRequired[int],
        "Count": NotRequired[int],
        "Type": NotRequired[DiskTypeType],
    },
)

DnsEntryTypeDef = TypedDict(
    "DnsEntryTypeDef",
    {
        "DnsName": NotRequired[str],
        "HostedZoneId": NotRequired[str],
    },
)

DnsServersOptionsModifyStructureTypeDef = TypedDict(
    "DnsServersOptionsModifyStructureTypeDef",
    {
        "CustomDnsServers": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "KmsKeyId": NotRequired[str],
        "Throughput": NotRequired[int],
        "OutpostArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
    },
)

EbsInfoTypeDef = TypedDict(
    "EbsInfoTypeDef",
    {
        "EbsOptimizedSupport": NotRequired[EbsOptimizedSupportType],
        "EncryptionSupport": NotRequired[EbsEncryptionSupportType],
        "EbsOptimizedInfo": NotRequired["EbsOptimizedInfoTypeDef"],
        "NvmeSupport": NotRequired[EbsNvmeSupportType],
    },
)

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "VolumeId": NotRequired[str],
    },
)

EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "DeleteOnTermination": NotRequired[bool],
        "Status": NotRequired[AttachmentStatusType],
        "VolumeId": NotRequired[str],
    },
)

EbsOptimizedInfoTypeDef = TypedDict(
    "EbsOptimizedInfoTypeDef",
    {
        "BaselineBandwidthInMbps": NotRequired[int],
        "BaselineThroughputInMBps": NotRequired[float],
        "BaselineIops": NotRequired[int],
        "MaximumBandwidthInMbps": NotRequired[int],
        "MaximumThroughputInMBps": NotRequired[float],
        "MaximumIops": NotRequired[int],
    },
)

EfaInfoTypeDef = TypedDict(
    "EfaInfoTypeDef",
    {
        "MaximumEfaInterfaces": NotRequired[int],
    },
)

EgressOnlyInternetGatewayTypeDef = TypedDict(
    "EgressOnlyInternetGatewayTypeDef",
    {
        "Attachments": NotRequired[List["InternetGatewayAttachmentTypeDef"]],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ElasticGpuAssociationTypeDef = TypedDict(
    "ElasticGpuAssociationTypeDef",
    {
        "ElasticGpuId": NotRequired[str],
        "ElasticGpuAssociationId": NotRequired[str],
        "ElasticGpuAssociationState": NotRequired[str],
        "ElasticGpuAssociationTime": NotRequired[str],
    },
)

ElasticGpuHealthTypeDef = TypedDict(
    "ElasticGpuHealthTypeDef",
    {
        "Status": NotRequired[ElasticGpuStatusType],
    },
)

ElasticGpuSpecificationResponseTypeDef = TypedDict(
    "ElasticGpuSpecificationResponseTypeDef",
    {
        "Type": NotRequired[str],
    },
)

ElasticGpuSpecificationTypeDef = TypedDict(
    "ElasticGpuSpecificationTypeDef",
    {
        "Type": str,
    },
)

ElasticGpusTypeDef = TypedDict(
    "ElasticGpusTypeDef",
    {
        "ElasticGpuId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "ElasticGpuType": NotRequired[str],
        "ElasticGpuHealth": NotRequired["ElasticGpuHealthTypeDef"],
        "ElasticGpuState": NotRequired[Literal["ATTACHED"]],
        "InstanceId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ElasticInferenceAcceleratorAssociationTypeDef = TypedDict(
    "ElasticInferenceAcceleratorAssociationTypeDef",
    {
        "ElasticInferenceAcceleratorArn": NotRequired[str],
        "ElasticInferenceAcceleratorAssociationId": NotRequired[str],
        "ElasticInferenceAcceleratorAssociationState": NotRequired[str],
        "ElasticInferenceAcceleratorAssociationTime": NotRequired[datetime],
    },
)

ElasticInferenceAcceleratorTypeDef = TypedDict(
    "ElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
        "Count": NotRequired[int],
    },
)

EnableEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

EnableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableFastLaunchRequestRequestTypeDef = TypedDict(
    "EnableFastLaunchRequestRequestTypeDef",
    {
        "ImageId": str,
        "ResourceType": NotRequired[str],
        "SnapshotConfiguration": NotRequired["FastLaunchSnapshotConfigurationRequestTypeDef"],
        "LaunchTemplate": NotRequired["FastLaunchLaunchTemplateSpecificationRequestTypeDef"],
        "MaxParallelLaunches": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

EnableFastLaunchResultTypeDef = TypedDict(
    "EnableFastLaunchResultTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": "FastLaunchSnapshotConfigurationResponseTypeDef",
        "LaunchTemplate": "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "FastSnapshotRestoreStateErrors": NotRequired[
            List["EnableFastSnapshotRestoreStateErrorItemTypeDef"]
        ],
    },
)

EnableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Error": NotRequired["EnableFastSnapshotRestoreStateErrorTypeDef"],
    },
)

EnableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

EnableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[FastSnapshotRestoreStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "EnablingTime": NotRequired[datetime],
        "OptimizingTime": NotRequired[datetime],
        "EnabledTime": NotRequired[datetime],
        "DisablingTime": NotRequired[datetime],
        "DisabledTime": NotRequired[datetime],
    },
)

EnableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "EnableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "SourceSnapshotIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

EnableFastSnapshotRestoresResultTypeDef = TypedDict(
    "EnableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List["EnableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["EnableFastSnapshotRestoreErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableImageDeprecationRequestRequestTypeDef = TypedDict(
    "EnableImageDeprecationRequestRequestTypeDef",
    {
        "ImageId": str,
        "DeprecateAt": Union[datetime, str],
        "DryRun": NotRequired[bool],
    },
)

EnableImageDeprecationResultTypeDef = TypedDict(
    "EnableImageDeprecationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
        "DryRun": NotRequired[bool],
    },
)

EnableIpamOrganizationAdminAccountResultTypeDef = TypedDict(
    "EnableIpamOrganizationAdminAccountResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableSerialConsoleAccessRequestRequestTypeDef = TypedDict(
    "EnableSerialConsoleAccessRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

EnableSerialConsoleAccessResultTypeDef = TypedDict(
    "EnableSerialConsoleAccessResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

EnableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    {
        "Propagation": "TransitGatewayPropagationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "EnableVgwRoutePropagationRequestRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

EnableVolumeIORequestRequestTypeDef = TypedDict(
    "EnableVolumeIORequestRequestTypeDef",
    {
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)

EnableVolumeIORequestVolumeEnableIoTypeDef = TypedDict(
    "EnableVolumeIORequestVolumeEnableIoTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

EnableVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "VpcId": NotRequired[str],
    },
)

EnableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "EnableVpcClassicLinkRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)

EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef = TypedDict(
    "EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

EnableVpcClassicLinkResultTypeDef = TypedDict(
    "EnableVpcClassicLinkResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnclaveOptionsRequestTypeDef = TypedDict(
    "EnclaveOptionsRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

EnclaveOptionsResponseMetadataTypeDef = TypedDict(
    "EnclaveOptionsResponseMetadataTypeDef",
    {
        "Enabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnclaveOptionsTypeDef = TypedDict(
    "EnclaveOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

EventInformationTypeDef = TypedDict(
    "EventInformationTypeDef",
    {
        "EventDescription": NotRequired[str],
        "EventSubType": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)

ExplanationTypeDef = TypedDict(
    "ExplanationTypeDef",
    {
        "Acl": NotRequired["AnalysisComponentTypeDef"],
        "AclRule": NotRequired["AnalysisAclRuleTypeDef"],
        "Address": NotRequired[str],
        "Addresses": NotRequired[List[str]],
        "AttachedTo": NotRequired["AnalysisComponentTypeDef"],
        "AvailabilityZones": NotRequired[List[str]],
        "Cidrs": NotRequired[List[str]],
        "Component": NotRequired["AnalysisComponentTypeDef"],
        "CustomerGateway": NotRequired["AnalysisComponentTypeDef"],
        "Destination": NotRequired["AnalysisComponentTypeDef"],
        "DestinationVpc": NotRequired["AnalysisComponentTypeDef"],
        "Direction": NotRequired[str],
        "ExplanationCode": NotRequired[str],
        "IngressRouteTable": NotRequired["AnalysisComponentTypeDef"],
        "InternetGateway": NotRequired["AnalysisComponentTypeDef"],
        "LoadBalancerArn": NotRequired[str],
        "ClassicLoadBalancerListener": NotRequired["AnalysisLoadBalancerListenerTypeDef"],
        "LoadBalancerListenerPort": NotRequired[int],
        "LoadBalancerTarget": NotRequired["AnalysisLoadBalancerTargetTypeDef"],
        "LoadBalancerTargetGroup": NotRequired["AnalysisComponentTypeDef"],
        "LoadBalancerTargetGroups": NotRequired[List["AnalysisComponentTypeDef"]],
        "LoadBalancerTargetPort": NotRequired[int],
        "ElasticLoadBalancerListener": NotRequired["AnalysisComponentTypeDef"],
        "MissingComponent": NotRequired[str],
        "NatGateway": NotRequired["AnalysisComponentTypeDef"],
        "NetworkInterface": NotRequired["AnalysisComponentTypeDef"],
        "PacketField": NotRequired[str],
        "VpcPeeringConnection": NotRequired["AnalysisComponentTypeDef"],
        "Port": NotRequired[int],
        "PortRanges": NotRequired[List["PortRangeTypeDef"]],
        "PrefixList": NotRequired["AnalysisComponentTypeDef"],
        "Protocols": NotRequired[List[str]],
        "RouteTableRoute": NotRequired["AnalysisRouteTableRouteTypeDef"],
        "RouteTable": NotRequired["AnalysisComponentTypeDef"],
        "SecurityGroup": NotRequired["AnalysisComponentTypeDef"],
        "SecurityGroupRule": NotRequired["AnalysisSecurityGroupRuleTypeDef"],
        "SecurityGroups": NotRequired[List["AnalysisComponentTypeDef"]],
        "SourceVpc": NotRequired["AnalysisComponentTypeDef"],
        "State": NotRequired[str],
        "Subnet": NotRequired["AnalysisComponentTypeDef"],
        "SubnetRouteTable": NotRequired["AnalysisComponentTypeDef"],
        "Vpc": NotRequired["AnalysisComponentTypeDef"],
        "VpcEndpoint": NotRequired["AnalysisComponentTypeDef"],
        "VpnConnection": NotRequired["AnalysisComponentTypeDef"],
        "VpnGateway": NotRequired["AnalysisComponentTypeDef"],
    },
)

ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)

ExportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    {
        "CertificateRevocationList": str,
        "Status": "ClientCertificateRevocationListStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportClientVpnClientConfigurationRequestRequestTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)

ExportClientVpnClientConfigurationResultTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationResultTypeDef",
    {
        "ClientConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportImageRequestRequestTypeDef = TypedDict(
    "ExportImageRequestRequestTypeDef",
    {
        "DiskImageFormat": DiskImageFormatType,
        "ImageId": str,
        "S3ExportLocation": "ExportTaskS3LocationRequestTypeDef",
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "RoleName": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

ExportImageResultTypeDef = TypedDict(
    "ExportImageResultTypeDef",
    {
        "Description": str,
        "DiskImageFormat": DiskImageFormatType,
        "ExportImageTaskId": str,
        "ImageId": str,
        "RoleName": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportImageTaskTypeDef = TypedDict(
    "ExportImageTaskTypeDef",
    {
        "Description": NotRequired[str],
        "ExportImageTaskId": NotRequired[str],
        "ImageId": NotRequired[str],
        "Progress": NotRequired[str],
        "S3ExportLocation": NotRequired["ExportTaskS3LocationTypeDef"],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ExportTaskS3LocationRequestTypeDef = TypedDict(
    "ExportTaskS3LocationRequestTypeDef",
    {
        "S3Bucket": str,
        "S3Prefix": NotRequired[str],
    },
)

ExportTaskS3LocationTypeDef = TypedDict(
    "ExportTaskS3LocationTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Prefix": NotRequired[str],
    },
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "Description": NotRequired[str],
        "ExportTaskId": NotRequired[str],
        "ExportToS3Task": NotRequired["ExportToS3TaskTypeDef"],
        "InstanceExportDetails": NotRequired["InstanceExportDetailsTypeDef"],
        "State": NotRequired[ExportTaskStateType],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ExportToS3TaskSpecificationTypeDef = TypedDict(
    "ExportToS3TaskSpecificationTypeDef",
    {
        "ContainerFormat": NotRequired[Literal["ova"]],
        "DiskImageFormat": NotRequired[DiskImageFormatType],
        "S3Bucket": NotRequired[str],
        "S3Prefix": NotRequired[str],
    },
)

ExportToS3TaskTypeDef = TypedDict(
    "ExportToS3TaskTypeDef",
    {
        "ContainerFormat": NotRequired[Literal["ova"]],
        "DiskImageFormat": NotRequired[DiskImageFormatType],
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)

ExportTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "ExportTransitGatewayRoutesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "S3Bucket": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

ExportTransitGatewayRoutesResultTypeDef = TypedDict(
    "ExportTransitGatewayRoutesResultTypeDef",
    {
        "S3Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedCapacityReservationFleetCancellationResultTypeDef = TypedDict(
    "FailedCapacityReservationFleetCancellationResultTypeDef",
    {
        "CapacityReservationFleetId": NotRequired[str],
        "CancelCapacityReservationFleetError": NotRequired[
            "CancelCapacityReservationFleetErrorTypeDef"
        ],
    },
)

FailedQueuedPurchaseDeletionTypeDef = TypedDict(
    "FailedQueuedPurchaseDeletionTypeDef",
    {
        "Error": NotRequired["DeleteQueuedReservedInstancesErrorTypeDef"],
        "ReservedInstancesId": NotRequired[str],
    },
)

FastLaunchLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationRequestTypeDef",
    {
        "Version": str,
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
    },
)

FastLaunchLaunchTemplateSpecificationResponseTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

FastLaunchSnapshotConfigurationRequestTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationRequestTypeDef",
    {
        "TargetResourceCount": NotRequired[int],
    },
)

FastLaunchSnapshotConfigurationResponseTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationResponseTypeDef",
    {
        "TargetResourceCount": NotRequired[int],
    },
)

FederatedAuthenticationRequestTypeDef = TypedDict(
    "FederatedAuthenticationRequestTypeDef",
    {
        "SAMLProviderArn": NotRequired[str],
        "SelfServiceSAMLProviderArn": NotRequired[str],
    },
)

FederatedAuthenticationTypeDef = TypedDict(
    "FederatedAuthenticationTypeDef",
    {
        "SamlProviderArn": NotRequired[str],
        "SelfServiceSamlProviderArn": NotRequired[str],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

FleetCapacityReservationTypeDef = TypedDict(
    "FleetCapacityReservationTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "InstancePlatform": NotRequired[CapacityReservationInstancePlatformType],
        "AvailabilityZone": NotRequired[str],
        "TotalInstanceCount": NotRequired[int],
        "FulfilledCapacity": NotRequired[float],
        "EbsOptimized": NotRequired[bool],
        "CreateDate": NotRequired[datetime],
        "Weight": NotRequired[float],
        "Priority": NotRequired[int],
    },
)

FleetDataTypeDef = TypedDict(
    "FleetDataTypeDef",
    {
        "ActivityStatus": NotRequired[FleetActivityStatusType],
        "CreateTime": NotRequired[datetime],
        "FleetId": NotRequired[str],
        "FleetState": NotRequired[FleetStateCodeType],
        "ClientToken": NotRequired[str],
        "ExcessCapacityTerminationPolicy": NotRequired[FleetExcessCapacityTerminationPolicyType],
        "FulfilledCapacity": NotRequired[float],
        "FulfilledOnDemandCapacity": NotRequired[float],
        "LaunchTemplateConfigs": NotRequired[List["FleetLaunchTemplateConfigTypeDef"]],
        "TargetCapacitySpecification": NotRequired["TargetCapacitySpecificationTypeDef"],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "SpotOptions": NotRequired["SpotOptionsTypeDef"],
        "OnDemandOptions": NotRequired["OnDemandOptionsTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Errors": NotRequired[List["DescribeFleetErrorTypeDef"]],
        "Instances": NotRequired[List["DescribeFleetsInstancesTypeDef"]],
        "Context": NotRequired[str],
    },
)

FleetLaunchTemplateConfigRequestTypeDef = TypedDict(
    "FleetLaunchTemplateConfigRequestTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[
            "FleetLaunchTemplateSpecificationRequestTypeDef"
        ],
        "Overrides": NotRequired[Sequence["FleetLaunchTemplateOverridesRequestTypeDef"]],
    },
)

FleetLaunchTemplateConfigTypeDef = TypedDict(
    "FleetLaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired["FleetLaunchTemplateSpecificationTypeDef"],
        "Overrides": NotRequired[List["FleetLaunchTemplateOverridesTypeDef"]],
    },
)

FleetLaunchTemplateOverridesRequestTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesRequestTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "Priority": NotRequired[float],
        "Placement": NotRequired["PlacementTypeDef"],
        "InstanceRequirements": NotRequired["InstanceRequirementsRequestTypeDef"],
    },
)

FleetLaunchTemplateOverridesTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "Priority": NotRequired[float],
        "Placement": NotRequired["PlacementResponseTypeDef"],
        "InstanceRequirements": NotRequired["InstanceRequirementsTypeDef"],
    },
)

FleetLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

FleetLaunchTemplateSpecificationTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

FleetSpotCapacityRebalanceRequestTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceRequestTypeDef",
    {
        "ReplacementStrategy": NotRequired[FleetReplacementStrategyType],
        "TerminationDelay": NotRequired[int],
    },
)

FleetSpotCapacityRebalanceTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": NotRequired[FleetReplacementStrategyType],
        "TerminationDelay": NotRequired[int],
    },
)

FleetSpotMaintenanceStrategiesRequestTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    {
        "CapacityRebalance": NotRequired["FleetSpotCapacityRebalanceRequestTypeDef"],
    },
)

FleetSpotMaintenanceStrategiesTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": NotRequired["FleetSpotCapacityRebalanceTypeDef"],
    },
)

FlowLogTypeDef = TypedDict(
    "FlowLogTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "DeliverLogsErrorMessage": NotRequired[str],
        "DeliverLogsPermissionArn": NotRequired[str],
        "DeliverLogsStatus": NotRequired[str],
        "FlowLogId": NotRequired[str],
        "FlowLogStatus": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "TrafficType": NotRequired[TrafficTypeType],
        "LogDestinationType": NotRequired[LogDestinationTypeType],
        "LogDestination": NotRequired[str],
        "LogFormat": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "MaxAggregationInterval": NotRequired[int],
        "DestinationOptions": NotRequired["DestinationOptionsResponseTypeDef"],
    },
)

FpgaDeviceInfoTypeDef = TypedDict(
    "FpgaDeviceInfoTypeDef",
    {
        "Name": NotRequired[str],
        "Manufacturer": NotRequired[str],
        "Count": NotRequired[int],
        "MemoryInfo": NotRequired["FpgaDeviceMemoryInfoTypeDef"],
    },
)

FpgaDeviceMemoryInfoTypeDef = TypedDict(
    "FpgaDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)

FpgaImageAttributeTypeDef = TypedDict(
    "FpgaImageAttributeTypeDef",
    {
        "FpgaImageId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoadPermissions": NotRequired[List["LoadPermissionTypeDef"]],
        "ProductCodes": NotRequired[List["ProductCodeTypeDef"]],
    },
)

FpgaImageStateTypeDef = TypedDict(
    "FpgaImageStateTypeDef",
    {
        "Code": NotRequired[FpgaImageStateCodeType],
        "Message": NotRequired[str],
    },
)

FpgaImageTypeDef = TypedDict(
    "FpgaImageTypeDef",
    {
        "FpgaImageId": NotRequired[str],
        "FpgaImageGlobalId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ShellVersion": NotRequired[str],
        "PciId": NotRequired["PciIdTypeDef"],
        "State": NotRequired["FpgaImageStateTypeDef"],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "ProductCodes": NotRequired[List["ProductCodeTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Public": NotRequired[bool],
        "DataRetentionSupport": NotRequired[bool],
    },
)

FpgaInfoTypeDef = TypedDict(
    "FpgaInfoTypeDef",
    {
        "Fpgas": NotRequired[List["FpgaDeviceInfoTypeDef"]],
        "TotalFpgaMemoryInMiB": NotRequired[int],
    },
)

GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetAssociatedEnclaveCertificateIamRolesResultTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    {
        "AssociatedRoles": List["AssociatedRoleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssociatedIpv6PoolCidrsRequestRequestTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    {
        "PoolId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

GetAssociatedIpv6PoolCidrsResultTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    {
        "Ipv6CidrAssociations": List["Ipv6CidrAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCapacityReservationUsageRequestRequestTypeDef = TypedDict(
    "GetCapacityReservationUsageRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

GetCapacityReservationUsageResultTypeDef = TypedDict(
    "GetCapacityReservationUsageResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationId": str,
        "InstanceType": str,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "State": CapacityReservationStateType,
        "InstanceUsages": List["InstanceUsageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoipPoolUsageRequestRequestTypeDef = TypedDict(
    "GetCoipPoolUsageRequestRequestTypeDef",
    {
        "PoolId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetCoipPoolUsageResultTypeDef = TypedDict(
    "GetCoipPoolUsageResultTypeDef",
    {
        "CoipPoolId": str,
        "CoipAddressUsages": List["CoipAddressUsageTypeDef"],
        "LocalGatewayRouteTableId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConsoleOutputRequestInstanceConsoleOutputTypeDef = TypedDict(
    "GetConsoleOutputRequestInstanceConsoleOutputTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Latest": NotRequired[bool],
    },
)

GetConsoleOutputRequestRequestTypeDef = TypedDict(
    "GetConsoleOutputRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "Latest": NotRequired[bool],
    },
)

GetConsoleOutputResultTypeDef = TypedDict(
    "GetConsoleOutputResultTypeDef",
    {
        "InstanceId": str,
        "Output": str,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConsoleScreenshotRequestRequestTypeDef = TypedDict(
    "GetConsoleScreenshotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "WakeUp": NotRequired[bool],
    },
)

GetConsoleScreenshotResultTypeDef = TypedDict(
    "GetConsoleScreenshotResultTypeDef",
    {
        "ImageData": str,
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "GetDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "DryRun": NotRequired[bool],
    },
)

GetDefaultCreditSpecificationResultTypeDef = TypedDict(
    "GetDefaultCreditSpecificationResultTypeDef",
    {
        "InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

GetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

GetEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFlowLogsIntegrationTemplateRequestRequestTypeDef = TypedDict(
    "GetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    {
        "FlowLogId": str,
        "ConfigDeliveryS3DestinationArn": str,
        "IntegrateServices": "IntegrateServicesTypeDef",
        "DryRun": NotRequired[bool],
    },
)

GetFlowLogsIntegrationTemplateResultTypeDef = TypedDict(
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupsForCapacityReservationRequestRequestTypeDef = TypedDict(
    "GetGroupsForCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

GetGroupsForCapacityReservationResultTypeDef = TypedDict(
    "GetGroupsForCapacityReservationResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationGroups": List["CapacityReservationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostReservationPurchasePreviewRequestRequestTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewRequestRequestTypeDef",
    {
        "HostIdSet": Sequence[str],
        "OfferingId": str,
    },
)

GetHostReservationPurchasePreviewResultTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewResultTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef = TypedDict(
    "GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    {
        "ArchitectureTypes": Sequence[ArchitectureTypeType],
        "VirtualizationTypes": Sequence[VirtualizationTypeType],
        "InstanceRequirements": "InstanceRequirementsRequestTypeDef",
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetInstanceTypesFromInstanceRequirementsResultTypeDef = TypedDict(
    "GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    {
        "InstanceTypes": List["InstanceTypeInfoFromInstanceRequirementsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIpamAddressHistoryRequestRequestTypeDef = TypedDict(
    "GetIpamAddressHistoryRequestRequestTypeDef",
    {
        "Cidr": str,
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "VpcId": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetIpamAddressHistoryResultTypeDef = TypedDict(
    "GetIpamAddressHistoryResultTypeDef",
    {
        "HistoryRecords": List["IpamAddressHistoryRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIpamPoolAllocationsRequestRequestTypeDef = TypedDict(
    "GetIpamPoolAllocationsRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "IpamPoolAllocationId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetIpamPoolAllocationsResultTypeDef = TypedDict(
    "GetIpamPoolAllocationsResultTypeDef",
    {
        "IpamPoolAllocations": List["IpamPoolAllocationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIpamPoolCidrsRequestRequestTypeDef = TypedDict(
    "GetIpamPoolCidrsRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetIpamPoolCidrsResultTypeDef = TypedDict(
    "GetIpamPoolCidrsResultTypeDef",
    {
        "IpamPoolCidrs": List["IpamPoolCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIpamResourceCidrsRequestRequestTypeDef = TypedDict(
    "GetIpamResourceCidrsRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamPoolId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[IpamResourceTypeType],
        "ResourceTag": NotRequired["RequestIpamResourceTagTypeDef"],
        "ResourceOwner": NotRequired[str],
    },
)

GetIpamResourceCidrsResultTypeDef = TypedDict(
    "GetIpamResourceCidrsResultTypeDef",
    {
        "NextToken": str,
        "IpamResourceCidrs": List["IpamResourceCidrTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchTemplateDataRequestRequestTypeDef = TypedDict(
    "GetLaunchTemplateDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

GetLaunchTemplateDataResultTypeDef = TypedDict(
    "GetLaunchTemplateDataResultTypeDef",
    {
        "LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedPrefixListAssociationsRequestRequestTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetManagedPrefixListAssociationsResultTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsResultTypeDef",
    {
        "PrefixListAssociations": List["PrefixListAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedPrefixListEntriesRequestRequestTypeDef = TypedDict(
    "GetManagedPrefixListEntriesRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "TargetVersion": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetManagedPrefixListEntriesResultTypeDef = TypedDict(
    "GetManagedPrefixListEntriesResultTypeDef",
    {
        "Entries": List["PrefixListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "AnalysisStatus": AnalysisStatusType,
        "AnalysisFindings": List["AccessScopeAnalysisFindingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkInsightsAccessScopeContentRequestRequestTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "DryRun": NotRequired[bool],
    },
)

GetNetworkInsightsAccessScopeContentResultTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeContentResultTypeDef",
    {
        "NetworkInsightsAccessScopeContent": "NetworkInsightsAccessScopeContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPasswordDataRequestInstancePasswordDataTypeDef = TypedDict(
    "GetPasswordDataRequestInstancePasswordDataTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

GetPasswordDataRequestRequestTypeDef = TypedDict(
    "GetPasswordDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

GetPasswordDataResultTypeDef = TypedDict(
    "GetPasswordDataResultTypeDef",
    {
        "InstanceId": str,
        "PasswordData": str,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "ReservedInstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
        "TargetConfigurations": NotRequired[Sequence["TargetConfigurationRequestTypeDef"]],
    },
)

GetReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    {
        "CurrencyCode": str,
        "IsValidExchange": bool,
        "OutputReservedInstancesWillExpireAt": datetime,
        "PaymentDue": str,
        "ReservedInstanceValueRollup": "ReservationValueTypeDef",
        "ReservedInstanceValueSet": List["ReservedInstanceReservationValueTypeDef"],
        "TargetConfigurationValueRollup": "ReservationValueTypeDef",
        "TargetConfigurationValueSet": List["TargetReservationValueTypeDef"],
        "ValidationFailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSerialConsoleAccessStatusRequestRequestTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

GetSerialConsoleAccessStatusResultTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSpotPlacementScoresRequestRequestTypeDef = TypedDict(
    "GetSpotPlacementScoresRequestRequestTypeDef",
    {
        "TargetCapacity": int,
        "InstanceTypes": NotRequired[Sequence[str]],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
        "SingleAvailabilityZone": NotRequired[bool],
        "RegionNames": NotRequired[Sequence[str]],
        "InstanceRequirementsWithMetadata": NotRequired[
            "InstanceRequirementsWithMetadataRequestTypeDef"
        ],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetSpotPlacementScoresResultTypeDef = TypedDict(
    "GetSpotPlacementScoresResultTypeDef",
    {
        "SpotPlacementScores": List["SpotPlacementScoreTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubnetCidrReservationsRequestRequestTypeDef = TypedDict(
    "GetSubnetCidrReservationsRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetSubnetCidrReservationsResultTypeDef = TypedDict(
    "GetSubnetCidrReservationsResultTypeDef",
    {
        "SubnetIpv4CidrReservations": List["SubnetCidrReservationTypeDef"],
        "SubnetIpv6CidrReservations": List["SubnetCidrReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetTransitGatewayAttachmentPropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    {
        "TransitGatewayAttachmentPropagations": List["TransitGatewayAttachmentPropagationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "MulticastDomainAssociations": List["TransitGatewayMulticastDomainAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayPrefixListReferencesRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetTransitGatewayPrefixListReferencesResultTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    {
        "TransitGatewayPrefixListReferences": List["TransitGatewayPrefixListReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetTransitGatewayRouteTableAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    {
        "Associations": List["TransitGatewayRouteTableAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetTransitGatewayRouteTablePropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    {
        "TransitGatewayRouteTablePropagations": List["TransitGatewayRouteTablePropagationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef = TypedDict(
    "GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnConnectionDeviceTypeId": str,
        "InternetKeyExchangeVersion": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetVpnConnectionDeviceSampleConfigurationResultTypeDef = TypedDict(
    "GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    {
        "VpnConnectionDeviceSampleConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpnConnectionDeviceTypesRequestRequestTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

GetVpnConnectionDeviceTypesResultTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesResultTypeDef",
    {
        "VpnConnectionDeviceTypes": List["VpnConnectionDeviceTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GpuDeviceInfoTypeDef = TypedDict(
    "GpuDeviceInfoTypeDef",
    {
        "Name": NotRequired[str],
        "Manufacturer": NotRequired[str],
        "Count": NotRequired[int],
        "MemoryInfo": NotRequired["GpuDeviceMemoryInfoTypeDef"],
    },
)

GpuDeviceMemoryInfoTypeDef = TypedDict(
    "GpuDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)

GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {
        "Gpus": NotRequired[List["GpuDeviceInfoTypeDef"]],
        "TotalGpuMemoryInMiB": NotRequired[int],
    },
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)

HibernationOptionsRequestTypeDef = TypedDict(
    "HibernationOptionsRequestTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)

HibernationOptionsResponseMetadataTypeDef = TypedDict(
    "HibernationOptionsResponseMetadataTypeDef",
    {
        "Configured": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HibernationOptionsTypeDef = TypedDict(
    "HibernationOptionsTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)

HistoryRecordEntryTypeDef = TypedDict(
    "HistoryRecordEntryTypeDef",
    {
        "EventInformation": NotRequired["EventInformationTypeDef"],
        "EventType": NotRequired[FleetEventTypeType],
        "Timestamp": NotRequired[datetime],
    },
)

HistoryRecordTypeDef = TypedDict(
    "HistoryRecordTypeDef",
    {
        "EventInformation": NotRequired["EventInformationTypeDef"],
        "EventType": NotRequired[EventTypeType],
        "Timestamp": NotRequired[datetime],
    },
)

HostInstanceTypeDef = TypedDict(
    "HostInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)

HostOfferingTypeDef = TypedDict(
    "HostOfferingTypeDef",
    {
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Duration": NotRequired[int],
        "HourlyPrice": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "OfferingId": NotRequired[str],
        "PaymentOption": NotRequired[PaymentOptionType],
        "UpfrontPrice": NotRequired[str],
    },
)

HostPropertiesTypeDef = TypedDict(
    "HostPropertiesTypeDef",
    {
        "Cores": NotRequired[int],
        "InstanceType": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "Sockets": NotRequired[int],
        "TotalVCpus": NotRequired[int],
    },
)

HostReservationTypeDef = TypedDict(
    "HostReservationTypeDef",
    {
        "Count": NotRequired[int],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Duration": NotRequired[int],
        "End": NotRequired[datetime],
        "HostIdSet": NotRequired[List[str]],
        "HostReservationId": NotRequired[str],
        "HourlyPrice": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "OfferingId": NotRequired[str],
        "PaymentOption": NotRequired[PaymentOptionType],
        "Start": NotRequired[datetime],
        "State": NotRequired[ReservationStateType],
        "UpfrontPrice": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "AutoPlacement": NotRequired[AutoPlacementType],
        "AvailabilityZone": NotRequired[str],
        "AvailableCapacity": NotRequired["AvailableCapacityTypeDef"],
        "ClientToken": NotRequired[str],
        "HostId": NotRequired[str],
        "HostProperties": NotRequired["HostPropertiesTypeDef"],
        "HostReservationId": NotRequired[str],
        "Instances": NotRequired[List["HostInstanceTypeDef"]],
        "State": NotRequired[AllocationStateType],
        "AllocationTime": NotRequired[datetime],
        "ReleaseTime": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
        "HostRecovery": NotRequired[HostRecoveryType],
        "AllowsMultipleInstanceTypes": NotRequired[AllowsMultipleInstanceTypesType],
        "OwnerId": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "MemberOfServiceLinkedResourceGroup": NotRequired[bool],
    },
)

IKEVersionsListValueTypeDef = TypedDict(
    "IKEVersionsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

IKEVersionsRequestListValueTypeDef = TypedDict(
    "IKEVersionsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

IamInstanceProfileAssociationTypeDef = TypedDict(
    "IamInstanceProfileAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IamInstanceProfile": NotRequired["IamInstanceProfileTypeDef"],
        "State": NotRequired[IamInstanceProfileAssociationStateType],
        "Timestamp": NotRequired[datetime],
    },
)

IamInstanceProfileResponseMetadataTypeDef = TypedDict(
    "IamInstanceProfileResponseMetadataTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamInstanceProfileSpecificationTypeDef = TypedDict(
    "IamInstanceProfileSpecificationTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
    },
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)

IdFormatTypeDef = TypedDict(
    "IdFormatTypeDef",
    {
        "Deadline": NotRequired[datetime],
        "Resource": NotRequired[str],
        "UseLongIds": NotRequired[bool],
    },
)

ImageAttributeTypeDef = TypedDict(
    "ImageAttributeTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "LaunchPermissions": List["LaunchPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "Description": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "RamdiskId": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "BootMode": "AttributeValueTypeDef",
        "LastLaunchedTime": "AttributeValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDiskContainerTypeDef = TypedDict(
    "ImageDiskContainerTypeDef",
    {
        "Description": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Format": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired["UserBucketTypeDef"],
    },
)

ImageRecycleBinInfoTypeDef = TypedDict(
    "ImageRecycleBinInfoTypeDef",
    {
        "ImageId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RecycleBinEnterTime": NotRequired[datetime],
        "RecycleBinExitTime": NotRequired[datetime],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Architecture": NotRequired[ArchitectureValuesType],
        "CreationDate": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageLocation": NotRequired[str],
        "ImageType": NotRequired[ImageTypeValuesType],
        "Public": NotRequired[bool],
        "KernelId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Platform": NotRequired[Literal["Windows"]],
        "PlatformDetails": NotRequired[str],
        "UsageOperation": NotRequired[str],
        "ProductCodes": NotRequired[List["ProductCodeTypeDef"]],
        "RamdiskId": NotRequired[str],
        "State": NotRequired[ImageStateType],
        "BlockDeviceMappings": NotRequired[List["BlockDeviceMappingTypeDef"]],
        "Description": NotRequired[str],
        "EnaSupport": NotRequired[bool],
        "Hypervisor": NotRequired[HypervisorTypeType],
        "ImageOwnerAlias": NotRequired[str],
        "Name": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "RootDeviceType": NotRequired[DeviceTypeType],
        "SriovNetSupport": NotRequired[str],
        "StateReason": NotRequired["StateReasonTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VirtualizationType": NotRequired[VirtualizationTypeType],
        "BootMode": NotRequired[BootModeValuesType],
        "DeprecationTime": NotRequired[str],
    },
)

ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "CertificateRevocationList": str,
        "DryRun": NotRequired[bool],
    },
)

ImportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportImageLicenseConfigurationRequestTypeDef = TypedDict(
    "ImportImageLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)

ImportImageLicenseConfigurationResponseTypeDef = TypedDict(
    "ImportImageLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)

ImportImageRequestRequestTypeDef = TypedDict(
    "ImportImageRequestRequestTypeDef",
    {
        "Architecture": NotRequired[str],
        "ClientData": NotRequired["ClientDataTypeDef"],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DiskContainers": NotRequired[Sequence["ImageDiskContainerTypeDef"]],
        "DryRun": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Hypervisor": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "LicenseType": NotRequired[str],
        "Platform": NotRequired[str],
        "RoleName": NotRequired[str],
        "LicenseSpecifications": NotRequired[
            Sequence["ImportImageLicenseConfigurationRequestTypeDef"]
        ],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "UsageOperation": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
    },
)

ImportImageResultTypeDef = TypedDict(
    "ImportImageResultTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
        "Tags": List["TagTypeDef"],
        "UsageOperation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportImageTaskTypeDef = TypedDict(
    "ImportImageTaskTypeDef",
    {
        "Architecture": NotRequired[str],
        "Description": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Hypervisor": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImportTaskId": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "LicenseType": NotRequired[str],
        "Platform": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotDetails": NotRequired[List["SnapshotDetailTypeDef"]],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "LicenseSpecifications": NotRequired[
            List["ImportImageLicenseConfigurationResponseTypeDef"]
        ],
        "UsageOperation": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
    },
)

ImportInstanceLaunchSpecificationTypeDef = TypedDict(
    "ImportInstanceLaunchSpecificationTypeDef",
    {
        "AdditionalInfo": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "GroupIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "InstanceType": NotRequired[InstanceTypeType],
        "Monitoring": NotRequired[bool],
        "Placement": NotRequired["PlacementTypeDef"],
        "PrivateIpAddress": NotRequired[str],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired["UserDataTypeDef"],
    },
)

ImportInstanceRequestRequestTypeDef = TypedDict(
    "ImportInstanceRequestRequestTypeDef",
    {
        "Platform": Literal["Windows"],
        "Description": NotRequired[str],
        "DiskImages": NotRequired[Sequence["DiskImageTypeDef"]],
        "DryRun": NotRequired[bool],
        "LaunchSpecification": NotRequired["ImportInstanceLaunchSpecificationTypeDef"],
    },
)

ImportInstanceResultTypeDef = TypedDict(
    "ImportInstanceResultTypeDef",
    {
        "ConversionTask": "ConversionTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportInstanceTaskDetailsTypeDef = TypedDict(
    "ImportInstanceTaskDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Platform": NotRequired[Literal["Windows"]],
        "Volumes": NotRequired[List["ImportInstanceVolumeDetailItemTypeDef"]],
    },
)

ImportInstanceVolumeDetailItemTypeDef = TypedDict(
    "ImportInstanceVolumeDetailItemTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "BytesConverted": NotRequired[int],
        "Description": NotRequired[str],
        "Image": NotRequired["DiskImageDescriptionTypeDef"],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Volume": NotRequired["DiskImageVolumeDescriptionTypeDef"],
    },
)

ImportKeyPairRequestRequestTypeDef = TypedDict(
    "ImportKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

ImportKeyPairRequestServiceResourceImportKeyPairTypeDef = TypedDict(
    "ImportKeyPairRequestServiceResourceImportKeyPairTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {
        "KeyFingerprint": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSnapshotRequestRequestTypeDef = TypedDict(
    "ImportSnapshotRequestRequestTypeDef",
    {
        "ClientData": NotRequired["ClientDataTypeDef"],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DiskContainer": NotRequired["SnapshotDiskContainerTypeDef"],
        "DryRun": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "RoleName": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

ImportSnapshotResultTypeDef = TypedDict(
    "ImportSnapshotResultTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSnapshotTaskTypeDef = TypedDict(
    "ImportSnapshotTaskTypeDef",
    {
        "Description": NotRequired[str],
        "ImportTaskId": NotRequired[str],
        "SnapshotTaskDetail": NotRequired["SnapshotTaskDetailTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ImportVolumeRequestRequestTypeDef = TypedDict(
    "ImportVolumeRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Image": "DiskImageDetailTypeDef",
        "Volume": "VolumeDetailTypeDef",
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ImportVolumeResultTypeDef = TypedDict(
    "ImportVolumeResultTypeDef",
    {
        "ConversionTask": "ConversionTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportVolumeTaskDetailsTypeDef = TypedDict(
    "ImportVolumeTaskDetailsTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "BytesConverted": NotRequired[int],
        "Description": NotRequired[str],
        "Image": NotRequired["DiskImageDescriptionTypeDef"],
        "Volume": NotRequired["DiskImageVolumeDescriptionTypeDef"],
    },
)

InferenceAcceleratorInfoTypeDef = TypedDict(
    "InferenceAcceleratorInfoTypeDef",
    {
        "Accelerators": NotRequired[List["InferenceDeviceInfoTypeDef"]],
    },
)

InferenceDeviceInfoTypeDef = TypedDict(
    "InferenceDeviceInfoTypeDef",
    {
        "Count": NotRequired[int],
        "Name": NotRequired[str],
        "Manufacturer": NotRequired[str],
    },
)

InstanceAttributeTypeDef = TypedDict(
    "InstanceAttributeTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "EnclaveOptions": "EnclaveOptionsTypeDef",
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "InstanceId": str,
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": "AttributeValueTypeDef",
        "RootDeviceName": "AttributeValueTypeDef",
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "AttributeValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceBlockDeviceMappingSpecificationTypeDef = TypedDict(
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired["EbsInstanceBlockDeviceSpecificationTypeDef"],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
    },
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired["EbsInstanceBlockDeviceTypeDef"],
    },
)

InstanceCapacityTypeDef = TypedDict(
    "InstanceCapacityTypeDef",
    {
        "AvailableCapacity": NotRequired[int],
        "InstanceType": NotRequired[str],
        "TotalCapacity": NotRequired[int],
    },
)

InstanceCountTypeDef = TypedDict(
    "InstanceCountTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "State": NotRequired[ListingStateType],
    },
)

InstanceCreditSpecificationRequestTypeDef = TypedDict(
    "InstanceCreditSpecificationRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "CpuCredits": NotRequired[str],
    },
)

InstanceCreditSpecificationTypeDef = TypedDict(
    "InstanceCreditSpecificationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "CpuCredits": NotRequired[str],
    },
)

InstanceDeleteTagsRequestTypeDef = TypedDict(
    "InstanceDeleteTagsRequestTypeDef",
    {
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

InstanceEventWindowAssociationRequestTypeDef = TypedDict(
    "InstanceEventWindowAssociationRequestTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "InstanceTags": NotRequired[Sequence["TagTypeDef"]],
        "DedicatedHostIds": NotRequired[Sequence[str]],
    },
)

InstanceEventWindowAssociationTargetTypeDef = TypedDict(
    "InstanceEventWindowAssociationTargetTypeDef",
    {
        "InstanceIds": NotRequired[List[str]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "DedicatedHostIds": NotRequired[List[str]],
    },
)

InstanceEventWindowDisassociationRequestTypeDef = TypedDict(
    "InstanceEventWindowDisassociationRequestTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "InstanceTags": NotRequired[Sequence["TagTypeDef"]],
        "DedicatedHostIds": NotRequired[Sequence[str]],
    },
)

InstanceEventWindowStateChangeTypeDef = TypedDict(
    "InstanceEventWindowStateChangeTypeDef",
    {
        "InstanceEventWindowId": NotRequired[str],
        "State": NotRequired[InstanceEventWindowStateType],
    },
)

InstanceEventWindowTimeRangeRequestTypeDef = TypedDict(
    "InstanceEventWindowTimeRangeRequestTypeDef",
    {
        "StartWeekDay": NotRequired[WeekDayType],
        "StartHour": NotRequired[int],
        "EndWeekDay": NotRequired[WeekDayType],
        "EndHour": NotRequired[int],
    },
)

InstanceEventWindowTimeRangeTypeDef = TypedDict(
    "InstanceEventWindowTimeRangeTypeDef",
    {
        "StartWeekDay": NotRequired[WeekDayType],
        "StartHour": NotRequired[int],
        "EndWeekDay": NotRequired[WeekDayType],
        "EndHour": NotRequired[int],
    },
)

InstanceEventWindowTypeDef = TypedDict(
    "InstanceEventWindowTypeDef",
    {
        "InstanceEventWindowId": NotRequired[str],
        "TimeRanges": NotRequired[List["InstanceEventWindowTimeRangeTypeDef"]],
        "Name": NotRequired[str],
        "CronExpression": NotRequired[str],
        "AssociationTarget": NotRequired["InstanceEventWindowAssociationTargetTypeDef"],
        "State": NotRequired[InstanceEventWindowStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

InstanceExportDetailsTypeDef = TypedDict(
    "InstanceExportDetailsTypeDef",
    {
        "InstanceId": NotRequired[str],
        "TargetEnvironment": NotRequired[ExportEnvironmentType],
    },
)

InstanceFamilyCreditSpecificationTypeDef = TypedDict(
    "InstanceFamilyCreditSpecificationTypeDef",
    {
        "InstanceFamily": NotRequired[UnlimitedSupportedInstanceFamilyType],
        "CpuCredits": NotRequired[str],
    },
)

InstanceIpv4PrefixTypeDef = TypedDict(
    "InstanceIpv4PrefixTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)

InstanceIpv6AddressRequestTypeDef = TypedDict(
    "InstanceIpv6AddressRequestTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)

InstanceIpv6AddressTypeDef = TypedDict(
    "InstanceIpv6AddressTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)

InstanceIpv6PrefixTypeDef = TypedDict(
    "InstanceIpv6PrefixTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)

InstanceMarketOptionsRequestTypeDef = TypedDict(
    "InstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": NotRequired[Literal["spot"]],
        "SpotOptions": NotRequired["SpotMarketOptionsTypeDef"],
    },
)

InstanceMetadataOptionsRequestTypeDef = TypedDict(
    "InstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": NotRequired[HttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[InstanceMetadataProtocolStateType],
        "InstanceMetadataTags": NotRequired[InstanceMetadataTagsStateType],
    },
)

InstanceMetadataOptionsResponseResponseMetadataTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseResponseMetadataTypeDef",
    {
        "State": InstanceMetadataOptionsStateType,
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
        "HttpProtocolIpv6": InstanceMetadataProtocolStateType,
        "InstanceMetadataTags": InstanceMetadataTagsStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceMetadataOptionsResponseTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseTypeDef",
    {
        "State": NotRequired[InstanceMetadataOptionsStateType],
        "HttpTokens": NotRequired[HttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[InstanceMetadataProtocolStateType],
        "InstanceMetadataTags": NotRequired[InstanceMetadataTagsStateType],
    },
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "InstanceId": NotRequired[str],
        "Monitoring": NotRequired["MonitoringTypeDef"],
    },
)

InstanceNetworkInterfaceAssociationTypeDef = TypedDict(
    "InstanceNetworkInterfaceAssociationTypeDef",
    {
        "CarrierIp": NotRequired[str],
        "CustomerOwnedIp": NotRequired[str],
        "IpOwnerId": NotRequired[str],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)

InstanceNetworkInterfaceAttachmentTypeDef = TypedDict(
    "InstanceNetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "Status": NotRequired[AttachmentStatusType],
        "NetworkCardIndex": NotRequired[int],
    },
)

InstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[List[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[List["InstanceIpv6AddressTypeDef"]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List["PrivateIpAddressSpecificationTypeDef"]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "AssociateCarrierIpAddress": NotRequired[bool],
        "InterfaceType": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[List["Ipv4PrefixSpecificationRequestTypeDef"]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[List["Ipv6PrefixSpecificationRequestTypeDef"]],
        "Ipv6PrefixCount": NotRequired[int],
    },
)

InstanceNetworkInterfaceTypeDef = TypedDict(
    "InstanceNetworkInterfaceTypeDef",
    {
        "Association": NotRequired["InstanceNetworkInterfaceAssociationTypeDef"],
        "Attachment": NotRequired["InstanceNetworkInterfaceAttachmentTypeDef"],
        "Description": NotRequired[str],
        "Groups": NotRequired[List["GroupIdentifierTypeDef"]],
        "Ipv6Addresses": NotRequired[List["InstanceIpv6AddressTypeDef"]],
        "MacAddress": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List["InstancePrivateIpAddressTypeDef"]],
        "SourceDestCheck": NotRequired[bool],
        "Status": NotRequired[NetworkInterfaceStatusType],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "InterfaceType": NotRequired[str],
        "Ipv4Prefixes": NotRequired[List["InstanceIpv4PrefixTypeDef"]],
        "Ipv6Prefixes": NotRequired[List["InstanceIpv6PrefixTypeDef"]],
    },
)

InstancePrivateIpAddressTypeDef = TypedDict(
    "InstancePrivateIpAddressTypeDef",
    {
        "Association": NotRequired["InstanceNetworkInterfaceAssociationTypeDef"],
        "Primary": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

InstanceRequirementsRequestTypeDef = TypedDict(
    "InstanceRequirementsRequestTypeDef",
    {
        "VCpuCount": "VCpuCountRangeRequestTypeDef",
        "MemoryMiB": "MemoryMiBRequestTypeDef",
        "CpuManufacturers": NotRequired[Sequence[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired["MemoryGiBPerVCpuRequestTypeDef"],
        "ExcludedInstanceTypes": NotRequired[Sequence[str]],
        "InstanceGenerations": NotRequired[Sequence[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired["NetworkInterfaceCountRequestTypeDef"],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[Sequence[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired["TotalLocalStorageGBRequestTypeDef"],
        "BaselineEbsBandwidthMbps": NotRequired["BaselineEbsBandwidthMbpsRequestTypeDef"],
        "AcceleratorTypes": NotRequired[Sequence[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired["AcceleratorCountRequestTypeDef"],
        "AcceleratorManufacturers": NotRequired[Sequence[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[Sequence[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired["AcceleratorTotalMemoryMiBRequestTypeDef"],
    },
)

InstanceRequirementsTypeDef = TypedDict(
    "InstanceRequirementsTypeDef",
    {
        "VCpuCount": NotRequired["VCpuCountRangeTypeDef"],
        "MemoryMiB": NotRequired["MemoryMiBTypeDef"],
        "CpuManufacturers": NotRequired[List[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired["MemoryGiBPerVCpuTypeDef"],
        "ExcludedInstanceTypes": NotRequired[List[str]],
        "InstanceGenerations": NotRequired[List[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired["NetworkInterfaceCountTypeDef"],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[List[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired["TotalLocalStorageGBTypeDef"],
        "BaselineEbsBandwidthMbps": NotRequired["BaselineEbsBandwidthMbpsTypeDef"],
        "AcceleratorTypes": NotRequired[List[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired["AcceleratorCountTypeDef"],
        "AcceleratorManufacturers": NotRequired[List[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[List[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired["AcceleratorTotalMemoryMiBTypeDef"],
    },
)

InstanceRequirementsWithMetadataRequestTypeDef = TypedDict(
    "InstanceRequirementsWithMetadataRequestTypeDef",
    {
        "ArchitectureTypes": NotRequired[Sequence[ArchitectureTypeType]],
        "VirtualizationTypes": NotRequired[Sequence[VirtualizationTypeType]],
        "InstanceRequirements": NotRequired["InstanceRequirementsRequestTypeDef"],
    },
)

InstanceSpecificationTypeDef = TypedDict(
    "InstanceSpecificationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "ExcludeBootVolume": NotRequired[bool],
    },
)

InstanceStateChangeTypeDef = TypedDict(
    "InstanceStateChangeTypeDef",
    {
        "CurrentState": NotRequired["InstanceStateTypeDef"],
        "InstanceId": NotRequired[str],
        "PreviousState": NotRequired["InstanceStateTypeDef"],
    },
)

InstanceStateResponseMetadataTypeDef = TypedDict(
    "InstanceStateResponseMetadataTypeDef",
    {
        "Code": int,
        "Name": InstanceStateNameType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "Code": NotRequired[int],
        "Name": NotRequired[InstanceStateNameType],
    },
)

InstanceStatusDetailsTypeDef = TypedDict(
    "InstanceStatusDetailsTypeDef",
    {
        "ImpairedSince": NotRequired[datetime],
        "Name": NotRequired[Literal["reachability"]],
        "Status": NotRequired[StatusTypeType],
    },
)

InstanceStatusEventTypeDef = TypedDict(
    "InstanceStatusEventTypeDef",
    {
        "InstanceEventId": NotRequired[str],
        "Code": NotRequired[EventCodeType],
        "Description": NotRequired[str],
        "NotAfter": NotRequired[datetime],
        "NotBefore": NotRequired[datetime],
        "NotBeforeDeadline": NotRequired[datetime],
    },
)

InstanceStatusSummaryTypeDef = TypedDict(
    "InstanceStatusSummaryTypeDef",
    {
        "Details": NotRequired[List["InstanceStatusDetailsTypeDef"]],
        "Status": NotRequired[SummaryStatusType],
    },
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Events": NotRequired[List["InstanceStatusEventTypeDef"]],
        "InstanceId": NotRequired[str],
        "InstanceState": NotRequired["InstanceStateTypeDef"],
        "InstanceStatus": NotRequired["InstanceStatusSummaryTypeDef"],
        "SystemStatus": NotRequired["InstanceStatusSummaryTypeDef"],
    },
)

InstanceStorageInfoTypeDef = TypedDict(
    "InstanceStorageInfoTypeDef",
    {
        "TotalSizeInGB": NotRequired[int],
        "Disks": NotRequired[List["DiskInfoTypeDef"]],
        "NvmeSupport": NotRequired[EphemeralNvmeSupportType],
        "EncryptionSupport": NotRequired[InstanceStorageEncryptionSupportType],
    },
)

InstanceTagNotificationAttributeTypeDef = TypedDict(
    "InstanceTagNotificationAttributeTypeDef",
    {
        "InstanceTagKeys": NotRequired[List[str]],
        "IncludeAllTagsOfInstance": NotRequired[bool],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AmiLaunchIndex": NotRequired[int],
        "ImageId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "Monitoring": NotRequired["MonitoringTypeDef"],
        "Placement": NotRequired["PlacementTypeDef"],
        "Platform": NotRequired[Literal["Windows"]],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "ProductCodes": NotRequired[List["ProductCodeTypeDef"]],
        "PublicDnsName": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "State": NotRequired["InstanceStateTypeDef"],
        "StateTransitionReason": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "BlockDeviceMappings": NotRequired[List["InstanceBlockDeviceMappingTypeDef"]],
        "ClientToken": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "EnaSupport": NotRequired[bool],
        "Hypervisor": NotRequired[HypervisorTypeType],
        "IamInstanceProfile": NotRequired["IamInstanceProfileTypeDef"],
        "InstanceLifecycle": NotRequired[InstanceLifecycleTypeType],
        "ElasticGpuAssociations": NotRequired[List["ElasticGpuAssociationTypeDef"]],
        "ElasticInferenceAcceleratorAssociations": NotRequired[
            List["ElasticInferenceAcceleratorAssociationTypeDef"]
        ],
        "NetworkInterfaces": NotRequired[List["InstanceNetworkInterfaceTypeDef"]],
        "OutpostArn": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "RootDeviceType": NotRequired[DeviceTypeType],
        "SecurityGroups": NotRequired[List["GroupIdentifierTypeDef"]],
        "SourceDestCheck": NotRequired[bool],
        "SpotInstanceRequestId": NotRequired[str],
        "SriovNetSupport": NotRequired[str],
        "StateReason": NotRequired["StateReasonTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VirtualizationType": NotRequired[VirtualizationTypeType],
        "CpuOptions": NotRequired["CpuOptionsTypeDef"],
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationSpecification": NotRequired[
            "CapacityReservationSpecificationResponseTypeDef"
        ],
        "HibernationOptions": NotRequired["HibernationOptionsTypeDef"],
        "Licenses": NotRequired[List["LicenseConfigurationTypeDef"]],
        "MetadataOptions": NotRequired["InstanceMetadataOptionsResponseTypeDef"],
        "EnclaveOptions": NotRequired["EnclaveOptionsTypeDef"],
        "BootMode": NotRequired[BootModeValuesType],
        "PlatformDetails": NotRequired[str],
        "UsageOperation": NotRequired[str],
        "UsageOperationUpdateTime": NotRequired[datetime],
        "PrivateDnsNameOptions": NotRequired["PrivateDnsNameOptionsResponseTypeDef"],
        "Ipv6Address": NotRequired[str],
    },
)

InstanceTypeInfoFromInstanceRequirementsTypeDef = TypedDict(
    "InstanceTypeInfoFromInstanceRequirementsTypeDef",
    {
        "InstanceType": NotRequired[str],
    },
)

InstanceTypeInfoTypeDef = TypedDict(
    "InstanceTypeInfoTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "CurrentGeneration": NotRequired[bool],
        "FreeTierEligible": NotRequired[bool],
        "SupportedUsageClasses": NotRequired[List[UsageClassTypeType]],
        "SupportedRootDeviceTypes": NotRequired[List[RootDeviceTypeType]],
        "SupportedVirtualizationTypes": NotRequired[List[VirtualizationTypeType]],
        "BareMetal": NotRequired[bool],
        "Hypervisor": NotRequired[InstanceTypeHypervisorType],
        "ProcessorInfo": NotRequired["ProcessorInfoTypeDef"],
        "VCpuInfo": NotRequired["VCpuInfoTypeDef"],
        "MemoryInfo": NotRequired["MemoryInfoTypeDef"],
        "InstanceStorageSupported": NotRequired[bool],
        "InstanceStorageInfo": NotRequired["InstanceStorageInfoTypeDef"],
        "EbsInfo": NotRequired["EbsInfoTypeDef"],
        "NetworkInfo": NotRequired["NetworkInfoTypeDef"],
        "GpuInfo": NotRequired["GpuInfoTypeDef"],
        "FpgaInfo": NotRequired["FpgaInfoTypeDef"],
        "PlacementGroupInfo": NotRequired["PlacementGroupInfoTypeDef"],
        "InferenceAcceleratorInfo": NotRequired["InferenceAcceleratorInfoTypeDef"],
        "HibernationSupported": NotRequired[bool],
        "BurstablePerformanceSupported": NotRequired[bool],
        "DedicatedHostsSupported": NotRequired[bool],
        "AutoRecoverySupported": NotRequired[bool],
        "SupportedBootModes": NotRequired[List[BootModeTypeType]],
    },
)

InstanceTypeOfferingTypeDef = TypedDict(
    "InstanceTypeOfferingTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "LocationType": NotRequired[LocationTypeType],
        "Location": NotRequired[str],
    },
)

InstanceUsageTypeDef = TypedDict(
    "InstanceUsageTypeDef",
    {
        "AccountId": NotRequired[str],
        "UsedInstanceCount": NotRequired[int],
    },
)

IntegrateServicesTypeDef = TypedDict(
    "IntegrateServicesTypeDef",
    {
        "AthenaIntegrations": NotRequired[Sequence["AthenaIntegrationTypeDef"]],
    },
)

InternetGatewayAttachmentTypeDef = TypedDict(
    "InternetGatewayAttachmentTypeDef",
    {
        "State": NotRequired[AttachmentStatusType],
        "VpcId": NotRequired[str],
    },
)

InternetGatewayTypeDef = TypedDict(
    "InternetGatewayTypeDef",
    {
        "Attachments": NotRequired[List["InternetGatewayAttachmentTypeDef"]],
        "InternetGatewayId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "IpRanges": NotRequired[Sequence["IpRangeTypeDef"]],
        "Ipv6Ranges": NotRequired[Sequence["Ipv6RangeTypeDef"]],
        "PrefixListIds": NotRequired[Sequence["PrefixListIdTypeDef"]],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[Sequence["UserIdGroupPairTypeDef"]],
    },
)

IpRangeTypeDef = TypedDict(
    "IpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
        "Description": NotRequired[str],
    },
)

IpamAddressHistoryRecordTypeDef = TypedDict(
    "IpamAddressHistoryRecordTypeDef",
    {
        "ResourceOwnerId": NotRequired[str],
        "ResourceRegion": NotRequired[str],
        "ResourceType": NotRequired[IpamAddressHistoryResourceTypeType],
        "ResourceId": NotRequired[str],
        "ResourceCidr": NotRequired[str],
        "ResourceName": NotRequired[str],
        "ResourceComplianceStatus": NotRequired[IpamComplianceStatusType],
        "ResourceOverlapStatus": NotRequired[IpamOverlapStatusType],
        "VpcId": NotRequired[str],
        "SampledStartTime": NotRequired[datetime],
        "SampledEndTime": NotRequired[datetime],
    },
)

IpamCidrAuthorizationContextTypeDef = TypedDict(
    "IpamCidrAuthorizationContextTypeDef",
    {
        "Message": NotRequired[str],
        "Signature": NotRequired[str],
    },
)

IpamOperatingRegionTypeDef = TypedDict(
    "IpamOperatingRegionTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)

IpamPoolAllocationTypeDef = TypedDict(
    "IpamPoolAllocationTypeDef",
    {
        "Cidr": NotRequired[str],
        "IpamPoolAllocationId": NotRequired[str],
        "Description": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[IpamPoolAllocationResourceTypeType],
        "ResourceRegion": NotRequired[str],
        "ResourceOwner": NotRequired[str],
    },
)

IpamPoolCidrFailureReasonTypeDef = TypedDict(
    "IpamPoolCidrFailureReasonTypeDef",
    {
        "Code": NotRequired[Literal["cidr-not-available"]],
        "Message": NotRequired[str],
    },
)

IpamPoolCidrTypeDef = TypedDict(
    "IpamPoolCidrTypeDef",
    {
        "Cidr": NotRequired[str],
        "State": NotRequired[IpamPoolCidrStateType],
        "FailureReason": NotRequired["IpamPoolCidrFailureReasonTypeDef"],
    },
)

IpamPoolTypeDef = TypedDict(
    "IpamPoolTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamPoolId": NotRequired[str],
        "SourceIpamPoolId": NotRequired[str],
        "IpamPoolArn": NotRequired[str],
        "IpamScopeArn": NotRequired[str],
        "IpamScopeType": NotRequired[IpamScopeTypeType],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "Locale": NotRequired[str],
        "PoolDepth": NotRequired[int],
        "State": NotRequired[IpamPoolStateType],
        "StateMessage": NotRequired[str],
        "Description": NotRequired[str],
        "AutoImport": NotRequired[bool],
        "PubliclyAdvertisable": NotRequired[bool],
        "AddressFamily": NotRequired[AddressFamilyType],
        "AllocationMinNetmaskLength": NotRequired[int],
        "AllocationMaxNetmaskLength": NotRequired[int],
        "AllocationDefaultNetmaskLength": NotRequired[int],
        "AllocationResourceTags": NotRequired[List["IpamResourceTagTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "AwsService": NotRequired[Literal["ec2"]],
    },
)

IpamResourceCidrTypeDef = TypedDict(
    "IpamResourceCidrTypeDef",
    {
        "IpamId": NotRequired[str],
        "IpamScopeId": NotRequired[str],
        "IpamPoolId": NotRequired[str],
        "ResourceRegion": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceName": NotRequired[str],
        "ResourceCidr": NotRequired[str],
        "ResourceType": NotRequired[IpamResourceTypeType],
        "ResourceTags": NotRequired[List["IpamResourceTagTypeDef"]],
        "IpUsage": NotRequired[float],
        "ComplianceStatus": NotRequired[IpamComplianceStatusType],
        "ManagementState": NotRequired[IpamManagementStateType],
        "OverlapStatus": NotRequired[IpamOverlapStatusType],
        "VpcId": NotRequired[str],
    },
)

IpamResourceTagTypeDef = TypedDict(
    "IpamResourceTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

IpamScopeTypeDef = TypedDict(
    "IpamScopeTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamScopeId": NotRequired[str],
        "IpamScopeArn": NotRequired[str],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "IpamScopeType": NotRequired[IpamScopeTypeType],
        "IsDefault": NotRequired[bool],
        "Description": NotRequired[str],
        "PoolCount": NotRequired[int],
        "State": NotRequired[IpamScopeStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

IpamTypeDef = TypedDict(
    "IpamTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamId": NotRequired[str],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "PublicDefaultScopeId": NotRequired[str],
        "PrivateDefaultScopeId": NotRequired[str],
        "ScopeCount": NotRequired[int],
        "Description": NotRequired[str],
        "OperatingRegions": NotRequired[List["IpamOperatingRegionTypeDef"]],
        "State": NotRequired[IpamStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

Ipv4PrefixSpecificationRequestTypeDef = TypedDict(
    "Ipv4PrefixSpecificationRequestTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)

Ipv4PrefixSpecificationResponseTypeDef = TypedDict(
    "Ipv4PrefixSpecificationResponseTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)

Ipv4PrefixSpecificationTypeDef = TypedDict(
    "Ipv4PrefixSpecificationTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)

Ipv6CidrAssociationTypeDef = TypedDict(
    "Ipv6CidrAssociationTypeDef",
    {
        "Ipv6Cidr": NotRequired[str],
        "AssociatedResource": NotRequired[str],
    },
)

Ipv6CidrBlockTypeDef = TypedDict(
    "Ipv6CidrBlockTypeDef",
    {
        "Ipv6CidrBlock": NotRequired[str],
    },
)

Ipv6PoolTypeDef = TypedDict(
    "Ipv6PoolTypeDef",
    {
        "PoolId": NotRequired[str],
        "Description": NotRequired[str],
        "PoolCidrBlocks": NotRequired[List["PoolCidrBlockTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

Ipv6PrefixSpecificationRequestTypeDef = TypedDict(
    "Ipv6PrefixSpecificationRequestTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)

Ipv6PrefixSpecificationResponseTypeDef = TypedDict(
    "Ipv6PrefixSpecificationResponseTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)

Ipv6PrefixSpecificationTypeDef = TypedDict(
    "Ipv6PrefixSpecificationTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)

Ipv6RangeTypeDef = TypedDict(
    "Ipv6RangeTypeDef",
    {
        "CidrIpv6": NotRequired[str],
        "Description": NotRequired[str],
    },
)

KeyPairInfoTypeDef = TypedDict(
    "KeyPairInfoTypeDef",
    {
        "KeyPairId": NotRequired[str],
        "KeyFingerprint": NotRequired[str],
        "KeyName": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "KeyFingerprint": str,
        "KeyMaterial": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LastErrorTypeDef = TypedDict(
    "LastErrorTypeDef",
    {
        "Message": NotRequired[str],
        "Code": NotRequired[str],
    },
)

LaunchPermissionModificationsTypeDef = TypedDict(
    "LaunchPermissionModificationsTypeDef",
    {
        "Add": NotRequired[Sequence["LaunchPermissionTypeDef"]],
        "Remove": NotRequired[Sequence["LaunchPermissionTypeDef"]],
    },
)

LaunchPermissionTypeDef = TypedDict(
    "LaunchPermissionTypeDef",
    {
        "Group": NotRequired[Literal["all"]],
        "UserId": NotRequired[str],
        "OrganizationArn": NotRequired[str],
        "OrganizationalUnitArn": NotRequired[str],
    },
)

LaunchSpecificationTypeDef = TypedDict(
    "LaunchSpecificationTypeDef",
    {
        "UserData": NotRequired[str],
        "SecurityGroups": NotRequired[List["GroupIdentifierTypeDef"]],
        "AddressingType": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List["BlockDeviceMappingTypeDef"]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["IamInstanceProfileSpecificationTypeDef"],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "NetworkInterfaces": NotRequired[List["InstanceNetworkInterfaceSpecificationTypeDef"]],
        "Placement": NotRequired["SpotPlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Monitoring": NotRequired["RunInstancesMonitoringEnabledTypeDef"],
    },
)

LaunchTemplateAndOverridesResponseTypeDef = TypedDict(
    "LaunchTemplateAndOverridesResponseTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired["FleetLaunchTemplateSpecificationTypeDef"],
        "Overrides": NotRequired["FleetLaunchTemplateOverridesTypeDef"],
    },
)

LaunchTemplateBlockDeviceMappingRequestTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    {
        "DeviceName": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired["LaunchTemplateEbsBlockDeviceRequestTypeDef"],
        "NoDevice": NotRequired[str],
    },
)

LaunchTemplateBlockDeviceMappingTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired["LaunchTemplateEbsBlockDeviceTypeDef"],
        "NoDevice": NotRequired[str],
    },
)

LaunchTemplateCapacityReservationSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired["CapacityReservationTargetTypeDef"],
    },
)

LaunchTemplateCapacityReservationSpecificationResponseTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired["CapacityReservationTargetResponseTypeDef"],
    },
)

LaunchTemplateConfigTypeDef = TypedDict(
    "LaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired["FleetLaunchTemplateSpecificationTypeDef"],
        "Overrides": NotRequired[List["LaunchTemplateOverridesTypeDef"]],
    },
)

LaunchTemplateCpuOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsRequestTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
    },
)

LaunchTemplateCpuOptionsTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
    },
)

LaunchTemplateEbsBlockDeviceRequestTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    {
        "Encrypted": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "Throughput": NotRequired[int],
    },
)

LaunchTemplateEbsBlockDeviceTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceTypeDef",
    {
        "Encrypted": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "Throughput": NotRequired[int],
    },
)

LaunchTemplateElasticInferenceAcceleratorResponseTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    {
        "Type": NotRequired[str],
        "Count": NotRequired[int],
    },
)

LaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
        "Count": NotRequired[int],
    },
)

LaunchTemplateEnclaveOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

LaunchTemplateEnclaveOptionsTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

LaunchTemplateHibernationOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)

LaunchTemplateHibernationOptionsTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)

LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

LaunchTemplateIamInstanceProfileSpecificationTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

LaunchTemplateInstanceMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": NotRequired[Literal["spot"]],
        "SpotOptions": NotRequired["LaunchTemplateSpotMarketOptionsRequestTypeDef"],
    },
)

LaunchTemplateInstanceMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    {
        "MarketType": NotRequired[Literal["spot"]],
        "SpotOptions": NotRequired["LaunchTemplateSpotMarketOptionsTypeDef"],
    },
)

LaunchTemplateInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": NotRequired[LaunchTemplateHttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[LaunchTemplateInstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[LaunchTemplateInstanceMetadataProtocolIpv6Type],
        "InstanceMetadataTags": NotRequired[LaunchTemplateInstanceMetadataTagsStateType],
    },
)

LaunchTemplateInstanceMetadataOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    {
        "State": NotRequired[LaunchTemplateInstanceMetadataOptionsStateType],
        "HttpTokens": NotRequired[LaunchTemplateHttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[LaunchTemplateInstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[LaunchTemplateInstanceMetadataProtocolIpv6Type],
        "InstanceMetadataTags": NotRequired[LaunchTemplateInstanceMetadataTagsStateType],
    },
)

LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "InterfaceType": NotRequired[str],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressRequestTypeDef"]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence["PrivateIpAddressSpecificationTypeDef"]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence["Ipv4PrefixSpecificationRequestTypeDef"]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence["Ipv6PrefixSpecificationRequestTypeDef"]],
        "Ipv6PrefixCount": NotRequired[int],
    },
)

LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[List[str]],
        "InterfaceType": NotRequired[str],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[List["InstanceIpv6AddressTypeDef"]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List["PrivateIpAddressSpecificationTypeDef"]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[List["Ipv4PrefixSpecificationResponseTypeDef"]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[List["Ipv6PrefixSpecificationResponseTypeDef"]],
        "Ipv6PrefixCount": NotRequired[int],
    },
)

LaunchTemplateLicenseConfigurationRequestTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)

LaunchTemplateLicenseConfigurationTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "SpotPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "Priority": NotRequired[float],
        "InstanceRequirements": NotRequired["InstanceRequirementsTypeDef"],
    },
)

LaunchTemplatePlacementRequestTypeDef = TypedDict(
    "LaunchTemplatePlacementRequestTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Affinity": NotRequired[str],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
        "SpreadDomain": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "PartitionNumber": NotRequired[int],
    },
)

LaunchTemplatePlacementTypeDef = TypedDict(
    "LaunchTemplatePlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Affinity": NotRequired[str],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
        "SpreadDomain": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "PartitionNumber": NotRequired[int],
    },
)

LaunchTemplatePrivateDnsNameOptionsRequestTypeDef = TypedDict(
    "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)

LaunchTemplatePrivateDnsNameOptionsTypeDef = TypedDict(
    "LaunchTemplatePrivateDnsNameOptionsTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

LaunchTemplateSpotMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    {
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[SpotInstanceTypeType],
        "BlockDurationMinutes": NotRequired[int],
        "ValidUntil": NotRequired[Union[datetime, str]],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)

LaunchTemplateSpotMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsTypeDef",
    {
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[SpotInstanceTypeType],
        "BlockDurationMinutes": NotRequired[int],
        "ValidUntil": NotRequired[datetime],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)

LaunchTemplateTagSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationRequestTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

LaunchTemplateTagSpecificationTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DefaultVersionNumber": NotRequired[int],
        "LatestVersionNumber": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LaunchTemplateVersionTypeDef = TypedDict(
    "LaunchTemplateVersionTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "VersionDescription": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DefaultVersion": NotRequired[bool],
        "LaunchTemplateData": NotRequired["ResponseLaunchTemplateDataTypeDef"],
    },
)

LaunchTemplatesMonitoringRequestTypeDef = TypedDict(
    "LaunchTemplatesMonitoringRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

LaunchTemplatesMonitoringTypeDef = TypedDict(
    "LaunchTemplatesMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

LicenseConfigurationRequestTypeDef = TypedDict(
    "LicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)

ListImagesInRecycleBinRequestRequestTypeDef = TypedDict(
    "ListImagesInRecycleBinRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

ListImagesInRecycleBinResultTypeDef = TypedDict(
    "ListImagesInRecycleBinResultTypeDef",
    {
        "Images": List["ImageRecycleBinInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSnapshotsInRecycleBinRequestRequestTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

ListSnapshotsInRecycleBinResultTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinResultTypeDef",
    {
        "Snapshots": List["SnapshotRecycleBinInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancersConfigTypeDef = TypedDict(
    "LoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancersConfig": NotRequired["ClassicLoadBalancersConfigTypeDef"],
        "TargetGroupsConfig": NotRequired["TargetGroupsConfigTypeDef"],
    },
)

LoadPermissionModificationsTypeDef = TypedDict(
    "LoadPermissionModificationsTypeDef",
    {
        "Add": NotRequired[Sequence["LoadPermissionRequestTypeDef"]],
        "Remove": NotRequired[Sequence["LoadPermissionRequestTypeDef"]],
    },
)

LoadPermissionRequestTypeDef = TypedDict(
    "LoadPermissionRequestTypeDef",
    {
        "Group": NotRequired[Literal["all"]],
        "UserId": NotRequired[str],
    },
)

LoadPermissionTypeDef = TypedDict(
    "LoadPermissionTypeDef",
    {
        "UserId": NotRequired[str],
        "Group": NotRequired[Literal["all"]],
    },
)

LocalGatewayRouteTableTypeDef = TypedDict(
    "LocalGatewayRouteTableTypeDef",
    {
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": NotRequired[str],
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LocalGatewayRouteTableVpcAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": NotRequired[str],
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LocalGatewayRouteTypeDef = TypedDict(
    "LocalGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "Type": NotRequired[LocalGatewayRouteTypeType],
        "State": NotRequired[LocalGatewayRouteStateType],
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)

LocalGatewayTypeDef = TypedDict(
    "LocalGatewayTypeDef",
    {
        "LocalGatewayId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LocalGatewayVirtualInterfaceGroupTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "LocalGatewayVirtualInterfaceIds": NotRequired[List[str]],
        "LocalGatewayId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LocalGatewayVirtualInterfaceTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceTypeDef",
    {
        "LocalGatewayVirtualInterfaceId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "Vlan": NotRequired[int],
        "LocalAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "LocalBgpAsn": NotRequired[int],
        "PeerBgpAsn": NotRequired[int],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ManagedPrefixListTypeDef = TypedDict(
    "ManagedPrefixListTypeDef",
    {
        "PrefixListId": NotRequired[str],
        "AddressFamily": NotRequired[str],
        "State": NotRequired[PrefixListStateType],
        "StateMessage": NotRequired[str],
        "PrefixListArn": NotRequired[str],
        "PrefixListName": NotRequired[str],
        "MaxEntries": NotRequired[int],
        "Version": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
        "OwnerId": NotRequired[str],
    },
)

MemoryGiBPerVCpuRequestTypeDef = TypedDict(
    "MemoryGiBPerVCpuRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)

MemoryGiBPerVCpuTypeDef = TypedDict(
    "MemoryGiBPerVCpuTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)

MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)

MemoryMiBRequestTypeDef = TypedDict(
    "MemoryMiBRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)

MemoryMiBTypeDef = TypedDict(
    "MemoryMiBTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

ModifyAddressAttributeRequestRequestTypeDef = TypedDict(
    "ModifyAddressAttributeRequestRequestTypeDef",
    {
        "AllocationId": str,
        "DomainName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ModifyAddressAttributeResultTypeDef = TypedDict(
    "ModifyAddressAttributeResultTypeDef",
    {
        "Address": "AddressAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyAvailabilityZoneGroupRequestRequestTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "OptInStatus": ModifyAvailabilityZoneOptInStatusType,
        "DryRun": NotRequired[bool],
    },
)

ModifyAvailabilityZoneGroupResultTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "ModifyCapacityReservationFleetRequestRequestTypeDef",
    {
        "CapacityReservationFleetId": str,
        "TotalTargetCapacity": NotRequired[int],
        "EndDate": NotRequired[Union[datetime, str]],
        "DryRun": NotRequired[bool],
        "RemoveEndDate": NotRequired[bool],
    },
)

ModifyCapacityReservationFleetResultTypeDef = TypedDict(
    "ModifyCapacityReservationFleetResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCapacityReservationRequestRequestTypeDef = TypedDict(
    "ModifyCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "InstanceCount": NotRequired[int],
        "EndDate": NotRequired[Union[datetime, str]],
        "EndDateType": NotRequired[EndDateTypeType],
        "Accept": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "AdditionalInfo": NotRequired[str],
    },
)

ModifyCapacityReservationResultTypeDef = TypedDict(
    "ModifyCapacityReservationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "ModifyClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "ServerCertificateArn": NotRequired[str],
        "ConnectionLogOptions": NotRequired["ConnectionLogOptionsTypeDef"],
        "DnsServers": NotRequired["DnsServersOptionsModifyStructureTypeDef"],
        "VpnPort": NotRequired[int],
        "Description": NotRequired[str],
        "SplitTunnel": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortal": NotRequired[SelfServicePortalType],
        "ClientConnectOptions": NotRequired["ClientConnectOptionsTypeDef"],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired["ClientLoginBannerOptionsTypeDef"],
    },
)

ModifyClientVpnEndpointResultTypeDef = TypedDict(
    "ModifyClientVpnEndpointResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "CpuCredits": str,
        "DryRun": NotRequired[bool],
    },
)

ModifyDefaultCreditSpecificationResultTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationResultTypeDef",
    {
        "InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "KmsKeyId": str,
        "DryRun": NotRequired[bool],
    },
)

ModifyEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyFleetRequestRequestTypeDef = TypedDict(
    "ModifyFleetRequestRequestTypeDef",
    {
        "FleetId": str,
        "DryRun": NotRequired[bool],
        "ExcessCapacityTerminationPolicy": NotRequired[FleetExcessCapacityTerminationPolicyType],
        "LaunchTemplateConfigs": NotRequired[Sequence["FleetLaunchTemplateConfigRequestTypeDef"]],
        "TargetCapacitySpecification": NotRequired["TargetCapacitySpecificationRequestTypeDef"],
        "Context": NotRequired[str],
    },
)

ModifyFleetResultTypeDef = TypedDict(
    "ModifyFleetResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "ModifyFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "DryRun": NotRequired[bool],
        "Attribute": NotRequired[FpgaImageAttributeNameType],
        "OperationType": NotRequired[OperationTypeType],
        "UserIds": NotRequired[Sequence[str]],
        "UserGroups": NotRequired[Sequence[str]],
        "ProductCodes": NotRequired[Sequence[str]],
        "LoadPermission": NotRequired["LoadPermissionModificationsTypeDef"],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ModifyFpgaImageAttributeResultTypeDef = TypedDict(
    "ModifyFpgaImageAttributeResultTypeDef",
    {
        "FpgaImageAttribute": "FpgaImageAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyHostsRequestRequestTypeDef = TypedDict(
    "ModifyHostsRequestRequestTypeDef",
    {
        "HostIds": Sequence[str],
        "AutoPlacement": NotRequired[AutoPlacementType],
        "HostRecovery": NotRequired[HostRecoveryType],
        "InstanceType": NotRequired[str],
        "InstanceFamily": NotRequired[str],
    },
)

ModifyHostsResultTypeDef = TypedDict(
    "ModifyHostsResultTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIdFormatRequestRequestTypeDef = TypedDict(
    "ModifyIdFormatRequestRequestTypeDef",
    {
        "Resource": str,
        "UseLongIds": bool,
    },
)

ModifyIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "ModifyIdentityIdFormatRequestRequestTypeDef",
    {
        "PrincipalArn": str,
        "Resource": str,
        "UseLongIds": bool,
    },
)

ModifyImageAttributeRequestImageModifyAttributeTypeDef = TypedDict(
    "ModifyImageAttributeRequestImageModifyAttributeTypeDef",
    {
        "Attribute": NotRequired[str],
        "Description": NotRequired["AttributeValueTypeDef"],
        "LaunchPermission": NotRequired["LaunchPermissionModificationsTypeDef"],
        "OperationType": NotRequired[OperationTypeType],
        "ProductCodes": NotRequired[Sequence[str]],
        "UserGroups": NotRequired[Sequence[str]],
        "UserIds": NotRequired[Sequence[str]],
        "Value": NotRequired[str],
        "DryRun": NotRequired[bool],
        "OrganizationArns": NotRequired[Sequence[str]],
        "OrganizationalUnitArns": NotRequired[Sequence[str]],
    },
)

ModifyImageAttributeRequestRequestTypeDef = TypedDict(
    "ModifyImageAttributeRequestRequestTypeDef",
    {
        "ImageId": str,
        "Attribute": NotRequired[str],
        "Description": NotRequired["AttributeValueTypeDef"],
        "LaunchPermission": NotRequired["LaunchPermissionModificationsTypeDef"],
        "OperationType": NotRequired[OperationTypeType],
        "ProductCodes": NotRequired[Sequence[str]],
        "UserGroups": NotRequired[Sequence[str]],
        "UserIds": NotRequired[Sequence[str]],
        "Value": NotRequired[str],
        "DryRun": NotRequired[bool],
        "OrganizationArns": NotRequired[Sequence[str]],
        "OrganizationalUnitArns": NotRequired[Sequence[str]],
    },
)

ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef = TypedDict(
    "ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef",
    {
        "SourceDestCheck": NotRequired["AttributeBooleanValueTypeDef"],
        "Attribute": NotRequired[InstanceAttributeNameType],
        "BlockDeviceMappings": NotRequired[
            Sequence["InstanceBlockDeviceMappingSpecificationTypeDef"]
        ],
        "DisableApiTermination": NotRequired["AttributeBooleanValueTypeDef"],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired["AttributeBooleanValueTypeDef"],
        "EnaSupport": NotRequired["AttributeBooleanValueTypeDef"],
        "Groups": NotRequired[Sequence[str]],
        "InstanceInitiatedShutdownBehavior": NotRequired["AttributeValueTypeDef"],
        "InstanceType": NotRequired["AttributeValueTypeDef"],
        "Kernel": NotRequired["AttributeValueTypeDef"],
        "Ramdisk": NotRequired["AttributeValueTypeDef"],
        "SriovNetSupport": NotRequired["AttributeValueTypeDef"],
        "UserData": NotRequired["BlobAttributeValueTypeDef"],
        "Value": NotRequired[str],
    },
)

ModifyInstanceAttributeRequestRequestTypeDef = TypedDict(
    "ModifyInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SourceDestCheck": NotRequired["AttributeBooleanValueTypeDef"],
        "Attribute": NotRequired[InstanceAttributeNameType],
        "BlockDeviceMappings": NotRequired[
            Sequence["InstanceBlockDeviceMappingSpecificationTypeDef"]
        ],
        "DisableApiTermination": NotRequired["AttributeBooleanValueTypeDef"],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired["AttributeBooleanValueTypeDef"],
        "EnaSupport": NotRequired["AttributeBooleanValueTypeDef"],
        "Groups": NotRequired[Sequence[str]],
        "InstanceInitiatedShutdownBehavior": NotRequired["AttributeValueTypeDef"],
        "InstanceType": NotRequired["AttributeValueTypeDef"],
        "Kernel": NotRequired["AttributeValueTypeDef"],
        "Ramdisk": NotRequired["AttributeValueTypeDef"],
        "SriovNetSupport": NotRequired["AttributeValueTypeDef"],
        "UserData": NotRequired["BlobAttributeValueTypeDef"],
        "Value": NotRequired[str],
    },
)

ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "DryRun": NotRequired[bool],
    },
)

ModifyInstanceCapacityReservationAttributesResultTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceCreditSpecificationRequestRequestTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceCreditSpecifications": Sequence["InstanceCreditSpecificationRequestTypeDef"],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

ModifyInstanceCreditSpecificationResultTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationResultTypeDef",
    {
        "SuccessfulInstanceCreditSpecifications": List[
            "SuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "UnsuccessfulInstanceCreditSpecifications": List[
            "UnsuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceEventStartTimeRequestRequestTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceEventId": str,
        "NotBefore": Union[datetime, str],
        "DryRun": NotRequired[bool],
    },
)

ModifyInstanceEventStartTimeResultTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeResultTypeDef",
    {
        "Event": "InstanceStatusEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "ModifyInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "DryRun": NotRequired[bool],
        "Name": NotRequired[str],
        "TimeRanges": NotRequired[Sequence["InstanceEventWindowTimeRangeRequestTypeDef"]],
        "CronExpression": NotRequired[str],
    },
)

ModifyInstanceEventWindowResultTypeDef = TypedDict(
    "ModifyInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceMetadataOptionsRequestRequestTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HttpTokens": NotRequired[HttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
        "DryRun": NotRequired[bool],
        "HttpProtocolIpv6": NotRequired[InstanceMetadataProtocolStateType],
        "InstanceMetadataTags": NotRequired[InstanceMetadataTagsStateType],
    },
)

ModifyInstanceMetadataOptionsResultTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsResultTypeDef",
    {
        "InstanceId": str,
        "InstanceMetadataOptions": "InstanceMetadataOptionsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstancePlacementRequestRequestTypeDef = TypedDict(
    "ModifyInstancePlacementRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Affinity": NotRequired[AffinityType],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[HostTenancyType],
        "PartitionNumber": NotRequired[int],
        "HostResourceGroupArn": NotRequired[str],
    },
)

ModifyInstancePlacementResultTypeDef = TypedDict(
    "ModifyInstancePlacementResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIpamPoolRequestRequestTypeDef = TypedDict(
    "ModifyIpamPoolRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "AutoImport": NotRequired[bool],
        "AllocationMinNetmaskLength": NotRequired[int],
        "AllocationMaxNetmaskLength": NotRequired[int],
        "AllocationDefaultNetmaskLength": NotRequired[int],
        "ClearAllocationDefaultNetmaskLength": NotRequired[bool],
        "AddAllocationResourceTags": NotRequired[Sequence["RequestIpamResourceTagTypeDef"]],
        "RemoveAllocationResourceTags": NotRequired[Sequence["RequestIpamResourceTagTypeDef"]],
    },
)

ModifyIpamPoolResultTypeDef = TypedDict(
    "ModifyIpamPoolResultTypeDef",
    {
        "IpamPool": "IpamPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIpamRequestRequestTypeDef = TypedDict(
    "ModifyIpamRequestRequestTypeDef",
    {
        "IpamId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "AddOperatingRegions": NotRequired[Sequence["AddIpamOperatingRegionTypeDef"]],
        "RemoveOperatingRegions": NotRequired[Sequence["RemoveIpamOperatingRegionTypeDef"]],
    },
)

ModifyIpamResourceCidrRequestRequestTypeDef = TypedDict(
    "ModifyIpamResourceCidrRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceCidr": str,
        "ResourceRegion": str,
        "CurrentIpamScopeId": str,
        "Monitored": bool,
        "DryRun": NotRequired[bool],
        "DestinationIpamScopeId": NotRequired[str],
    },
)

ModifyIpamResourceCidrResultTypeDef = TypedDict(
    "ModifyIpamResourceCidrResultTypeDef",
    {
        "IpamResourceCidr": "IpamResourceCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIpamResultTypeDef = TypedDict(
    "ModifyIpamResultTypeDef",
    {
        "Ipam": "IpamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIpamScopeRequestRequestTypeDef = TypedDict(
    "ModifyIpamScopeRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
    },
)

ModifyIpamScopeResultTypeDef = TypedDict(
    "ModifyIpamScopeResultTypeDef",
    {
        "IpamScope": "IpamScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLaunchTemplateRequestRequestTypeDef = TypedDict(
    "ModifyLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "DefaultVersion": NotRequired[str],
    },
)

ModifyLaunchTemplateResultTypeDef = TypedDict(
    "ModifyLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyManagedPrefixListRequestRequestTypeDef = TypedDict(
    "ModifyManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "CurrentVersion": NotRequired[int],
        "PrefixListName": NotRequired[str],
        "AddEntries": NotRequired[Sequence["AddPrefixListEntryTypeDef"]],
        "RemoveEntries": NotRequired[Sequence["RemovePrefixListEntryTypeDef"]],
        "MaxEntries": NotRequired[int],
    },
)

ModifyManagedPrefixListResultTypeDef = TypedDict(
    "ModifyManagedPrefixListResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef = TypedDict(
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef",
    {
        "Attachment": NotRequired["NetworkInterfaceAttachmentChangesTypeDef"],
        "Description": NotRequired["AttributeValueTypeDef"],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "SourceDestCheck": NotRequired["AttributeBooleanValueTypeDef"],
    },
)

ModifyNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "ModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Attachment": NotRequired["NetworkInterfaceAttachmentChangesTypeDef"],
        "Description": NotRequired["AttributeValueTypeDef"],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "SourceDestCheck": NotRequired["AttributeBooleanValueTypeDef"],
    },
)

ModifyPrivateDnsNameOptionsRequestRequestTypeDef = TypedDict(
    "ModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "PrivateDnsHostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)

ModifyPrivateDnsNameOptionsResultTypeDef = TypedDict(
    "ModifyPrivateDnsNameOptionsResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReservedInstancesRequestRequestTypeDef = TypedDict(
    "ModifyReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstancesIds": Sequence[str],
        "TargetConfigurations": Sequence["ReservedInstancesConfigurationTypeDef"],
        "ClientToken": NotRequired[str],
    },
)

ModifyReservedInstancesResultTypeDef = TypedDict(
    "ModifyReservedInstancesResultTypeDef",
    {
        "ReservedInstancesModificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "ModifySecurityGroupRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "SecurityGroupRules": Sequence["SecurityGroupRuleUpdateTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

ModifySecurityGroupRulesResultTypeDef = TypedDict(
    "ModifySecurityGroupRulesResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySnapshotAttributeRequestRequestTypeDef = TypedDict(
    "ModifySnapshotAttributeRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "Attribute": NotRequired[SnapshotAttributeNameType],
        "CreateVolumePermission": NotRequired["CreateVolumePermissionModificationsTypeDef"],
        "GroupNames": NotRequired[Sequence[str]],
        "OperationType": NotRequired[OperationTypeType],
        "UserIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef = TypedDict(
    "ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef",
    {
        "Attribute": NotRequired[SnapshotAttributeNameType],
        "CreateVolumePermission": NotRequired["CreateVolumePermissionModificationsTypeDef"],
        "GroupNames": NotRequired[Sequence[str]],
        "OperationType": NotRequired[OperationTypeType],
        "UserIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

ModifySnapshotTierRequestRequestTypeDef = TypedDict(
    "ModifySnapshotTierRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "StorageTier": NotRequired[Literal["archive"]],
        "DryRun": NotRequired[bool],
    },
)

ModifySnapshotTierResultTypeDef = TypedDict(
    "ModifySnapshotTierResultTypeDef",
    {
        "SnapshotId": str,
        "TieringStartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySpotFleetRequestRequestRequestTypeDef = TypedDict(
    "ModifySpotFleetRequestRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "ExcessCapacityTerminationPolicy": NotRequired[ExcessCapacityTerminationPolicyType],
        "LaunchTemplateConfigs": NotRequired[Sequence["LaunchTemplateConfigTypeDef"]],
        "TargetCapacity": NotRequired[int],
        "OnDemandTargetCapacity": NotRequired[int],
        "Context": NotRequired[str],
    },
)

ModifySpotFleetRequestResponseTypeDef = TypedDict(
    "ModifySpotFleetRequestResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySubnetAttributeRequestRequestTypeDef = TypedDict(
    "ModifySubnetAttributeRequestRequestTypeDef",
    {
        "SubnetId": str,
        "AssignIpv6AddressOnCreation": NotRequired["AttributeBooleanValueTypeDef"],
        "MapPublicIpOnLaunch": NotRequired["AttributeBooleanValueTypeDef"],
        "MapCustomerOwnedIpOnLaunch": NotRequired["AttributeBooleanValueTypeDef"],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "EnableDns64": NotRequired["AttributeBooleanValueTypeDef"],
        "PrivateDnsHostnameTypeOnLaunch": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecordOnLaunch": NotRequired["AttributeBooleanValueTypeDef"],
        "EnableResourceNameDnsAAAARecordOnLaunch": NotRequired["AttributeBooleanValueTypeDef"],
        "EnableLniAtDeviceIndex": NotRequired[int],
        "DisableLniAtDeviceIndex": NotRequired["AttributeBooleanValueTypeDef"],
    },
)

ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "AddNetworkServices": NotRequired[Sequence[Literal["amazon-dns"]]],
        "RemoveNetworkServices": NotRequired[Sequence[Literal["amazon-dns"]]],
        "DryRun": NotRequired[bool],
    },
)

ModifyTrafficMirrorFilterNetworkServicesResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    {
        "TrafficMirrorFilter": "TrafficMirrorFilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "TrafficDirection": NotRequired[TrafficDirectionType],
        "RuleNumber": NotRequired[int],
        "RuleAction": NotRequired[TrafficMirrorRuleActionType],
        "DestinationPortRange": NotRequired["TrafficMirrorPortRangeRequestTypeDef"],
        "SourcePortRange": NotRequired["TrafficMirrorPortRangeRequestTypeDef"],
        "Protocol": NotRequired[int],
        "DestinationCidrBlock": NotRequired[str],
        "SourceCidrBlock": NotRequired[str],
        "Description": NotRequired[str],
        "RemoveFields": NotRequired[Sequence[TrafficMirrorFilterRuleFieldType]],
        "DryRun": NotRequired[bool],
    },
)

ModifyTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "TrafficMirrorTargetId": NotRequired[str],
        "TrafficMirrorFilterId": NotRequired[str],
        "PacketLength": NotRequired[int],
        "SessionNumber": NotRequired[int],
        "VirtualNetworkId": NotRequired[int],
        "Description": NotRequired[str],
        "RemoveFields": NotRequired[Sequence[TrafficMirrorSessionFieldType]],
        "DryRun": NotRequired[bool],
    },
)

ModifyTrafficMirrorSessionResultTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSession": "TrafficMirrorSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayOptionsTypeDef",
    {
        "AddTransitGatewayCidrBlocks": NotRequired[Sequence[str]],
        "RemoveTransitGatewayCidrBlocks": NotRequired[Sequence[str]],
        "VpnEcmpSupport": NotRequired[VpnEcmpSupportValueType],
        "DnsSupport": NotRequired[DnsSupportValueType],
        "AutoAcceptSharedAttachments": NotRequired[AutoAcceptSharedAttachmentsValueType],
        "DefaultRouteTableAssociation": NotRequired[DefaultRouteTableAssociationValueType],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[DefaultRouteTablePropagationValueType],
        "PropagationDefaultRouteTableId": NotRequired[str],
    },
)

ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

ModifyTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayRequestRequestTypeDef = TypedDict(
    "ModifyTransitGatewayRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "Description": NotRequired[str],
        "Options": NotRequired["ModifyTransitGatewayOptionsTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

ModifyTransitGatewayResultTypeDef = TypedDict(
    "ModifyTransitGatewayResultTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": NotRequired[DnsSupportValueType],
        "Ipv6Support": NotRequired[Ipv6SupportValueType],
        "ApplianceModeSupport": NotRequired[ApplianceModeSupportValueType],
    },
)

ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "AddSubnetIds": NotRequired[Sequence[str]],
        "RemoveSubnetIds": NotRequired[Sequence[str]],
        "Options": NotRequired["ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

ModifyTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVolumeAttributeRequestRequestTypeDef = TypedDict(
    "ModifyVolumeAttributeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "AutoEnableIO": NotRequired["AttributeBooleanValueTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef = TypedDict(
    "ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef",
    {
        "AutoEnableIO": NotRequired["AttributeBooleanValueTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

ModifyVolumeRequestRequestTypeDef = TypedDict(
    "ModifyVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "DryRun": NotRequired[bool],
        "Size": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "Iops": NotRequired[int],
        "Throughput": NotRequired[int],
        "MultiAttachEnabled": NotRequired[bool],
    },
)

ModifyVolumeResultTypeDef = TypedDict(
    "ModifyVolumeResultTypeDef",
    {
        "VolumeModification": "VolumeModificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcAttributeRequestRequestTypeDef = TypedDict(
    "ModifyVpcAttributeRequestRequestTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": NotRequired["AttributeBooleanValueTypeDef"],
        "EnableDnsSupport": NotRequired["AttributeBooleanValueTypeDef"],
    },
)

ModifyVpcAttributeRequestVpcModifyAttributeTypeDef = TypedDict(
    "ModifyVpcAttributeRequestVpcModifyAttributeTypeDef",
    {
        "EnableDnsHostnames": NotRequired["AttributeBooleanValueTypeDef"],
        "EnableDnsSupport": NotRequired["AttributeBooleanValueTypeDef"],
    },
)

ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "ConnectionNotificationId": str,
        "DryRun": NotRequired[bool],
        "ConnectionNotificationArn": NotRequired[str],
        "ConnectionEvents": NotRequired[Sequence[str]],
    },
)

ModifyVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcEndpointRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointRequestRequestTypeDef",
    {
        "VpcEndpointId": str,
        "DryRun": NotRequired[bool],
        "ResetPolicy": NotRequired[bool],
        "PolicyDocument": NotRequired[str],
        "AddRouteTableIds": NotRequired[Sequence[str]],
        "RemoveRouteTableIds": NotRequired[Sequence[str]],
        "AddSubnetIds": NotRequired[Sequence[str]],
        "RemoveSubnetIds": NotRequired[Sequence[str]],
        "AddSecurityGroupIds": NotRequired[Sequence[str]],
        "RemoveSecurityGroupIds": NotRequired[Sequence[str]],
        "PrivateDnsEnabled": NotRequired[bool],
    },
)

ModifyVpcEndpointResultTypeDef = TypedDict(
    "ModifyVpcEndpointResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "RemovePrivateDnsName": NotRequired[bool],
        "AcceptanceRequired": NotRequired[bool],
        "AddNetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "RemoveNetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "AddGatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "RemoveGatewayLoadBalancerArns": NotRequired[Sequence[str]],
    },
)

ModifyVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    {
        "ServiceId": str,
        "PayerResponsibility": Literal["ServiceOwner"],
        "DryRun": NotRequired[bool],
    },
)

ModifyVpcEndpointServicePayerResponsibilityResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "AddAllowedPrincipals": NotRequired[Sequence[str]],
        "RemoveAllowedPrincipals": NotRequired[Sequence[str]],
    },
)

ModifyVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "AccepterPeeringConnectionOptions": NotRequired["PeeringConnectionOptionsRequestTypeDef"],
        "DryRun": NotRequired[bool],
        "RequesterPeeringConnectionOptions": NotRequired["PeeringConnectionOptionsRequestTypeDef"],
    },
)

ModifyVpcPeeringConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    {
        "AccepterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "RequesterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpcTenancyRequestRequestTypeDef = TypedDict(
    "ModifyVpcTenancyRequestRequestTypeDef",
    {
        "VpcId": str,
        "InstanceTenancy": Literal["default"],
        "DryRun": NotRequired[bool],
    },
)

ModifyVpcTenancyResultTypeDef = TypedDict(
    "ModifyVpcTenancyResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnConnectionOptionsRequestRequestTypeDef = TypedDict(
    "ModifyVpnConnectionOptionsRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "LocalIpv4NetworkCidr": NotRequired[str],
        "RemoteIpv4NetworkCidr": NotRequired[str],
        "LocalIpv6NetworkCidr": NotRequired[str],
        "RemoteIpv6NetworkCidr": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ModifyVpnConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpnConnectionOptionsResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnConnectionRequestRequestTypeDef = TypedDict(
    "ModifyVpnConnectionRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "TransitGatewayId": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ModifyVpnConnectionResultTypeDef = TypedDict(
    "ModifyVpnConnectionResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnTunnelCertificateRequestRequestTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "DryRun": NotRequired[bool],
    },
)

ModifyVpnTunnelCertificateResultTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnTunnelOptionsRequestRequestTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "TunnelOptions": "ModifyVpnTunnelOptionsSpecificationTypeDef",
        "DryRun": NotRequired[bool],
    },
)

ModifyVpnTunnelOptionsResultTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": NotRequired[str],
        "TunnelInsideIpv6Cidr": NotRequired[str],
        "PreSharedKey": NotRequired[str],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2LifetimeSeconds": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "RekeyFuzzPercentage": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "DPDTimeoutSeconds": NotRequired[int],
        "DPDTimeoutAction": NotRequired[str],
        "Phase1EncryptionAlgorithms": NotRequired[
            Sequence["Phase1EncryptionAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase2EncryptionAlgorithms": NotRequired[
            Sequence["Phase2EncryptionAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase1IntegrityAlgorithms": NotRequired[
            Sequence["Phase1IntegrityAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase2IntegrityAlgorithms": NotRequired[
            Sequence["Phase2IntegrityAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase1DHGroupNumbers": NotRequired[
            Sequence["Phase1DHGroupNumbersRequestListValueTypeDef"]
        ],
        "Phase2DHGroupNumbers": NotRequired[
            Sequence["Phase2DHGroupNumbersRequestListValueTypeDef"]
        ],
        "IKEVersions": NotRequired[Sequence["IKEVersionsRequestListValueTypeDef"]],
        "StartupAction": NotRequired[str],
    },
)

MonitorInstancesRequestInstanceMonitorTypeDef = TypedDict(
    "MonitorInstancesRequestInstanceMonitorTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

MonitorInstancesRequestRequestTypeDef = TypedDict(
    "MonitorInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

MonitorInstancesResultTypeDef = TypedDict(
    "MonitorInstancesResultTypeDef",
    {
        "InstanceMonitorings": List["InstanceMonitoringTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringResponseMetadataTypeDef = TypedDict(
    "MonitoringResponseMetadataTypeDef",
    {
        "State": MonitoringStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringTypeDef = TypedDict(
    "MonitoringTypeDef",
    {
        "State": NotRequired[MonitoringStateType],
    },
)

MoveAddressToVpcRequestRequestTypeDef = TypedDict(
    "MoveAddressToVpcRequestRequestTypeDef",
    {
        "PublicIp": str,
        "DryRun": NotRequired[bool],
    },
)

MoveAddressToVpcResultTypeDef = TypedDict(
    "MoveAddressToVpcResultTypeDef",
    {
        "AllocationId": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MoveByoipCidrToIpamRequestRequestTypeDef = TypedDict(
    "MoveByoipCidrToIpamRequestRequestTypeDef",
    {
        "Cidr": str,
        "IpamPoolId": str,
        "IpamPoolOwner": str,
        "DryRun": NotRequired[bool],
    },
)

MoveByoipCidrToIpamResultTypeDef = TypedDict(
    "MoveByoipCidrToIpamResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MovingAddressStatusTypeDef = TypedDict(
    "MovingAddressStatusTypeDef",
    {
        "MoveStatus": NotRequired[MoveStatusType],
        "PublicIp": NotRequired[str],
    },
)

NatGatewayAddressTypeDef = TypedDict(
    "NatGatewayAddressTypeDef",
    {
        "AllocationId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIp": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)

NatGatewayTypeDef = TypedDict(
    "NatGatewayTypeDef",
    {
        "CreateTime": NotRequired[datetime],
        "DeleteTime": NotRequired[datetime],
        "FailureCode": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "NatGatewayAddresses": NotRequired[List["NatGatewayAddressTypeDef"]],
        "NatGatewayId": NotRequired[str],
        "ProvisionedBandwidth": NotRequired["ProvisionedBandwidthTypeDef"],
        "State": NotRequired[NatGatewayStateType],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "ConnectivityType": NotRequired[ConnectivityTypeType],
    },
)

NetworkAclAssociationTypeDef = TypedDict(
    "NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": NotRequired[str],
        "NetworkAclId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)

NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Egress": NotRequired[bool],
        "IcmpTypeCode": NotRequired["IcmpTypeCodeTypeDef"],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired["PortRangeTypeDef"],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[RuleActionType],
        "RuleNumber": NotRequired[int],
    },
)

NetworkAclTypeDef = TypedDict(
    "NetworkAclTypeDef",
    {
        "Associations": NotRequired[List["NetworkAclAssociationTypeDef"]],
        "Entries": NotRequired[List["NetworkAclEntryTypeDef"]],
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)

NetworkCardInfoTypeDef = TypedDict(
    "NetworkCardInfoTypeDef",
    {
        "NetworkCardIndex": NotRequired[int],
        "NetworkPerformance": NotRequired[str],
        "MaximumNetworkInterfaces": NotRequired[int],
    },
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "NetworkPerformance": NotRequired[str],
        "MaximumNetworkInterfaces": NotRequired[int],
        "MaximumNetworkCards": NotRequired[int],
        "DefaultNetworkCardIndex": NotRequired[int],
        "NetworkCards": NotRequired[List["NetworkCardInfoTypeDef"]],
        "Ipv4AddressesPerInterface": NotRequired[int],
        "Ipv6AddressesPerInterface": NotRequired[int],
        "Ipv6Supported": NotRequired[bool],
        "EnaSupport": NotRequired[EnaSupportType],
        "EfaSupported": NotRequired[bool],
        "EfaInfo": NotRequired["EfaInfoTypeDef"],
        "EncryptionInTransitSupported": NotRequired[bool],
    },
)

NetworkInsightsAccessScopeAnalysisTypeDef = TypedDict(
    "NetworkInsightsAccessScopeAnalysisTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": NotRequired[str],
        "NetworkInsightsAccessScopeAnalysisArn": NotRequired[str],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "Status": NotRequired[AnalysisStatusType],
        "StatusMessage": NotRequired[str],
        "WarningMessage": NotRequired[str],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "FindingsFound": NotRequired[FindingsFoundType],
        "AnalyzedEniCount": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

NetworkInsightsAccessScopeContentTypeDef = TypedDict(
    "NetworkInsightsAccessScopeContentTypeDef",
    {
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "MatchPaths": NotRequired[List["AccessScopePathTypeDef"]],
        "ExcludePaths": NotRequired[List["AccessScopePathTypeDef"]],
    },
)

NetworkInsightsAccessScopeTypeDef = TypedDict(
    "NetworkInsightsAccessScopeTypeDef",
    {
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "NetworkInsightsAccessScopeArn": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "UpdatedDate": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

NetworkInsightsAnalysisTypeDef = TypedDict(
    "NetworkInsightsAnalysisTypeDef",
    {
        "NetworkInsightsAnalysisId": NotRequired[str],
        "NetworkInsightsAnalysisArn": NotRequired[str],
        "NetworkInsightsPathId": NotRequired[str],
        "FilterInArns": NotRequired[List[str]],
        "StartDate": NotRequired[datetime],
        "Status": NotRequired[AnalysisStatusType],
        "StatusMessage": NotRequired[str],
        "WarningMessage": NotRequired[str],
        "NetworkPathFound": NotRequired[bool],
        "ForwardPathComponents": NotRequired[List["PathComponentTypeDef"]],
        "ReturnPathComponents": NotRequired[List["PathComponentTypeDef"]],
        "Explanations": NotRequired[List["ExplanationTypeDef"]],
        "AlternatePathHints": NotRequired[List["AlternatePathHintTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

NetworkInsightsPathTypeDef = TypedDict(
    "NetworkInsightsPathTypeDef",
    {
        "NetworkInsightsPathId": NotRequired[str],
        "NetworkInsightsPathArn": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "SourceIp": NotRequired[str],
        "DestinationIp": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "DestinationPort": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

NetworkInterfaceAssociationResponseMetadataTypeDef = TypedDict(
    "NetworkInterfaceAssociationResponseMetadataTypeDef",
    {
        "AllocationId": str,
        "AssociationId": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
        "CustomerOwnedIp": str,
        "CarrierIp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceAssociationTypeDef = TypedDict(
    "NetworkInterfaceAssociationTypeDef",
    {
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "IpOwnerId": NotRequired[str],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
        "CustomerOwnedIp": NotRequired[str],
        "CarrierIp": NotRequired[str],
    },
)

NetworkInterfaceAttachmentChangesTypeDef = TypedDict(
    "NetworkInterfaceAttachmentChangesTypeDef",
    {
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
    },
)

NetworkInterfaceAttachmentResponseMetadataTypeDef = TypedDict(
    "NetworkInterfaceAttachmentResponseMetadataTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "NetworkCardIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": AttachmentStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceAttachmentTypeDef = TypedDict(
    "NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "NetworkCardIndex": NotRequired[int],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "Status": NotRequired[AttachmentStatusType],
    },
)

NetworkInterfaceCountRequestTypeDef = TypedDict(
    "NetworkInterfaceCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

NetworkInterfaceCountTypeDef = TypedDict(
    "NetworkInterfaceCountTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

NetworkInterfaceIpv6AddressTypeDef = TypedDict(
    "NetworkInterfaceIpv6AddressTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)

NetworkInterfacePermissionStateTypeDef = TypedDict(
    "NetworkInterfacePermissionStateTypeDef",
    {
        "State": NotRequired[NetworkInterfacePermissionStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)

NetworkInterfacePermissionTypeDef = TypedDict(
    "NetworkInterfacePermissionTypeDef",
    {
        "NetworkInterfacePermissionId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "AwsAccountId": NotRequired[str],
        "AwsService": NotRequired[str],
        "Permission": NotRequired[InterfacePermissionTypeType],
        "PermissionState": NotRequired["NetworkInterfacePermissionStateTypeDef"],
    },
)

NetworkInterfacePrivateIpAddressTypeDef = TypedDict(
    "NetworkInterfacePrivateIpAddressTypeDef",
    {
        "Association": NotRequired["NetworkInterfaceAssociationTypeDef"],
        "Primary": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Association": NotRequired["NetworkInterfaceAssociationTypeDef"],
        "Attachment": NotRequired["NetworkInterfaceAttachmentTypeDef"],
        "AvailabilityZone": NotRequired[str],
        "Description": NotRequired[str],
        "Groups": NotRequired[List["GroupIdentifierTypeDef"]],
        "InterfaceType": NotRequired[NetworkInterfaceTypeType],
        "Ipv6Addresses": NotRequired[List["NetworkInterfaceIpv6AddressTypeDef"]],
        "MacAddress": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List["NetworkInterfacePrivateIpAddressTypeDef"]],
        "Ipv4Prefixes": NotRequired[List["Ipv4PrefixSpecificationTypeDef"]],
        "Ipv6Prefixes": NotRequired[List["Ipv6PrefixSpecificationTypeDef"]],
        "RequesterId": NotRequired[str],
        "RequesterManaged": NotRequired[bool],
        "SourceDestCheck": NotRequired[bool],
        "Status": NotRequired[NetworkInterfaceStatusType],
        "SubnetId": NotRequired[str],
        "TagSet": NotRequired[List["TagTypeDef"]],
        "VpcId": NotRequired[str],
        "DenyAllIgwTraffic": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "Ipv6Address": NotRequired[str],
    },
)

NewDhcpConfigurationTypeDef = TypedDict(
    "NewDhcpConfigurationTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

OnDemandOptionsRequestTypeDef = TypedDict(
    "OnDemandOptionsRequestTypeDef",
    {
        "AllocationStrategy": NotRequired[FleetOnDemandAllocationStrategyType],
        "CapacityReservationOptions": NotRequired["CapacityReservationOptionsRequestTypeDef"],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)

OnDemandOptionsTypeDef = TypedDict(
    "OnDemandOptionsTypeDef",
    {
        "AllocationStrategy": NotRequired[FleetOnDemandAllocationStrategyType],
        "CapacityReservationOptions": NotRequired["CapacityReservationOptionsTypeDef"],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)

PacketHeaderStatementRequestTypeDef = TypedDict(
    "PacketHeaderStatementRequestTypeDef",
    {
        "SourceAddresses": NotRequired[Sequence[str]],
        "DestinationAddresses": NotRequired[Sequence[str]],
        "SourcePorts": NotRequired[Sequence[str]],
        "DestinationPorts": NotRequired[Sequence[str]],
        "SourcePrefixLists": NotRequired[Sequence[str]],
        "DestinationPrefixLists": NotRequired[Sequence[str]],
        "Protocols": NotRequired[Sequence[ProtocolType]],
    },
)

PacketHeaderStatementTypeDef = TypedDict(
    "PacketHeaderStatementTypeDef",
    {
        "SourceAddresses": NotRequired[List[str]],
        "DestinationAddresses": NotRequired[List[str]],
        "SourcePorts": NotRequired[List[str]],
        "DestinationPorts": NotRequired[List[str]],
        "SourcePrefixLists": NotRequired[List[str]],
        "DestinationPrefixLists": NotRequired[List[str]],
        "Protocols": NotRequired[List[ProtocolType]],
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

PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "SequenceNumber": NotRequired[int],
        "AclRule": NotRequired["AnalysisAclRuleTypeDef"],
        "AttachedTo": NotRequired["AnalysisComponentTypeDef"],
        "Component": NotRequired["AnalysisComponentTypeDef"],
        "DestinationVpc": NotRequired["AnalysisComponentTypeDef"],
        "OutboundHeader": NotRequired["AnalysisPacketHeaderTypeDef"],
        "InboundHeader": NotRequired["AnalysisPacketHeaderTypeDef"],
        "RouteTableRoute": NotRequired["AnalysisRouteTableRouteTypeDef"],
        "SecurityGroupRule": NotRequired["AnalysisSecurityGroupRuleTypeDef"],
        "SourceVpc": NotRequired["AnalysisComponentTypeDef"],
        "Subnet": NotRequired["AnalysisComponentTypeDef"],
        "Vpc": NotRequired["AnalysisComponentTypeDef"],
    },
)

PathStatementRequestTypeDef = TypedDict(
    "PathStatementRequestTypeDef",
    {
        "PacketHeaderStatement": NotRequired["PacketHeaderStatementRequestTypeDef"],
        "ResourceStatement": NotRequired["ResourceStatementRequestTypeDef"],
    },
)

PathStatementTypeDef = TypedDict(
    "PathStatementTypeDef",
    {
        "PacketHeaderStatement": NotRequired["PacketHeaderStatementTypeDef"],
        "ResourceStatement": NotRequired["ResourceStatementTypeDef"],
    },
)

PciIdTypeDef = TypedDict(
    "PciIdTypeDef",
    {
        "DeviceId": NotRequired[str],
        "VendorId": NotRequired[str],
        "SubsystemId": NotRequired[str],
        "SubsystemVendorId": NotRequired[str],
    },
)

PeeringAttachmentStatusTypeDef = TypedDict(
    "PeeringAttachmentStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

PeeringConnectionOptionsRequestTypeDef = TypedDict(
    "PeeringConnectionOptionsRequestTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)

PeeringConnectionOptionsTypeDef = TypedDict(
    "PeeringConnectionOptionsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)

PeeringTgwInfoTypeDef = TypedDict(
    "PeeringTgwInfoTypeDef",
    {
        "TransitGatewayId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Region": NotRequired[str],
    },
)

Phase1DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)

Phase1DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)

Phase1EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase1EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase1IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase1IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase2DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)

Phase2DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)

Phase2EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase2EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase2IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

Phase2IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

PlacementGroupInfoTypeDef = TypedDict(
    "PlacementGroupInfoTypeDef",
    {
        "SupportedStrategies": NotRequired[List[PlacementGroupStrategyType]],
    },
)

PlacementGroupTypeDef = TypedDict(
    "PlacementGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "State": NotRequired[PlacementGroupStateType],
        "Strategy": NotRequired[PlacementStrategyType],
        "PartitionCount": NotRequired[int],
        "GroupId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "GroupArn": NotRequired[str],
    },
)

PlacementResponseMetadataTypeDef = TypedDict(
    "PlacementResponseMetadataTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "PartitionNumber": int,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PlacementResponseTypeDef = TypedDict(
    "PlacementResponseTypeDef",
    {
        "GroupName": NotRequired[str],
    },
)

PlacementTypeDef = TypedDict(
    "PlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Affinity": NotRequired[str],
        "GroupName": NotRequired[str],
        "PartitionNumber": NotRequired[int],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
        "SpreadDomain": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
    },
)

PoolCidrBlockTypeDef = TypedDict(
    "PoolCidrBlockTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
    },
)

PrefixListAssociationTypeDef = TypedDict(
    "PrefixListAssociationTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceOwner": NotRequired[str],
    },
)

PrefixListEntryTypeDef = TypedDict(
    "PrefixListEntryTypeDef",
    {
        "Cidr": NotRequired[str],
        "Description": NotRequired[str],
    },
)

PrefixListIdTypeDef = TypedDict(
    "PrefixListIdTypeDef",
    {
        "Description": NotRequired[str],
        "PrefixListId": NotRequired[str],
    },
)

PrefixListTypeDef = TypedDict(
    "PrefixListTypeDef",
    {
        "Cidrs": NotRequired[List[str]],
        "PrefixListId": NotRequired[str],
        "PrefixListName": NotRequired[str],
    },
)

PriceScheduleSpecificationTypeDef = TypedDict(
    "PriceScheduleSpecificationTypeDef",
    {
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Price": NotRequired[float],
        "Term": NotRequired[int],
    },
)

PriceScheduleTypeDef = TypedDict(
    "PriceScheduleTypeDef",
    {
        "Active": NotRequired[bool],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Price": NotRequired[float],
        "Term": NotRequired[int],
    },
)

PricingDetailTypeDef = TypedDict(
    "PricingDetailTypeDef",
    {
        "Count": NotRequired[int],
        "Price": NotRequired[float],
    },
)

PrincipalIdFormatTypeDef = TypedDict(
    "PrincipalIdFormatTypeDef",
    {
        "Arn": NotRequired[str],
        "Statuses": NotRequired[List["IdFormatTypeDef"]],
    },
)

PrivateDnsDetailsTypeDef = TypedDict(
    "PrivateDnsDetailsTypeDef",
    {
        "PrivateDnsName": NotRequired[str],
    },
)

PrivateDnsNameConfigurationTypeDef = TypedDict(
    "PrivateDnsNameConfigurationTypeDef",
    {
        "State": NotRequired[DnsNameStateType],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
        "Name": NotRequired[str],
    },
)

PrivateDnsNameOptionsOnLaunchResponseMetadataTypeDef = TypedDict(
    "PrivateDnsNameOptionsOnLaunchResponseMetadataTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrivateDnsNameOptionsOnLaunchTypeDef = TypedDict(
    "PrivateDnsNameOptionsOnLaunchTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)

PrivateDnsNameOptionsRequestTypeDef = TypedDict(
    "PrivateDnsNameOptionsRequestTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)

PrivateDnsNameOptionsResponseResponseMetadataTypeDef = TypedDict(
    "PrivateDnsNameOptionsResponseResponseMetadataTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrivateDnsNameOptionsResponseTypeDef = TypedDict(
    "PrivateDnsNameOptionsResponseTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)

PrivateIpAddressSpecificationTypeDef = TypedDict(
    "PrivateIpAddressSpecificationTypeDef",
    {
        "Primary": NotRequired[bool],
        "PrivateIpAddress": NotRequired[str],
    },
)

ProcessorInfoTypeDef = TypedDict(
    "ProcessorInfoTypeDef",
    {
        "SupportedArchitectures": NotRequired[List[ArchitectureTypeType]],
        "SustainedClockSpeedInGhz": NotRequired[float],
    },
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "ProductCodeId": NotRequired[str],
        "ProductCodeType": NotRequired[ProductCodeValuesType],
    },
)

PropagatingVgwTypeDef = TypedDict(
    "PropagatingVgwTypeDef",
    {
        "GatewayId": NotRequired[str],
    },
)

ProvisionByoipCidrRequestRequestTypeDef = TypedDict(
    "ProvisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CidrAuthorizationContext": NotRequired["CidrAuthorizationContextTypeDef"],
        "PubliclyAdvertisable": NotRequired[bool],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "PoolTagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "MultiRegion": NotRequired[bool],
    },
)

ProvisionByoipCidrResultTypeDef = TypedDict(
    "ProvisionByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "ProvisionIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cidr": NotRequired[str],
        "CidrAuthorizationContext": NotRequired["IpamCidrAuthorizationContextTypeDef"],
    },
)

ProvisionIpamPoolCidrResultTypeDef = TypedDict(
    "ProvisionIpamPoolCidrResultTypeDef",
    {
        "IpamPoolCidr": "IpamPoolCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "ProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "PoolId": str,
        "NetmaskLength": int,
        "DryRun": NotRequired[bool],
    },
)

ProvisionPublicIpv4PoolCidrResultTypeDef = TypedDict(
    "ProvisionPublicIpv4PoolCidrResultTypeDef",
    {
        "PoolId": str,
        "PoolAddressRange": "PublicIpv4PoolRangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedBandwidthTypeDef = TypedDict(
    "ProvisionedBandwidthTypeDef",
    {
        "ProvisionTime": NotRequired[datetime],
        "Provisioned": NotRequired[str],
        "RequestTime": NotRequired[datetime],
        "Requested": NotRequired[str],
        "Status": NotRequired[str],
    },
)

PtrUpdateStatusTypeDef = TypedDict(
    "PtrUpdateStatusTypeDef",
    {
        "Value": NotRequired[str],
        "Status": NotRequired[str],
        "Reason": NotRequired[str],
    },
)

PublicIpv4PoolRangeTypeDef = TypedDict(
    "PublicIpv4PoolRangeTypeDef",
    {
        "FirstAddress": NotRequired[str],
        "LastAddress": NotRequired[str],
        "AddressCount": NotRequired[int],
        "AvailableAddressCount": NotRequired[int],
    },
)

PublicIpv4PoolTypeDef = TypedDict(
    "PublicIpv4PoolTypeDef",
    {
        "PoolId": NotRequired[str],
        "Description": NotRequired[str],
        "PoolAddressRanges": NotRequired[List["PublicIpv4PoolRangeTypeDef"]],
        "TotalAddressCount": NotRequired[int],
        "TotalAvailableAddressCount": NotRequired[int],
        "NetworkBorderGroup": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

PurchaseHostReservationRequestRequestTypeDef = TypedDict(
    "PurchaseHostReservationRequestRequestTypeDef",
    {
        "HostIdSet": Sequence[str],
        "OfferingId": str,
        "ClientToken": NotRequired[str],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "LimitPrice": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

PurchaseHostReservationResultTypeDef = TypedDict(
    "PurchaseHostReservationResultTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseRequestTypeDef = TypedDict(
    "PurchaseRequestTypeDef",
    {
        "InstanceCount": int,
        "PurchaseToken": str,
    },
)

PurchaseReservedInstancesOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingRequestRequestTypeDef",
    {
        "InstanceCount": int,
        "ReservedInstancesOfferingId": str,
        "DryRun": NotRequired[bool],
        "LimitPrice": NotRequired["ReservedInstanceLimitPriceTypeDef"],
        "PurchaseTime": NotRequired[Union[datetime, str]],
    },
)

PurchaseReservedInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingResultTypeDef",
    {
        "ReservedInstancesId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseScheduledInstancesRequestRequestTypeDef = TypedDict(
    "PurchaseScheduledInstancesRequestRequestTypeDef",
    {
        "PurchaseRequests": Sequence["PurchaseRequestTypeDef"],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

PurchaseScheduledInstancesResultTypeDef = TypedDict(
    "PurchaseScheduledInstancesResultTypeDef",
    {
        "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseTypeDef = TypedDict(
    "PurchaseTypeDef",
    {
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Duration": NotRequired[int],
        "HostIdSet": NotRequired[List[str]],
        "HostReservationId": NotRequired[str],
        "HourlyPrice": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "PaymentOption": NotRequired[PaymentOptionType],
        "UpfrontPrice": NotRequired[str],
    },
)

RebootInstancesRequestInstanceRebootTypeDef = TypedDict(
    "RebootInstancesRequestInstanceRebootTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

RebootInstancesRequestRequestTypeDef = TypedDict(
    "RebootInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "Amount": NotRequired[float],
        "Frequency": NotRequired[Literal["Hourly"]],
    },
)

ReferencedSecurityGroupTypeDef = TypedDict(
    "ReferencedSecurityGroupTypeDef",
    {
        "GroupId": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "Endpoint": NotRequired[str],
        "RegionName": NotRequired[str],
        "OptInStatus": NotRequired[str],
    },
)

RegisterImageRequestRequestTypeDef = TypedDict(
    "RegisterImageRequestRequestTypeDef",
    {
        "Name": str,
        "ImageLocation": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EnaSupport": NotRequired[bool],
        "KernelId": NotRequired[str],
        "BillingProducts": NotRequired[Sequence[str]],
        "RamdiskId": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "SriovNetSupport": NotRequired[str],
        "VirtualizationType": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
    },
)

RegisterImageRequestServiceResourceRegisterImageTypeDef = TypedDict(
    "RegisterImageRequestServiceResourceRegisterImageTypeDef",
    {
        "Name": str,
        "ImageLocation": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EnaSupport": NotRequired[bool],
        "KernelId": NotRequired[str],
        "BillingProducts": NotRequired[Sequence[str]],
        "RamdiskId": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "SriovNetSupport": NotRequired[str],
        "VirtualizationType": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
    },
)

RegisterImageResultTypeDef = TypedDict(
    "RegisterImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceTagAttribute": NotRequired["RegisterInstanceTagAttributeRequestTypeDef"],
    },
)

RegisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "RegisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": NotRequired[bool],
        "InstanceTagKeys": NotRequired[Sequence[str]],
    },
)

RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "GroupIpAddress": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

RegisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {
        "RegisteredMulticastGroupMembers": "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "GroupIpAddress": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

RegisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {
        "RegisteredMulticastGroupSources": "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)

RejectTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

RejectTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)

RejectTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

RejectVpcEndpointConnectionsResultTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "RejectVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)

RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef = TypedDict(
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

RejectVpcPeeringConnectionResultTypeDef = TypedDict(
    "RejectVpcPeeringConnectionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReleaseAddressRequestClassicAddressReleaseTypeDef = TypedDict(
    "ReleaseAddressRequestClassicAddressReleaseTypeDef",
    {
        "AllocationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ReleaseAddressRequestRequestTypeDef = TypedDict(
    "ReleaseAddressRequestRequestTypeDef",
    {
        "AllocationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ReleaseAddressRequestVpcAddressReleaseTypeDef = TypedDict(
    "ReleaseAddressRequestVpcAddressReleaseTypeDef",
    {
        "AllocationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

ReleaseHostsRequestRequestTypeDef = TypedDict(
    "ReleaseHostsRequestRequestTypeDef",
    {
        "HostIds": Sequence[str],
    },
)

ReleaseHostsResultTypeDef = TypedDict(
    "ReleaseHostsResultTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReleaseIpamPoolAllocationRequestRequestTypeDef = TypedDict(
    "ReleaseIpamPoolAllocationRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "Cidr": str,
        "IpamPoolAllocationId": str,
        "DryRun": NotRequired[bool],
    },
)

ReleaseIpamPoolAllocationResultTypeDef = TypedDict(
    "ReleaseIpamPoolAllocationResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveIpamOperatingRegionTypeDef = TypedDict(
    "RemoveIpamOperatingRegionTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)

RemovePrefixListEntryTypeDef = TypedDict(
    "RemovePrefixListEntryTypeDef",
    {
        "Cidr": str,
    },
)

ReplaceIamInstanceProfileAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationRequestRequestTypeDef",
    {
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "AssociationId": str,
    },
)

ReplaceIamInstanceProfileAssociationResultTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef",
    {
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)

ReplaceNetworkAclAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "NetworkAclId": str,
        "DryRun": NotRequired[bool],
    },
)

ReplaceNetworkAclAssociationResultTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationResultTypeDef",
    {
        "NewAssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef = TypedDict(
    "ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired["IcmpTypeCodeTypeDef"],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired["PortRangeTypeDef"],
    },
)

ReplaceNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "ReplaceNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired["IcmpTypeCodeTypeDef"],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired["PortRangeTypeDef"],
    },
)

ReplaceRootVolumeTaskTypeDef = TypedDict(
    "ReplaceRootVolumeTaskTypeDef",
    {
        "ReplaceRootVolumeTaskId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "TaskState": NotRequired[ReplaceRootVolumeTaskStateType],
        "StartTime": NotRequired[str],
        "CompleteTime": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ReplaceRouteRequestRequestTypeDef = TypedDict(
    "ReplaceRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "LocalTarget": NotRequired[bool],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)

ReplaceRouteRequestRouteReplaceTypeDef = TypedDict(
    "ReplaceRouteRequestRouteReplaceTypeDef",
    {
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "LocalTarget": NotRequired[bool],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)

ReplaceRouteTableAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceRouteTableAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef = TypedDict(
    "ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef",
    {
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)

ReplaceRouteTableAssociationResultTypeDef = TypedDict(
    "ReplaceRouteTableAssociationResultTypeDef",
    {
        "NewAssociationId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplaceTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

ReplaceTransitGatewayRouteResultTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteResultTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportInstanceStatusRequestInstanceReportStatusTypeDef = TypedDict(
    "ReportInstanceStatusRequestInstanceReportStatusTypeDef",
    {
        "ReasonCodes": Sequence[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[Union[datetime, str]],
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

ReportInstanceStatusRequestRequestTypeDef = TypedDict(
    "ReportInstanceStatusRequestRequestTypeDef",
    {
        "Instances": Sequence[str],
        "ReasonCodes": Sequence[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[Union[datetime, str]],
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

RequestIpamResourceTagTypeDef = TypedDict(
    "RequestIpamResourceTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

RequestLaunchTemplateDataTypeDef = TypedDict(
    "RequestLaunchTemplateDataTypeDef",
    {
        "KernelId": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[
            "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef"
        ],
        "BlockDeviceMappings": NotRequired[
            Sequence["LaunchTemplateBlockDeviceMappingRequestTypeDef"]
        ],
        "NetworkInterfaces": NotRequired[
            Sequence["LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef"]
        ],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["LaunchTemplatesMonitoringRequestTypeDef"],
        "Placement": NotRequired["LaunchTemplatePlacementRequestTypeDef"],
        "RamDiskId": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "UserData": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence["LaunchTemplateTagSpecificationRequestTypeDef"]],
        "ElasticGpuSpecifications": NotRequired[Sequence["ElasticGpuSpecificationTypeDef"]],
        "ElasticInferenceAccelerators": NotRequired[
            Sequence["LaunchTemplateElasticInferenceAcceleratorTypeDef"]
        ],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "InstanceMarketOptions": NotRequired["LaunchTemplateInstanceMarketOptionsRequestTypeDef"],
        "CreditSpecification": NotRequired["CreditSpecificationRequestTypeDef"],
        "CpuOptions": NotRequired["LaunchTemplateCpuOptionsRequestTypeDef"],
        "CapacityReservationSpecification": NotRequired[
            "LaunchTemplateCapacityReservationSpecificationRequestTypeDef"
        ],
        "LicenseSpecifications": NotRequired[
            Sequence["LaunchTemplateLicenseConfigurationRequestTypeDef"]
        ],
        "HibernationOptions": NotRequired["LaunchTemplateHibernationOptionsRequestTypeDef"],
        "MetadataOptions": NotRequired["LaunchTemplateInstanceMetadataOptionsRequestTypeDef"],
        "EnclaveOptions": NotRequired["LaunchTemplateEnclaveOptionsRequestTypeDef"],
        "InstanceRequirements": NotRequired["InstanceRequirementsRequestTypeDef"],
        "PrivateDnsNameOptions": NotRequired["LaunchTemplatePrivateDnsNameOptionsRequestTypeDef"],
    },
)

RequestSpotFleetRequestRequestTypeDef = TypedDict(
    "RequestSpotFleetRequestRequestTypeDef",
    {
        "SpotFleetRequestConfig": "SpotFleetRequestConfigDataTypeDef",
        "DryRun": NotRequired[bool],
    },
)

RequestSpotFleetResponseTypeDef = TypedDict(
    "RequestSpotFleetResponseTypeDef",
    {
        "SpotFleetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestSpotInstancesRequestRequestTypeDef = TypedDict(
    "RequestSpotInstancesRequestRequestTypeDef",
    {
        "AvailabilityZoneGroup": NotRequired[str],
        "BlockDurationMinutes": NotRequired[int],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "InstanceCount": NotRequired[int],
        "LaunchGroup": NotRequired[str],
        "LaunchSpecification": NotRequired["RequestSpotLaunchSpecificationTypeDef"],
        "SpotPrice": NotRequired[str],
        "Type": NotRequired[SpotInstanceTypeType],
        "ValidFrom": NotRequired[Union[datetime, str]],
        "ValidUntil": NotRequired[Union[datetime, str]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)

RequestSpotInstancesResultTypeDef = TypedDict(
    "RequestSpotInstancesResultTypeDef",
    {
        "SpotInstanceRequests": List["SpotInstanceRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestSpotLaunchSpecificationTypeDef = TypedDict(
    "RequestSpotLaunchSpecificationTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "AddressingType": NotRequired[str],
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["IamInstanceProfileSpecificationTypeDef"],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["RunInstancesMonitoringEnabledTypeDef"],
        "NetworkInterfaces": NotRequired[Sequence["InstanceNetworkInterfaceSpecificationTypeDef"]],
        "Placement": NotRequired["SpotPlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
    },
)

ReservationFleetInstanceSpecificationTypeDef = TypedDict(
    "ReservationFleetInstanceSpecificationTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "InstancePlatform": NotRequired[CapacityReservationInstancePlatformType],
        "Weight": NotRequired[float],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "Priority": NotRequired[int],
    },
)

ReservationResponseMetadataTypeDef = TypedDict(
    "ReservationResponseMetadataTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "OwnerId": str,
        "RequesterId": str,
        "ReservationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Groups": NotRequired[List["GroupIdentifierTypeDef"]],
        "Instances": NotRequired[List["InstanceTypeDef"]],
        "OwnerId": NotRequired[str],
        "RequesterId": NotRequired[str],
        "ReservationId": NotRequired[str],
    },
)

ReservationValueTypeDef = TypedDict(
    "ReservationValueTypeDef",
    {
        "HourlyPrice": NotRequired[str],
        "RemainingTotalValue": NotRequired[str],
        "RemainingUpfrontValue": NotRequired[str],
    },
)

ReservedInstanceLimitPriceTypeDef = TypedDict(
    "ReservedInstanceLimitPriceTypeDef",
    {
        "Amount": NotRequired[float],
        "CurrencyCode": NotRequired[Literal["USD"]],
    },
)

ReservedInstanceReservationValueTypeDef = TypedDict(
    "ReservedInstanceReservationValueTypeDef",
    {
        "ReservationValue": NotRequired["ReservationValueTypeDef"],
        "ReservedInstanceId": NotRequired[str],
    },
)

ReservedInstancesConfigurationTypeDef = TypedDict(
    "ReservedInstancesConfigurationTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[InstanceTypeType],
        "Platform": NotRequired[str],
        "Scope": NotRequired[scopeType],
    },
)

ReservedInstancesIdTypeDef = TypedDict(
    "ReservedInstancesIdTypeDef",
    {
        "ReservedInstancesId": NotRequired[str],
    },
)

ReservedInstancesListingTypeDef = TypedDict(
    "ReservedInstancesListingTypeDef",
    {
        "ClientToken": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "InstanceCounts": NotRequired[List["InstanceCountTypeDef"]],
        "PriceSchedules": NotRequired[List["PriceScheduleTypeDef"]],
        "ReservedInstancesId": NotRequired[str],
        "ReservedInstancesListingId": NotRequired[str],
        "Status": NotRequired[ListingStatusType],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "UpdateDate": NotRequired[datetime],
    },
)

ReservedInstancesModificationResultTypeDef = TypedDict(
    "ReservedInstancesModificationResultTypeDef",
    {
        "ReservedInstancesId": NotRequired[str],
        "TargetConfiguration": NotRequired["ReservedInstancesConfigurationTypeDef"],
    },
)

ReservedInstancesModificationTypeDef = TypedDict(
    "ReservedInstancesModificationTypeDef",
    {
        "ClientToken": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "EffectiveDate": NotRequired[datetime],
        "ModificationResults": NotRequired[List["ReservedInstancesModificationResultTypeDef"]],
        "ReservedInstancesIds": NotRequired[List["ReservedInstancesIdTypeDef"]],
        "ReservedInstancesModificationId": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "UpdateDate": NotRequired[datetime],
    },
)

ReservedInstancesOfferingTypeDef = TypedDict(
    "ReservedInstancesOfferingTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "InstanceType": NotRequired[InstanceTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesOfferingId": NotRequired[str],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "InstanceTenancy": NotRequired[TenancyType],
        "Marketplace": NotRequired[bool],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "OfferingType": NotRequired[OfferingTypeValuesType],
        "PricingDetails": NotRequired[List["PricingDetailTypeDef"]],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
        "Scope": NotRequired[scopeType],
    },
)

ReservedInstancesTypeDef = TypedDict(
    "ReservedInstancesTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Duration": NotRequired[int],
        "End": NotRequired[datetime],
        "FixedPrice": NotRequired[float],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[InstanceTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesId": NotRequired[str],
        "Start": NotRequired[datetime],
        "State": NotRequired[ReservedInstanceStateType],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "InstanceTenancy": NotRequired[TenancyType],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "OfferingType": NotRequired[OfferingTypeValuesType],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
        "Scope": NotRequired[scopeType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ResetAddressAttributeRequestRequestTypeDef = TypedDict(
    "ResetAddressAttributeRequestRequestTypeDef",
    {
        "AllocationId": str,
        "Attribute": Literal["domain-name"],
        "DryRun": NotRequired[bool],
    },
)

ResetAddressAttributeResultTypeDef = TypedDict(
    "ResetAddressAttributeResultTypeDef",
    {
        "Address": "AddressAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

ResetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "ResetFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "DryRun": NotRequired[bool],
        "Attribute": NotRequired[Literal["loadPermission"]],
    },
)

ResetFpgaImageAttributeResultTypeDef = TypedDict(
    "ResetFpgaImageAttributeResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetImageAttributeRequestImageResetAttributeTypeDef = TypedDict(
    "ResetImageAttributeRequestImageResetAttributeTypeDef",
    {
        "Attribute": Literal["launchPermission"],
        "DryRun": NotRequired[bool],
    },
)

ResetImageAttributeRequestRequestTypeDef = TypedDict(
    "ResetImageAttributeRequestRequestTypeDef",
    {
        "Attribute": Literal["launchPermission"],
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)

ResetInstanceAttributeRequestInstanceResetAttributeTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetAttributeTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

ResetInstanceAttributeRequestInstanceResetKernelTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetKernelTypeDef",
    {
        "Attribute": NotRequired[InstanceAttributeNameType],
        "DryRun": NotRequired[bool],
    },
)

ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef",
    {
        "Attribute": NotRequired[InstanceAttributeNameType],
        "DryRun": NotRequired[bool],
    },
)

ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef",
    {
        "Attribute": NotRequired[InstanceAttributeNameType],
        "DryRun": NotRequired[bool],
    },
)

ResetInstanceAttributeRequestRequestTypeDef = TypedDict(
    "ResetInstanceAttributeRequestRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef = TypedDict(
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef",
    {
        "DryRun": NotRequired[bool],
        "SourceDestCheck": NotRequired[str],
    },
)

ResetNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "ResetNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "DryRun": NotRequired[bool],
        "SourceDestCheck": NotRequired[str],
    },
)

ResetSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "ResetSnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)

ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef = TypedDict(
    "ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)

ResourceStatementRequestTypeDef = TypedDict(
    "ResourceStatementRequestTypeDef",
    {
        "Resources": NotRequired[Sequence[str]],
        "ResourceTypes": NotRequired[Sequence[str]],
    },
)

ResourceStatementTypeDef = TypedDict(
    "ResourceStatementTypeDef",
    {
        "Resources": NotRequired[List[str]],
        "ResourceTypes": NotRequired[List[str]],
    },
)

ResponseErrorTypeDef = TypedDict(
    "ResponseErrorTypeDef",
    {
        "Code": NotRequired[LaunchTemplateErrorCodeType],
        "Message": NotRequired[str],
    },
)

ResponseLaunchTemplateDataTypeDef = TypedDict(
    "ResponseLaunchTemplateDataTypeDef",
    {
        "KernelId": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["LaunchTemplateIamInstanceProfileSpecificationTypeDef"],
        "BlockDeviceMappings": NotRequired[List["LaunchTemplateBlockDeviceMappingTypeDef"]],
        "NetworkInterfaces": NotRequired[
            List["LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef"]
        ],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["LaunchTemplatesMonitoringTypeDef"],
        "Placement": NotRequired["LaunchTemplatePlacementTypeDef"],
        "RamDiskId": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "UserData": NotRequired[str],
        "TagSpecifications": NotRequired[List["LaunchTemplateTagSpecificationTypeDef"]],
        "ElasticGpuSpecifications": NotRequired[List["ElasticGpuSpecificationResponseTypeDef"]],
        "ElasticInferenceAccelerators": NotRequired[
            List["LaunchTemplateElasticInferenceAcceleratorResponseTypeDef"]
        ],
        "SecurityGroupIds": NotRequired[List[str]],
        "SecurityGroups": NotRequired[List[str]],
        "InstanceMarketOptions": NotRequired["LaunchTemplateInstanceMarketOptionsTypeDef"],
        "CreditSpecification": NotRequired["CreditSpecificationTypeDef"],
        "CpuOptions": NotRequired["LaunchTemplateCpuOptionsTypeDef"],
        "CapacityReservationSpecification": NotRequired[
            "LaunchTemplateCapacityReservationSpecificationResponseTypeDef"
        ],
        "LicenseSpecifications": NotRequired[List["LaunchTemplateLicenseConfigurationTypeDef"]],
        "HibernationOptions": NotRequired["LaunchTemplateHibernationOptionsTypeDef"],
        "MetadataOptions": NotRequired["LaunchTemplateInstanceMetadataOptionsTypeDef"],
        "EnclaveOptions": NotRequired["LaunchTemplateEnclaveOptionsTypeDef"],
        "InstanceRequirements": NotRequired["InstanceRequirementsTypeDef"],
        "PrivateDnsNameOptions": NotRequired["LaunchTemplatePrivateDnsNameOptionsTypeDef"],
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

RestoreAddressToClassicRequestRequestTypeDef = TypedDict(
    "RestoreAddressToClassicRequestRequestTypeDef",
    {
        "PublicIp": str,
        "DryRun": NotRequired[bool],
    },
)

RestoreAddressToClassicResultTypeDef = TypedDict(
    "RestoreAddressToClassicResultTypeDef",
    {
        "PublicIp": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreImageFromRecycleBinRequestRequestTypeDef = TypedDict(
    "RestoreImageFromRecycleBinRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)

RestoreImageFromRecycleBinResultTypeDef = TypedDict(
    "RestoreImageFromRecycleBinResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreManagedPrefixListVersionRequestRequestTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "PreviousVersion": int,
        "CurrentVersion": int,
        "DryRun": NotRequired[bool],
    },
)

RestoreManagedPrefixListVersionResultTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreSnapshotFromRecycleBinRequestRequestTypeDef = TypedDict(
    "RestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)

RestoreSnapshotFromRecycleBinResultTypeDef = TypedDict(
    "RestoreSnapshotFromRecycleBinResultTypeDef",
    {
        "SnapshotId": str,
        "OutpostArn": str,
        "Description": str,
        "Encrypted": bool,
        "OwnerId": str,
        "Progress": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "VolumeId": str,
        "VolumeSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreSnapshotTierRequestRequestTypeDef = TypedDict(
    "RestoreSnapshotTierRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "TemporaryRestoreDays": NotRequired[int],
        "PermanentRestore": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

RestoreSnapshotTierResultTypeDef = TypedDict(
    "RestoreSnapshotTierResultTypeDef",
    {
        "SnapshotId": str,
        "RestoreStartTime": datetime,
        "RestoreDuration": int,
        "IsPermanentRestore": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "RevokeClientVpnIngressRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
        "AccessGroupId": NotRequired[str],
        "RevokeAllGroups": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)

RevokeClientVpnIngressResultTypeDef = TypedDict(
    "RevokeClientVpnIngressResultTypeDef",
    {
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "RevokeSecurityGroupEgressRequestRequestTypeDef",
    {
        "GroupId": str,
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)

RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef = TypedDict(
    "RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)

RevokeSecurityGroupEgressResultTypeDef = TypedDict(
    "RevokeSecurityGroupEgressResultTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List["IpPermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeSecurityGroupIngressRequestRequestTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestRequestTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
    },
)

RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
    },
)

RevokeSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeSecurityGroupIngressResultTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List["IpPermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RouteTableAssociationStateResponseMetadataTypeDef = TypedDict(
    "RouteTableAssociationStateResponseMetadataTypeDef",
    {
        "State": RouteTableAssociationStateCodeType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RouteTableAssociationStateTypeDef = TypedDict(
    "RouteTableAssociationStateTypeDef",
    {
        "State": NotRequired[RouteTableAssociationStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)

RouteTableAssociationTypeDef = TypedDict(
    "RouteTableAssociationTypeDef",
    {
        "Main": NotRequired[bool],
        "RouteTableAssociationId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "AssociationState": NotRequired["RouteTableAssociationStateTypeDef"],
    },
)

RouteTableTypeDef = TypedDict(
    "RouteTableTypeDef",
    {
        "Associations": NotRequired[List["RouteTableAssociationTypeDef"]],
        "PropagatingVgws": NotRequired[List["PropagatingVgwTypeDef"]],
        "RouteTableId": NotRequired[str],
        "Routes": NotRequired[List["RouteTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "Origin": NotRequired[RouteOriginType],
        "State": NotRequired[RouteStateType],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)

RunInstancesMonitoringEnabledTypeDef = TypedDict(
    "RunInstancesMonitoringEnabledTypeDef",
    {
        "Enabled": bool,
    },
)

RunInstancesRequestRequestTypeDef = TypedDict(
    "RunInstancesRequestRequestTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressTypeDef"]],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["RunInstancesMonitoringEnabledTypeDef"],
        "Placement": NotRequired["PlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["IamInstanceProfileSpecificationTypeDef"],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "NetworkInterfaces": NotRequired[Sequence["InstanceNetworkInterfaceSpecificationTypeDef"]],
        "PrivateIpAddress": NotRequired[str],
        "ElasticGpuSpecification": NotRequired[Sequence["ElasticGpuSpecificationTypeDef"]],
        "ElasticInferenceAccelerators": NotRequired[Sequence["ElasticInferenceAcceleratorTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "InstanceMarketOptions": NotRequired["InstanceMarketOptionsRequestTypeDef"],
        "CreditSpecification": NotRequired["CreditSpecificationRequestTypeDef"],
        "CpuOptions": NotRequired["CpuOptionsRequestTypeDef"],
        "CapacityReservationSpecification": NotRequired["CapacityReservationSpecificationTypeDef"],
        "HibernationOptions": NotRequired["HibernationOptionsRequestTypeDef"],
        "LicenseSpecifications": NotRequired[Sequence["LicenseConfigurationRequestTypeDef"]],
        "MetadataOptions": NotRequired["InstanceMetadataOptionsRequestTypeDef"],
        "EnclaveOptions": NotRequired["EnclaveOptionsRequestTypeDef"],
        "PrivateDnsNameOptions": NotRequired["PrivateDnsNameOptionsRequestTypeDef"],
    },
)

RunInstancesRequestServiceResourceCreateInstancesTypeDef = TypedDict(
    "RunInstancesRequestServiceResourceCreateInstancesTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressTypeDef"]],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["RunInstancesMonitoringEnabledTypeDef"],
        "Placement": NotRequired["PlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["IamInstanceProfileSpecificationTypeDef"],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "NetworkInterfaces": NotRequired[Sequence["InstanceNetworkInterfaceSpecificationTypeDef"]],
        "PrivateIpAddress": NotRequired[str],
        "ElasticGpuSpecification": NotRequired[Sequence["ElasticGpuSpecificationTypeDef"]],
        "ElasticInferenceAccelerators": NotRequired[Sequence["ElasticInferenceAcceleratorTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "InstanceMarketOptions": NotRequired["InstanceMarketOptionsRequestTypeDef"],
        "CreditSpecification": NotRequired["CreditSpecificationRequestTypeDef"],
        "CpuOptions": NotRequired["CpuOptionsRequestTypeDef"],
        "CapacityReservationSpecification": NotRequired["CapacityReservationSpecificationTypeDef"],
        "HibernationOptions": NotRequired["HibernationOptionsRequestTypeDef"],
        "LicenseSpecifications": NotRequired[Sequence["LicenseConfigurationRequestTypeDef"]],
        "MetadataOptions": NotRequired["InstanceMetadataOptionsRequestTypeDef"],
        "EnclaveOptions": NotRequired["EnclaveOptionsRequestTypeDef"],
        "PrivateDnsNameOptions": NotRequired["PrivateDnsNameOptionsRequestTypeDef"],
    },
)

RunInstancesRequestSubnetCreateInstancesTypeDef = TypedDict(
    "RunInstancesRequestSubnetCreateInstancesTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["InstanceIpv6AddressTypeDef"]],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["RunInstancesMonitoringEnabledTypeDef"],
        "Placement": NotRequired["PlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "UserData": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["IamInstanceProfileSpecificationTypeDef"],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "NetworkInterfaces": NotRequired[Sequence["InstanceNetworkInterfaceSpecificationTypeDef"]],
        "PrivateIpAddress": NotRequired[str],
        "ElasticGpuSpecification": NotRequired[Sequence["ElasticGpuSpecificationTypeDef"]],
        "ElasticInferenceAccelerators": NotRequired[Sequence["ElasticInferenceAcceleratorTypeDef"]],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "InstanceMarketOptions": NotRequired["InstanceMarketOptionsRequestTypeDef"],
        "CreditSpecification": NotRequired["CreditSpecificationRequestTypeDef"],
        "CpuOptions": NotRequired["CpuOptionsRequestTypeDef"],
        "CapacityReservationSpecification": NotRequired["CapacityReservationSpecificationTypeDef"],
        "HibernationOptions": NotRequired["HibernationOptionsRequestTypeDef"],
        "LicenseSpecifications": NotRequired[Sequence["LicenseConfigurationRequestTypeDef"]],
        "MetadataOptions": NotRequired["InstanceMetadataOptionsRequestTypeDef"],
        "EnclaveOptions": NotRequired["EnclaveOptionsRequestTypeDef"],
        "PrivateDnsNameOptions": NotRequired["PrivateDnsNameOptionsRequestTypeDef"],
    },
)

RunScheduledInstancesRequestRequestTypeDef = TypedDict(
    "RunScheduledInstancesRequestRequestTypeDef",
    {
        "LaunchSpecification": "ScheduledInstancesLaunchSpecificationTypeDef",
        "ScheduledInstanceId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "InstanceCount": NotRequired[int],
    },
)

RunScheduledInstancesResultTypeDef = TypedDict(
    "RunScheduledInstancesResultTypeDef",
    {
        "InstanceIdSet": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ObjectTagTypeDef = TypedDict(
    "S3ObjectTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

S3StorageTypeDef = TypedDict(
    "S3StorageTypeDef",
    {
        "AWSAccessKeyId": NotRequired[str],
        "Bucket": NotRequired[str],
        "Prefix": NotRequired[str],
        "UploadPolicy": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "UploadPolicySignature": NotRequired[str],
    },
)

ScheduledInstanceAvailabilityTypeDef = TypedDict(
    "ScheduledInstanceAvailabilityTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailableInstanceCount": NotRequired[int],
        "FirstSlotStartTime": NotRequired[datetime],
        "HourlyPrice": NotRequired[str],
        "InstanceType": NotRequired[str],
        "MaxTermDurationInDays": NotRequired[int],
        "MinTermDurationInDays": NotRequired[int],
        "NetworkPlatform": NotRequired[str],
        "Platform": NotRequired[str],
        "PurchaseToken": NotRequired[str],
        "Recurrence": NotRequired["ScheduledInstanceRecurrenceTypeDef"],
        "SlotDurationInHours": NotRequired[int],
        "TotalScheduledInstanceHours": NotRequired[int],
    },
)

ScheduledInstanceRecurrenceRequestTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceRequestTypeDef",
    {
        "Frequency": NotRequired[str],
        "Interval": NotRequired[int],
        "OccurrenceDays": NotRequired[Sequence[int]],
        "OccurrenceRelativeToEnd": NotRequired[bool],
        "OccurrenceUnit": NotRequired[str],
    },
)

ScheduledInstanceRecurrenceTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceTypeDef",
    {
        "Frequency": NotRequired[str],
        "Interval": NotRequired[int],
        "OccurrenceDaySet": NotRequired[List[int]],
        "OccurrenceRelativeToEnd": NotRequired[bool],
        "OccurrenceUnit": NotRequired[str],
    },
)

ScheduledInstanceTypeDef = TypedDict(
    "ScheduledInstanceTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "HourlyPrice": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "NetworkPlatform": NotRequired[str],
        "NextSlotStartTime": NotRequired[datetime],
        "Platform": NotRequired[str],
        "PreviousSlotEndTime": NotRequired[datetime],
        "Recurrence": NotRequired["ScheduledInstanceRecurrenceTypeDef"],
        "ScheduledInstanceId": NotRequired[str],
        "SlotDurationInHours": NotRequired[int],
        "TermEndDate": NotRequired[datetime],
        "TermStartDate": NotRequired[datetime],
        "TotalScheduledInstanceHours": NotRequired[int],
    },
)

ScheduledInstancesBlockDeviceMappingTypeDef = TypedDict(
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired["ScheduledInstancesEbsTypeDef"],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
    },
)

ScheduledInstancesEbsTypeDef = TypedDict(
    "ScheduledInstancesEbsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)

ScheduledInstancesIamInstanceProfileTypeDef = TypedDict(
    "ScheduledInstancesIamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ScheduledInstancesIpv6AddressTypeDef = TypedDict(
    "ScheduledInstancesIpv6AddressTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)

ScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "ScheduledInstancesLaunchSpecificationTypeDef",
    {
        "ImageId": str,
        "BlockDeviceMappings": NotRequired[Sequence["ScheduledInstancesBlockDeviceMappingTypeDef"]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["ScheduledInstancesIamInstanceProfileTypeDef"],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["ScheduledInstancesMonitoringTypeDef"],
        "NetworkInterfaces": NotRequired[Sequence["ScheduledInstancesNetworkInterfaceTypeDef"]],
        "Placement": NotRequired["ScheduledInstancesPlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
    },
)

ScheduledInstancesMonitoringTypeDef = TypedDict(
    "ScheduledInstancesMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

ScheduledInstancesNetworkInterfaceTypeDef = TypedDict(
    "ScheduledInstancesNetworkInterfaceTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence["ScheduledInstancesIpv6AddressTypeDef"]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddressConfigs": NotRequired[
            Sequence["ScheduledInstancesPrivateIpAddressConfigTypeDef"]
        ],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
    },
)

ScheduledInstancesPlacementTypeDef = TypedDict(
    "ScheduledInstancesPlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)

ScheduledInstancesPrivateIpAddressConfigTypeDef = TypedDict(
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    {
        "Primary": NotRequired[bool],
        "PrivateIpAddress": NotRequired[str],
    },
)

SearchLocalGatewayRoutesRequestRequestTypeDef = TypedDict(
    "SearchLocalGatewayRoutesRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

SearchLocalGatewayRoutesResultTypeDef = TypedDict(
    "SearchLocalGatewayRoutesResultTypeDef",
    {
        "Routes": List["LocalGatewayRouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchTransitGatewayMulticastGroupsRequestRequestTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

SearchTransitGatewayMulticastGroupsResultTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    {
        "MulticastGroups": List["TransitGatewayMulticastGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "SearchTransitGatewayRoutesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": Sequence["FilterTypeDef"],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)

SearchTransitGatewayRoutesResultTypeDef = TypedDict(
    "SearchTransitGatewayRoutesResultTypeDef",
    {
        "Routes": List["TransitGatewayRouteTypeDef"],
        "AdditionalRoutesAvailable": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)

SecurityGroupReferenceTypeDef = TypedDict(
    "SecurityGroupReferenceTypeDef",
    {
        "GroupId": NotRequired[str],
        "ReferencingVpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "SecurityGroupRuleId": NotRequired[str],
        "Description": NotRequired[str],
    },
)

SecurityGroupRuleRequestTypeDef = TypedDict(
    "SecurityGroupRuleRequestTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "CidrIpv4": NotRequired[str],
        "CidrIpv6": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "ReferencedGroupId": NotRequired[str],
        "Description": NotRequired[str],
    },
)

SecurityGroupRuleTypeDef = TypedDict(
    "SecurityGroupRuleTypeDef",
    {
        "SecurityGroupRuleId": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupOwnerId": NotRequired[str],
        "IsEgress": NotRequired[bool],
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "CidrIpv4": NotRequired[str],
        "CidrIpv6": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "ReferencedGroupInfo": NotRequired["ReferencedSecurityGroupTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

SecurityGroupRuleUpdateTypeDef = TypedDict(
    "SecurityGroupRuleUpdateTypeDef",
    {
        "SecurityGroupRuleId": NotRequired[str],
        "SecurityGroupRule": NotRequired["SecurityGroupRuleRequestTypeDef"],
    },
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "Description": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[List["IpPermissionTypeDef"]],
        "OwnerId": NotRequired[str],
        "GroupId": NotRequired[str],
        "IpPermissionsEgress": NotRequired[List["IpPermissionTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

SendDiagnosticInterruptRequestRequestTypeDef = TypedDict(
    "SendDiagnosticInterruptRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)

ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "ServiceType": NotRequired[List["ServiceTypeDetailTypeDef"]],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[ServiceStateType],
        "AvailabilityZones": NotRequired[List[str]],
        "AcceptanceRequired": NotRequired[bool],
        "ManagesVpcEndpoints": NotRequired[bool],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "PrivateDnsNameConfiguration": NotRequired["PrivateDnsNameConfigurationTypeDef"],
        "PayerResponsibility": NotRequired[Literal["ServiceOwner"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ServiceDetailTypeDef = TypedDict(
    "ServiceDetailTypeDef",
    {
        "ServiceName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceType": NotRequired[List["ServiceTypeDetailTypeDef"]],
        "AvailabilityZones": NotRequired[List[str]],
        "Owner": NotRequired[str],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "PrivateDnsNames": NotRequired[List["PrivateDnsDetailsTypeDef"]],
        "VpcEndpointPolicySupported": NotRequired[bool],
        "AcceptanceRequired": NotRequired[bool],
        "ManagesVpcEndpoints": NotRequired[bool],
        "PayerResponsibility": NotRequired[Literal["ServiceOwner"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "PrivateDnsNameVerificationState": NotRequired[DnsNameStateType],
    },
)

ServiceResourceClassicAddressRequestTypeDef = TypedDict(
    "ServiceResourceClassicAddressRequestTypeDef",
    {
        "public_ip": str,
    },
)

ServiceResourceDhcpOptionsRequestTypeDef = TypedDict(
    "ServiceResourceDhcpOptionsRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceImageRequestTypeDef = TypedDict(
    "ServiceResourceImageRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceInstanceRequestTypeDef = TypedDict(
    "ServiceResourceInstanceRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceInternetGatewayRequestTypeDef = TypedDict(
    "ServiceResourceInternetGatewayRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceKeyPairRequestTypeDef = TypedDict(
    "ServiceResourceKeyPairRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceNetworkAclRequestTypeDef = TypedDict(
    "ServiceResourceNetworkAclRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceNetworkInterfaceAssociationRequestTypeDef = TypedDict(
    "ServiceResourceNetworkInterfaceAssociationRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceNetworkInterfaceRequestTypeDef = TypedDict(
    "ServiceResourceNetworkInterfaceRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourcePlacementGroupRequestTypeDef = TypedDict(
    "ServiceResourcePlacementGroupRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceRouteRequestTypeDef = TypedDict(
    "ServiceResourceRouteRequestTypeDef",
    {
        "route_table_id": str,
        "destination_cidr_block": str,
    },
)

ServiceResourceRouteTableAssociationRequestTypeDef = TypedDict(
    "ServiceResourceRouteTableAssociationRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceRouteTableRequestTypeDef = TypedDict(
    "ServiceResourceRouteTableRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSecurityGroupRequestTypeDef = TypedDict(
    "ServiceResourceSecurityGroupRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSnapshotRequestTypeDef = TypedDict(
    "ServiceResourceSnapshotRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSubnetRequestTypeDef = TypedDict(
    "ServiceResourceSubnetRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceTagRequestTypeDef = TypedDict(
    "ServiceResourceTagRequestTypeDef",
    {
        "resource_id": str,
        "key": str,
        "value": str,
    },
)

ServiceResourceVolumeRequestTypeDef = TypedDict(
    "ServiceResourceVolumeRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceVpcAddressRequestTypeDef = TypedDict(
    "ServiceResourceVpcAddressRequestTypeDef",
    {
        "allocation_id": str,
    },
)

ServiceResourceVpcPeeringConnectionRequestTypeDef = TypedDict(
    "ServiceResourceVpcPeeringConnectionRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceVpcRequestTypeDef = TypedDict(
    "ServiceResourceVpcRequestTypeDef",
    {
        "id": str,
    },
)

ServiceTypeDetailTypeDef = TypedDict(
    "ServiceTypeDetailTypeDef",
    {
        "ServiceType": NotRequired[ServiceTypeType],
    },
)

SlotDateTimeRangeRequestTypeDef = TypedDict(
    "SlotDateTimeRangeRequestTypeDef",
    {
        "EarliestTime": Union[datetime, str],
        "LatestTime": Union[datetime, str],
    },
)

SlotStartTimeRangeRequestTypeDef = TypedDict(
    "SlotStartTimeRangeRequestTypeDef",
    {
        "EarliestTime": NotRequired[Union[datetime, str]],
        "LatestTime": NotRequired[Union[datetime, str]],
    },
)

SnapshotDetailTypeDef = TypedDict(
    "SnapshotDetailTypeDef",
    {
        "Description": NotRequired[str],
        "DeviceName": NotRequired[str],
        "DiskImageSize": NotRequired[float],
        "Format": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired["UserBucketDetailsTypeDef"],
    },
)

SnapshotDiskContainerTypeDef = TypedDict(
    "SnapshotDiskContainerTypeDef",
    {
        "Description": NotRequired[str],
        "Format": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired["UserBucketTypeDef"],
    },
)

SnapshotInfoTypeDef = TypedDict(
    "SnapshotInfoTypeDef",
    {
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Encrypted": NotRequired[bool],
        "VolumeId": NotRequired[str],
        "State": NotRequired[SnapshotStateType],
        "VolumeSize": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "Progress": NotRequired[str],
        "OwnerId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "OutpostArn": NotRequired[str],
    },
)

SnapshotRecycleBinInfoTypeDef = TypedDict(
    "SnapshotRecycleBinInfoTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "RecycleBinEnterTime": NotRequired[datetime],
        "RecycleBinExitTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "VolumeId": NotRequired[str],
    },
)

SnapshotResponseMetadataTypeDef = TypedDict(
    "SnapshotResponseMetadataTypeDef",
    {
        "DataEncryptionKeyId": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OwnerId": str,
        "Progress": str,
        "SnapshotId": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "StateMessage": str,
        "VolumeId": str,
        "VolumeSize": int,
        "OwnerAlias": str,
        "OutpostArn": str,
        "Tags": List["TagTypeDef"],
        "StorageTier": StorageTierType,
        "RestoreExpiryTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotTaskDetailTypeDef = TypedDict(
    "SnapshotTaskDetailTypeDef",
    {
        "Description": NotRequired[str],
        "DiskImageSize": NotRequired[float],
        "Encrypted": NotRequired[bool],
        "Format": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired["UserBucketDetailsTypeDef"],
    },
)

SnapshotTierStatusTypeDef = TypedDict(
    "SnapshotTierStatusTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "VolumeId": NotRequired[str],
        "Status": NotRequired[SnapshotStateType],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "StorageTier": NotRequired[StorageTierType],
        "LastTieringStartTime": NotRequired[datetime],
        "LastTieringProgress": NotRequired[int],
        "LastTieringOperationStatus": NotRequired[TieringOperationStatusType],
        "LastTieringOperationStatusDetail": NotRequired[str],
        "ArchivalCompleteTime": NotRequired[datetime],
        "RestoreExpiryTime": NotRequired[datetime],
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DataEncryptionKeyId": NotRequired[str],
        "Description": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "State": NotRequired[SnapshotStateType],
        "StateMessage": NotRequired[str],
        "VolumeId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "OwnerAlias": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "StorageTier": NotRequired[StorageTierType],
        "RestoreExpiryTime": NotRequired[datetime],
    },
)

SpotCapacityRebalanceTypeDef = TypedDict(
    "SpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": NotRequired[ReplacementStrategyType],
        "TerminationDelay": NotRequired[int],
    },
)

SpotDatafeedSubscriptionTypeDef = TypedDict(
    "SpotDatafeedSubscriptionTypeDef",
    {
        "Bucket": NotRequired[str],
        "Fault": NotRequired["SpotInstanceStateFaultTypeDef"],
        "OwnerId": NotRequired[str],
        "Prefix": NotRequired[str],
        "State": NotRequired[DatafeedSubscriptionStateType],
    },
)

SpotFleetLaunchSpecificationTypeDef = TypedDict(
    "SpotFleetLaunchSpecificationTypeDef",
    {
        "SecurityGroups": NotRequired[List["GroupIdentifierTypeDef"]],
        "AddressingType": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List["BlockDeviceMappingTypeDef"]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired["IamInstanceProfileSpecificationTypeDef"],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired["SpotFleetMonitoringTypeDef"],
        "NetworkInterfaces": NotRequired[List["InstanceNetworkInterfaceSpecificationTypeDef"]],
        "Placement": NotRequired["SpotPlacementTypeDef"],
        "RamdiskId": NotRequired[str],
        "SpotPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "TagSpecifications": NotRequired[List["SpotFleetTagSpecificationTypeDef"]],
        "InstanceRequirements": NotRequired["InstanceRequirementsTypeDef"],
    },
)

SpotFleetMonitoringTypeDef = TypedDict(
    "SpotFleetMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

SpotFleetRequestConfigDataTypeDef = TypedDict(
    "SpotFleetRequestConfigDataTypeDef",
    {
        "IamFleetRole": str,
        "TargetCapacity": int,
        "AllocationStrategy": NotRequired[AllocationStrategyType],
        "OnDemandAllocationStrategy": NotRequired[OnDemandAllocationStrategyType],
        "SpotMaintenanceStrategies": NotRequired["SpotMaintenanceStrategiesTypeDef"],
        "ClientToken": NotRequired[str],
        "ExcessCapacityTerminationPolicy": NotRequired[ExcessCapacityTerminationPolicyType],
        "FulfilledCapacity": NotRequired[float],
        "OnDemandFulfilledCapacity": NotRequired[float],
        "LaunchSpecifications": NotRequired[List["SpotFleetLaunchSpecificationTypeDef"]],
        "LaunchTemplateConfigs": NotRequired[List["LaunchTemplateConfigTypeDef"]],
        "SpotPrice": NotRequired[str],
        "OnDemandTargetCapacity": NotRequired[int],
        "OnDemandMaxTotalPrice": NotRequired[str],
        "SpotMaxTotalPrice": NotRequired[str],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
        "LoadBalancersConfig": NotRequired["LoadBalancersConfigTypeDef"],
        "InstancePoolsToUseCount": NotRequired[int],
        "Context": NotRequired[str],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
        "TagSpecifications": NotRequired[List["TagSpecificationTypeDef"]],
    },
)

SpotFleetRequestConfigTypeDef = TypedDict(
    "SpotFleetRequestConfigTypeDef",
    {
        "ActivityStatus": NotRequired[ActivityStatusType],
        "CreateTime": NotRequired[datetime],
        "SpotFleetRequestConfig": NotRequired["SpotFleetRequestConfigDataTypeDef"],
        "SpotFleetRequestId": NotRequired[str],
        "SpotFleetRequestState": NotRequired[BatchStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

SpotFleetTagSpecificationTypeDef = TypedDict(
    "SpotFleetTagSpecificationTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

SpotInstanceRequestTypeDef = TypedDict(
    "SpotInstanceRequestTypeDef",
    {
        "ActualBlockHourlyPrice": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
        "BlockDurationMinutes": NotRequired[int],
        "CreateTime": NotRequired[datetime],
        "Fault": NotRequired["SpotInstanceStateFaultTypeDef"],
        "InstanceId": NotRequired[str],
        "LaunchGroup": NotRequired[str],
        "LaunchSpecification": NotRequired["LaunchSpecificationTypeDef"],
        "LaunchedAvailabilityZone": NotRequired[str],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "SpotInstanceRequestId": NotRequired[str],
        "SpotPrice": NotRequired[str],
        "State": NotRequired[SpotInstanceStateType],
        "Status": NotRequired["SpotInstanceStatusTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Type": NotRequired[SpotInstanceTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)

SpotInstanceStateFaultTypeDef = TypedDict(
    "SpotInstanceStateFaultTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

SpotInstanceStatusTypeDef = TypedDict(
    "SpotInstanceStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
        "UpdateTime": NotRequired[datetime],
    },
)

SpotMaintenanceStrategiesTypeDef = TypedDict(
    "SpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": NotRequired["SpotCapacityRebalanceTypeDef"],
    },
)

SpotMarketOptionsTypeDef = TypedDict(
    "SpotMarketOptionsTypeDef",
    {
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[SpotInstanceTypeType],
        "BlockDurationMinutes": NotRequired[int],
        "ValidUntil": NotRequired[Union[datetime, str]],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)

SpotOptionsRequestTypeDef = TypedDict(
    "SpotOptionsRequestTypeDef",
    {
        "AllocationStrategy": NotRequired[SpotAllocationStrategyType],
        "MaintenanceStrategies": NotRequired["FleetSpotMaintenanceStrategiesRequestTypeDef"],
        "InstanceInterruptionBehavior": NotRequired[SpotInstanceInterruptionBehaviorType],
        "InstancePoolsToUseCount": NotRequired[int],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)

SpotOptionsTypeDef = TypedDict(
    "SpotOptionsTypeDef",
    {
        "AllocationStrategy": NotRequired[SpotAllocationStrategyType],
        "MaintenanceStrategies": NotRequired["FleetSpotMaintenanceStrategiesTypeDef"],
        "InstanceInterruptionBehavior": NotRequired[SpotInstanceInterruptionBehaviorType],
        "InstancePoolsToUseCount": NotRequired[int],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)

SpotPlacementScoreTypeDef = TypedDict(
    "SpotPlacementScoreTypeDef",
    {
        "Region": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Score": NotRequired[int],
    },
)

SpotPlacementTypeDef = TypedDict(
    "SpotPlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "GroupName": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
    },
)

SpotPriceTypeDef = TypedDict(
    "SpotPriceTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "SpotPrice": NotRequired[str],
        "Timestamp": NotRequired[datetime],
    },
)

StaleIpPermissionTypeDef = TypedDict(
    "StaleIpPermissionTypeDef",
    {
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "IpRanges": NotRequired[List[str]],
        "PrefixListIds": NotRequired[List[str]],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[List["UserIdGroupPairTypeDef"]],
    },
)

StaleSecurityGroupTypeDef = TypedDict(
    "StaleSecurityGroupTypeDef",
    {
        "Description": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "StaleIpPermissions": NotRequired[List["StaleIpPermissionTypeDef"]],
        "StaleIpPermissionsEgress": NotRequired[List["StaleIpPermissionTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

StartInstancesRequestInstanceStartTypeDef = TypedDict(
    "StartInstancesRequestInstanceStartTypeDef",
    {
        "AdditionalInfo": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

StartInstancesRequestRequestTypeDef = TypedDict(
    "StartInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "AdditionalInfo": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

StartInstancesResultTypeDef = TypedDict(
    "StartInstancesResultTypeDef",
    {
        "StartingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "ClientToken": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

StartNetworkInsightsAccessScopeAnalysisResultTypeDef = TypedDict(
    "StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysis": "NetworkInsightsAccessScopeAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "StartNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ClientToken": str,
        "FilterInArns": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence["TagSpecificationTypeDef"]],
    },
)

StartNetworkInsightsAnalysisResultTypeDef = TypedDict(
    "StartNetworkInsightsAnalysisResultTypeDef",
    {
        "NetworkInsightsAnalysis": "NetworkInsightsAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
    },
)

StartVpcEndpointServicePrivateDnsVerificationResultTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StateReasonResponseMetadataTypeDef = TypedDict(
    "StateReasonResponseMetadataTypeDef",
    {
        "Code": str,
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StateReasonTypeDef = TypedDict(
    "StateReasonTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

StopInstancesRequestInstanceStopTypeDef = TypedDict(
    "StopInstancesRequestInstanceStopTypeDef",
    {
        "Hibernate": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)

StopInstancesRequestRequestTypeDef = TypedDict(
    "StopInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "Hibernate": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)

StopInstancesResultTypeDef = TypedDict(
    "StopInstancesResultTypeDef",
    {
        "StoppingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)

StorageTypeDef = TypedDict(
    "StorageTypeDef",
    {
        "S3": NotRequired["S3StorageTypeDef"],
    },
)

StoreImageTaskResultTypeDef = TypedDict(
    "StoreImageTaskResultTypeDef",
    {
        "AmiId": NotRequired[str],
        "TaskStartTime": NotRequired[datetime],
        "Bucket": NotRequired[str],
        "S3objectKey": NotRequired[str],
        "ProgressPercentage": NotRequired[int],
        "StoreTaskState": NotRequired[str],
        "StoreTaskFailureReason": NotRequired[str],
    },
)

SubnetAssociationTypeDef = TypedDict(
    "SubnetAssociationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "State": NotRequired[TransitGatewayMulitcastDomainAssociationStateType],
    },
)

SubnetCidrBlockStateTypeDef = TypedDict(
    "SubnetCidrBlockStateTypeDef",
    {
        "State": NotRequired[SubnetCidrBlockStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)

SubnetCidrReservationTypeDef = TypedDict(
    "SubnetCidrReservationTypeDef",
    {
        "SubnetCidrReservationId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Cidr": NotRequired[str],
        "ReservationType": NotRequired[SubnetCidrReservationTypeType],
        "OwnerId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

SubnetIpv6CidrBlockAssociationTypeDef = TypedDict(
    "SubnetIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv6CidrBlockState": NotRequired["SubnetCidrBlockStateTypeDef"],
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "EnableLniAtDeviceIndex": NotRequired[int],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "MapCustomerOwnedIpOnLaunch": NotRequired[bool],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "State": NotRequired[SubnetStateType],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "Ipv6CidrBlockAssociationSet": NotRequired[List["SubnetIpv6CidrBlockAssociationTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "SubnetArn": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "EnableDns64": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "PrivateDnsNameOptionsOnLaunch": NotRequired["PrivateDnsNameOptionsOnLaunchTypeDef"],
    },
)

SuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": NotRequired[str],
    },
)

SuccessfulQueuedPurchaseDeletionTypeDef = TypedDict(
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    {
        "ReservedInstancesId": NotRequired[str],
    },
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "Key": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "Value": NotRequired[str],
    },
)

TagSpecificationTypeDef = TypedDict(
    "TagSpecificationTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

TargetCapacitySpecificationRequestTypeDef = TypedDict(
    "TargetCapacitySpecificationRequestTypeDef",
    {
        "TotalTargetCapacity": int,
        "OnDemandTargetCapacity": NotRequired[int],
        "SpotTargetCapacity": NotRequired[int],
        "DefaultTargetCapacityType": NotRequired[DefaultTargetCapacityTypeType],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
    },
)

TargetCapacitySpecificationTypeDef = TypedDict(
    "TargetCapacitySpecificationTypeDef",
    {
        "TotalTargetCapacity": NotRequired[int],
        "OnDemandTargetCapacity": NotRequired[int],
        "SpotTargetCapacity": NotRequired[int],
        "DefaultTargetCapacityType": NotRequired[DefaultTargetCapacityTypeType],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
    },
)

TargetConfigurationRequestTypeDef = TypedDict(
    "TargetConfigurationRequestTypeDef",
    {
        "OfferingId": str,
        "InstanceCount": NotRequired[int],
    },
)

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "OfferingId": NotRequired[str],
    },
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

TargetGroupsConfigTypeDef = TypedDict(
    "TargetGroupsConfigTypeDef",
    {
        "TargetGroups": NotRequired[List["TargetGroupTypeDef"]],
    },
)

TargetNetworkTypeDef = TypedDict(
    "TargetNetworkTypeDef",
    {
        "AssociationId": NotRequired[str],
        "VpcId": NotRequired[str],
        "TargetNetworkId": NotRequired[str],
        "ClientVpnEndpointId": NotRequired[str],
        "Status": NotRequired["AssociationStatusTypeDef"],
        "SecurityGroups": NotRequired[List[str]],
    },
)

TargetReservationValueTypeDef = TypedDict(
    "TargetReservationValueTypeDef",
    {
        "ReservationValue": NotRequired["ReservationValueTypeDef"],
        "TargetConfiguration": NotRequired["TargetConfigurationTypeDef"],
    },
)

TerminateClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "TerminateClientVpnConnectionsRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "ConnectionId": NotRequired[str],
        "Username": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

TerminateClientVpnConnectionsResultTypeDef = TypedDict(
    "TerminateClientVpnConnectionsResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Username": str,
        "ConnectionStatuses": List["TerminateConnectionStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TerminateConnectionStatusTypeDef = TypedDict(
    "TerminateConnectionStatusTypeDef",
    {
        "ConnectionId": NotRequired[str],
        "PreviousStatus": NotRequired["ClientVpnConnectionStatusTypeDef"],
        "CurrentStatus": NotRequired["ClientVpnConnectionStatusTypeDef"],
    },
)

TerminateInstancesRequestInstanceTerminateTypeDef = TypedDict(
    "TerminateInstancesRequestInstanceTerminateTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

TerminateInstancesRequestRequestTypeDef = TypedDict(
    "TerminateInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

TerminateInstancesResultTypeDef = TypedDict(
    "TerminateInstancesResultTypeDef",
    {
        "TerminatingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThroughResourcesStatementRequestTypeDef = TypedDict(
    "ThroughResourcesStatementRequestTypeDef",
    {
        "ResourceStatement": NotRequired["ResourceStatementRequestTypeDef"],
    },
)

ThroughResourcesStatementTypeDef = TypedDict(
    "ThroughResourcesStatementTypeDef",
    {
        "ResourceStatement": NotRequired["ResourceStatementTypeDef"],
    },
)

TotalLocalStorageGBRequestTypeDef = TypedDict(
    "TotalLocalStorageGBRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)

TotalLocalStorageGBTypeDef = TypedDict(
    "TotalLocalStorageGBTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)

TrafficMirrorFilterRuleTypeDef = TypedDict(
    "TrafficMirrorFilterRuleTypeDef",
    {
        "TrafficMirrorFilterRuleId": NotRequired[str],
        "TrafficMirrorFilterId": NotRequired[str],
        "TrafficDirection": NotRequired[TrafficDirectionType],
        "RuleNumber": NotRequired[int],
        "RuleAction": NotRequired[TrafficMirrorRuleActionType],
        "Protocol": NotRequired[int],
        "DestinationPortRange": NotRequired["TrafficMirrorPortRangeTypeDef"],
        "SourcePortRange": NotRequired["TrafficMirrorPortRangeTypeDef"],
        "DestinationCidrBlock": NotRequired[str],
        "SourceCidrBlock": NotRequired[str],
        "Description": NotRequired[str],
    },
)

TrafficMirrorFilterTypeDef = TypedDict(
    "TrafficMirrorFilterTypeDef",
    {
        "TrafficMirrorFilterId": NotRequired[str],
        "IngressFilterRules": NotRequired[List["TrafficMirrorFilterRuleTypeDef"]],
        "EgressFilterRules": NotRequired[List["TrafficMirrorFilterRuleTypeDef"]],
        "NetworkServices": NotRequired[List[Literal["amazon-dns"]]],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TrafficMirrorPortRangeRequestTypeDef = TypedDict(
    "TrafficMirrorPortRangeRequestTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)

TrafficMirrorPortRangeTypeDef = TypedDict(
    "TrafficMirrorPortRangeTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)

TrafficMirrorSessionTypeDef = TypedDict(
    "TrafficMirrorSessionTypeDef",
    {
        "TrafficMirrorSessionId": NotRequired[str],
        "TrafficMirrorTargetId": NotRequired[str],
        "TrafficMirrorFilterId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "PacketLength": NotRequired[int],
        "SessionNumber": NotRequired[int],
        "VirtualNetworkId": NotRequired[int],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TrafficMirrorTargetTypeDef = TypedDict(
    "TrafficMirrorTargetTypeDef",
    {
        "TrafficMirrorTargetId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkLoadBalancerArn": NotRequired[str],
        "Type": NotRequired[TrafficMirrorTargetTypeType],
        "Description": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayAssociationTypeDef = TypedDict(
    "TransitGatewayAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)

TransitGatewayAttachmentAssociationTypeDef = TypedDict(
    "TransitGatewayAttachmentAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)

TransitGatewayAttachmentBgpConfigurationTypeDef = TypedDict(
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    {
        "TransitGatewayAsn": NotRequired[int],
        "PeerAsn": NotRequired[int],
        "TransitGatewayAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "BgpStatus": NotRequired[BgpStatusType],
    },
)

TransitGatewayAttachmentPropagationTypeDef = TypedDict(
    "TransitGatewayAttachmentPropagationTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayPropagationStateType],
    },
)

TransitGatewayAttachmentTypeDef = TypedDict(
    "TransitGatewayAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "TransitGatewayOwnerId": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceId": NotRequired[str],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "Association": NotRequired["TransitGatewayAttachmentAssociationTypeDef"],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayConnectOptionsTypeDef = TypedDict(
    "TransitGatewayConnectOptionsTypeDef",
    {
        "Protocol": NotRequired[Literal["gre"]],
    },
)

TransitGatewayConnectPeerConfigurationTypeDef = TypedDict(
    "TransitGatewayConnectPeerConfigurationTypeDef",
    {
        "TransitGatewayAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "Protocol": NotRequired[Literal["gre"]],
        "BgpConfigurations": NotRequired[List["TransitGatewayAttachmentBgpConfigurationTypeDef"]],
    },
)

TransitGatewayConnectPeerTypeDef = TypedDict(
    "TransitGatewayConnectPeerTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayConnectPeerId": NotRequired[str],
        "State": NotRequired[TransitGatewayConnectPeerStateType],
        "CreationTime": NotRequired[datetime],
        "ConnectPeerConfiguration": NotRequired["TransitGatewayConnectPeerConfigurationTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayConnectRequestBgpOptionsTypeDef = TypedDict(
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    {
        "PeerAsn": NotRequired[int],
    },
)

TransitGatewayConnectTypeDef = TypedDict(
    "TransitGatewayConnectTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransportTransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "CreationTime": NotRequired[datetime],
        "Options": NotRequired["TransitGatewayConnectOptionsTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayMulticastDeregisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "DeregisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)

TransitGatewayMulticastDeregisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "DeregisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)

TransitGatewayMulticastDomainAssociationTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "Subnet": NotRequired["SubnetAssociationTypeDef"],
    },
)

TransitGatewayMulticastDomainAssociationsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "Subnets": NotRequired[List["SubnetAssociationTypeDef"]],
    },
)

TransitGatewayMulticastDomainOptionsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainOptionsTypeDef",
    {
        "Igmpv2Support": NotRequired[Igmpv2SupportValueType],
        "StaticSourcesSupport": NotRequired[StaticSourcesSupportValueType],
        "AutoAcceptSharedAssociations": NotRequired[AutoAcceptSharedAssociationsValueType],
    },
)

TransitGatewayMulticastDomainTypeDef = TypedDict(
    "TransitGatewayMulticastDomainTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "TransitGatewayMulticastDomainArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Options": NotRequired["TransitGatewayMulticastDomainOptionsTypeDef"],
        "State": NotRequired[TransitGatewayMulticastDomainStateType],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayMulticastGroupTypeDef = TypedDict(
    "TransitGatewayMulticastGroupTypeDef",
    {
        "GroupIpAddress": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "GroupMember": NotRequired[bool],
        "GroupSource": NotRequired[bool],
        "MemberType": NotRequired[MembershipTypeType],
        "SourceType": NotRequired[MembershipTypeType],
    },
)

TransitGatewayMulticastRegisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "RegisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)

TransitGatewayMulticastRegisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "RegisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)

TransitGatewayOptionsTypeDef = TypedDict(
    "TransitGatewayOptionsTypeDef",
    {
        "AmazonSideAsn": NotRequired[int],
        "TransitGatewayCidrBlocks": NotRequired[List[str]],
        "AutoAcceptSharedAttachments": NotRequired[AutoAcceptSharedAttachmentsValueType],
        "DefaultRouteTableAssociation": NotRequired[DefaultRouteTableAssociationValueType],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[DefaultRouteTablePropagationValueType],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "VpnEcmpSupport": NotRequired[VpnEcmpSupportValueType],
        "DnsSupport": NotRequired[DnsSupportValueType],
        "MulticastSupport": NotRequired[MulticastSupportValueType],
    },
)

TransitGatewayPeeringAttachmentTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "RequesterTgwInfo": NotRequired["PeeringTgwInfoTypeDef"],
        "AccepterTgwInfo": NotRequired["PeeringTgwInfoTypeDef"],
        "Status": NotRequired["PeeringAttachmentStatusTypeDef"],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayPrefixListAttachmentTypeDef = TypedDict(
    "TransitGatewayPrefixListAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceId": NotRequired[str],
    },
)

TransitGatewayPrefixListReferenceTypeDef = TypedDict(
    "TransitGatewayPrefixListReferenceTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "PrefixListOwnerId": NotRequired[str],
        "State": NotRequired[TransitGatewayPrefixListReferenceStateType],
        "Blackhole": NotRequired[bool],
        "TransitGatewayAttachment": NotRequired["TransitGatewayPrefixListAttachmentTypeDef"],
    },
)

TransitGatewayPropagationTypeDef = TypedDict(
    "TransitGatewayPropagationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayPropagationStateType],
    },
)

TransitGatewayRequestOptionsTypeDef = TypedDict(
    "TransitGatewayRequestOptionsTypeDef",
    {
        "AmazonSideAsn": NotRequired[int],
        "AutoAcceptSharedAttachments": NotRequired[AutoAcceptSharedAttachmentsValueType],
        "DefaultRouteTableAssociation": NotRequired[DefaultRouteTableAssociationValueType],
        "DefaultRouteTablePropagation": NotRequired[DefaultRouteTablePropagationValueType],
        "VpnEcmpSupport": NotRequired[VpnEcmpSupportValueType],
        "DnsSupport": NotRequired[DnsSupportValueType],
        "MulticastSupport": NotRequired[MulticastSupportValueType],
        "TransitGatewayCidrBlocks": NotRequired[Sequence[str]],
    },
)

TransitGatewayRouteAttachmentTypeDef = TypedDict(
    "TransitGatewayRouteAttachmentTypeDef",
    {
        "ResourceId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
    },
)

TransitGatewayRouteTableAssociationTypeDef = TypedDict(
    "TransitGatewayRouteTableAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)

TransitGatewayRouteTablePropagationTypeDef = TypedDict(
    "TransitGatewayRouteTablePropagationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayPropagationStateType],
    },
)

TransitGatewayRouteTableTypeDef = TypedDict(
    "TransitGatewayRouteTableTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "State": NotRequired[TransitGatewayRouteTableStateType],
        "DefaultAssociationRouteTable": NotRequired[bool],
        "DefaultPropagationRouteTable": NotRequired[bool],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayRouteTypeDef = TypedDict(
    "TransitGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "TransitGatewayAttachments": NotRequired[List["TransitGatewayRouteAttachmentTypeDef"]],
        "Type": NotRequired[TransitGatewayRouteTypeType],
        "State": NotRequired[TransitGatewayRouteStateType],
    },
)

TransitGatewayTypeDef = TypedDict(
    "TransitGatewayTypeDef",
    {
        "TransitGatewayId": NotRequired[str],
        "TransitGatewayArn": NotRequired[str],
        "State": NotRequired[TransitGatewayStateType],
        "OwnerId": NotRequired[str],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Options": NotRequired["TransitGatewayOptionsTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransitGatewayVpcAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    {
        "DnsSupport": NotRequired[DnsSupportValueType],
        "Ipv6Support": NotRequired[Ipv6SupportValueType],
        "ApplianceModeSupport": NotRequired[ApplianceModeSupportValueType],
    },
)

TransitGatewayVpcAttachmentTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcOwnerId": NotRequired[str],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "SubnetIds": NotRequired[List[str]],
        "CreationTime": NotRequired[datetime],
        "Options": NotRequired["TransitGatewayVpcAttachmentOptionsTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TrunkInterfaceAssociationTypeDef = TypedDict(
    "TrunkInterfaceAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "BranchInterfaceId": NotRequired[str],
        "TrunkInterfaceId": NotRequired[str],
        "InterfaceProtocol": NotRequired[InterfaceProtocolTypeType],
        "VlanId": NotRequired[int],
        "GreKey": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TunnelOptionTypeDef = TypedDict(
    "TunnelOptionTypeDef",
    {
        "OutsideIpAddress": NotRequired[str],
        "TunnelInsideCidr": NotRequired[str],
        "TunnelInsideIpv6Cidr": NotRequired[str],
        "PreSharedKey": NotRequired[str],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2LifetimeSeconds": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "RekeyFuzzPercentage": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "DpdTimeoutSeconds": NotRequired[int],
        "DpdTimeoutAction": NotRequired[str],
        "Phase1EncryptionAlgorithms": NotRequired[
            List["Phase1EncryptionAlgorithmsListValueTypeDef"]
        ],
        "Phase2EncryptionAlgorithms": NotRequired[
            List["Phase2EncryptionAlgorithmsListValueTypeDef"]
        ],
        "Phase1IntegrityAlgorithms": NotRequired[List["Phase1IntegrityAlgorithmsListValueTypeDef"]],
        "Phase2IntegrityAlgorithms": NotRequired[List["Phase2IntegrityAlgorithmsListValueTypeDef"]],
        "Phase1DHGroupNumbers": NotRequired[List["Phase1DHGroupNumbersListValueTypeDef"]],
        "Phase2DHGroupNumbers": NotRequired[List["Phase2DHGroupNumbersListValueTypeDef"]],
        "IkeVersions": NotRequired[List["IKEVersionsListValueTypeDef"]],
        "StartupAction": NotRequired[str],
    },
)

UnassignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "UnassignIpv6AddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Ipv6Addresses": NotRequired[Sequence[str]],
        "Ipv6Prefixes": NotRequired[Sequence[str]],
    },
)

UnassignIpv6AddressesResultTypeDef = TypedDict(
    "UnassignIpv6AddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "UnassignedIpv6Addresses": List[str],
        "UnassignedIpv6Prefixes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef",
    {
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
    },
)

UnassignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
    },
)

UnmonitorInstancesRequestInstanceUnmonitorTypeDef = TypedDict(
    "UnmonitorInstancesRequestInstanceUnmonitorTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)

UnmonitorInstancesRequestRequestTypeDef = TypedDict(
    "UnmonitorInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)

UnmonitorInstancesResultTypeDef = TypedDict(
    "UnmonitorInstancesResultTypeDef",
    {
        "InstanceMonitorings": List["InstanceMonitoringTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    {
        "Code": NotRequired[UnsuccessfulInstanceCreditSpecificationErrorCodeType],
        "Message": NotRequired[str],
    },
)

UnsuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": NotRequired[str],
        "Error": NotRequired["UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef"],
    },
)

UnsuccessfulItemErrorTypeDef = TypedDict(
    "UnsuccessfulItemErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

UnsuccessfulItemTypeDef = TypedDict(
    "UnsuccessfulItemTypeDef",
    {
        "Error": NotRequired["UnsuccessfulItemErrorTypeDef"],
        "ResourceId": NotRequired[str],
    },
)

UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "SecurityGroupRuleDescriptions": NotRequired[
            Sequence["SecurityGroupRuleDescriptionTypeDef"]
        ],
    },
)

UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "SecurityGroupRuleDescriptions": NotRequired[
            Sequence["SecurityGroupRuleDescriptionTypeDef"]
        ],
    },
)

UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserBucketDetailsTypeDef = TypedDict(
    "UserBucketDetailsTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)

UserBucketTypeDef = TypedDict(
    "UserBucketTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "Data": NotRequired[str],
    },
)

UserIdGroupPairTypeDef = TypedDict(
    "UserIdGroupPairTypeDef",
    {
        "Description": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

VCpuCountRangeRequestTypeDef = TypedDict(
    "VCpuCountRangeRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)

VCpuCountRangeTypeDef = TypedDict(
    "VCpuCountRangeTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

VCpuInfoTypeDef = TypedDict(
    "VCpuInfoTypeDef",
    {
        "DefaultVCpus": NotRequired[int],
        "DefaultCores": NotRequired[int],
        "DefaultThreadsPerCore": NotRequired[int],
        "ValidCores": NotRequired[List[int]],
        "ValidThreadsPerCore": NotRequired[List[int]],
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "Errors": NotRequired[List["ValidationErrorTypeDef"]],
    },
)

VgwTelemetryTypeDef = TypedDict(
    "VgwTelemetryTypeDef",
    {
        "AcceptedRouteCount": NotRequired[int],
        "LastStatusChange": NotRequired[datetime],
        "OutsideIpAddress": NotRequired[str],
        "Status": NotRequired[TelemetryStatusType],
        "StatusMessage": NotRequired[str],
        "CertificateArn": NotRequired[str],
    },
)

VolumeAttachmentResponseMetadataTypeDef = TypedDict(
    "VolumeAttachmentResponseMetadataTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": VolumeAttachmentStateType,
        "VolumeId": str,
        "DeleteOnTermination": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeAttachmentTypeDef = TypedDict(
    "VolumeAttachmentTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "Device": NotRequired[str],
        "InstanceId": NotRequired[str],
        "State": NotRequired[VolumeAttachmentStateType],
        "VolumeId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
    },
)

VolumeDetailTypeDef = TypedDict(
    "VolumeDetailTypeDef",
    {
        "Size": int,
    },
)

VolumeModificationTypeDef = TypedDict(
    "VolumeModificationTypeDef",
    {
        "VolumeId": NotRequired[str],
        "ModificationState": NotRequired[VolumeModificationStateType],
        "StatusMessage": NotRequired[str],
        "TargetSize": NotRequired[int],
        "TargetIops": NotRequired[int],
        "TargetVolumeType": NotRequired[VolumeTypeType],
        "TargetThroughput": NotRequired[int],
        "TargetMultiAttachEnabled": NotRequired[bool],
        "OriginalSize": NotRequired[int],
        "OriginalIops": NotRequired[int],
        "OriginalVolumeType": NotRequired[VolumeTypeType],
        "OriginalThroughput": NotRequired[int],
        "OriginalMultiAttachEnabled": NotRequired[bool],
        "Progress": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

VolumeResponseMetadataTypeDef = TypedDict(
    "VolumeResponseMetadataTypeDef",
    {
        "Attachments": List["VolumeAttachmentTypeDef"],
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "State": VolumeStateType,
        "VolumeId": str,
        "Iops": int,
        "Tags": List["TagTypeDef"],
        "VolumeType": VolumeTypeType,
        "FastRestored": bool,
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeStatusActionTypeDef = TypedDict(
    "VolumeStatusActionTypeDef",
    {
        "Code": NotRequired[str],
        "Description": NotRequired[str],
        "EventId": NotRequired[str],
        "EventType": NotRequired[str],
    },
)

VolumeStatusAttachmentStatusTypeDef = TypedDict(
    "VolumeStatusAttachmentStatusTypeDef",
    {
        "IoPerformance": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)

VolumeStatusDetailsTypeDef = TypedDict(
    "VolumeStatusDetailsTypeDef",
    {
        "Name": NotRequired[VolumeStatusNameType],
        "Status": NotRequired[str],
    },
)

VolumeStatusEventTypeDef = TypedDict(
    "VolumeStatusEventTypeDef",
    {
        "Description": NotRequired[str],
        "EventId": NotRequired[str],
        "EventType": NotRequired[str],
        "NotAfter": NotRequired[datetime],
        "NotBefore": NotRequired[datetime],
        "InstanceId": NotRequired[str],
    },
)

VolumeStatusInfoTypeDef = TypedDict(
    "VolumeStatusInfoTypeDef",
    {
        "Details": NotRequired[List["VolumeStatusDetailsTypeDef"]],
        "Status": NotRequired[VolumeStatusInfoStatusType],
    },
)

VolumeStatusItemTypeDef = TypedDict(
    "VolumeStatusItemTypeDef",
    {
        "Actions": NotRequired[List["VolumeStatusActionTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Events": NotRequired[List["VolumeStatusEventTypeDef"]],
        "VolumeId": NotRequired[str],
        "VolumeStatus": NotRequired["VolumeStatusInfoTypeDef"],
        "AttachmentStatuses": NotRequired[List["VolumeStatusAttachmentStatusTypeDef"]],
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Attachments": NotRequired[List["VolumeAttachmentTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "State": NotRequired[VolumeStateType],
        "VolumeId": NotRequired[str],
        "Iops": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VolumeType": NotRequired[VolumeTypeType],
        "FastRestored": NotRequired[bool],
        "MultiAttachEnabled": NotRequired[bool],
        "Throughput": NotRequired[int],
    },
)

VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "State": NotRequired[AttachmentStatusType],
        "VpcId": NotRequired[str],
    },
)

VpcCidrBlockAssociationTypeDef = TypedDict(
    "VpcCidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired["VpcCidrBlockStateTypeDef"],
    },
)

VpcCidrBlockStateTypeDef = TypedDict(
    "VpcCidrBlockStateTypeDef",
    {
        "State": NotRequired[VpcCidrBlockStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)

VpcClassicLinkTypeDef = TypedDict(
    "VpcClassicLinkTypeDef",
    {
        "ClassicLinkEnabled": NotRequired[bool],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

VpcEndpointConnectionTypeDef = TypedDict(
    "VpcEndpointConnectionTypeDef",
    {
        "ServiceId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
        "VpcEndpointOwner": NotRequired[str],
        "VpcEndpointState": NotRequired[StateType],
        "CreationTimestamp": NotRequired[datetime],
        "DnsEntries": NotRequired[List["DnsEntryTypeDef"]],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
    },
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": NotRequired[str],
        "VpcEndpointType": NotRequired[VpcEndpointTypeType],
        "VpcId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "State": NotRequired[StateType],
        "PolicyDocument": NotRequired[str],
        "RouteTableIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "Groups": NotRequired[List["SecurityGroupIdentifierTypeDef"]],
        "PrivateDnsEnabled": NotRequired[bool],
        "RequesterManaged": NotRequired[bool],
        "NetworkInterfaceIds": NotRequired[List[str]],
        "DnsEntries": NotRequired[List["DnsEntryTypeDef"]],
        "CreationTimestamp": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
        "OwnerId": NotRequired[str],
        "LastError": NotRequired["LastErrorTypeDef"],
    },
)

VpcIpv6CidrBlockAssociationTypeDef = TypedDict(
    "VpcIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv6CidrBlockState": NotRequired["VpcCidrBlockStateTypeDef"],
        "NetworkBorderGroup": NotRequired[str],
        "Ipv6Pool": NotRequired[str],
    },
)

VpcPeeringConnectionOptionsDescriptionTypeDef = TypedDict(
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)

VpcPeeringConnectionStateReasonResponseMetadataTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonResponseMetadataTypeDef",
    {
        "Code": VpcPeeringConnectionStateReasonCodeType,
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcPeeringConnectionStateReasonTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonTypeDef",
    {
        "Code": NotRequired[VpcPeeringConnectionStateReasonCodeType],
        "Message": NotRequired[str],
    },
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "AccepterVpcInfo": NotRequired["VpcPeeringConnectionVpcInfoTypeDef"],
        "ExpirationTime": NotRequired[datetime],
        "RequesterVpcInfo": NotRequired["VpcPeeringConnectionVpcInfoTypeDef"],
        "Status": NotRequired["VpcPeeringConnectionStateReasonTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)

VpcPeeringConnectionVpcInfoResponseMetadataTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoResponseMetadataTypeDef",
    {
        "CidrBlock": str,
        "Ipv6CidrBlockSet": List["Ipv6CidrBlockTypeDef"],
        "CidrBlockSet": List["CidrBlockTypeDef"],
        "OwnerId": str,
        "PeeringOptions": "VpcPeeringConnectionOptionsDescriptionTypeDef",
        "VpcId": str,
        "Region": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcPeeringConnectionVpcInfoTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlockSet": NotRequired[List["Ipv6CidrBlockTypeDef"]],
        "CidrBlockSet": NotRequired[List["CidrBlockTypeDef"]],
        "OwnerId": NotRequired[str],
        "PeeringOptions": NotRequired["VpcPeeringConnectionOptionsDescriptionTypeDef"],
        "VpcId": NotRequired[str],
        "Region": NotRequired[str],
    },
)

VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[VpcStateType],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "InstanceTenancy": NotRequired[TenancyType],
        "Ipv6CidrBlockAssociationSet": NotRequired[List["VpcIpv6CidrBlockAssociationTypeDef"]],
        "CidrBlockAssociationSet": NotRequired[List["VpcCidrBlockAssociationTypeDef"]],
        "IsDefault": NotRequired[bool],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

VpnConnectionDeviceTypeTypeDef = TypedDict(
    "VpnConnectionDeviceTypeTypeDef",
    {
        "VpnConnectionDeviceTypeId": NotRequired[str],
        "Vendor": NotRequired[str],
        "Platform": NotRequired[str],
        "Software": NotRequired[str],
    },
)

VpnConnectionOptionsSpecificationTypeDef = TypedDict(
    "VpnConnectionOptionsSpecificationTypeDef",
    {
        "EnableAcceleration": NotRequired[bool],
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelInsideIpVersion": NotRequired[TunnelInsideIpVersionType],
        "TunnelOptions": NotRequired[Sequence["VpnTunnelOptionsSpecificationTypeDef"]],
        "LocalIpv4NetworkCidr": NotRequired[str],
        "RemoteIpv4NetworkCidr": NotRequired[str],
        "LocalIpv6NetworkCidr": NotRequired[str],
        "RemoteIpv6NetworkCidr": NotRequired[str],
    },
)

VpnConnectionOptionsTypeDef = TypedDict(
    "VpnConnectionOptionsTypeDef",
    {
        "EnableAcceleration": NotRequired[bool],
        "StaticRoutesOnly": NotRequired[bool],
        "LocalIpv4NetworkCidr": NotRequired[str],
        "RemoteIpv4NetworkCidr": NotRequired[str],
        "LocalIpv6NetworkCidr": NotRequired[str],
        "RemoteIpv6NetworkCidr": NotRequired[str],
        "TunnelInsideIpVersion": NotRequired[TunnelInsideIpVersionType],
        "TunnelOptions": NotRequired[List["TunnelOptionTypeDef"]],
    },
)

VpnConnectionTypeDef = TypedDict(
    "VpnConnectionTypeDef",
    {
        "CustomerGatewayConfiguration": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "State": NotRequired[VpnStateType],
        "Type": NotRequired[Literal["ipsec.1"]],
        "VpnConnectionId": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "CoreNetworkAttachmentArn": NotRequired[str],
        "GatewayAssociationState": NotRequired[GatewayAssociationStateType],
        "Options": NotRequired["VpnConnectionOptionsTypeDef"],
        "Routes": NotRequired[List["VpnStaticRouteTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VgwTelemetry": NotRequired[List["VgwTelemetryTypeDef"]],
    },
)

VpnGatewayTypeDef = TypedDict(
    "VpnGatewayTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[VpnStateType],
        "Type": NotRequired[Literal["ipsec.1"]],
        "VpcAttachments": NotRequired[List["VpcAttachmentTypeDef"]],
        "VpnGatewayId": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

VpnStaticRouteTypeDef = TypedDict(
    "VpnStaticRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "Source": NotRequired[Literal["Static"]],
        "State": NotRequired[VpnStateType],
    },
)

VpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": NotRequired[str],
        "TunnelInsideIpv6Cidr": NotRequired[str],
        "PreSharedKey": NotRequired[str],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2LifetimeSeconds": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "RekeyFuzzPercentage": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "DPDTimeoutSeconds": NotRequired[int],
        "DPDTimeoutAction": NotRequired[str],
        "Phase1EncryptionAlgorithms": NotRequired[
            Sequence["Phase1EncryptionAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase2EncryptionAlgorithms": NotRequired[
            Sequence["Phase2EncryptionAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase1IntegrityAlgorithms": NotRequired[
            Sequence["Phase1IntegrityAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase2IntegrityAlgorithms": NotRequired[
            Sequence["Phase2IntegrityAlgorithmsRequestListValueTypeDef"]
        ],
        "Phase1DHGroupNumbers": NotRequired[
            Sequence["Phase1DHGroupNumbersRequestListValueTypeDef"]
        ],
        "Phase2DHGroupNumbers": NotRequired[
            Sequence["Phase2DHGroupNumbersRequestListValueTypeDef"]
        ],
        "IKEVersions": NotRequired[Sequence["IKEVersionsRequestListValueTypeDef"]],
        "StartupAction": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WithdrawByoipCidrRequestRequestTypeDef = TypedDict(
    "WithdrawByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)

WithdrawByoipCidrResultTypeDef = TypedDict(
    "WithdrawByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
