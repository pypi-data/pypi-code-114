"""
Type annotations for medialive service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_medialive.type_defs import AacSettingsTypeDef

    data: AacSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AacCodingModeType,
    AacInputTypeType,
    AacProfileType,
    AacRateControlModeType,
    AacRawFormatType,
    AacSpecType,
    AacVbrQualityType,
    Ac3BitstreamModeType,
    Ac3CodingModeType,
    Ac3DrcProfileType,
    Ac3LfeFilterType,
    Ac3MetadataControlType,
    AfdSignalingType,
    AudioDescriptionAudioTypeControlType,
    AudioDescriptionLanguageCodeControlType,
    AudioLanguageSelectionPolicyType,
    AudioNormalizationAlgorithmType,
    AudioOnlyHlsSegmentTypeType,
    AudioOnlyHlsTrackTypeType,
    AudioTypeType,
    AuthenticationSchemeType,
    AvailBlankingStateType,
    BlackoutSlateNetworkEndBlackoutType,
    BlackoutSlateStateType,
    BurnInAlignmentType,
    BurnInBackgroundColorType,
    BurnInFontColorType,
    BurnInOutlineColorType,
    BurnInShadowColorType,
    BurnInTeletextGridControlType,
    CdiInputResolutionType,
    ChannelClassType,
    ChannelStateType,
    DeviceSettingsSyncStateType,
    DeviceUpdateStatusType,
    DvbSdtOutputSdtType,
    DvbSubDestinationAlignmentType,
    DvbSubDestinationBackgroundColorType,
    DvbSubDestinationFontColorType,
    DvbSubDestinationOutlineColorType,
    DvbSubDestinationShadowColorType,
    DvbSubDestinationTeletextGridControlType,
    DvbSubOcrLanguageType,
    Eac3AttenuationControlType,
    Eac3BitstreamModeType,
    Eac3CodingModeType,
    Eac3DcFilterType,
    Eac3DrcLineType,
    Eac3DrcRfType,
    Eac3LfeControlType,
    Eac3LfeFilterType,
    Eac3MetadataControlType,
    Eac3PassthroughControlType,
    Eac3PhaseControlType,
    Eac3StereoDownmixType,
    Eac3SurroundExModeType,
    Eac3SurroundModeType,
    EbuTtDDestinationStyleControlType,
    EbuTtDFillLineGapControlType,
    EmbeddedConvert608To708Type,
    EmbeddedScte20DetectionType,
    FeatureActivationsInputPrepareScheduleActionsType,
    FecOutputIncludeFecType,
    FixedAfdType,
    Fmp4NielsenId3BehaviorType,
    Fmp4TimedMetadataBehaviorType,
    FollowPointType,
    FrameCaptureIntervalUnitType,
    GlobalConfigurationInputEndActionType,
    GlobalConfigurationLowFramerateInputsType,
    GlobalConfigurationOutputLockingModeType,
    GlobalConfigurationOutputTimingSourceType,
    H264AdaptiveQuantizationType,
    H264ColorMetadataType,
    H264EntropyEncodingType,
    H264FlickerAqType,
    H264ForceFieldPicturesType,
    H264FramerateControlType,
    H264GopBReferenceType,
    H264GopSizeUnitsType,
    H264LevelType,
    H264LookAheadRateControlType,
    H264ParControlType,
    H264ProfileType,
    H264QualityLevelType,
    H264RateControlModeType,
    H264ScanTypeType,
    H264SceneChangeDetectType,
    H264SpatialAqType,
    H264SubGopLengthType,
    H264SyntaxType,
    H264TemporalAqType,
    H264TimecodeInsertionBehaviorType,
    H265AdaptiveQuantizationType,
    H265AlternativeTransferFunctionType,
    H265ColorMetadataType,
    H265FlickerAqType,
    H265GopSizeUnitsType,
    H265LevelType,
    H265LookAheadRateControlType,
    H265ProfileType,
    H265RateControlModeType,
    H265ScanTypeType,
    H265SceneChangeDetectType,
    H265TierType,
    H265TimecodeInsertionBehaviorType,
    HlsAdMarkersType,
    HlsAkamaiHttpTransferModeType,
    HlsCaptionLanguageSettingType,
    HlsClientCacheType,
    HlsCodecSpecificationType,
    HlsDirectoryStructureType,
    HlsDiscontinuityTagsType,
    HlsEncryptionTypeType,
    HlsH265PackagingTypeType,
    HlsId3SegmentTaggingStateType,
    HlsIncompleteSegmentBehaviorType,
    HlsIvInManifestType,
    HlsIvSourceType,
    HlsManifestCompressionType,
    HlsManifestDurationFormatType,
    HlsModeType,
    HlsOutputSelectionType,
    HlsProgramDateTimeClockType,
    HlsProgramDateTimeType,
    HlsRedundantManifestType,
    HlsScte35SourceTypeType,
    HlsSegmentationModeType,
    HlsStreamInfResolutionType,
    HlsTimedMetadataId3FrameType,
    HlsTsFileModeType,
    HlsWebdavHttpTransferModeType,
    IFrameOnlyPlaylistTypeType,
    InputClassType,
    InputCodecType,
    InputDeblockFilterType,
    InputDenoiseFilterType,
    InputDeviceActiveInputType,
    InputDeviceConfiguredInputType,
    InputDeviceConnectionStateType,
    InputDeviceIpSchemeType,
    InputDeviceScanTypeType,
    InputDeviceStateType,
    InputDeviceTransferTypeType,
    InputFilterType,
    InputLossActionForHlsOutType,
    InputLossActionForMsSmoothOutType,
    InputLossActionForRtmpOutType,
    InputLossActionForUdpOutType,
    InputLossImageTypeType,
    InputMaximumBitrateType,
    InputPreferenceType,
    InputResolutionType,
    InputSecurityGroupStateType,
    InputSourceEndBehaviorType,
    InputSourceTypeType,
    InputStateType,
    InputTimecodeSourceType,
    InputTypeType,
    LastFrameClippingBehaviorType,
    LogLevelType,
    M2tsAbsentInputAudioBehaviorType,
    M2tsAribCaptionsPidControlType,
    M2tsAribType,
    M2tsAudioBufferModelType,
    M2tsAudioIntervalType,
    M2tsAudioStreamTypeType,
    M2tsBufferModelType,
    M2tsCcDescriptorType,
    M2tsEbifControlType,
    M2tsEbpPlacementType,
    M2tsEsRateInPesType,
    M2tsKlvType,
    M2tsNielsenId3BehaviorType,
    M2tsPcrControlType,
    M2tsRateModeType,
    M2tsScte35ControlType,
    M2tsSegmentationMarkersType,
    M2tsSegmentationStyleType,
    M2tsTimedMetadataBehaviorType,
    M3u8NielsenId3BehaviorType,
    M3u8PcrControlType,
    M3u8Scte35BehaviorType,
    M3u8TimedMetadataBehaviorType,
    MotionGraphicsInsertionType,
    Mp2CodingModeType,
    Mpeg2AdaptiveQuantizationType,
    Mpeg2ColorMetadataType,
    Mpeg2ColorSpaceType,
    Mpeg2DisplayRatioType,
    Mpeg2GopSizeUnitsType,
    Mpeg2ScanTypeType,
    Mpeg2SubGopLengthType,
    Mpeg2TimecodeInsertionBehaviorType,
    MsSmoothH265PackagingTypeType,
    MultiplexStateType,
    NetworkInputServerValidationType,
    NielsenPcmToId3TaggingStateType,
    NielsenWatermarksCbetStepasideType,
    NielsenWatermarksDistributionTypesType,
    PipelineIdType,
    PreferredChannelPipelineType,
    ReservationCodecType,
    ReservationMaximumBitrateType,
    ReservationMaximumFramerateType,
    ReservationResolutionType,
    ReservationResourceTypeType,
    ReservationSpecialFeatureType,
    ReservationStateType,
    ReservationVideoQualityType,
    RtmpCacheFullBehaviorType,
    RtmpCaptionDataType,
    RtmpOutputCertificateModeType,
    S3CannedAclType,
    Scte20Convert608To708Type,
    Scte27OcrLanguageType,
    Scte35AposNoRegionalBlackoutBehaviorType,
    Scte35AposWebDeliveryAllowedBehaviorType,
    Scte35ArchiveAllowedFlagType,
    Scte35DeviceRestrictionsType,
    Scte35NoRegionalBlackoutFlagType,
    Scte35SegmentationCancelIndicatorType,
    Scte35SpliceInsertNoRegionalBlackoutBehaviorType,
    Scte35SpliceInsertWebDeliveryAllowedBehaviorType,
    Scte35WebDeliveryAllowedFlagType,
    SmoothGroupAudioOnlyTimecodeControlType,
    SmoothGroupCertificateModeType,
    SmoothGroupEventIdModeType,
    SmoothGroupEventStopBehaviorType,
    SmoothGroupSegmentationModeType,
    SmoothGroupSparseTrackTypeType,
    SmoothGroupStreamManifestBehaviorType,
    SmoothGroupTimestampOffsetModeType,
    Smpte2038DataPreferenceType,
    TemporalFilterPostFilterSharpeningType,
    TemporalFilterStrengthType,
    TimecodeConfigSourceType,
    TtmlDestinationStyleControlType,
    UdpTimedMetadataId3FrameType,
    VideoDescriptionRespondToAfdType,
    VideoDescriptionScalingBehaviorType,
    VideoSelectorColorSpaceType,
    VideoSelectorColorSpaceUsageType,
    WavCodingModeType,
    WebvttDestinationStyleControlType,
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
    "AacSettingsTypeDef",
    "Ac3SettingsTypeDef",
    "AcceptInputDeviceTransferRequestRequestTypeDef",
    "AncillarySourceSettingsTypeDef",
    "ArchiveCdnSettingsTypeDef",
    "ArchiveContainerSettingsTypeDef",
    "ArchiveGroupSettingsTypeDef",
    "ArchiveOutputSettingsTypeDef",
    "ArchiveS3SettingsTypeDef",
    "AudioChannelMappingTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionTypeDef",
    "AudioHlsRenditionSelectionTypeDef",
    "AudioLanguageSelectionTypeDef",
    "AudioNormalizationSettingsTypeDef",
    "AudioOnlyHlsSettingsTypeDef",
    "AudioPidSelectionTypeDef",
    "AudioSelectorSettingsTypeDef",
    "AudioSelectorTypeDef",
    "AudioSilenceFailoverSettingsTypeDef",
    "AudioTrackSelectionTypeDef",
    "AudioTrackTypeDef",
    "AudioWatermarkSettingsTypeDef",
    "AutomaticInputFailoverSettingsTypeDef",
    "AvailBlankingTypeDef",
    "AvailConfigurationTypeDef",
    "AvailSettingsTypeDef",
    "BatchDeleteRequestRequestTypeDef",
    "BatchDeleteResponseTypeDef",
    "BatchFailedResultModelTypeDef",
    "BatchScheduleActionCreateRequestTypeDef",
    "BatchScheduleActionCreateResultTypeDef",
    "BatchScheduleActionDeleteRequestTypeDef",
    "BatchScheduleActionDeleteResultTypeDef",
    "BatchStartRequestRequestTypeDef",
    "BatchStartResponseTypeDef",
    "BatchStopRequestRequestTypeDef",
    "BatchStopResponseTypeDef",
    "BatchSuccessfulResultModelTypeDef",
    "BatchUpdateScheduleRequestRequestTypeDef",
    "BatchUpdateScheduleResponseTypeDef",
    "BlackoutSlateTypeDef",
    "BurnInDestinationSettingsTypeDef",
    "CancelInputDeviceTransferRequestRequestTypeDef",
    "CaptionDescriptionTypeDef",
    "CaptionDestinationSettingsTypeDef",
    "CaptionLanguageMappingTypeDef",
    "CaptionRectangleTypeDef",
    "CaptionSelectorSettingsTypeDef",
    "CaptionSelectorTypeDef",
    "CdiInputSpecificationTypeDef",
    "ChannelEgressEndpointTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ClaimDeviceRequestRequestTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateInputRequestRequestTypeDef",
    "CreateInputResponseTypeDef",
    "CreateInputSecurityGroupRequestRequestTypeDef",
    "CreateInputSecurityGroupResponseTypeDef",
    "CreateMultiplexProgramRequestRequestTypeDef",
    "CreateMultiplexProgramResponseTypeDef",
    "CreateMultiplexRequestRequestTypeDef",
    "CreateMultiplexResponseTypeDef",
    "CreatePartnerInputRequestRequestTypeDef",
    "CreatePartnerInputResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteChannelResponseTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DeleteInputSecurityGroupRequestRequestTypeDef",
    "DeleteMultiplexProgramRequestRequestTypeDef",
    "DeleteMultiplexProgramResponseTypeDef",
    "DeleteMultiplexRequestRequestTypeDef",
    "DeleteMultiplexResponseTypeDef",
    "DeleteReservationRequestRequestTypeDef",
    "DeleteReservationResponseTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeInputDeviceRequestRequestTypeDef",
    "DescribeInputDeviceResponseTypeDef",
    "DescribeInputDeviceThumbnailRequestRequestTypeDef",
    "DescribeInputDeviceThumbnailResponseTypeDef",
    "DescribeInputRequestRequestTypeDef",
    "DescribeInputResponseTypeDef",
    "DescribeInputSecurityGroupRequestRequestTypeDef",
    "DescribeInputSecurityGroupResponseTypeDef",
    "DescribeMultiplexProgramRequestRequestTypeDef",
    "DescribeMultiplexProgramResponseTypeDef",
    "DescribeMultiplexRequestRequestTypeDef",
    "DescribeMultiplexResponseTypeDef",
    "DescribeOfferingRequestRequestTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationRequestRequestTypeDef",
    "DescribeReservationResponseTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "DescribeScheduleResponseTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EbuTtDDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EncoderSettingsTypeDef",
    "FailoverConditionSettingsTypeDef",
    "FailoverConditionTypeDef",
    "FeatureActivationsTypeDef",
    "FecOutputSettingsTypeDef",
    "FixedModeScheduleActionStartSettingsTypeDef",
    "Fmp4HlsSettingsTypeDef",
    "FollowModeScheduleActionStartSettingsTypeDef",
    "FrameCaptureCdnSettingsTypeDef",
    "FrameCaptureGroupSettingsTypeDef",
    "FrameCaptureOutputSettingsTypeDef",
    "FrameCaptureS3SettingsTypeDef",
    "FrameCaptureSettingsTypeDef",
    "GlobalConfigurationTypeDef",
    "H264ColorSpaceSettingsTypeDef",
    "H264FilterSettingsTypeDef",
    "H264SettingsTypeDef",
    "H265ColorSpaceSettingsTypeDef",
    "H265FilterSettingsTypeDef",
    "H265SettingsTypeDef",
    "Hdr10SettingsTypeDef",
    "HlsAkamaiSettingsTypeDef",
    "HlsBasicPutSettingsTypeDef",
    "HlsCdnSettingsTypeDef",
    "HlsGroupSettingsTypeDef",
    "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
    "HlsInputSettingsTypeDef",
    "HlsMediaStoreSettingsTypeDef",
    "HlsOutputSettingsTypeDef",
    "HlsS3SettingsTypeDef",
    "HlsSettingsTypeDef",
    "HlsTimedMetadataScheduleActionSettingsTypeDef",
    "HlsWebdavSettingsTypeDef",
    "InputAttachmentTypeDef",
    "InputChannelLevelTypeDef",
    "InputClippingSettingsTypeDef",
    "InputDestinationRequestTypeDef",
    "InputDestinationTypeDef",
    "InputDestinationVpcTypeDef",
    "InputDeviceConfigurableSettingsTypeDef",
    "InputDeviceHdSettingsTypeDef",
    "InputDeviceNetworkSettingsTypeDef",
    "InputDeviceRequestTypeDef",
    "InputDeviceSettingsTypeDef",
    "InputDeviceSummaryTypeDef",
    "InputDeviceUhdSettingsTypeDef",
    "InputLocationTypeDef",
    "InputLossBehaviorTypeDef",
    "InputLossFailoverSettingsTypeDef",
    "InputPrepareScheduleActionSettingsTypeDef",
    "InputSecurityGroupTypeDef",
    "InputSettingsTypeDef",
    "InputSourceRequestTypeDef",
    "InputSourceTypeDef",
    "InputSpecificationTypeDef",
    "InputSwitchScheduleActionSettingsTypeDef",
    "InputTypeDef",
    "InputVpcRequestTypeDef",
    "InputWhitelistRuleCidrTypeDef",
    "InputWhitelistRuleTypeDef",
    "KeyProviderSettingsTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListInputDeviceTransfersRequestRequestTypeDef",
    "ListInputDeviceTransfersResponseTypeDef",
    "ListInputDevicesRequestRequestTypeDef",
    "ListInputDevicesResponseTypeDef",
    "ListInputSecurityGroupsRequestRequestTypeDef",
    "ListInputSecurityGroupsResponseTypeDef",
    "ListInputsRequestRequestTypeDef",
    "ListInputsResponseTypeDef",
    "ListMultiplexProgramsRequestRequestTypeDef",
    "ListMultiplexProgramsResponseTypeDef",
    "ListMultiplexesRequestRequestTypeDef",
    "ListMultiplexesResponseTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsRequestRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
    "MediaConnectFlowRequestTypeDef",
    "MediaConnectFlowTypeDef",
    "MediaPackageGroupSettingsTypeDef",
    "MediaPackageOutputDestinationSettingsTypeDef",
    "MotionGraphicsActivateScheduleActionSettingsTypeDef",
    "MotionGraphicsConfigurationTypeDef",
    "MotionGraphicsSettingsTypeDef",
    "Mp2SettingsTypeDef",
    "Mpeg2FilterSettingsTypeDef",
    "Mpeg2SettingsTypeDef",
    "MsSmoothGroupSettingsTypeDef",
    "MsSmoothOutputSettingsTypeDef",
    "MultiplexMediaConnectOutputDestinationSettingsTypeDef",
    "MultiplexOutputDestinationTypeDef",
    "MultiplexOutputSettingsTypeDef",
    "MultiplexProgramChannelDestinationSettingsTypeDef",
    "MultiplexProgramPacketIdentifiersMapTypeDef",
    "MultiplexProgramPipelineDetailTypeDef",
    "MultiplexProgramServiceDescriptorTypeDef",
    "MultiplexProgramSettingsTypeDef",
    "MultiplexProgramSummaryTypeDef",
    "MultiplexProgramTypeDef",
    "MultiplexSettingsSummaryTypeDef",
    "MultiplexSettingsTypeDef",
    "MultiplexStatmuxVideoSettingsTypeDef",
    "MultiplexSummaryTypeDef",
    "MultiplexTypeDef",
    "MultiplexVideoSettingsTypeDef",
    "NetworkInputSettingsTypeDef",
    "NielsenCBETTypeDef",
    "NielsenConfigurationTypeDef",
    "NielsenNaesIiNwTypeDef",
    "NielsenWatermarksSettingsTypeDef",
    "OfferingTypeDef",
    "OutputDestinationSettingsTypeDef",
    "OutputDestinationTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupTypeDef",
    "OutputLocationRefTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PauseStateScheduleActionSettingsTypeDef",
    "PipelineDetailTypeDef",
    "PipelinePauseStateSettingsTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RejectInputDeviceTransferRequestRequestTypeDef",
    "RemixSettingsTypeDef",
    "ReservationResourceSpecificationTypeDef",
    "ReservationTypeDef",
    "ResponseMetadataTypeDef",
    "RtmpGroupSettingsTypeDef",
    "RtmpOutputSettingsTypeDef",
    "ScheduleActionSettingsTypeDef",
    "ScheduleActionStartSettingsTypeDef",
    "ScheduleActionTypeDef",
    "Scte20SourceSettingsTypeDef",
    "Scte27SourceSettingsTypeDef",
    "Scte35DeliveryRestrictionsTypeDef",
    "Scte35DescriptorSettingsTypeDef",
    "Scte35DescriptorTypeDef",
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
    "Scte35SegmentationDescriptorTypeDef",
    "Scte35SpliceInsertScheduleActionSettingsTypeDef",
    "Scte35SpliceInsertTypeDef",
    "Scte35TimeSignalAposTypeDef",
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    "StandardHlsSettingsTypeDef",
    "StartChannelRequestRequestTypeDef",
    "StartChannelResponseTypeDef",
    "StartMultiplexRequestRequestTypeDef",
    "StartMultiplexResponseTypeDef",
    "StartTimecodeTypeDef",
    "StaticImageActivateScheduleActionSettingsTypeDef",
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    "StaticKeySettingsTypeDef",
    "StopChannelRequestRequestTypeDef",
    "StopChannelResponseTypeDef",
    "StopMultiplexRequestRequestTypeDef",
    "StopMultiplexResponseTypeDef",
    "StopTimecodeTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TemporalFilterSettingsTypeDef",
    "TimecodeConfigTypeDef",
    "TransferInputDeviceRequestRequestTypeDef",
    "TransferringInputDeviceSummaryTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "UdpContainerSettingsTypeDef",
    "UdpGroupSettingsTypeDef",
    "UdpOutputSettingsTypeDef",
    "UpdateChannelClassRequestRequestTypeDef",
    "UpdateChannelClassResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateInputDeviceRequestRequestTypeDef",
    "UpdateInputDeviceResponseTypeDef",
    "UpdateInputRequestRequestTypeDef",
    "UpdateInputResponseTypeDef",
    "UpdateInputSecurityGroupRequestRequestTypeDef",
    "UpdateInputSecurityGroupResponseTypeDef",
    "UpdateMultiplexProgramRequestRequestTypeDef",
    "UpdateMultiplexProgramResponseTypeDef",
    "UpdateMultiplexRequestRequestTypeDef",
    "UpdateMultiplexResponseTypeDef",
    "UpdateReservationRequestRequestTypeDef",
    "UpdateReservationResponseTypeDef",
    "VideoBlackFailoverSettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionTypeDef",
    "VideoSelectorColorSpaceSettingsTypeDef",
    "VideoSelectorPidTypeDef",
    "VideoSelectorProgramIdTypeDef",
    "VideoSelectorSettingsTypeDef",
    "VideoSelectorTypeDef",
    "VpcOutputSettingsDescriptionTypeDef",
    "VpcOutputSettingsTypeDef",
    "WaiterConfigTypeDef",
    "WavSettingsTypeDef",
    "WebvttDestinationSettingsTypeDef",
)

AacSettingsTypeDef = TypedDict(
    "AacSettingsTypeDef",
    {
        "Bitrate": NotRequired[float],
        "CodingMode": NotRequired[AacCodingModeType],
        "InputType": NotRequired[AacInputTypeType],
        "Profile": NotRequired[AacProfileType],
        "RateControlMode": NotRequired[AacRateControlModeType],
        "RawFormat": NotRequired[AacRawFormatType],
        "SampleRate": NotRequired[float],
        "Spec": NotRequired[AacSpecType],
        "VbrQuality": NotRequired[AacVbrQualityType],
    },
)

Ac3SettingsTypeDef = TypedDict(
    "Ac3SettingsTypeDef",
    {
        "Bitrate": NotRequired[float],
        "BitstreamMode": NotRequired[Ac3BitstreamModeType],
        "CodingMode": NotRequired[Ac3CodingModeType],
        "Dialnorm": NotRequired[int],
        "DrcProfile": NotRequired[Ac3DrcProfileType],
        "LfeFilter": NotRequired[Ac3LfeFilterType],
        "MetadataControl": NotRequired[Ac3MetadataControlType],
    },
)

AcceptInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "AcceptInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

AncillarySourceSettingsTypeDef = TypedDict(
    "AncillarySourceSettingsTypeDef",
    {
        "SourceAncillaryChannelNumber": NotRequired[int],
    },
)

ArchiveCdnSettingsTypeDef = TypedDict(
    "ArchiveCdnSettingsTypeDef",
    {
        "ArchiveS3Settings": NotRequired["ArchiveS3SettingsTypeDef"],
    },
)

ArchiveContainerSettingsTypeDef = TypedDict(
    "ArchiveContainerSettingsTypeDef",
    {
        "M2tsSettings": NotRequired["M2tsSettingsTypeDef"],
        "RawSettings": NotRequired[Mapping[str, Any]],
    },
)

ArchiveGroupSettingsTypeDef = TypedDict(
    "ArchiveGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
        "ArchiveCdnSettings": NotRequired["ArchiveCdnSettingsTypeDef"],
        "RolloverInterval": NotRequired[int],
    },
)

ArchiveOutputSettingsTypeDef = TypedDict(
    "ArchiveOutputSettingsTypeDef",
    {
        "ContainerSettings": "ArchiveContainerSettingsTypeDef",
        "Extension": NotRequired[str],
        "NameModifier": NotRequired[str],
    },
)

ArchiveS3SettingsTypeDef = TypedDict(
    "ArchiveS3SettingsTypeDef",
    {
        "CannedAcl": NotRequired[S3CannedAclType],
    },
)

AudioChannelMappingTypeDef = TypedDict(
    "AudioChannelMappingTypeDef",
    {
        "InputChannelLevels": Sequence["InputChannelLevelTypeDef"],
        "OutputChannel": int,
    },
)

AudioCodecSettingsTypeDef = TypedDict(
    "AudioCodecSettingsTypeDef",
    {
        "AacSettings": NotRequired["AacSettingsTypeDef"],
        "Ac3Settings": NotRequired["Ac3SettingsTypeDef"],
        "Eac3Settings": NotRequired["Eac3SettingsTypeDef"],
        "Mp2Settings": NotRequired["Mp2SettingsTypeDef"],
        "PassThroughSettings": NotRequired[Mapping[str, Any]],
        "WavSettings": NotRequired["WavSettingsTypeDef"],
    },
)

AudioDescriptionTypeDef = TypedDict(
    "AudioDescriptionTypeDef",
    {
        "AudioSelectorName": str,
        "Name": str,
        "AudioNormalizationSettings": NotRequired["AudioNormalizationSettingsTypeDef"],
        "AudioType": NotRequired[AudioTypeType],
        "AudioTypeControl": NotRequired[AudioDescriptionAudioTypeControlType],
        "AudioWatermarkingSettings": NotRequired["AudioWatermarkSettingsTypeDef"],
        "CodecSettings": NotRequired["AudioCodecSettingsTypeDef"],
        "LanguageCode": NotRequired[str],
        "LanguageCodeControl": NotRequired[AudioDescriptionLanguageCodeControlType],
        "RemixSettings": NotRequired["RemixSettingsTypeDef"],
        "StreamName": NotRequired[str],
    },
)

AudioHlsRenditionSelectionTypeDef = TypedDict(
    "AudioHlsRenditionSelectionTypeDef",
    {
        "GroupId": str,
        "Name": str,
    },
)

AudioLanguageSelectionTypeDef = TypedDict(
    "AudioLanguageSelectionTypeDef",
    {
        "LanguageCode": str,
        "LanguageSelectionPolicy": NotRequired[AudioLanguageSelectionPolicyType],
    },
)

AudioNormalizationSettingsTypeDef = TypedDict(
    "AudioNormalizationSettingsTypeDef",
    {
        "Algorithm": NotRequired[AudioNormalizationAlgorithmType],
        "AlgorithmControl": NotRequired[Literal["CORRECT_AUDIO"]],
        "TargetLkfs": NotRequired[float],
    },
)

AudioOnlyHlsSettingsTypeDef = TypedDict(
    "AudioOnlyHlsSettingsTypeDef",
    {
        "AudioGroupId": NotRequired[str],
        "AudioOnlyImage": NotRequired["InputLocationTypeDef"],
        "AudioTrackType": NotRequired[AudioOnlyHlsTrackTypeType],
        "SegmentType": NotRequired[AudioOnlyHlsSegmentTypeType],
    },
)

AudioPidSelectionTypeDef = TypedDict(
    "AudioPidSelectionTypeDef",
    {
        "Pid": int,
    },
)

AudioSelectorSettingsTypeDef = TypedDict(
    "AudioSelectorSettingsTypeDef",
    {
        "AudioHlsRenditionSelection": NotRequired["AudioHlsRenditionSelectionTypeDef"],
        "AudioLanguageSelection": NotRequired["AudioLanguageSelectionTypeDef"],
        "AudioPidSelection": NotRequired["AudioPidSelectionTypeDef"],
        "AudioTrackSelection": NotRequired["AudioTrackSelectionTypeDef"],
    },
)

AudioSelectorTypeDef = TypedDict(
    "AudioSelectorTypeDef",
    {
        "Name": str,
        "SelectorSettings": NotRequired["AudioSelectorSettingsTypeDef"],
    },
)

AudioSilenceFailoverSettingsTypeDef = TypedDict(
    "AudioSilenceFailoverSettingsTypeDef",
    {
        "AudioSelectorName": str,
        "AudioSilenceThresholdMsec": NotRequired[int],
    },
)

AudioTrackSelectionTypeDef = TypedDict(
    "AudioTrackSelectionTypeDef",
    {
        "Tracks": Sequence["AudioTrackTypeDef"],
    },
)

AudioTrackTypeDef = TypedDict(
    "AudioTrackTypeDef",
    {
        "Track": int,
    },
)

AudioWatermarkSettingsTypeDef = TypedDict(
    "AudioWatermarkSettingsTypeDef",
    {
        "NielsenWatermarksSettings": NotRequired["NielsenWatermarksSettingsTypeDef"],
    },
)

AutomaticInputFailoverSettingsTypeDef = TypedDict(
    "AutomaticInputFailoverSettingsTypeDef",
    {
        "SecondaryInputId": str,
        "ErrorClearTimeMsec": NotRequired[int],
        "FailoverConditions": NotRequired[Sequence["FailoverConditionTypeDef"]],
        "InputPreference": NotRequired[InputPreferenceType],
    },
)

AvailBlankingTypeDef = TypedDict(
    "AvailBlankingTypeDef",
    {
        "AvailBlankingImage": NotRequired["InputLocationTypeDef"],
        "State": NotRequired[AvailBlankingStateType],
    },
)

AvailConfigurationTypeDef = TypedDict(
    "AvailConfigurationTypeDef",
    {
        "AvailSettings": NotRequired["AvailSettingsTypeDef"],
    },
)

AvailSettingsTypeDef = TypedDict(
    "AvailSettingsTypeDef",
    {
        "Scte35SpliceInsert": NotRequired["Scte35SpliceInsertTypeDef"],
        "Scte35TimeSignalApos": NotRequired["Scte35TimeSignalAposTypeDef"],
    },
)

BatchDeleteRequestRequestTypeDef = TypedDict(
    "BatchDeleteRequestRequestTypeDef",
    {
        "ChannelIds": NotRequired[Sequence[str]],
        "InputIds": NotRequired[Sequence[str]],
        "InputSecurityGroupIds": NotRequired[Sequence[str]],
        "MultiplexIds": NotRequired[Sequence[str]],
    },
)

BatchDeleteResponseTypeDef = TypedDict(
    "BatchDeleteResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchFailedResultModelTypeDef = TypedDict(
    "BatchFailedResultModelTypeDef",
    {
        "Arn": NotRequired[str],
        "Code": NotRequired[str],
        "Id": NotRequired[str],
        "Message": NotRequired[str],
    },
)

BatchScheduleActionCreateRequestTypeDef = TypedDict(
    "BatchScheduleActionCreateRequestTypeDef",
    {
        "ScheduleActions": Sequence["ScheduleActionTypeDef"],
    },
)

BatchScheduleActionCreateResultTypeDef = TypedDict(
    "BatchScheduleActionCreateResultTypeDef",
    {
        "ScheduleActions": List["ScheduleActionTypeDef"],
    },
)

BatchScheduleActionDeleteRequestTypeDef = TypedDict(
    "BatchScheduleActionDeleteRequestTypeDef",
    {
        "ActionNames": Sequence[str],
    },
)

BatchScheduleActionDeleteResultTypeDef = TypedDict(
    "BatchScheduleActionDeleteResultTypeDef",
    {
        "ScheduleActions": List["ScheduleActionTypeDef"],
    },
)

BatchStartRequestRequestTypeDef = TypedDict(
    "BatchStartRequestRequestTypeDef",
    {
        "ChannelIds": NotRequired[Sequence[str]],
        "MultiplexIds": NotRequired[Sequence[str]],
    },
)

BatchStartResponseTypeDef = TypedDict(
    "BatchStartResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopRequestRequestTypeDef = TypedDict(
    "BatchStopRequestRequestTypeDef",
    {
        "ChannelIds": NotRequired[Sequence[str]],
        "MultiplexIds": NotRequired[Sequence[str]],
    },
)

BatchStopResponseTypeDef = TypedDict(
    "BatchStopResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSuccessfulResultModelTypeDef = TypedDict(
    "BatchSuccessfulResultModelTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "State": NotRequired[str],
    },
)

BatchUpdateScheduleRequestRequestTypeDef = TypedDict(
    "BatchUpdateScheduleRequestRequestTypeDef",
    {
        "ChannelId": str,
        "Creates": NotRequired["BatchScheduleActionCreateRequestTypeDef"],
        "Deletes": NotRequired["BatchScheduleActionDeleteRequestTypeDef"],
    },
)

BatchUpdateScheduleResponseTypeDef = TypedDict(
    "BatchUpdateScheduleResponseTypeDef",
    {
        "Creates": "BatchScheduleActionCreateResultTypeDef",
        "Deletes": "BatchScheduleActionDeleteResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlackoutSlateTypeDef = TypedDict(
    "BlackoutSlateTypeDef",
    {
        "BlackoutSlateImage": NotRequired["InputLocationTypeDef"],
        "NetworkEndBlackout": NotRequired[BlackoutSlateNetworkEndBlackoutType],
        "NetworkEndBlackoutImage": NotRequired["InputLocationTypeDef"],
        "NetworkId": NotRequired[str],
        "State": NotRequired[BlackoutSlateStateType],
    },
)

BurnInDestinationSettingsTypeDef = TypedDict(
    "BurnInDestinationSettingsTypeDef",
    {
        "Alignment": NotRequired[BurnInAlignmentType],
        "BackgroundColor": NotRequired[BurnInBackgroundColorType],
        "BackgroundOpacity": NotRequired[int],
        "Font": NotRequired["InputLocationTypeDef"],
        "FontColor": NotRequired[BurnInFontColorType],
        "FontOpacity": NotRequired[int],
        "FontResolution": NotRequired[int],
        "FontSize": NotRequired[str],
        "OutlineColor": NotRequired[BurnInOutlineColorType],
        "OutlineSize": NotRequired[int],
        "ShadowColor": NotRequired[BurnInShadowColorType],
        "ShadowOpacity": NotRequired[int],
        "ShadowXOffset": NotRequired[int],
        "ShadowYOffset": NotRequired[int],
        "TeletextGridControl": NotRequired[BurnInTeletextGridControlType],
        "XPosition": NotRequired[int],
        "YPosition": NotRequired[int],
    },
)

CancelInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "CancelInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

CaptionDescriptionTypeDef = TypedDict(
    "CaptionDescriptionTypeDef",
    {
        "CaptionSelectorName": str,
        "Name": str,
        "DestinationSettings": NotRequired["CaptionDestinationSettingsTypeDef"],
        "LanguageCode": NotRequired[str],
        "LanguageDescription": NotRequired[str],
    },
)

CaptionDestinationSettingsTypeDef = TypedDict(
    "CaptionDestinationSettingsTypeDef",
    {
        "AribDestinationSettings": NotRequired[Mapping[str, Any]],
        "BurnInDestinationSettings": NotRequired["BurnInDestinationSettingsTypeDef"],
        "DvbSubDestinationSettings": NotRequired["DvbSubDestinationSettingsTypeDef"],
        "EbuTtDDestinationSettings": NotRequired["EbuTtDDestinationSettingsTypeDef"],
        "EmbeddedDestinationSettings": NotRequired[Mapping[str, Any]],
        "EmbeddedPlusScte20DestinationSettings": NotRequired[Mapping[str, Any]],
        "RtmpCaptionInfoDestinationSettings": NotRequired[Mapping[str, Any]],
        "Scte20PlusEmbeddedDestinationSettings": NotRequired[Mapping[str, Any]],
        "Scte27DestinationSettings": NotRequired[Mapping[str, Any]],
        "SmpteTtDestinationSettings": NotRequired[Mapping[str, Any]],
        "TeletextDestinationSettings": NotRequired[Mapping[str, Any]],
        "TtmlDestinationSettings": NotRequired["TtmlDestinationSettingsTypeDef"],
        "WebvttDestinationSettings": NotRequired["WebvttDestinationSettingsTypeDef"],
    },
)

CaptionLanguageMappingTypeDef = TypedDict(
    "CaptionLanguageMappingTypeDef",
    {
        "CaptionChannel": int,
        "LanguageCode": str,
        "LanguageDescription": str,
    },
)

CaptionRectangleTypeDef = TypedDict(
    "CaptionRectangleTypeDef",
    {
        "Height": float,
        "LeftOffset": float,
        "TopOffset": float,
        "Width": float,
    },
)

CaptionSelectorSettingsTypeDef = TypedDict(
    "CaptionSelectorSettingsTypeDef",
    {
        "AncillarySourceSettings": NotRequired["AncillarySourceSettingsTypeDef"],
        "AribSourceSettings": NotRequired[Mapping[str, Any]],
        "DvbSubSourceSettings": NotRequired["DvbSubSourceSettingsTypeDef"],
        "EmbeddedSourceSettings": NotRequired["EmbeddedSourceSettingsTypeDef"],
        "Scte20SourceSettings": NotRequired["Scte20SourceSettingsTypeDef"],
        "Scte27SourceSettings": NotRequired["Scte27SourceSettingsTypeDef"],
        "TeletextSourceSettings": NotRequired["TeletextSourceSettingsTypeDef"],
    },
)

CaptionSelectorTypeDef = TypedDict(
    "CaptionSelectorTypeDef",
    {
        "Name": str,
        "LanguageCode": NotRequired[str],
        "SelectorSettings": NotRequired["CaptionSelectorSettingsTypeDef"],
    },
)

CdiInputSpecificationTypeDef = TypedDict(
    "CdiInputSpecificationTypeDef",
    {
        "Resolution": NotRequired[CdiInputResolutionType],
    },
)

ChannelEgressEndpointTypeDef = TypedDict(
    "ChannelEgressEndpointTypeDef",
    {
        "SourceIp": NotRequired[str],
    },
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CdiInputSpecification": NotRequired["CdiInputSpecificationTypeDef"],
        "ChannelClass": NotRequired[ChannelClassType],
        "Destinations": NotRequired[List["OutputDestinationTypeDef"]],
        "EgressEndpoints": NotRequired[List["ChannelEgressEndpointTypeDef"]],
        "Id": NotRequired[str],
        "InputAttachments": NotRequired[List["InputAttachmentTypeDef"]],
        "InputSpecification": NotRequired["InputSpecificationTypeDef"],
        "LogLevel": NotRequired[LogLevelType],
        "Name": NotRequired[str],
        "PipelinesRunningCount": NotRequired[int],
        "RoleArn": NotRequired[str],
        "State": NotRequired[ChannelStateType],
        "Tags": NotRequired[Dict[str, str]],
        "Vpc": NotRequired["VpcOutputSettingsDescriptionTypeDef"],
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": NotRequired[str],
        "CdiInputSpecification": NotRequired["CdiInputSpecificationTypeDef"],
        "ChannelClass": NotRequired[ChannelClassType],
        "Destinations": NotRequired[List["OutputDestinationTypeDef"]],
        "EgressEndpoints": NotRequired[List["ChannelEgressEndpointTypeDef"]],
        "EncoderSettings": NotRequired["EncoderSettingsTypeDef"],
        "Id": NotRequired[str],
        "InputAttachments": NotRequired[List["InputAttachmentTypeDef"]],
        "InputSpecification": NotRequired["InputSpecificationTypeDef"],
        "LogLevel": NotRequired[LogLevelType],
        "Name": NotRequired[str],
        "PipelineDetails": NotRequired[List["PipelineDetailTypeDef"]],
        "PipelinesRunningCount": NotRequired[int],
        "RoleArn": NotRequired[str],
        "State": NotRequired[ChannelStateType],
        "Tags": NotRequired[Dict[str, str]],
        "Vpc": NotRequired["VpcOutputSettingsDescriptionTypeDef"],
    },
)

ClaimDeviceRequestRequestTypeDef = TypedDict(
    "ClaimDeviceRequestRequestTypeDef",
    {
        "Id": NotRequired[str],
    },
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "CdiInputSpecification": NotRequired["CdiInputSpecificationTypeDef"],
        "ChannelClass": NotRequired[ChannelClassType],
        "Destinations": NotRequired[Sequence["OutputDestinationTypeDef"]],
        "EncoderSettings": NotRequired["EncoderSettingsTypeDef"],
        "InputAttachments": NotRequired[Sequence["InputAttachmentTypeDef"]],
        "InputSpecification": NotRequired["InputSpecificationTypeDef"],
        "LogLevel": NotRequired[LogLevelType],
        "Name": NotRequired[str],
        "RequestId": NotRequired[str],
        "Reserved": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Vpc": NotRequired["VpcOutputSettingsTypeDef"],
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInputRequestRequestTypeDef = TypedDict(
    "CreateInputRequestRequestTypeDef",
    {
        "Destinations": NotRequired[Sequence["InputDestinationRequestTypeDef"]],
        "InputDevices": NotRequired[Sequence["InputDeviceSettingsTypeDef"]],
        "InputSecurityGroups": NotRequired[Sequence[str]],
        "MediaConnectFlows": NotRequired[Sequence["MediaConnectFlowRequestTypeDef"]],
        "Name": NotRequired[str],
        "RequestId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Sources": NotRequired[Sequence["InputSourceRequestTypeDef"]],
        "Tags": NotRequired[Mapping[str, str]],
        "Type": NotRequired[InputTypeType],
        "Vpc": NotRequired["InputVpcRequestTypeDef"],
    },
)

CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef",
    {
        "Input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "CreateInputSecurityGroupRequestRequestTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
        "WhitelistRules": NotRequired[Sequence["InputWhitelistRuleCidrTypeDef"]],
    },
)

CreateInputSecurityGroupResponseTypeDef = TypedDict(
    "CreateInputSecurityGroupResponseTypeDef",
    {
        "SecurityGroup": "InputSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultiplexProgramRequestRequestTypeDef = TypedDict(
    "CreateMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "ProgramName": str,
        "RequestId": str,
    },
)

CreateMultiplexProgramResponseTypeDef = TypedDict(
    "CreateMultiplexProgramResponseTypeDef",
    {
        "MultiplexProgram": "MultiplexProgramTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultiplexRequestRequestTypeDef = TypedDict(
    "CreateMultiplexRequestRequestTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "RequestId": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateMultiplexResponseTypeDef = TypedDict(
    "CreateMultiplexResponseTypeDef",
    {
        "Multiplex": "MultiplexTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePartnerInputRequestRequestTypeDef = TypedDict(
    "CreatePartnerInputRequestRequestTypeDef",
    {
        "InputId": str,
        "RequestId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePartnerInputResponseTypeDef = TypedDict(
    "CreatePartnerInputResponseTypeDef",
    {
        "Input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

DeleteChannelResponseTypeDef = TypedDict(
    "DeleteChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInputRequestRequestTypeDef = TypedDict(
    "DeleteInputRequestRequestTypeDef",
    {
        "InputId": str,
    },
)

DeleteInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "DeleteInputSecurityGroupRequestRequestTypeDef",
    {
        "InputSecurityGroupId": str,
    },
)

DeleteMultiplexProgramRequestRequestTypeDef = TypedDict(
    "DeleteMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
    },
)

DeleteMultiplexProgramResponseTypeDef = TypedDict(
    "DeleteMultiplexProgramResponseTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMultiplexRequestRequestTypeDef = TypedDict(
    "DeleteMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

DeleteMultiplexResponseTypeDef = TypedDict(
    "DeleteMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReservationRequestRequestTypeDef = TypedDict(
    "DeleteReservationRequestRequestTypeDef",
    {
        "ReservationId": str,
    },
)

DeleteReservationResponseTypeDef = TypedDict(
    "DeleteReservationResponseTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationStateType,
        "Tags": Dict[str, str],
        "UsagePrice": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputDeviceRequestRequestTypeDef = TypedDict(
    "DescribeInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

DescribeInputDeviceResponseTypeDef = TypedDict(
    "DescribeInputDeviceResponseTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionStateType,
        "DeviceSettingsSyncState": DeviceSettingsSyncStateType,
        "DeviceUpdateStatus": DeviceUpdateStatusType,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputDeviceThumbnailRequestRequestTypeDef = TypedDict(
    "DescribeInputDeviceThumbnailRequestRequestTypeDef",
    {
        "InputDeviceId": str,
        "Accept": Literal["image/jpeg"],
    },
)

DescribeInputDeviceThumbnailResponseTypeDef = TypedDict(
    "DescribeInputDeviceThumbnailResponseTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": Literal["image/jpeg"],
        "ContentLength": int,
        "ETag": str,
        "LastModified": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputRequestRequestTypeDef = TypedDict(
    "DescribeInputRequestRequestTypeDef",
    {
        "InputId": str,
    },
)

DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "Arn": str,
        "AttachedChannels": List[str],
        "Destinations": List["InputDestinationTypeDef"],
        "Id": str,
        "InputClass": InputClassType,
        "InputDevices": List["InputDeviceSettingsTypeDef"],
        "InputPartnerIds": List[str],
        "InputSourceType": InputSourceTypeType,
        "MediaConnectFlows": List["MediaConnectFlowTypeDef"],
        "Name": str,
        "RoleArn": str,
        "SecurityGroups": List[str],
        "Sources": List["InputSourceTypeDef"],
        "State": InputStateType,
        "Tags": Dict[str, str],
        "Type": InputTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "DescribeInputSecurityGroupRequestRequestTypeDef",
    {
        "InputSecurityGroupId": str,
    },
)

DescribeInputSecurityGroupResponseTypeDef = TypedDict(
    "DescribeInputSecurityGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Inputs": List[str],
        "State": InputSecurityGroupStateType,
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMultiplexProgramRequestRequestTypeDef = TypedDict(
    "DescribeMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
    },
)

DescribeMultiplexProgramResponseTypeDef = TypedDict(
    "DescribeMultiplexProgramResponseTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMultiplexRequestRequestTypeDef = TypedDict(
    "DescribeMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

DescribeMultiplexResponseTypeDef = TypedDict(
    "DescribeMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOfferingRequestRequestTypeDef = TypedDict(
    "DescribeOfferingRequestRequestTypeDef",
    {
        "OfferingId": str,
    },
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Arn": str,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "FixedPrice": float,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "UsagePrice": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservationRequestRequestTypeDef = TypedDict(
    "DescribeReservationRequestRequestTypeDef",
    {
        "ReservationId": str,
    },
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationStateType,
        "Tags": Dict[str, str],
        "UsagePrice": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduleRequestRequestTypeDef = TypedDict(
    "DescribeScheduleRequestRequestTypeDef",
    {
        "ChannelId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "NextToken": str,
        "ScheduleActions": List["ScheduleActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DvbNitSettingsTypeDef = TypedDict(
    "DvbNitSettingsTypeDef",
    {
        "NetworkId": int,
        "NetworkName": str,
        "RepInterval": NotRequired[int],
    },
)

DvbSdtSettingsTypeDef = TypedDict(
    "DvbSdtSettingsTypeDef",
    {
        "OutputSdt": NotRequired[DvbSdtOutputSdtType],
        "RepInterval": NotRequired[int],
        "ServiceName": NotRequired[str],
        "ServiceProviderName": NotRequired[str],
    },
)

DvbSubDestinationSettingsTypeDef = TypedDict(
    "DvbSubDestinationSettingsTypeDef",
    {
        "Alignment": NotRequired[DvbSubDestinationAlignmentType],
        "BackgroundColor": NotRequired[DvbSubDestinationBackgroundColorType],
        "BackgroundOpacity": NotRequired[int],
        "Font": NotRequired["InputLocationTypeDef"],
        "FontColor": NotRequired[DvbSubDestinationFontColorType],
        "FontOpacity": NotRequired[int],
        "FontResolution": NotRequired[int],
        "FontSize": NotRequired[str],
        "OutlineColor": NotRequired[DvbSubDestinationOutlineColorType],
        "OutlineSize": NotRequired[int],
        "ShadowColor": NotRequired[DvbSubDestinationShadowColorType],
        "ShadowOpacity": NotRequired[int],
        "ShadowXOffset": NotRequired[int],
        "ShadowYOffset": NotRequired[int],
        "TeletextGridControl": NotRequired[DvbSubDestinationTeletextGridControlType],
        "XPosition": NotRequired[int],
        "YPosition": NotRequired[int],
    },
)

DvbSubSourceSettingsTypeDef = TypedDict(
    "DvbSubSourceSettingsTypeDef",
    {
        "OcrLanguage": NotRequired[DvbSubOcrLanguageType],
        "Pid": NotRequired[int],
    },
)

DvbTdtSettingsTypeDef = TypedDict(
    "DvbTdtSettingsTypeDef",
    {
        "RepInterval": NotRequired[int],
    },
)

Eac3SettingsTypeDef = TypedDict(
    "Eac3SettingsTypeDef",
    {
        "AttenuationControl": NotRequired[Eac3AttenuationControlType],
        "Bitrate": NotRequired[float],
        "BitstreamMode": NotRequired[Eac3BitstreamModeType],
        "CodingMode": NotRequired[Eac3CodingModeType],
        "DcFilter": NotRequired[Eac3DcFilterType],
        "Dialnorm": NotRequired[int],
        "DrcLine": NotRequired[Eac3DrcLineType],
        "DrcRf": NotRequired[Eac3DrcRfType],
        "LfeControl": NotRequired[Eac3LfeControlType],
        "LfeFilter": NotRequired[Eac3LfeFilterType],
        "LoRoCenterMixLevel": NotRequired[float],
        "LoRoSurroundMixLevel": NotRequired[float],
        "LtRtCenterMixLevel": NotRequired[float],
        "LtRtSurroundMixLevel": NotRequired[float],
        "MetadataControl": NotRequired[Eac3MetadataControlType],
        "PassthroughControl": NotRequired[Eac3PassthroughControlType],
        "PhaseControl": NotRequired[Eac3PhaseControlType],
        "StereoDownmix": NotRequired[Eac3StereoDownmixType],
        "SurroundExMode": NotRequired[Eac3SurroundExModeType],
        "SurroundMode": NotRequired[Eac3SurroundModeType],
    },
)

EbuTtDDestinationSettingsTypeDef = TypedDict(
    "EbuTtDDestinationSettingsTypeDef",
    {
        "CopyrightHolder": NotRequired[str],
        "FillLineGap": NotRequired[EbuTtDFillLineGapControlType],
        "FontFamily": NotRequired[str],
        "StyleControl": NotRequired[EbuTtDDestinationStyleControlType],
    },
)

EmbeddedSourceSettingsTypeDef = TypedDict(
    "EmbeddedSourceSettingsTypeDef",
    {
        "Convert608To708": NotRequired[EmbeddedConvert608To708Type],
        "Scte20Detection": NotRequired[EmbeddedScte20DetectionType],
        "Source608ChannelNumber": NotRequired[int],
        "Source608TrackNumber": NotRequired[int],
    },
)

EncoderSettingsTypeDef = TypedDict(
    "EncoderSettingsTypeDef",
    {
        "AudioDescriptions": Sequence["AudioDescriptionTypeDef"],
        "OutputGroups": Sequence["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "VideoDescriptions": Sequence["VideoDescriptionTypeDef"],
        "AvailBlanking": NotRequired["AvailBlankingTypeDef"],
        "AvailConfiguration": NotRequired["AvailConfigurationTypeDef"],
        "BlackoutSlate": NotRequired["BlackoutSlateTypeDef"],
        "CaptionDescriptions": NotRequired[Sequence["CaptionDescriptionTypeDef"]],
        "FeatureActivations": NotRequired["FeatureActivationsTypeDef"],
        "GlobalConfiguration": NotRequired["GlobalConfigurationTypeDef"],
        "MotionGraphicsConfiguration": NotRequired["MotionGraphicsConfigurationTypeDef"],
        "NielsenConfiguration": NotRequired["NielsenConfigurationTypeDef"],
    },
)

FailoverConditionSettingsTypeDef = TypedDict(
    "FailoverConditionSettingsTypeDef",
    {
        "AudioSilenceSettings": NotRequired["AudioSilenceFailoverSettingsTypeDef"],
        "InputLossSettings": NotRequired["InputLossFailoverSettingsTypeDef"],
        "VideoBlackSettings": NotRequired["VideoBlackFailoverSettingsTypeDef"],
    },
)

FailoverConditionTypeDef = TypedDict(
    "FailoverConditionTypeDef",
    {
        "FailoverConditionSettings": NotRequired["FailoverConditionSettingsTypeDef"],
    },
)

FeatureActivationsTypeDef = TypedDict(
    "FeatureActivationsTypeDef",
    {
        "InputPrepareScheduleActions": NotRequired[
            FeatureActivationsInputPrepareScheduleActionsType
        ],
    },
)

FecOutputSettingsTypeDef = TypedDict(
    "FecOutputSettingsTypeDef",
    {
        "ColumnDepth": NotRequired[int],
        "IncludeFec": NotRequired[FecOutputIncludeFecType],
        "RowLength": NotRequired[int],
    },
)

FixedModeScheduleActionStartSettingsTypeDef = TypedDict(
    "FixedModeScheduleActionStartSettingsTypeDef",
    {
        "Time": str,
    },
)

Fmp4HlsSettingsTypeDef = TypedDict(
    "Fmp4HlsSettingsTypeDef",
    {
        "AudioRenditionSets": NotRequired[str],
        "NielsenId3Behavior": NotRequired[Fmp4NielsenId3BehaviorType],
        "TimedMetadataBehavior": NotRequired[Fmp4TimedMetadataBehaviorType],
    },
)

FollowModeScheduleActionStartSettingsTypeDef = TypedDict(
    "FollowModeScheduleActionStartSettingsTypeDef",
    {
        "FollowPoint": FollowPointType,
        "ReferenceActionName": str,
    },
)

FrameCaptureCdnSettingsTypeDef = TypedDict(
    "FrameCaptureCdnSettingsTypeDef",
    {
        "FrameCaptureS3Settings": NotRequired["FrameCaptureS3SettingsTypeDef"],
    },
)

FrameCaptureGroupSettingsTypeDef = TypedDict(
    "FrameCaptureGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
        "FrameCaptureCdnSettings": NotRequired["FrameCaptureCdnSettingsTypeDef"],
    },
)

FrameCaptureOutputSettingsTypeDef = TypedDict(
    "FrameCaptureOutputSettingsTypeDef",
    {
        "NameModifier": NotRequired[str],
    },
)

FrameCaptureS3SettingsTypeDef = TypedDict(
    "FrameCaptureS3SettingsTypeDef",
    {
        "CannedAcl": NotRequired[S3CannedAclType],
    },
)

FrameCaptureSettingsTypeDef = TypedDict(
    "FrameCaptureSettingsTypeDef",
    {
        "CaptureInterval": NotRequired[int],
        "CaptureIntervalUnits": NotRequired[FrameCaptureIntervalUnitType],
    },
)

GlobalConfigurationTypeDef = TypedDict(
    "GlobalConfigurationTypeDef",
    {
        "InitialAudioGain": NotRequired[int],
        "InputEndAction": NotRequired[GlobalConfigurationInputEndActionType],
        "InputLossBehavior": NotRequired["InputLossBehaviorTypeDef"],
        "OutputLockingMode": NotRequired[GlobalConfigurationOutputLockingModeType],
        "OutputTimingSource": NotRequired[GlobalConfigurationOutputTimingSourceType],
        "SupportLowFramerateInputs": NotRequired[GlobalConfigurationLowFramerateInputsType],
    },
)

H264ColorSpaceSettingsTypeDef = TypedDict(
    "H264ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": NotRequired[Mapping[str, Any]],
        "Rec601Settings": NotRequired[Mapping[str, Any]],
        "Rec709Settings": NotRequired[Mapping[str, Any]],
    },
)

H264FilterSettingsTypeDef = TypedDict(
    "H264FilterSettingsTypeDef",
    {
        "TemporalFilterSettings": NotRequired["TemporalFilterSettingsTypeDef"],
    },
)

H264SettingsTypeDef = TypedDict(
    "H264SettingsTypeDef",
    {
        "AdaptiveQuantization": NotRequired[H264AdaptiveQuantizationType],
        "AfdSignaling": NotRequired[AfdSignalingType],
        "Bitrate": NotRequired[int],
        "BufFillPct": NotRequired[int],
        "BufSize": NotRequired[int],
        "ColorMetadata": NotRequired[H264ColorMetadataType],
        "ColorSpaceSettings": NotRequired["H264ColorSpaceSettingsTypeDef"],
        "EntropyEncoding": NotRequired[H264EntropyEncodingType],
        "FilterSettings": NotRequired["H264FilterSettingsTypeDef"],
        "FixedAfd": NotRequired[FixedAfdType],
        "FlickerAq": NotRequired[H264FlickerAqType],
        "ForceFieldPictures": NotRequired[H264ForceFieldPicturesType],
        "FramerateControl": NotRequired[H264FramerateControlType],
        "FramerateDenominator": NotRequired[int],
        "FramerateNumerator": NotRequired[int],
        "GopBReference": NotRequired[H264GopBReferenceType],
        "GopClosedCadence": NotRequired[int],
        "GopNumBFrames": NotRequired[int],
        "GopSize": NotRequired[float],
        "GopSizeUnits": NotRequired[H264GopSizeUnitsType],
        "Level": NotRequired[H264LevelType],
        "LookAheadRateControl": NotRequired[H264LookAheadRateControlType],
        "MaxBitrate": NotRequired[int],
        "MinIInterval": NotRequired[int],
        "NumRefFrames": NotRequired[int],
        "ParControl": NotRequired[H264ParControlType],
        "ParDenominator": NotRequired[int],
        "ParNumerator": NotRequired[int],
        "Profile": NotRequired[H264ProfileType],
        "QualityLevel": NotRequired[H264QualityLevelType],
        "QvbrQualityLevel": NotRequired[int],
        "RateControlMode": NotRequired[H264RateControlModeType],
        "ScanType": NotRequired[H264ScanTypeType],
        "SceneChangeDetect": NotRequired[H264SceneChangeDetectType],
        "Slices": NotRequired[int],
        "Softness": NotRequired[int],
        "SpatialAq": NotRequired[H264SpatialAqType],
        "SubgopLength": NotRequired[H264SubGopLengthType],
        "Syntax": NotRequired[H264SyntaxType],
        "TemporalAq": NotRequired[H264TemporalAqType],
        "TimecodeInsertion": NotRequired[H264TimecodeInsertionBehaviorType],
    },
)

H265ColorSpaceSettingsTypeDef = TypedDict(
    "H265ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": NotRequired[Mapping[str, Any]],
        "Hdr10Settings": NotRequired["Hdr10SettingsTypeDef"],
        "Rec601Settings": NotRequired[Mapping[str, Any]],
        "Rec709Settings": NotRequired[Mapping[str, Any]],
    },
)

H265FilterSettingsTypeDef = TypedDict(
    "H265FilterSettingsTypeDef",
    {
        "TemporalFilterSettings": NotRequired["TemporalFilterSettingsTypeDef"],
    },
)

H265SettingsTypeDef = TypedDict(
    "H265SettingsTypeDef",
    {
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "AdaptiveQuantization": NotRequired[H265AdaptiveQuantizationType],
        "AfdSignaling": NotRequired[AfdSignalingType],
        "AlternativeTransferFunction": NotRequired[H265AlternativeTransferFunctionType],
        "Bitrate": NotRequired[int],
        "BufSize": NotRequired[int],
        "ColorMetadata": NotRequired[H265ColorMetadataType],
        "ColorSpaceSettings": NotRequired["H265ColorSpaceSettingsTypeDef"],
        "FilterSettings": NotRequired["H265FilterSettingsTypeDef"],
        "FixedAfd": NotRequired[FixedAfdType],
        "FlickerAq": NotRequired[H265FlickerAqType],
        "GopClosedCadence": NotRequired[int],
        "GopSize": NotRequired[float],
        "GopSizeUnits": NotRequired[H265GopSizeUnitsType],
        "Level": NotRequired[H265LevelType],
        "LookAheadRateControl": NotRequired[H265LookAheadRateControlType],
        "MaxBitrate": NotRequired[int],
        "MinIInterval": NotRequired[int],
        "ParDenominator": NotRequired[int],
        "ParNumerator": NotRequired[int],
        "Profile": NotRequired[H265ProfileType],
        "QvbrQualityLevel": NotRequired[int],
        "RateControlMode": NotRequired[H265RateControlModeType],
        "ScanType": NotRequired[H265ScanTypeType],
        "SceneChangeDetect": NotRequired[H265SceneChangeDetectType],
        "Slices": NotRequired[int],
        "Tier": NotRequired[H265TierType],
        "TimecodeInsertion": NotRequired[H265TimecodeInsertionBehaviorType],
    },
)

Hdr10SettingsTypeDef = TypedDict(
    "Hdr10SettingsTypeDef",
    {
        "MaxCll": NotRequired[int],
        "MaxFall": NotRequired[int],
    },
)

HlsAkamaiSettingsTypeDef = TypedDict(
    "HlsAkamaiSettingsTypeDef",
    {
        "ConnectionRetryInterval": NotRequired[int],
        "FilecacheDuration": NotRequired[int],
        "HttpTransferMode": NotRequired[HlsAkamaiHttpTransferModeType],
        "NumRetries": NotRequired[int],
        "RestartDelay": NotRequired[int],
        "Salt": NotRequired[str],
        "Token": NotRequired[str],
    },
)

HlsBasicPutSettingsTypeDef = TypedDict(
    "HlsBasicPutSettingsTypeDef",
    {
        "ConnectionRetryInterval": NotRequired[int],
        "FilecacheDuration": NotRequired[int],
        "NumRetries": NotRequired[int],
        "RestartDelay": NotRequired[int],
    },
)

HlsCdnSettingsTypeDef = TypedDict(
    "HlsCdnSettingsTypeDef",
    {
        "HlsAkamaiSettings": NotRequired["HlsAkamaiSettingsTypeDef"],
        "HlsBasicPutSettings": NotRequired["HlsBasicPutSettingsTypeDef"],
        "HlsMediaStoreSettings": NotRequired["HlsMediaStoreSettingsTypeDef"],
        "HlsS3Settings": NotRequired["HlsS3SettingsTypeDef"],
        "HlsWebdavSettings": NotRequired["HlsWebdavSettingsTypeDef"],
    },
)

HlsGroupSettingsTypeDef = TypedDict(
    "HlsGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
        "AdMarkers": NotRequired[Sequence[HlsAdMarkersType]],
        "BaseUrlContent": NotRequired[str],
        "BaseUrlContent1": NotRequired[str],
        "BaseUrlManifest": NotRequired[str],
        "BaseUrlManifest1": NotRequired[str],
        "CaptionLanguageMappings": NotRequired[Sequence["CaptionLanguageMappingTypeDef"]],
        "CaptionLanguageSetting": NotRequired[HlsCaptionLanguageSettingType],
        "ClientCache": NotRequired[HlsClientCacheType],
        "CodecSpecification": NotRequired[HlsCodecSpecificationType],
        "ConstantIv": NotRequired[str],
        "DirectoryStructure": NotRequired[HlsDirectoryStructureType],
        "DiscontinuityTags": NotRequired[HlsDiscontinuityTagsType],
        "EncryptionType": NotRequired[HlsEncryptionTypeType],
        "HlsCdnSettings": NotRequired["HlsCdnSettingsTypeDef"],
        "HlsId3SegmentTagging": NotRequired[HlsId3SegmentTaggingStateType],
        "IFrameOnlyPlaylists": NotRequired[IFrameOnlyPlaylistTypeType],
        "IncompleteSegmentBehavior": NotRequired[HlsIncompleteSegmentBehaviorType],
        "IndexNSegments": NotRequired[int],
        "InputLossAction": NotRequired[InputLossActionForHlsOutType],
        "IvInManifest": NotRequired[HlsIvInManifestType],
        "IvSource": NotRequired[HlsIvSourceType],
        "KeepSegments": NotRequired[int],
        "KeyFormat": NotRequired[str],
        "KeyFormatVersions": NotRequired[str],
        "KeyProviderSettings": NotRequired["KeyProviderSettingsTypeDef"],
        "ManifestCompression": NotRequired[HlsManifestCompressionType],
        "ManifestDurationFormat": NotRequired[HlsManifestDurationFormatType],
        "MinSegmentLength": NotRequired[int],
        "Mode": NotRequired[HlsModeType],
        "OutputSelection": NotRequired[HlsOutputSelectionType],
        "ProgramDateTime": NotRequired[HlsProgramDateTimeType],
        "ProgramDateTimeClock": NotRequired[HlsProgramDateTimeClockType],
        "ProgramDateTimePeriod": NotRequired[int],
        "RedundantManifest": NotRequired[HlsRedundantManifestType],
        "SegmentLength": NotRequired[int],
        "SegmentationMode": NotRequired[HlsSegmentationModeType],
        "SegmentsPerSubdirectory": NotRequired[int],
        "StreamInfResolution": NotRequired[HlsStreamInfResolutionType],
        "TimedMetadataId3Frame": NotRequired[HlsTimedMetadataId3FrameType],
        "TimedMetadataId3Period": NotRequired[int],
        "TimestampDeltaMilliseconds": NotRequired[int],
        "TsFileMode": NotRequired[HlsTsFileModeType],
    },
)

HlsId3SegmentTaggingScheduleActionSettingsTypeDef = TypedDict(
    "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
    {
        "Tag": str,
    },
)

HlsInputSettingsTypeDef = TypedDict(
    "HlsInputSettingsTypeDef",
    {
        "Bandwidth": NotRequired[int],
        "BufferSegments": NotRequired[int],
        "Retries": NotRequired[int],
        "RetryInterval": NotRequired[int],
        "Scte35Source": NotRequired[HlsScte35SourceTypeType],
    },
)

HlsMediaStoreSettingsTypeDef = TypedDict(
    "HlsMediaStoreSettingsTypeDef",
    {
        "ConnectionRetryInterval": NotRequired[int],
        "FilecacheDuration": NotRequired[int],
        "MediaStoreStorageClass": NotRequired[Literal["TEMPORAL"]],
        "NumRetries": NotRequired[int],
        "RestartDelay": NotRequired[int],
    },
)

HlsOutputSettingsTypeDef = TypedDict(
    "HlsOutputSettingsTypeDef",
    {
        "HlsSettings": "HlsSettingsTypeDef",
        "H265PackagingType": NotRequired[HlsH265PackagingTypeType],
        "NameModifier": NotRequired[str],
        "SegmentModifier": NotRequired[str],
    },
)

HlsS3SettingsTypeDef = TypedDict(
    "HlsS3SettingsTypeDef",
    {
        "CannedAcl": NotRequired[S3CannedAclType],
    },
)

HlsSettingsTypeDef = TypedDict(
    "HlsSettingsTypeDef",
    {
        "AudioOnlyHlsSettings": NotRequired["AudioOnlyHlsSettingsTypeDef"],
        "Fmp4HlsSettings": NotRequired["Fmp4HlsSettingsTypeDef"],
        "FrameCaptureHlsSettings": NotRequired[Mapping[str, Any]],
        "StandardHlsSettings": NotRequired["StandardHlsSettingsTypeDef"],
    },
)

HlsTimedMetadataScheduleActionSettingsTypeDef = TypedDict(
    "HlsTimedMetadataScheduleActionSettingsTypeDef",
    {
        "Id3": str,
    },
)

HlsWebdavSettingsTypeDef = TypedDict(
    "HlsWebdavSettingsTypeDef",
    {
        "ConnectionRetryInterval": NotRequired[int],
        "FilecacheDuration": NotRequired[int],
        "HttpTransferMode": NotRequired[HlsWebdavHttpTransferModeType],
        "NumRetries": NotRequired[int],
        "RestartDelay": NotRequired[int],
    },
)

InputAttachmentTypeDef = TypedDict(
    "InputAttachmentTypeDef",
    {
        "AutomaticInputFailoverSettings": NotRequired["AutomaticInputFailoverSettingsTypeDef"],
        "InputAttachmentName": NotRequired[str],
        "InputId": NotRequired[str],
        "InputSettings": NotRequired["InputSettingsTypeDef"],
    },
)

InputChannelLevelTypeDef = TypedDict(
    "InputChannelLevelTypeDef",
    {
        "Gain": int,
        "InputChannel": int,
    },
)

InputClippingSettingsTypeDef = TypedDict(
    "InputClippingSettingsTypeDef",
    {
        "InputTimecodeSource": InputTimecodeSourceType,
        "StartTimecode": NotRequired["StartTimecodeTypeDef"],
        "StopTimecode": NotRequired["StopTimecodeTypeDef"],
    },
)

InputDestinationRequestTypeDef = TypedDict(
    "InputDestinationRequestTypeDef",
    {
        "StreamName": NotRequired[str],
    },
)

InputDestinationTypeDef = TypedDict(
    "InputDestinationTypeDef",
    {
        "Ip": NotRequired[str],
        "Port": NotRequired[str],
        "Url": NotRequired[str],
        "Vpc": NotRequired["InputDestinationVpcTypeDef"],
    },
)

InputDestinationVpcTypeDef = TypedDict(
    "InputDestinationVpcTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
    },
)

InputDeviceConfigurableSettingsTypeDef = TypedDict(
    "InputDeviceConfigurableSettingsTypeDef",
    {
        "ConfiguredInput": NotRequired[InputDeviceConfiguredInputType],
        "MaxBitrate": NotRequired[int],
    },
)

InputDeviceHdSettingsTypeDef = TypedDict(
    "InputDeviceHdSettingsTypeDef",
    {
        "ActiveInput": NotRequired[InputDeviceActiveInputType],
        "ConfiguredInput": NotRequired[InputDeviceConfiguredInputType],
        "DeviceState": NotRequired[InputDeviceStateType],
        "Framerate": NotRequired[float],
        "Height": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "ScanType": NotRequired[InputDeviceScanTypeType],
        "Width": NotRequired[int],
    },
)

InputDeviceNetworkSettingsTypeDef = TypedDict(
    "InputDeviceNetworkSettingsTypeDef",
    {
        "DnsAddresses": NotRequired[List[str]],
        "Gateway": NotRequired[str],
        "IpAddress": NotRequired[str],
        "IpScheme": NotRequired[InputDeviceIpSchemeType],
        "SubnetMask": NotRequired[str],
    },
)

InputDeviceRequestTypeDef = TypedDict(
    "InputDeviceRequestTypeDef",
    {
        "Id": NotRequired[str],
    },
)

InputDeviceSettingsTypeDef = TypedDict(
    "InputDeviceSettingsTypeDef",
    {
        "Id": NotRequired[str],
    },
)

InputDeviceSummaryTypeDef = TypedDict(
    "InputDeviceSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectionState": NotRequired[InputDeviceConnectionStateType],
        "DeviceSettingsSyncState": NotRequired[DeviceSettingsSyncStateType],
        "DeviceUpdateStatus": NotRequired[DeviceUpdateStatusType],
        "HdDeviceSettings": NotRequired["InputDeviceHdSettingsTypeDef"],
        "Id": NotRequired[str],
        "MacAddress": NotRequired[str],
        "Name": NotRequired[str],
        "NetworkSettings": NotRequired["InputDeviceNetworkSettingsTypeDef"],
        "SerialNumber": NotRequired[str],
        "Type": NotRequired[Literal["HD"]],
        "UhdDeviceSettings": NotRequired["InputDeviceUhdSettingsTypeDef"],
    },
)

InputDeviceUhdSettingsTypeDef = TypedDict(
    "InputDeviceUhdSettingsTypeDef",
    {
        "ActiveInput": NotRequired[InputDeviceActiveInputType],
        "ConfiguredInput": NotRequired[InputDeviceConfiguredInputType],
        "DeviceState": NotRequired[InputDeviceStateType],
        "Framerate": NotRequired[float],
        "Height": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "ScanType": NotRequired[InputDeviceScanTypeType],
        "Width": NotRequired[int],
    },
)

InputLocationTypeDef = TypedDict(
    "InputLocationTypeDef",
    {
        "Uri": str,
        "PasswordParam": NotRequired[str],
        "Username": NotRequired[str],
    },
)

InputLossBehaviorTypeDef = TypedDict(
    "InputLossBehaviorTypeDef",
    {
        "BlackFrameMsec": NotRequired[int],
        "InputLossImageColor": NotRequired[str],
        "InputLossImageSlate": NotRequired["InputLocationTypeDef"],
        "InputLossImageType": NotRequired[InputLossImageTypeType],
        "RepeatFrameMsec": NotRequired[int],
    },
)

InputLossFailoverSettingsTypeDef = TypedDict(
    "InputLossFailoverSettingsTypeDef",
    {
        "InputLossThresholdMsec": NotRequired[int],
    },
)

InputPrepareScheduleActionSettingsTypeDef = TypedDict(
    "InputPrepareScheduleActionSettingsTypeDef",
    {
        "InputAttachmentNameReference": NotRequired[str],
        "InputClippingSettings": NotRequired["InputClippingSettingsTypeDef"],
        "UrlPath": NotRequired[Sequence[str]],
    },
)

InputSecurityGroupTypeDef = TypedDict(
    "InputSecurityGroupTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Inputs": NotRequired[List[str]],
        "State": NotRequired[InputSecurityGroupStateType],
        "Tags": NotRequired[Dict[str, str]],
        "WhitelistRules": NotRequired[List["InputWhitelistRuleTypeDef"]],
    },
)

InputSettingsTypeDef = TypedDict(
    "InputSettingsTypeDef",
    {
        "AudioSelectors": NotRequired[Sequence["AudioSelectorTypeDef"]],
        "CaptionSelectors": NotRequired[Sequence["CaptionSelectorTypeDef"]],
        "DeblockFilter": NotRequired[InputDeblockFilterType],
        "DenoiseFilter": NotRequired[InputDenoiseFilterType],
        "FilterStrength": NotRequired[int],
        "InputFilter": NotRequired[InputFilterType],
        "NetworkInputSettings": NotRequired["NetworkInputSettingsTypeDef"],
        "Scte35Pid": NotRequired[int],
        "Smpte2038DataPreference": NotRequired[Smpte2038DataPreferenceType],
        "SourceEndBehavior": NotRequired[InputSourceEndBehaviorType],
        "VideoSelector": NotRequired["VideoSelectorTypeDef"],
    },
)

InputSourceRequestTypeDef = TypedDict(
    "InputSourceRequestTypeDef",
    {
        "PasswordParam": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
    },
)

InputSourceTypeDef = TypedDict(
    "InputSourceTypeDef",
    {
        "PasswordParam": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
    },
)

InputSpecificationTypeDef = TypedDict(
    "InputSpecificationTypeDef",
    {
        "Codec": NotRequired[InputCodecType],
        "MaximumBitrate": NotRequired[InputMaximumBitrateType],
        "Resolution": NotRequired[InputResolutionType],
    },
)

InputSwitchScheduleActionSettingsTypeDef = TypedDict(
    "InputSwitchScheduleActionSettingsTypeDef",
    {
        "InputAttachmentNameReference": str,
        "InputClippingSettings": NotRequired["InputClippingSettingsTypeDef"],
        "UrlPath": NotRequired[Sequence[str]],
    },
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "Arn": NotRequired[str],
        "AttachedChannels": NotRequired[List[str]],
        "Destinations": NotRequired[List["InputDestinationTypeDef"]],
        "Id": NotRequired[str],
        "InputClass": NotRequired[InputClassType],
        "InputDevices": NotRequired[List["InputDeviceSettingsTypeDef"]],
        "InputPartnerIds": NotRequired[List[str]],
        "InputSourceType": NotRequired[InputSourceTypeType],
        "MediaConnectFlows": NotRequired[List["MediaConnectFlowTypeDef"]],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "Sources": NotRequired[List["InputSourceTypeDef"]],
        "State": NotRequired[InputStateType],
        "Tags": NotRequired[Dict[str, str]],
        "Type": NotRequired[InputTypeType],
    },
)

InputVpcRequestTypeDef = TypedDict(
    "InputVpcRequestTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

InputWhitelistRuleCidrTypeDef = TypedDict(
    "InputWhitelistRuleCidrTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)

InputWhitelistRuleTypeDef = TypedDict(
    "InputWhitelistRuleTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)

KeyProviderSettingsTypeDef = TypedDict(
    "KeyProviderSettingsTypeDef",
    {
        "StaticKeySettings": NotRequired["StaticKeySettingsTypeDef"],
    },
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputDeviceTransfersRequestRequestTypeDef = TypedDict(
    "ListInputDeviceTransfersRequestRequestTypeDef",
    {
        "TransferType": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInputDeviceTransfersResponseTypeDef = TypedDict(
    "ListInputDeviceTransfersResponseTypeDef",
    {
        "InputDeviceTransfers": List["TransferringInputDeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputDevicesRequestRequestTypeDef = TypedDict(
    "ListInputDevicesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInputDevicesResponseTypeDef = TypedDict(
    "ListInputDevicesResponseTypeDef",
    {
        "InputDevices": List["InputDeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputSecurityGroupsRequestRequestTypeDef = TypedDict(
    "ListInputSecurityGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInputSecurityGroupsResponseTypeDef = TypedDict(
    "ListInputSecurityGroupsResponseTypeDef",
    {
        "InputSecurityGroups": List["InputSecurityGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputsRequestRequestTypeDef = TypedDict(
    "ListInputsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef",
    {
        "Inputs": List["InputTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultiplexProgramsRequestRequestTypeDef = TypedDict(
    "ListMultiplexProgramsRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListMultiplexProgramsResponseTypeDef = TypedDict(
    "ListMultiplexProgramsResponseTypeDef",
    {
        "MultiplexPrograms": List["MultiplexProgramSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultiplexesRequestRequestTypeDef = TypedDict(
    "ListMultiplexesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListMultiplexesResponseTypeDef = TypedDict(
    "ListMultiplexesResponseTypeDef",
    {
        "Multiplexes": List["MultiplexSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "ChannelClass": NotRequired[str],
        "ChannelConfiguration": NotRequired[str],
        "Codec": NotRequired[str],
        "Duration": NotRequired[str],
        "MaxResults": NotRequired[int],
        "MaximumBitrate": NotRequired[str],
        "MaximumFramerate": NotRequired[str],
        "NextToken": NotRequired[str],
        "Resolution": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SpecialFeature": NotRequired[str],
        "VideoQuality": NotRequired[str],
    },
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReservationsRequestRequestTypeDef = TypedDict(
    "ListReservationsRequestRequestTypeDef",
    {
        "ChannelClass": NotRequired[str],
        "Codec": NotRequired[str],
        "MaxResults": NotRequired[int],
        "MaximumBitrate": NotRequired[str],
        "MaximumFramerate": NotRequired[str],
        "NextToken": NotRequired[str],
        "Resolution": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SpecialFeature": NotRequired[str],
        "VideoQuality": NotRequired[str],
    },
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
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

M2tsSettingsTypeDef = TypedDict(
    "M2tsSettingsTypeDef",
    {
        "AbsentInputAudioBehavior": NotRequired[M2tsAbsentInputAudioBehaviorType],
        "Arib": NotRequired[M2tsAribType],
        "AribCaptionsPid": NotRequired[str],
        "AribCaptionsPidControl": NotRequired[M2tsAribCaptionsPidControlType],
        "AudioBufferModel": NotRequired[M2tsAudioBufferModelType],
        "AudioFramesPerPes": NotRequired[int],
        "AudioPids": NotRequired[str],
        "AudioStreamType": NotRequired[M2tsAudioStreamTypeType],
        "Bitrate": NotRequired[int],
        "BufferModel": NotRequired[M2tsBufferModelType],
        "CcDescriptor": NotRequired[M2tsCcDescriptorType],
        "DvbNitSettings": NotRequired["DvbNitSettingsTypeDef"],
        "DvbSdtSettings": NotRequired["DvbSdtSettingsTypeDef"],
        "DvbSubPids": NotRequired[str],
        "DvbTdtSettings": NotRequired["DvbTdtSettingsTypeDef"],
        "DvbTeletextPid": NotRequired[str],
        "Ebif": NotRequired[M2tsEbifControlType],
        "EbpAudioInterval": NotRequired[M2tsAudioIntervalType],
        "EbpLookaheadMs": NotRequired[int],
        "EbpPlacement": NotRequired[M2tsEbpPlacementType],
        "EcmPid": NotRequired[str],
        "EsRateInPes": NotRequired[M2tsEsRateInPesType],
        "EtvPlatformPid": NotRequired[str],
        "EtvSignalPid": NotRequired[str],
        "FragmentTime": NotRequired[float],
        "Klv": NotRequired[M2tsKlvType],
        "KlvDataPids": NotRequired[str],
        "NielsenId3Behavior": NotRequired[M2tsNielsenId3BehaviorType],
        "NullPacketBitrate": NotRequired[float],
        "PatInterval": NotRequired[int],
        "PcrControl": NotRequired[M2tsPcrControlType],
        "PcrPeriod": NotRequired[int],
        "PcrPid": NotRequired[str],
        "PmtInterval": NotRequired[int],
        "PmtPid": NotRequired[str],
        "ProgramNum": NotRequired[int],
        "RateMode": NotRequired[M2tsRateModeType],
        "Scte27Pids": NotRequired[str],
        "Scte35Control": NotRequired[M2tsScte35ControlType],
        "Scte35Pid": NotRequired[str],
        "SegmentationMarkers": NotRequired[M2tsSegmentationMarkersType],
        "SegmentationStyle": NotRequired[M2tsSegmentationStyleType],
        "SegmentationTime": NotRequired[float],
        "TimedMetadataBehavior": NotRequired[M2tsTimedMetadataBehaviorType],
        "TimedMetadataPid": NotRequired[str],
        "TransportStreamId": NotRequired[int],
        "VideoPid": NotRequired[str],
    },
)

M3u8SettingsTypeDef = TypedDict(
    "M3u8SettingsTypeDef",
    {
        "AudioFramesPerPes": NotRequired[int],
        "AudioPids": NotRequired[str],
        "EcmPid": NotRequired[str],
        "NielsenId3Behavior": NotRequired[M3u8NielsenId3BehaviorType],
        "PatInterval": NotRequired[int],
        "PcrControl": NotRequired[M3u8PcrControlType],
        "PcrPeriod": NotRequired[int],
        "PcrPid": NotRequired[str],
        "PmtInterval": NotRequired[int],
        "PmtPid": NotRequired[str],
        "ProgramNum": NotRequired[int],
        "Scte35Behavior": NotRequired[M3u8Scte35BehaviorType],
        "Scte35Pid": NotRequired[str],
        "TimedMetadataBehavior": NotRequired[M3u8TimedMetadataBehaviorType],
        "TimedMetadataPid": NotRequired[str],
        "TransportStreamId": NotRequired[int],
        "VideoPid": NotRequired[str],
    },
)

MediaConnectFlowRequestTypeDef = TypedDict(
    "MediaConnectFlowRequestTypeDef",
    {
        "FlowArn": NotRequired[str],
    },
)

MediaConnectFlowTypeDef = TypedDict(
    "MediaConnectFlowTypeDef",
    {
        "FlowArn": NotRequired[str],
    },
)

MediaPackageGroupSettingsTypeDef = TypedDict(
    "MediaPackageGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)

MediaPackageOutputDestinationSettingsTypeDef = TypedDict(
    "MediaPackageOutputDestinationSettingsTypeDef",
    {
        "ChannelId": NotRequired[str],
    },
)

MotionGraphicsActivateScheduleActionSettingsTypeDef = TypedDict(
    "MotionGraphicsActivateScheduleActionSettingsTypeDef",
    {
        "Duration": NotRequired[int],
        "PasswordParam": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
    },
)

MotionGraphicsConfigurationTypeDef = TypedDict(
    "MotionGraphicsConfigurationTypeDef",
    {
        "MotionGraphicsSettings": "MotionGraphicsSettingsTypeDef",
        "MotionGraphicsInsertion": NotRequired[MotionGraphicsInsertionType],
    },
)

MotionGraphicsSettingsTypeDef = TypedDict(
    "MotionGraphicsSettingsTypeDef",
    {
        "HtmlMotionGraphicsSettings": NotRequired[Mapping[str, Any]],
    },
)

Mp2SettingsTypeDef = TypedDict(
    "Mp2SettingsTypeDef",
    {
        "Bitrate": NotRequired[float],
        "CodingMode": NotRequired[Mp2CodingModeType],
        "SampleRate": NotRequired[float],
    },
)

Mpeg2FilterSettingsTypeDef = TypedDict(
    "Mpeg2FilterSettingsTypeDef",
    {
        "TemporalFilterSettings": NotRequired["TemporalFilterSettingsTypeDef"],
    },
)

Mpeg2SettingsTypeDef = TypedDict(
    "Mpeg2SettingsTypeDef",
    {
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "AdaptiveQuantization": NotRequired[Mpeg2AdaptiveQuantizationType],
        "AfdSignaling": NotRequired[AfdSignalingType],
        "ColorMetadata": NotRequired[Mpeg2ColorMetadataType],
        "ColorSpace": NotRequired[Mpeg2ColorSpaceType],
        "DisplayAspectRatio": NotRequired[Mpeg2DisplayRatioType],
        "FilterSettings": NotRequired["Mpeg2FilterSettingsTypeDef"],
        "FixedAfd": NotRequired[FixedAfdType],
        "GopClosedCadence": NotRequired[int],
        "GopNumBFrames": NotRequired[int],
        "GopSize": NotRequired[float],
        "GopSizeUnits": NotRequired[Mpeg2GopSizeUnitsType],
        "ScanType": NotRequired[Mpeg2ScanTypeType],
        "SubgopLength": NotRequired[Mpeg2SubGopLengthType],
        "TimecodeInsertion": NotRequired[Mpeg2TimecodeInsertionBehaviorType],
    },
)

MsSmoothGroupSettingsTypeDef = TypedDict(
    "MsSmoothGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
        "AcquisitionPointId": NotRequired[str],
        "AudioOnlyTimecodeControl": NotRequired[SmoothGroupAudioOnlyTimecodeControlType],
        "CertificateMode": NotRequired[SmoothGroupCertificateModeType],
        "ConnectionRetryInterval": NotRequired[int],
        "EventId": NotRequired[str],
        "EventIdMode": NotRequired[SmoothGroupEventIdModeType],
        "EventStopBehavior": NotRequired[SmoothGroupEventStopBehaviorType],
        "FilecacheDuration": NotRequired[int],
        "FragmentLength": NotRequired[int],
        "InputLossAction": NotRequired[InputLossActionForMsSmoothOutType],
        "NumRetries": NotRequired[int],
        "RestartDelay": NotRequired[int],
        "SegmentationMode": NotRequired[SmoothGroupSegmentationModeType],
        "SendDelayMs": NotRequired[int],
        "SparseTrackType": NotRequired[SmoothGroupSparseTrackTypeType],
        "StreamManifestBehavior": NotRequired[SmoothGroupStreamManifestBehaviorType],
        "TimestampOffset": NotRequired[str],
        "TimestampOffsetMode": NotRequired[SmoothGroupTimestampOffsetModeType],
    },
)

MsSmoothOutputSettingsTypeDef = TypedDict(
    "MsSmoothOutputSettingsTypeDef",
    {
        "H265PackagingType": NotRequired[MsSmoothH265PackagingTypeType],
        "NameModifier": NotRequired[str],
    },
)

MultiplexMediaConnectOutputDestinationSettingsTypeDef = TypedDict(
    "MultiplexMediaConnectOutputDestinationSettingsTypeDef",
    {
        "EntitlementArn": NotRequired[str],
    },
)

MultiplexOutputDestinationTypeDef = TypedDict(
    "MultiplexOutputDestinationTypeDef",
    {
        "MediaConnectSettings": NotRequired[
            "MultiplexMediaConnectOutputDestinationSettingsTypeDef"
        ],
    },
)

MultiplexOutputSettingsTypeDef = TypedDict(
    "MultiplexOutputSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)

MultiplexProgramChannelDestinationSettingsTypeDef = TypedDict(
    "MultiplexProgramChannelDestinationSettingsTypeDef",
    {
        "MultiplexId": NotRequired[str],
        "ProgramName": NotRequired[str],
    },
)

MultiplexProgramPacketIdentifiersMapTypeDef = TypedDict(
    "MultiplexProgramPacketIdentifiersMapTypeDef",
    {
        "AudioPids": NotRequired[List[int]],
        "DvbSubPids": NotRequired[List[int]],
        "DvbTeletextPid": NotRequired[int],
        "EtvPlatformPid": NotRequired[int],
        "EtvSignalPid": NotRequired[int],
        "KlvDataPids": NotRequired[List[int]],
        "PcrPid": NotRequired[int],
        "PmtPid": NotRequired[int],
        "PrivateMetadataPid": NotRequired[int],
        "Scte27Pids": NotRequired[List[int]],
        "Scte35Pid": NotRequired[int],
        "TimedMetadataPid": NotRequired[int],
        "VideoPid": NotRequired[int],
    },
)

MultiplexProgramPipelineDetailTypeDef = TypedDict(
    "MultiplexProgramPipelineDetailTypeDef",
    {
        "ActiveChannelPipeline": NotRequired[str],
        "PipelineId": NotRequired[str],
    },
)

MultiplexProgramServiceDescriptorTypeDef = TypedDict(
    "MultiplexProgramServiceDescriptorTypeDef",
    {
        "ProviderName": str,
        "ServiceName": str,
    },
)

MultiplexProgramSettingsTypeDef = TypedDict(
    "MultiplexProgramSettingsTypeDef",
    {
        "ProgramNumber": int,
        "PreferredChannelPipeline": NotRequired[PreferredChannelPipelineType],
        "ServiceDescriptor": NotRequired["MultiplexProgramServiceDescriptorTypeDef"],
        "VideoSettings": NotRequired["MultiplexVideoSettingsTypeDef"],
    },
)

MultiplexProgramSummaryTypeDef = TypedDict(
    "MultiplexProgramSummaryTypeDef",
    {
        "ChannelId": NotRequired[str],
        "ProgramName": NotRequired[str],
    },
)

MultiplexProgramTypeDef = TypedDict(
    "MultiplexProgramTypeDef",
    {
        "ChannelId": NotRequired[str],
        "MultiplexProgramSettings": NotRequired["MultiplexProgramSettingsTypeDef"],
        "PacketIdentifiersMap": NotRequired["MultiplexProgramPacketIdentifiersMapTypeDef"],
        "PipelineDetails": NotRequired[List["MultiplexProgramPipelineDetailTypeDef"]],
        "ProgramName": NotRequired[str],
    },
)

MultiplexSettingsSummaryTypeDef = TypedDict(
    "MultiplexSettingsSummaryTypeDef",
    {
        "TransportStreamBitrate": NotRequired[int],
    },
)

MultiplexSettingsTypeDef = TypedDict(
    "MultiplexSettingsTypeDef",
    {
        "TransportStreamBitrate": int,
        "TransportStreamId": int,
        "MaximumVideoBufferDelayMilliseconds": NotRequired[int],
        "TransportStreamReservedBitrate": NotRequired[int],
    },
)

MultiplexStatmuxVideoSettingsTypeDef = TypedDict(
    "MultiplexStatmuxVideoSettingsTypeDef",
    {
        "MaximumBitrate": NotRequired[int],
        "MinimumBitrate": NotRequired[int],
        "Priority": NotRequired[int],
    },
)

MultiplexSummaryTypeDef = TypedDict(
    "MultiplexSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "Id": NotRequired[str],
        "MultiplexSettings": NotRequired["MultiplexSettingsSummaryTypeDef"],
        "Name": NotRequired[str],
        "PipelinesRunningCount": NotRequired[int],
        "ProgramCount": NotRequired[int],
        "State": NotRequired[MultiplexStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

MultiplexTypeDef = TypedDict(
    "MultiplexTypeDef",
    {
        "Arn": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "Destinations": NotRequired[List["MultiplexOutputDestinationTypeDef"]],
        "Id": NotRequired[str],
        "MultiplexSettings": NotRequired["MultiplexSettingsTypeDef"],
        "Name": NotRequired[str],
        "PipelinesRunningCount": NotRequired[int],
        "ProgramCount": NotRequired[int],
        "State": NotRequired[MultiplexStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

MultiplexVideoSettingsTypeDef = TypedDict(
    "MultiplexVideoSettingsTypeDef",
    {
        "ConstantBitrate": NotRequired[int],
        "StatmuxSettings": NotRequired["MultiplexStatmuxVideoSettingsTypeDef"],
    },
)

NetworkInputSettingsTypeDef = TypedDict(
    "NetworkInputSettingsTypeDef",
    {
        "HlsInputSettings": NotRequired["HlsInputSettingsTypeDef"],
        "ServerValidation": NotRequired[NetworkInputServerValidationType],
    },
)

NielsenCBETTypeDef = TypedDict(
    "NielsenCBETTypeDef",
    {
        "CbetCheckDigitString": str,
        "CbetStepaside": NielsenWatermarksCbetStepasideType,
        "Csid": str,
    },
)

NielsenConfigurationTypeDef = TypedDict(
    "NielsenConfigurationTypeDef",
    {
        "DistributorId": NotRequired[str],
        "NielsenPcmToId3Tagging": NotRequired[NielsenPcmToId3TaggingStateType],
    },
)

NielsenNaesIiNwTypeDef = TypedDict(
    "NielsenNaesIiNwTypeDef",
    {
        "CheckDigitString": str,
        "Sid": float,
    },
)

NielsenWatermarksSettingsTypeDef = TypedDict(
    "NielsenWatermarksSettingsTypeDef",
    {
        "NielsenCbetSettings": NotRequired["NielsenCBETTypeDef"],
        "NielsenDistributionType": NotRequired[NielsenWatermarksDistributionTypesType],
        "NielsenNaesIiNwSettings": NotRequired["NielsenNaesIiNwTypeDef"],
    },
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "Arn": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "Duration": NotRequired[int],
        "DurationUnits": NotRequired[Literal["MONTHS"]],
        "FixedPrice": NotRequired[float],
        "OfferingDescription": NotRequired[str],
        "OfferingId": NotRequired[str],
        "OfferingType": NotRequired[Literal["NO_UPFRONT"]],
        "Region": NotRequired[str],
        "ResourceSpecification": NotRequired["ReservationResourceSpecificationTypeDef"],
        "UsagePrice": NotRequired[float],
    },
)

OutputDestinationSettingsTypeDef = TypedDict(
    "OutputDestinationSettingsTypeDef",
    {
        "PasswordParam": NotRequired[str],
        "StreamName": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
    },
)

OutputDestinationTypeDef = TypedDict(
    "OutputDestinationTypeDef",
    {
        "Id": NotRequired[str],
        "MediaPackageSettings": NotRequired[
            Sequence["MediaPackageOutputDestinationSettingsTypeDef"]
        ],
        "MultiplexSettings": NotRequired["MultiplexProgramChannelDestinationSettingsTypeDef"],
        "Settings": NotRequired[Sequence["OutputDestinationSettingsTypeDef"]],
    },
)

OutputGroupSettingsTypeDef = TypedDict(
    "OutputGroupSettingsTypeDef",
    {
        "ArchiveGroupSettings": NotRequired["ArchiveGroupSettingsTypeDef"],
        "FrameCaptureGroupSettings": NotRequired["FrameCaptureGroupSettingsTypeDef"],
        "HlsGroupSettings": NotRequired["HlsGroupSettingsTypeDef"],
        "MediaPackageGroupSettings": NotRequired["MediaPackageGroupSettingsTypeDef"],
        "MsSmoothGroupSettings": NotRequired["MsSmoothGroupSettingsTypeDef"],
        "MultiplexGroupSettings": NotRequired[Mapping[str, Any]],
        "RtmpGroupSettings": NotRequired["RtmpGroupSettingsTypeDef"],
        "UdpGroupSettings": NotRequired["UdpGroupSettingsTypeDef"],
    },
)

OutputGroupTypeDef = TypedDict(
    "OutputGroupTypeDef",
    {
        "OutputGroupSettings": "OutputGroupSettingsTypeDef",
        "Outputs": Sequence["OutputTypeDef"],
        "Name": NotRequired[str],
    },
)

OutputLocationRefTypeDef = TypedDict(
    "OutputLocationRefTypeDef",
    {
        "DestinationRefId": NotRequired[str],
    },
)

OutputSettingsTypeDef = TypedDict(
    "OutputSettingsTypeDef",
    {
        "ArchiveOutputSettings": NotRequired["ArchiveOutputSettingsTypeDef"],
        "FrameCaptureOutputSettings": NotRequired["FrameCaptureOutputSettingsTypeDef"],
        "HlsOutputSettings": NotRequired["HlsOutputSettingsTypeDef"],
        "MediaPackageOutputSettings": NotRequired[Mapping[str, Any]],
        "MsSmoothOutputSettings": NotRequired["MsSmoothOutputSettingsTypeDef"],
        "MultiplexOutputSettings": NotRequired["MultiplexOutputSettingsTypeDef"],
        "RtmpOutputSettings": NotRequired["RtmpOutputSettingsTypeDef"],
        "UdpOutputSettings": NotRequired["UdpOutputSettingsTypeDef"],
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "OutputSettings": "OutputSettingsTypeDef",
        "AudioDescriptionNames": NotRequired[Sequence[str]],
        "CaptionDescriptionNames": NotRequired[Sequence[str]],
        "OutputName": NotRequired[str],
        "VideoDescriptionName": NotRequired[str],
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

PauseStateScheduleActionSettingsTypeDef = TypedDict(
    "PauseStateScheduleActionSettingsTypeDef",
    {
        "Pipelines": NotRequired[Sequence["PipelinePauseStateSettingsTypeDef"]],
    },
)

PipelineDetailTypeDef = TypedDict(
    "PipelineDetailTypeDef",
    {
        "ActiveInputAttachmentName": NotRequired[str],
        "ActiveInputSwitchActionName": NotRequired[str],
        "ActiveMotionGraphicsActionName": NotRequired[str],
        "ActiveMotionGraphicsUri": NotRequired[str],
        "PipelineId": NotRequired[str],
    },
)

PipelinePauseStateSettingsTypeDef = TypedDict(
    "PipelinePauseStateSettingsTypeDef",
    {
        "PipelineId": PipelineIdType,
    },
)

PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "Count": int,
        "OfferingId": str,
        "Name": NotRequired[str],
        "RequestId": NotRequired[str],
        "Start": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "RejectInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

RemixSettingsTypeDef = TypedDict(
    "RemixSettingsTypeDef",
    {
        "ChannelMappings": Sequence["AudioChannelMappingTypeDef"],
        "ChannelsIn": NotRequired[int],
        "ChannelsOut": NotRequired[int],
    },
)

ReservationResourceSpecificationTypeDef = TypedDict(
    "ReservationResourceSpecificationTypeDef",
    {
        "ChannelClass": NotRequired[ChannelClassType],
        "Codec": NotRequired[ReservationCodecType],
        "MaximumBitrate": NotRequired[ReservationMaximumBitrateType],
        "MaximumFramerate": NotRequired[ReservationMaximumFramerateType],
        "Resolution": NotRequired[ReservationResolutionType],
        "ResourceType": NotRequired[ReservationResourceTypeType],
        "SpecialFeature": NotRequired[ReservationSpecialFeatureType],
        "VideoQuality": NotRequired[ReservationVideoQualityType],
    },
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Arn": NotRequired[str],
        "Count": NotRequired[int],
        "CurrencyCode": NotRequired[str],
        "Duration": NotRequired[int],
        "DurationUnits": NotRequired[Literal["MONTHS"]],
        "End": NotRequired[str],
        "FixedPrice": NotRequired[float],
        "Name": NotRequired[str],
        "OfferingDescription": NotRequired[str],
        "OfferingId": NotRequired[str],
        "OfferingType": NotRequired[Literal["NO_UPFRONT"]],
        "Region": NotRequired[str],
        "ReservationId": NotRequired[str],
        "ResourceSpecification": NotRequired["ReservationResourceSpecificationTypeDef"],
        "Start": NotRequired[str],
        "State": NotRequired[ReservationStateType],
        "Tags": NotRequired[Dict[str, str]],
        "UsagePrice": NotRequired[float],
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

RtmpGroupSettingsTypeDef = TypedDict(
    "RtmpGroupSettingsTypeDef",
    {
        "AdMarkers": NotRequired[Sequence[Literal["ON_CUE_POINT_SCTE35"]]],
        "AuthenticationScheme": NotRequired[AuthenticationSchemeType],
        "CacheFullBehavior": NotRequired[RtmpCacheFullBehaviorType],
        "CacheLength": NotRequired[int],
        "CaptionData": NotRequired[RtmpCaptionDataType],
        "InputLossAction": NotRequired[InputLossActionForRtmpOutType],
        "RestartDelay": NotRequired[int],
    },
)

RtmpOutputSettingsTypeDef = TypedDict(
    "RtmpOutputSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
        "CertificateMode": NotRequired[RtmpOutputCertificateModeType],
        "ConnectionRetryInterval": NotRequired[int],
        "NumRetries": NotRequired[int],
    },
)

ScheduleActionSettingsTypeDef = TypedDict(
    "ScheduleActionSettingsTypeDef",
    {
        "HlsId3SegmentTaggingSettings": NotRequired[
            "HlsId3SegmentTaggingScheduleActionSettingsTypeDef"
        ],
        "HlsTimedMetadataSettings": NotRequired["HlsTimedMetadataScheduleActionSettingsTypeDef"],
        "InputPrepareSettings": NotRequired["InputPrepareScheduleActionSettingsTypeDef"],
        "InputSwitchSettings": NotRequired["InputSwitchScheduleActionSettingsTypeDef"],
        "MotionGraphicsImageActivateSettings": NotRequired[
            "MotionGraphicsActivateScheduleActionSettingsTypeDef"
        ],
        "MotionGraphicsImageDeactivateSettings": NotRequired[Mapping[str, Any]],
        "PauseStateSettings": NotRequired["PauseStateScheduleActionSettingsTypeDef"],
        "Scte35ReturnToNetworkSettings": NotRequired[
            "Scte35ReturnToNetworkScheduleActionSettingsTypeDef"
        ],
        "Scte35SpliceInsertSettings": NotRequired[
            "Scte35SpliceInsertScheduleActionSettingsTypeDef"
        ],
        "Scte35TimeSignalSettings": NotRequired["Scte35TimeSignalScheduleActionSettingsTypeDef"],
        "StaticImageActivateSettings": NotRequired[
            "StaticImageActivateScheduleActionSettingsTypeDef"
        ],
        "StaticImageDeactivateSettings": NotRequired[
            "StaticImageDeactivateScheduleActionSettingsTypeDef"
        ],
    },
)

ScheduleActionStartSettingsTypeDef = TypedDict(
    "ScheduleActionStartSettingsTypeDef",
    {
        "FixedModeScheduleActionStartSettings": NotRequired[
            "FixedModeScheduleActionStartSettingsTypeDef"
        ],
        "FollowModeScheduleActionStartSettings": NotRequired[
            "FollowModeScheduleActionStartSettingsTypeDef"
        ],
        "ImmediateModeScheduleActionStartSettings": NotRequired[Mapping[str, Any]],
    },
)

ScheduleActionTypeDef = TypedDict(
    "ScheduleActionTypeDef",
    {
        "ActionName": str,
        "ScheduleActionSettings": "ScheduleActionSettingsTypeDef",
        "ScheduleActionStartSettings": "ScheduleActionStartSettingsTypeDef",
    },
)

Scte20SourceSettingsTypeDef = TypedDict(
    "Scte20SourceSettingsTypeDef",
    {
        "Convert608To708": NotRequired[Scte20Convert608To708Type],
        "Source608ChannelNumber": NotRequired[int],
    },
)

Scte27SourceSettingsTypeDef = TypedDict(
    "Scte27SourceSettingsTypeDef",
    {
        "OcrLanguage": NotRequired[Scte27OcrLanguageType],
        "Pid": NotRequired[int],
    },
)

Scte35DeliveryRestrictionsTypeDef = TypedDict(
    "Scte35DeliveryRestrictionsTypeDef",
    {
        "ArchiveAllowedFlag": Scte35ArchiveAllowedFlagType,
        "DeviceRestrictions": Scte35DeviceRestrictionsType,
        "NoRegionalBlackoutFlag": Scte35NoRegionalBlackoutFlagType,
        "WebDeliveryAllowedFlag": Scte35WebDeliveryAllowedFlagType,
    },
)

Scte35DescriptorSettingsTypeDef = TypedDict(
    "Scte35DescriptorSettingsTypeDef",
    {
        "SegmentationDescriptorScte35DescriptorSettings": "Scte35SegmentationDescriptorTypeDef",
    },
)

Scte35DescriptorTypeDef = TypedDict(
    "Scte35DescriptorTypeDef",
    {
        "Scte35DescriptorSettings": "Scte35DescriptorSettingsTypeDef",
    },
)

Scte35ReturnToNetworkScheduleActionSettingsTypeDef = TypedDict(
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
    {
        "SpliceEventId": int,
    },
)

Scte35SegmentationDescriptorTypeDef = TypedDict(
    "Scte35SegmentationDescriptorTypeDef",
    {
        "SegmentationCancelIndicator": Scte35SegmentationCancelIndicatorType,
        "SegmentationEventId": int,
        "DeliveryRestrictions": NotRequired["Scte35DeliveryRestrictionsTypeDef"],
        "SegmentNum": NotRequired[int],
        "SegmentationDuration": NotRequired[int],
        "SegmentationTypeId": NotRequired[int],
        "SegmentationUpid": NotRequired[str],
        "SegmentationUpidType": NotRequired[int],
        "SegmentsExpected": NotRequired[int],
        "SubSegmentNum": NotRequired[int],
        "SubSegmentsExpected": NotRequired[int],
    },
)

Scte35SpliceInsertScheduleActionSettingsTypeDef = TypedDict(
    "Scte35SpliceInsertScheduleActionSettingsTypeDef",
    {
        "SpliceEventId": int,
        "Duration": NotRequired[int],
    },
)

Scte35SpliceInsertTypeDef = TypedDict(
    "Scte35SpliceInsertTypeDef",
    {
        "AdAvailOffset": NotRequired[int],
        "NoRegionalBlackoutFlag": NotRequired[Scte35SpliceInsertNoRegionalBlackoutBehaviorType],
        "WebDeliveryAllowedFlag": NotRequired[Scte35SpliceInsertWebDeliveryAllowedBehaviorType],
    },
)

Scte35TimeSignalAposTypeDef = TypedDict(
    "Scte35TimeSignalAposTypeDef",
    {
        "AdAvailOffset": NotRequired[int],
        "NoRegionalBlackoutFlag": NotRequired[Scte35AposNoRegionalBlackoutBehaviorType],
        "WebDeliveryAllowedFlag": NotRequired[Scte35AposWebDeliveryAllowedBehaviorType],
    },
)

Scte35TimeSignalScheduleActionSettingsTypeDef = TypedDict(
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    {
        "Scte35Descriptors": Sequence["Scte35DescriptorTypeDef"],
    },
)

StandardHlsSettingsTypeDef = TypedDict(
    "StandardHlsSettingsTypeDef",
    {
        "M3u8Settings": "M3u8SettingsTypeDef",
        "AudioRenditionSets": NotRequired[str],
    },
)

StartChannelRequestRequestTypeDef = TypedDict(
    "StartChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

StartChannelResponseTypeDef = TypedDict(
    "StartChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMultiplexRequestRequestTypeDef = TypedDict(
    "StartMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

StartMultiplexResponseTypeDef = TypedDict(
    "StartMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTimecodeTypeDef = TypedDict(
    "StartTimecodeTypeDef",
    {
        "Timecode": NotRequired[str],
    },
)

StaticImageActivateScheduleActionSettingsTypeDef = TypedDict(
    "StaticImageActivateScheduleActionSettingsTypeDef",
    {
        "Image": "InputLocationTypeDef",
        "Duration": NotRequired[int],
        "FadeIn": NotRequired[int],
        "FadeOut": NotRequired[int],
        "Height": NotRequired[int],
        "ImageX": NotRequired[int],
        "ImageY": NotRequired[int],
        "Layer": NotRequired[int],
        "Opacity": NotRequired[int],
        "Width": NotRequired[int],
    },
)

StaticImageDeactivateScheduleActionSettingsTypeDef = TypedDict(
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    {
        "FadeOut": NotRequired[int],
        "Layer": NotRequired[int],
    },
)

StaticKeySettingsTypeDef = TypedDict(
    "StaticKeySettingsTypeDef",
    {
        "StaticKeyValue": str,
        "KeyProviderServer": NotRequired["InputLocationTypeDef"],
    },
)

StopChannelRequestRequestTypeDef = TypedDict(
    "StopChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

StopChannelResponseTypeDef = TypedDict(
    "StopChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMultiplexRequestRequestTypeDef = TypedDict(
    "StopMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

StopMultiplexResponseTypeDef = TypedDict(
    "StopMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTimecodeTypeDef = TypedDict(
    "StopTimecodeTypeDef",
    {
        "LastFrameClippingBehavior": NotRequired[LastFrameClippingBehaviorType],
        "Timecode": NotRequired[str],
    },
)

TeletextSourceSettingsTypeDef = TypedDict(
    "TeletextSourceSettingsTypeDef",
    {
        "OutputRectangle": NotRequired["CaptionRectangleTypeDef"],
        "PageNumber": NotRequired[str],
    },
)

TemporalFilterSettingsTypeDef = TypedDict(
    "TemporalFilterSettingsTypeDef",
    {
        "PostFilterSharpening": NotRequired[TemporalFilterPostFilterSharpeningType],
        "Strength": NotRequired[TemporalFilterStrengthType],
    },
)

TimecodeConfigTypeDef = TypedDict(
    "TimecodeConfigTypeDef",
    {
        "Source": TimecodeConfigSourceType,
        "SyncThreshold": NotRequired[int],
    },
)

TransferInputDeviceRequestRequestTypeDef = TypedDict(
    "TransferInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
        "TargetCustomerId": NotRequired[str],
        "TargetRegion": NotRequired[str],
        "TransferMessage": NotRequired[str],
    },
)

TransferringInputDeviceSummaryTypeDef = TypedDict(
    "TransferringInputDeviceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Message": NotRequired[str],
        "TargetCustomerId": NotRequired[str],
        "TransferType": NotRequired[InputDeviceTransferTypeType],
    },
)

TtmlDestinationSettingsTypeDef = TypedDict(
    "TtmlDestinationSettingsTypeDef",
    {
        "StyleControl": NotRequired[TtmlDestinationStyleControlType],
    },
)

UdpContainerSettingsTypeDef = TypedDict(
    "UdpContainerSettingsTypeDef",
    {
        "M2tsSettings": NotRequired["M2tsSettingsTypeDef"],
    },
)

UdpGroupSettingsTypeDef = TypedDict(
    "UdpGroupSettingsTypeDef",
    {
        "InputLossAction": NotRequired[InputLossActionForUdpOutType],
        "TimedMetadataId3Frame": NotRequired[UdpTimedMetadataId3FrameType],
        "TimedMetadataId3Period": NotRequired[int],
    },
)

UdpOutputSettingsTypeDef = TypedDict(
    "UdpOutputSettingsTypeDef",
    {
        "ContainerSettings": "UdpContainerSettingsTypeDef",
        "Destination": "OutputLocationRefTypeDef",
        "BufferMsec": NotRequired[int],
        "FecOutputSettings": NotRequired["FecOutputSettingsTypeDef"],
    },
)

UpdateChannelClassRequestRequestTypeDef = TypedDict(
    "UpdateChannelClassRequestRequestTypeDef",
    {
        "ChannelClass": ChannelClassType,
        "ChannelId": str,
        "Destinations": NotRequired[Sequence["OutputDestinationTypeDef"]],
    },
)

UpdateChannelClassResponseTypeDef = TypedDict(
    "UpdateChannelClassResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
        "CdiInputSpecification": NotRequired["CdiInputSpecificationTypeDef"],
        "Destinations": NotRequired[Sequence["OutputDestinationTypeDef"]],
        "EncoderSettings": NotRequired["EncoderSettingsTypeDef"],
        "InputAttachments": NotRequired[Sequence["InputAttachmentTypeDef"]],
        "InputSpecification": NotRequired["InputSpecificationTypeDef"],
        "LogLevel": NotRequired[LogLevelType],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInputDeviceRequestRequestTypeDef = TypedDict(
    "UpdateInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
        "HdDeviceSettings": NotRequired["InputDeviceConfigurableSettingsTypeDef"],
        "Name": NotRequired[str],
        "UhdDeviceSettings": NotRequired["InputDeviceConfigurableSettingsTypeDef"],
    },
)

UpdateInputDeviceResponseTypeDef = TypedDict(
    "UpdateInputDeviceResponseTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionStateType,
        "DeviceSettingsSyncState": DeviceSettingsSyncStateType,
        "DeviceUpdateStatus": DeviceUpdateStatusType,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInputRequestRequestTypeDef = TypedDict(
    "UpdateInputRequestRequestTypeDef",
    {
        "InputId": str,
        "Destinations": NotRequired[Sequence["InputDestinationRequestTypeDef"]],
        "InputDevices": NotRequired[Sequence["InputDeviceRequestTypeDef"]],
        "InputSecurityGroups": NotRequired[Sequence[str]],
        "MediaConnectFlows": NotRequired[Sequence["MediaConnectFlowRequestTypeDef"]],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Sources": NotRequired[Sequence["InputSourceRequestTypeDef"]],
    },
)

UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef",
    {
        "Input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "UpdateInputSecurityGroupRequestRequestTypeDef",
    {
        "InputSecurityGroupId": str,
        "Tags": NotRequired[Mapping[str, str]],
        "WhitelistRules": NotRequired[Sequence["InputWhitelistRuleCidrTypeDef"]],
    },
)

UpdateInputSecurityGroupResponseTypeDef = TypedDict(
    "UpdateInputSecurityGroupResponseTypeDef",
    {
        "SecurityGroup": "InputSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMultiplexProgramRequestRequestTypeDef = TypedDict(
    "UpdateMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
        "MultiplexProgramSettings": NotRequired["MultiplexProgramSettingsTypeDef"],
    },
)

UpdateMultiplexProgramResponseTypeDef = TypedDict(
    "UpdateMultiplexProgramResponseTypeDef",
    {
        "MultiplexProgram": "MultiplexProgramTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMultiplexRequestRequestTypeDef = TypedDict(
    "UpdateMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "MultiplexSettings": NotRequired["MultiplexSettingsTypeDef"],
        "Name": NotRequired[str],
    },
)

UpdateMultiplexResponseTypeDef = TypedDict(
    "UpdateMultiplexResponseTypeDef",
    {
        "Multiplex": "MultiplexTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReservationRequestRequestTypeDef = TypedDict(
    "UpdateReservationRequestRequestTypeDef",
    {
        "ReservationId": str,
        "Name": NotRequired[str],
    },
)

UpdateReservationResponseTypeDef = TypedDict(
    "UpdateReservationResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoBlackFailoverSettingsTypeDef = TypedDict(
    "VideoBlackFailoverSettingsTypeDef",
    {
        "BlackDetectThreshold": NotRequired[float],
        "VideoBlackThresholdMsec": NotRequired[int],
    },
)

VideoCodecSettingsTypeDef = TypedDict(
    "VideoCodecSettingsTypeDef",
    {
        "FrameCaptureSettings": NotRequired["FrameCaptureSettingsTypeDef"],
        "H264Settings": NotRequired["H264SettingsTypeDef"],
        "H265Settings": NotRequired["H265SettingsTypeDef"],
        "Mpeg2Settings": NotRequired["Mpeg2SettingsTypeDef"],
    },
)

VideoDescriptionTypeDef = TypedDict(
    "VideoDescriptionTypeDef",
    {
        "Name": str,
        "CodecSettings": NotRequired["VideoCodecSettingsTypeDef"],
        "Height": NotRequired[int],
        "RespondToAfd": NotRequired[VideoDescriptionRespondToAfdType],
        "ScalingBehavior": NotRequired[VideoDescriptionScalingBehaviorType],
        "Sharpness": NotRequired[int],
        "Width": NotRequired[int],
    },
)

VideoSelectorColorSpaceSettingsTypeDef = TypedDict(
    "VideoSelectorColorSpaceSettingsTypeDef",
    {
        "Hdr10Settings": NotRequired["Hdr10SettingsTypeDef"],
    },
)

VideoSelectorPidTypeDef = TypedDict(
    "VideoSelectorPidTypeDef",
    {
        "Pid": NotRequired[int],
    },
)

VideoSelectorProgramIdTypeDef = TypedDict(
    "VideoSelectorProgramIdTypeDef",
    {
        "ProgramId": NotRequired[int],
    },
)

VideoSelectorSettingsTypeDef = TypedDict(
    "VideoSelectorSettingsTypeDef",
    {
        "VideoSelectorPid": NotRequired["VideoSelectorPidTypeDef"],
        "VideoSelectorProgramId": NotRequired["VideoSelectorProgramIdTypeDef"],
    },
)

VideoSelectorTypeDef = TypedDict(
    "VideoSelectorTypeDef",
    {
        "ColorSpace": NotRequired[VideoSelectorColorSpaceType],
        "ColorSpaceSettings": NotRequired["VideoSelectorColorSpaceSettingsTypeDef"],
        "ColorSpaceUsage": NotRequired[VideoSelectorColorSpaceUsageType],
        "SelectorSettings": NotRequired["VideoSelectorSettingsTypeDef"],
    },
)

VpcOutputSettingsDescriptionTypeDef = TypedDict(
    "VpcOutputSettingsDescriptionTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "NetworkInterfaceIds": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
    },
)

VpcOutputSettingsTypeDef = TypedDict(
    "VpcOutputSettingsTypeDef",
    {
        "SubnetIds": Sequence[str],
        "PublicAddressAllocationIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WavSettingsTypeDef = TypedDict(
    "WavSettingsTypeDef",
    {
        "BitDepth": NotRequired[float],
        "CodingMode": NotRequired[WavCodingModeType],
        "SampleRate": NotRequired[float],
    },
)

WebvttDestinationSettingsTypeDef = TypedDict(
    "WebvttDestinationSettingsTypeDef",
    {
        "StyleControl": NotRequired[WebvttDestinationStyleControlType],
    },
)
