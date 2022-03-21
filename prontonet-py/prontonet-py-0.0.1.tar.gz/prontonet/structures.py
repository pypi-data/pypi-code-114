from dataclasses import dataclass
from typing import Type
from prontonet.constants import IP_SECURITY_STRING
from prontonet.enums import Command, DeviceNet, LineStatus, IPCallType, AlarmStatus, Codec, BitsSample, AudioMode, \
    EncoderMix, MPEGLayer, Frequency, BondingType, AACMode, BitRate, APTXType, G711Law, MPEGL3Polarity, \
    StreamingProtocol, DeviceSubNet, ProntoNetCodecMode, AudioConfig, SIPAddressType, AudioAlgorithm, \
    EthernetInterface, EthernetNegotiatedSpeed, AudioModeAlgorithm, Acknowledge


@dataclass
class ProntonetCommand:
    command: bytes
    unpack_pattern: str
    response_type: Type


@dataclass
class AcknowledgeResponse:
    command: Command
    acknowledge: Acknowledge


@dataclass
class CSConnect:
    securityString = bytes(IP_SECURITY_STRING, "utf-8")


@dataclass
class CSCommandResponse:
    command: int
    response: int


@dataclass
class StatusDeviceNetChanged:
    device_net: DeviceNet


@dataclass
class StatusLineStatusChanged:
    line: int
    line_status: LineStatus
    number: str
    disconnection_code: int
    ip_call_type: IPCallType


@dataclass
class StatusAlarmsStatusChanged:
    alarm_status: AlarmStatus


@dataclass
class StatusDecoderAudioModeChanged:
    codec: Codec
    name: str


@dataclass
class StatusEncoderAudioModeChanged:
    codec: Codec
    name: str


@dataclass
class CommandDeviceNet:
    device_net: DeviceNet


@dataclass
class CommandCall:
    line: int
    number: str
    ip_call_type: IPCallType


@dataclass
class CommandHangUp:
    line: int


@dataclass
class CommandGetLineStatus:
    line: int


@dataclass
class CommandGetLineStatusResponse:
    line_status: LineStatus


@dataclass
class CommandGetVUMetersResponse:
    input_left_vu_meter: int
    input_right_vu_meter: int
    output_left_vu_meter: int
    output_right_vu_meter: int


@dataclass
class CommandGetMonitorsResponse:
    v12_main: int
    v12_backup: int
    temp: int
    fan_rpm: int


@dataclass
class CommandAlarmsGetStatusResponse:
    alarm_status: AlarmStatus


@dataclass
class CommandDecoderGetAudioMode:
    codec: Codec


@dataclass
class CommandEncoderGetAudioMode:
    codec: Codec


@dataclass
class CommandEncoderSetAudioModePCM:
    codec: Codec
    bits_sample: BitsSample
    audio_mode: AudioMode
    encoder_mix: EncoderMix


@dataclass
class CommandEncoderSetAudioModeMPEG:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    mpeg_layer: MPEGLayer
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType


@dataclass
class CommandEncoderSetAudioModeAAC:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    aac_mode: AACMode
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType


@dataclass
class CommandEncoderSetAudioModeG711:
    codec: Codec
    encoder_mix: EncoderMix


@dataclass
class CommandEncoderSetAudioModeG722:
    codec: Codec
    encoder_mix: EncoderMix


@dataclass
class CommandEncoderSetAudioModeAuto:
    codec: Codec
    aux_data: bool


@dataclass
class CommandEncoderSetAudioModeAPTX:
    codec: Codec
    audio_mode: AudioMode
    aptx_type: APTXType
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix


@dataclass
class CommandGetLineStatusDetails:
    line: int


@dataclass
class CommandGetLineStatusDetailsResponse:
    number: str
    disconnection_code: int
    ip_call_type: IPCallType


@dataclass
class CommandAnswer:
    line: int


@dataclass
class CommandEncoderSetAudioModeG711v2:
    codec: Codec
    encoder_mix: EncoderMix
    g711_law: G711Law


@dataclass
class CommandEncoderSetAudioModeG722v2:
    codec: Codec
    encoder_mix: EncoderMix
    g722_dither: bool


@dataclass
class CommandEncoderSetAudioModeMPEGv2:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    mpeg_layer: MPEGLayer
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType
    mpeg_l3_polarity: MPEGL3Polarity


@dataclass
class CommandIPSetStreamingProtocol:
    streaming_protocol: StreamingProtocol


@dataclass
class CommandX21EnableTX:
    enable: bool


@dataclass
class CommandLoadPreset:
    name: str


@dataclass
class CommandCallFromBook:
    line: int
    book_entry: int


@dataclass
class CommandCallFromBookAllLines:
    book_entry: int


@dataclass
class CommandDeviceNetV2:
    device_net: DeviceNet
    device_sub_net: DeviceSubNet
    pronto_net_codec_mode: ProntoNetCodecMode
    multi_unicast: bool
    streaming_protocol: StreamingProtocol


@dataclass
class CommandCallV2:
    line: int
    number: str
    ip_call_type: IPCallType
    target_codec: Codec


@dataclass
class CommandEnableNetBackup:
    enable: bool


@dataclass
class CommandGetLoadedPresetIndex:
    index: int


@dataclass
class CommandRunGPIAction:
    gpi: int
    active: bool


@dataclass
class CommandGetLoadedPresetName:
    last_loaded_preset_name: str


@dataclass
class CommandGetStreamingStats:
    target_codec: Codec


@dataclass
class CommandGetStreamingStatsResponse:
    lost_packets: int
    disordered_packets: int
    recovered_packets: int
    current_jitter: int


@dataclass
class CommandGetSIPServerRegisterStatus:
    registered: bool


@dataclass
class CommandGetSTUNServerRegisterStatus:
    registered: bool


@dataclass
class CommandGetCallDuration:
    line: int


@dataclass
class CommandGetCallDurationResponse:
    duration_seconds = int


@dataclass
class CommandAudioGetConfigurationResponse:
    command_supported: bool
    audio_config: AudioConfig
    db_in_left: int
    db_in_right: int
    db_out_left: int
    db_out_right: int


@dataclass
class CommandAudioSetConfiguration:
    audio_config: AudioConfig
    db_in_left: int
    db_in_right: int
    db_out_left: int
    db_out_right: int


@dataclass
class CommandSysDeviceName:
    device_name: str


@dataclass
class CommandSysGetVersionInfo:
    serial_number: bytes
    version: bytes


@dataclass
class CommandSIPConfiguration:
    sip_port: int
    audio_port: int
    auto_answer: bool
    enable_fec: bool
    fec_port: int
    audio_packets_per_fec_packet: int
    register_in_server: bool
    sip_user_name: str
    sip_server_address: str
    sip_server_user: str
    sip_server_password: str
    sip_server_timeout: int
    sip_address_type: SIPAddressType
    public_address: str
    stun_address: str
    stun_request_period: int


@dataclass
class CommandProdysV4Configuration:
    line_1_port: int
    enable_control_port: bool
    auto_answer: bool
    enable_fec: bool
    audio_packets_per_fec_packet: int
    fec_delay: int


@dataclass
class CommandProdysV4ConfigurationResponse:
    line_1_port: int
    enable_control_port: bool
    auto_answer: bool
    enable_fec: bool
    audio_packets_per_fec_packet: int
    fec_delay: int


@dataclass
class CommandStreamingTXCodecGetConfiguration:
    codec: Codec
    audio_algorithm: AudioAlgorithm


@dataclass
class CommandStreamingTXCodecGetConfigurationResponse:
    valid_request: bool
    time_between_packets: int


@dataclass
class CommandStreamingTXCodecSetConfiguration:
    codec: Codec
    audio_algorithm = AudioAlgorithm
    time_between_packets: int


@dataclass
class CommandStreamingRXCodecGetConfiguration:
    codec = Codec


@dataclass
class CommandStreamingRXCodecGetConfigurationResponse:
    valid_request: bool
    auto_adjustment: bool
    auto_min_delay: bool
    auto_min_delay_duration: int
    auto_max_delay: bool
    auto_max_delay_duration: int
    manual_max_delay: int


@dataclass
class CommandStreamingRXCodecSetConfiguration:
    codec: Codec
    auto_adjustment: bool
    auto_min_delay: bool
    auto_min_delay_duration: int
    auto_max_delay: bool
    auto_max_delay_duration: int
    manual_max_delay: int


@dataclass
class CommandGetStreamingStatsV2:
    codec: Codec


@dataclass
class CommandGetStreamingStatsV2Response:
    valid_request: bool
    call_in_progress: bool
    detected_bitrate: int
    rx_buffer_last_value: int
    lost_packets: int
    disordered_packets: int
    recovered_by_fec_packets: int
    current_jitter: int
    max_jitter: int
    mean_jitter: int


@dataclass
class CommandEthernetGetSpeed:
    ethernet_interface: EthernetInterface


@dataclass
class CommandEthernetGetSpeedResponse:
    valid_request: bool
    interface_enabled: bool
    ethernet_negotiated_speed: EthernetNegotiatedSpeed


@dataclass
class CommandStreamingStatsReset:
    codec: Codec


@dataclass
class CommandAudioModeConfigPCMV2:
    codec: Codec
    bits_sample: BitsSample
    audio_mode: AudioMode
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandAudioModeConfigG711V3:
    codec: Codec
    g711_law: G711Law
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandAudioModeConfigG722V3:
    codec: Codec
    encoder_mix: EncoderMix
    aux_data: bool
    g722_dither: bool


@dataclass
class CommandAudioModeConfigAPTXV2:
    codec: Codec
    aptx_type: APTXType
    bit_rate: BitRate
    audio_mode: AudioMode
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandGetAudioModeAlgorithm:
    codec: Codec


@dataclass
class CommandEncoderGetAudioModeAlgorithmResponse:
    valid_request: bool
    audio_mode_algorithm: AudioModeAlgorithm


@dataclass
class CommandDecoderGetAudioModeAlgorithmResponse:
    valid_request: bool
    is_framed: bool
    audio_mode_algorithm: AudioModeAlgorithm


@dataclass
class CommandEncoderGetAudioModeAutoResponse:
    codec: Codec
    aux_data: bool


@dataclass
class CommandEncoderGetAudioModePCMResponse:
    codec: Codec
    bits_sample: BitsSample
    audio_mode: AudioMode
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandEncoderGetAudioModeG711Response:
    codec: Codec
    g711_law: G711Law
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandEncoderGetAudioModeG722Response:
    codec: Codec
    encoder_mix: EncoderMix
    aux_data: bool
    g722_dither: bool


@dataclass
class CommandEncoderGetAudioModeMPEGResponse:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    mpeg_layer: MPEGLayer
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType
    mpeg_l3_polarity: MPEGL3Polarity


@dataclass
class CommandEncoderGetAudioModeAACResponse:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    aac_mode: AACMode
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType


@dataclass
class CommandEncoderGetAudioModeAPTXResponse:
    codec: Codec
    aptx_type: APTXType
    bit_rate: BitRate
    audio_mode: AudioMode
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandDecoderGetAudioModePCMResponse:
    codec: Codec
    bits_sample: BitsSample
    audio_mode: AudioMode
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandDecoderGetAudioModeG711Response:
    codec: Codec
    g711_law: G711Law
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandDecoderGetAudioModeG722Response:
    codec: Codec
    encoder_mix: EncoderMix
    aux_data: bool
    g722_dither: bool


@dataclass
class CommandDecoderGetAudioModeMPEGResponse:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    mpeg_layer: MPEGLayer
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType
    mpeg_l3_polarity: MPEGL3Polarity


@dataclass
class CommandDecoderGetAudioModeAACResponse:
    codec: Codec
    bit_rate: BitRate
    audio_mode: AudioMode
    aac_mode: AACMode
    frequency: Frequency
    crc: bool
    aux_data: bool
    encoder_mix: EncoderMix
    bonding_type: BondingType


@dataclass
class CommandDecoderGetAudioModeAPTXResponse:
    codec: Codec
    aptx_type: APTXType
    bit_rate: BitRate
    audio_mode: AudioMode
    encoder_mix: EncoderMix
    aux_data: bool


@dataclass
class CommandAudioModeOPUS:
    codec: Codec
    bit_rate: BitRate
    encoder_mix: EncoderMix
    aux_data: bool
