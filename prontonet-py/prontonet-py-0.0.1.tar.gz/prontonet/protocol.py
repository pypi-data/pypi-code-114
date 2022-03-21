import struct
from prontonet.structures import *
from prontonet.enums import *


class ProntonetProtocol:
    @staticmethod
    def connect():
        """
        Creates initial connect message.

        Returns
        -------
        bytes
            Connect message.
        """

        command_code = Command.CONNECT
        cs = CSConnect.securityString
        b = struct.pack("<ii", command_code, 20)
        return b + cs.zfill(20)

    @staticmethod
    def get_device_net() -> ProntonetCommand:
        """
        Get device network.

        Returns
        -------
        ProntonetCommand
            Dataclass with get device network message, struct.unpack() pattern for response and response type.
        """
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_DEVICE_NET, 0),
            "iii",
            DeviceNet
        )

    @staticmethod
    def set_device_net(arg: CommandDeviceNet) -> ProntonetCommand:
        """
        Set device network.

        Parameters
        ----------
        arg : CommandDeviceNet
            Settings to be sent to device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set device network message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_SET_DEVICE_NET, 4, arg.device_net),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def call(arg: CommandCall) -> ProntonetCommand:
        """
        Call.

        Parameters
        ----------
        arg : CommandCall
            Call settings.

        Returns
        -------
        ProntonetCommand
            Dataclass with call message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_CALL, 40, arg.line)
            + arg.number[0:32].ljust(32, '\x00').encode("utf-8")
            + struct.pack("<i", arg.ip_call_type),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def answer(arg: CommandAnswer) -> ProntonetCommand:
        """
        Answer a call.

        Parameters
        ----------
        arg : CommandAnswer
            Answer command settings.

        Returns
        -------
        ProntonetCommand
            Dataclass with answer message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ANSWER, 4, arg.line),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def hang_up(arg: CommandHangUp) -> ProntonetCommand:
        """
        Hang up a call.

        Parameters
        ----------
        arg : CommandHangUp
            Hang up command settings.

        Returns
        -------
        ProntonetCommand
            Dataclass with hang up message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_HANG_UP, 4, arg.line),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_line_status(arg: CommandGetLineStatus) -> ProntonetCommand:
        """
        Get the current line status.

        Parameters
        ----------
        arg : CommandGetLineStatus
            Command settings (line number).

        Returns
        -------
        ProntonetCommand
            Dataclass with get line status message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_LINE_STATUS, 4, arg.line),
            "iii",
            CommandGetLineStatusResponse
        )

    @staticmethod
    def get_line_status_details(arg: CommandGetLineStatusDetails) -> ProntonetCommand:
        """
        Get the current line status details.

        Parameters
        ----------
        arg : CommandGetLineStatus
            Command settings (line number).

        Returns
        -------
        ProntonetCommand
            Dataclass with get line status details message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_LINE_STATUS_DETAILS, 4, arg.line),
            "ii32sii",
            CommandGetLineStatusDetailsResponse
        )

    @staticmethod
    def get_vu_meters() -> ProntonetCommand:
        """
        Get current input and output VU meters.

        Returns
        -------
        ProntonetCommand
            Dataclass with get VU meters message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_VU_METERS, 0),
            "iiiiii",
            CommandGetVUMetersResponse
        )

    @staticmethod
    def get_monitors() -> ProntonetCommand:
        """
        Get current system monitor values (hardware diagnostic data).

        Returns
        -------
        ProntonetCommand
            Dataclass with get monitors message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_MONITORS, 0),
            "iiiiii",
            CommandGetMonitorsResponse
        )

    @staticmethod
    def get_alarm_status() -> ProntonetCommand:
        """
        Get current alarm status.

        Returns
        -------
        ProntonetCommand
            Dataclass with get alarm status message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_GET_STATUS, 0),
            "iii",
            AlarmStatus
        )

    @staticmethod
    def get_decoder_audio_mode(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get decoder's audio mode.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command settings (codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE, 4, arg.codec),
            "ii#",
            bytes
        )

    @staticmethod
    def get_encoder_audio_mode(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get encoder's audio mode.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command settings (codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE, 4, arg.codec),
            "ii#",
            bytes
        )

    @staticmethod
    def set_encoder_audio_mode_pcm(arg: CommandEncoderSetAudioModePCM) -> ProntonetCommand:
        """
        Set encoder's audio mode to PCM.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModePCM
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode PCM message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_PCM, 16,
                        arg.codec, arg.bits_sample, arg.audio_mode, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_mpeg(arg: CommandEncoderSetAudioModeMPEG) -> ProntonetCommand:
        """
        Set encoder's audio mode to MPEG.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeMPEG
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode MPEG message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii9i", Command.COMMAND_ENCODER_GET_AUDIO_MODE_MPEG, 36,
                        arg.codec, arg.bit_rate, arg.audio_mode, arg.mpeg_layer, arg.frequency, arg.crc,
                        arg.aux_data, arg.encoder_mix, arg.bonding_type),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_aac(arg: CommandEncoderSetAudioModeAAC) -> ProntonetCommand:
        """
        Set encoder's audio mode to AAC.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeAAC
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode AAC message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii9i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_AAC, 36,
                        arg.codec, arg.bit_rate, arg.audio_mode, arg.aac_mode, arg.frequency, arg.crc,
                        arg.aux_data, arg.encoder_mix, arg.bonding_type),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g711(arg: CommandEncoderSetAudioModeG711) -> ProntonetCommand:
        """
        Set encoder's audio mode to G711.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeG711
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode G711 message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711, 8,
                        arg.codec, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g722(arg: CommandEncoderSetAudioModeG722) -> ProntonetCommand:
        """
        Set encoder's audio mode to G722.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeG722
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode G722 message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711, 8,
                        arg.codec, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_auto(arg: CommandEncoderSetAudioModeAuto) -> ProntonetCommand:
        """
        Set encoder's audio mode to AUTO.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeAuto
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode AUTO message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_AUTO, 8,
                        arg.codec, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_aptx(arg: CommandEncoderSetAudioModeAPTX) -> ProntonetCommand:
        """
        Set encoder's audio mode to APTX.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeAPTX
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode APTX message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii7i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_APTX, 28,
                        arg.codec, arg.audio_mode, arg.aptx_type, arg.frequency,
                        arg.crc, arg.aux_data, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g711_v2(arg: CommandEncoderSetAudioModeG711v2) -> ProntonetCommand:
        """
        Set encoder's audio mode to G711.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeG711v2
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode G711v2 message, struct.unpack() pattern for response
            and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii3i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711_V2, 12,
                        arg.codec, arg.encoder_mix, arg.g711_law),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g722_v2(arg: CommandEncoderSetAudioModeG722v2) -> ProntonetCommand:
        """
        Set encoder's audio mode to G722.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeG722v2
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode G722v2 message, struct.unpack() pattern for response
            and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii3i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G722_V2, 12,
                        arg.codec, arg.encoder_mix, arg.g722_dither),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_mpeg_v2(arg: CommandEncoderSetAudioModeMPEGv2) -> ProntonetCommand:
        """
        Set encoder's audio mode to MPEG.

        Parameters
        ----------
        arg : CommandEncoderSetAudioModeMPEGv2
            Settings to be applied on device.

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode MPEGv2 message, struct.unpack() pattern for response
            and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii10i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_MPEG_V2, 40,
                        arg.codec, arg.bit_rate, arg.audio_mode, arg.mpeg_layer, arg.frequency,
                        arg.crc, arg.aux_data, arg.encoder_mix, arg.bonding_type, arg.mpeg_l3_polarity),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_ip_streaming_protocol() -> ProntonetCommand:
        """
        Get actual IP streaming protocol.

        Returns
        -------
        ProntonetCommand
            Dataclass with get IP streaming protocol message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_IP_GET_STREAMING_PROTOCOL, 0),
            "iii",
            StreamingProtocol
        )

    @staticmethod
    def set_ip_streaming_protocol(arg: CommandIPSetStreamingProtocol) -> ProntonetCommand:
        """
        Set IP streaming protocol.

        Parameters
        ----------
        arg : CommandIPSetStreamingProtocol
            Settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with set IP streaming protocol message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_IP_SET_STREAMING_PROTOCOL, 4, arg.streaming_protocol),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def x21_enable_tx(arg: CommandX21EnableTX) -> ProntonetCommand:
        """
        Enable or disable the transmission of the X21 interface (clock + data).

        Parameters
        ----------
        arg : CommandX21EnableTX
            Settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with x21 enable/disable message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_IP_SET_STREAMING_PROTOCOL, 4, arg.enable),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def load_preset(arg: CommandLoadPreset) -> ProntonetCommand:
        """
        Load and apply the specified preset.

        Parameters
        ----------
        arg : CommandLoadPreset
            Settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with load preset message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_LOAD_PRESET, 255)
            + arg.name[0:255].ljust(255, '\x00').encode("utf-8"),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def call_from_book(arg: CommandCallFromBook) -> ProntonetCommand:
        """
        Make a call using phonebook.

        Parameters
        ----------
        arg : CommandCallFromBook
            Dataclass with line number and book entry.

        Returns
        -------
        ProntonetCommand
            Dataclass with call from book message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_CALL_FROM_BOOK, 8, arg.line, arg.book_entry),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def alarms_ack() -> ProntonetCommand:
        """
        Acknowledge all the alarms from the alarms history.

        Returns
        -------
        ProntonetCommand
            Dataclass with alarms acknowledge message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_ACK, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def alarms_delete() -> ProntonetCommand:
        """
        Delete all the alarms from the alarms history.

        Returns
        -------
        ProntonetCommand
            Dataclass with alarms delete message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_DELETE, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def call_from_book_all_lines(arg: CommandCallFromBookAllLines) -> ProntonetCommand:
        """
        Make a call using phonebook to all the lines specified in the phonebook.

        Parameters
        ----------
        arg : CommandCallFromBookAllLines
            Dataclass which specifies phonebook entry ID.

        Returns
        -------
        ProntonetCommand
            Dataclass with call from book using all lines message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_CALL_FROM_BOOK_ALL_LINES, 4, arg.book_entry),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_device_net_v2() -> ProntonetCommand:
        """
        Get the network in use and its parameters.

        Returns
        -------
        ProntonetCommand
            Dataclass with get device network V2 message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_DEVICE_NET_V2, 0),
            "ii5i",
            CommandDeviceNetV2
        )

    @staticmethod
    def set_device_net_v2(arg: CommandDeviceNetV2) -> ProntonetCommand:
        """
        Set the network and its parameters.
        Several restrictions apply to the parameters (not all the combinations are allowed).

        Parameters
        ----------
        arg : CommandDeviceNetV2
            Dataclass which contains DeviceNet, DeviceSubNet, ProntonetCodecMode, MultiUnicast
            and StreamingProtocol settings.

        Returns
        -------
        ProntonetCommand
            Dataclass with set device network V2 message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii5i", Command.COMMAND_SET_DEVICE_NET_V2, 20, arg.device_net, arg.device_sub_net,
                        arg.pronto_net_codec_mode, arg.multi_unicast, arg.streaming_protocol),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def call_v2(arg: CommandCallV2) -> ProntonetCommand:
        """
        Make a call. Current connection (if any) will be disconnected before trying the new call.

        Parameters
        ----------
        arg : CommandCallV2
            Dataclass which contains line number, callee number, IPCallType and Codec settings.

        Returns
        -------
        ProntonetCommand
            Dataclass with call V2 message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_CALL_V2, 44, arg.line)
            + arg.number[0:32].ljust(32, '\x00').encode("utf-8")
            + struct.pack("<ii", arg.ip_call_type, arg.target_codec),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_loaded_preset_index() -> ProntonetCommand:
        """
        Get the index of the current loaded preset.

        Returns
        -------
        ProntonetCommand
            Dataclass with get loaded preset index message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_LOADED_PRESET_INDEX, 0),
            "iii",
            CommandGetLoadedPresetIndex
        )

    @staticmethod
    def run_gpi_action(arg: CommandRunGPIAction) -> ProntonetCommand:
        """
        Execute a GPI action.

        Parameters
        ----------
        arg : CommandRunGPIAction
            Dataclass which contains GPI number and active/not active information.

        Returns
        -------
        ProntonetCommand
            Dataclass with run GPI action message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_RUN_GPI_ACTION, 8, arg.gpi, arg.active),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def enable_net_backup(arg: CommandEnableNetBackup) -> ProntonetCommand:
        """
        Enable/disable the network backup feature.

        Parameters
        ----------
        arg : CommandEnableNetBackup
            Settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with enable/disable network backup message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENABLE_NET_BACKUP, 4, arg.enable),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def reset_device() -> ProntonetCommand:
        """
        Reboot the system.

        Returns
        -------
        ProntonetCommand
            Dataclass with reset device message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_RESET_DEVICE, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_loaded_preset_name() -> ProntonetCommand:
        """
        Get the name of the last loaded preset configuration.

        Returns
        -------
        ProntonetCommand
            Dataclass with get loaded preset name message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_LOADED_PRESET_NAME, 0),
            "#",
            bytes
        )

    @staticmethod
    def get_streaming_stats(arg: CommandGetStreamingStats) -> ProntonetCommand:
        """
        Get streaming statistics for a specific codec.

        Parameters
        ----------
        arg : CommandGetStreamingStats
            Command settings (codec index).

        Returns
        -------
        ProntonetCommand
            Dataclass with get streaming statistics message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_STREAMING_STATS, 20, arg.target_codec),
            "ii4i",
            CommandGetStreamingStatsResponse
        )

    @staticmethod
    def get_sip_server_register_status() -> ProntonetCommand:
        """
        Get the status of the SIP server.

        Returns
        -------
        ProntonetCommand
            Dataclass with get SIP server registration status message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_SIP_SERVER_REGISTER_STATUS, 0),
            "iii",
            CommandGetSIPServerRegisterStatus
        )

    @staticmethod
    def get_stun_server_register_status() -> ProntonetCommand:
        """
        Get the status of the STUN server.

        Returns
        -------
        ProntonetCommand
            Dataclass with get STUN server registration status message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_STUN_SERVER_REGISTER_STATUS, 0),
            "iii",
            CommandGetSTUNServerRegisterStatus
        )

    @staticmethod
    def get_call_duration(arg: CommandGetCallDuration) -> ProntonetCommand:
        """
        Get the current duration of one active call in seconds.

        Parameters
        ----------
        arg : CommandGetCallDuration
            Command parameter (line number).

        Returns
        -------
        ProntonetCommand
            Dataclass with get call duration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_CALL_DURATION, 4, arg.line),
            "iii",
            CommandGetCallDurationResponse
        )

    @staticmethod
    def alarms_get_log() -> ProntonetCommand:
        """
        Get machine's alarms log as string which can be saved in an XML file.

        Returns
        -------
        ProntonetCommand
            Dataclass with get alarms log message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_GET_LOG, 0),
            "ii#",
            bytes
        )

    @staticmethod
    def get_audio_configuration() -> ProntonetCommand:
        """
        Get the machine's audio configuration (only if it is stationary unit, not a portable one).

        Returns
        -------
        ProntonetCommand
            Dataclass with get audio configuration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_AUDIO_GET_CONFIGURATION, 0),
            "ii6i",
            CommandAudioGetConfigurationResponse
        )

    @staticmethod
    def set_audio_configuration(arg: CommandAudioSetConfiguration) -> ProntonetCommand:
        """
        Set the machine's audio configuration (only if it is stationary unit, not a portable one).

        Parameters
        ----------
        arg : CommandAudioSetConfiguration
            Settings to be applied (AudioConfig - the audio mode, dB left input, dB right input, dB left output,
            dB right output).

        Returns
        -------
        ProntonetCommand
            Dataclass with set audio configuration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii5i", Command.COMMAND_AUDIO_SET_CONFIGURATION, 20,
                        arg.audio_config, arg.db_in_left, arg.db_in_right, arg.db_out_left, arg.db_out_right),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_device_name() -> ProntonetCommand:
        """
        Get device's configured name.

        Returns
        -------
        ProntonetCommand
            Dataclass with get device's name message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SYS_GET_DEVICE_NAME, 0),
            "ii#",
            bytes
        )

    @staticmethod
    def set_device_name(arg: CommandSysDeviceName) -> ProntonetCommand:
        """
        Set the device name.

        Parameters
        ----------
        arg : CommandSysDeviceName
            Dataclass which contains new device name.

        Returns
        -------
        ProntonetCommand
            Dataclass with set device's name message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SYS_SET_DEVICE_NAME, 256)
            + arg.device_name[0:256].ljust(256, '\x00').encode("utf-8"),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def blink_device() -> ProntonetCommand:
        """
        Blink the front LEDs of the unit for some seconds.

        Returns
        -------
        ProntonetCommand
            Dataclass with blink device message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SYS_BLINK_DEVICE, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_version_info() -> ProntonetCommand:
        """
        Get the device's serial number and software version.

        Returns
        -------
        ProntonetCommand
            Dataclass with get version info message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SYS_GET_VERSION_INFO, 0),
            "ii16s16s",
            CommandSysGetVersionInfo
        )

    @staticmethod
    def get_sip_configuration() -> ProntonetCommand:
        """
        Get the configuration parameters of the SIP protocol from the unit.

        Returns
        -------
        ProntonetCommand
            Dataclass with get SIP configuration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SIP_GET_CONFIGURATION, 0),
            "iiiiiiiii256s256s256s256sii256s256si",
            CommandSIPConfiguration
        )

    @staticmethod
    def set_sip_configuration(arg: CommandSIPConfiguration) -> ProntonetCommand:
        """
        Set the configuration parameters of the SIP protocol of the unit.

        Parameters
        ----------
        arg : CommandSIPConfiguration
            SIP settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with set SIP configuration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SIP_SET_CONFIGURATION, 1576)
            + struct.pack("<7i", arg.sip_port, arg.audio_port, arg.auto_answer, arg.enable_fec, arg.fec_port,
                          arg.audio_packets_per_fec_packet, arg.register_in_server)
            + arg.sip_user_name[0:256].ljust(256, '\x00').encode("utf-8")
            + arg.sip_server_address[0:256].ljust(256, '\x00').encode("utf-8")
            + arg.sip_server_user[0:256].ljust(256, '\x00').encode("utf-8")
            + arg.sip_server_password[0:256].ljust(256, '\x00').encode("utf-8")
            + struct.pack("<ii", arg.sip_server_timeout, arg.sip_address_type)
            + arg.public_address[0:256].ljust(256, '\x00').encode("utf-8")
            + arg.stun_address[0:256].ljust(256, '\x00').encode("utf-8")
            + struct.pack("<i", arg.stun_request_period),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_configuration_v4() -> ProntonetCommand:
        """
        Get the configuration parameters of the Prodys' Proprietary Protocol V4 from the unit.

        Returns
        -------
        ProntonetCommand
            Dataclass with get PP V4 configuration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_PRODYS_V4_GET_CONFIGURATION, 0),
            "ii6i",
            CommandProdysV4ConfigurationResponse
        )

    @staticmethod
    def set_configuration_v4(arg: CommandProdysV4Configuration) -> ProntonetCommand:
        """
        Set the configuration parameters of the Prodys' Proprietary Protocol V4 of the unit.

        Parameters
        ----------
        arg : CommandProdysV4Configuration
            Settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with set PP V4 configuration message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii6i", Command.COMMAND_PRODYS_V4_SET_CONFIGURATION, 24, arg.line_1_port,
                        arg.enable_control_port, arg.auto_answer, arg.enable_fec, arg.audio_packets_per_fec_packet,
                        arg.fec_delay),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_streaming_tx_codec_configuration(arg: CommandStreamingTXCodecGetConfiguration) -> ProntonetCommand:
        """
        Get the configuration parameters of the streaming TX for a given codec and audio algorithm.

        Parameters
        ----------
        arg : CommandStreamingTXCodecGetConfiguration
            Command parameters (Codec and AudioAlgorithm).

        Returns
        -------
        ProntonetCommand
            Dataclass with get streaming TX codec configuration message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_STREAMING_TX_GET_CODEC_CONFIGURATION,
                        arg.codec, arg.audio_algorithm),
            "iiii",
            CommandStreamingTXCodecGetConfigurationResponse
        )

    @staticmethod
    def set_streaming_tx_codec_configuration(arg: CommandStreamingTXCodecSetConfiguration) -> ProntonetCommand:
        """
        Set the configuration parameters of the streaming TX for a given codec.

        Parameters
        ----------
        arg : CommandStreamingTXCodecSetConfiguration
            Command parameters (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with set streaming TX codec configuration message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii3i", Command.COMMAND_STREAMING_TX_SET_CODEC_CONFIGURATION,
                        arg.codec, arg.audio_algorithm, arg.time_between_packets),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_streaming_rx_codec_configuration(arg: CommandStreamingRXCodecGetConfiguration) -> ProntonetCommand:
        """
        Get the configuration parameters of the streaming RX for a given codec.

        Parameters
        ----------
        arg : CommandStreamingRXCodecGetConfiguration
            Command parameters (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get streaming RX codec configuration message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_STREAMING_RX_GET_CODEC_CONFIGURATION, 4, arg.codec),
            "ii7i",
            CommandStreamingRXCodecGetConfigurationResponse
        )

    @staticmethod
    def set_streaming_rx_codec_configuration(arg: CommandStreamingRXCodecSetConfiguration) -> ProntonetCommand:
        """
        Set the configuration parameters of the streaming RX for a given codec.

        Parameters
        ----------
        arg : CommandStreamingRXCodecSetConfiguration
            Settings to be applied.

        Returns
        -------
        ProntonetCommand
            Dataclass with set streaming RX codec configuration message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii7i", Command.COMMAND_STREAMING_RX_SET_CODEC_CONFIGURATION, 28,
                        arg.codec, arg.auto_adjustment, arg.auto_min_delay, arg.auto_min_delay_duration,
                        arg.auto_max_delay, arg.auto_max_delay_duration, arg.manual_max_delay),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_streaming_stats_v2(arg: CommandGetStreamingStatsV2) -> ProntonetCommand:
        """
        Get the extended streaming statistics for a given codec.

        Parameters
        ----------
        arg : CommandGetStreamingStatsV2
            Command parameters (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get streaming statistics V2 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_STREAMING_STATS_V2, 4, arg.codec),
            "ii10i",
            CommandGetStreamingStatsV2Response
        )

    @staticmethod
    def get_ethernet_speed(arg: CommandEthernetGetSpeed) -> ProntonetCommand:
        """
        Get the current negotiated speed on a given Ethernet interface.

        Parameters
        ----------
        arg : CommandEthernetGetSpeed
            Command parameters (EthernetInterface).

        Returns
        -------
        ProntonetCommand
            Dataclass with get ethernet speed message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ETHERNET_GET_SPEED, 4, arg.ethernet_interface),
            "ii3i",
            CommandEthernetGetSpeedResponse
        )

    @staticmethod
    def streaming_stats_reset(arg: CommandStreamingStatsReset) -> ProntonetCommand:
        """
        Clear the full streaming statistics for a given codec, or both.

        Parameters
        ----------
        arg : CommandStreamingStatsReset
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with reset streaming statistics message, struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_STREAMING_STATS_RESET, 4, arg.codec),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_pcm_v2(arg: CommandAudioModeConfigPCMV2) -> ProntonetCommand:
        """
        Set the audio configuration for a given codec with PCM algorithm.

        Parameters
        ----------
        arg : CommandAudioModeConfigPCMV2
            Settings to be applied (Codec, BitsSample, AudioMode, EncoderMix, AuxData).

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode PCM V2 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii5i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_PCM_V2, 20,
                        arg.codec, arg.bits_sample, arg.audio_mode, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g711_v3(arg: CommandAudioModeConfigG711V3) -> ProntonetCommand:
        """
        Set the audio configuration for a given codec with G711 algorithm.

        Parameters
        ----------
        arg : CommandAudioModeConfigG711V3
            Settings to be applied (Codec, G711Law, EncoderMix, AuxData).

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode G711 V3 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711_V3, 16,
                        arg.codec, arg.g711_law, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g722_v3(arg: CommandAudioModeConfigG722V3) -> ProntonetCommand:
        """
        Set the audio configuration for a given codec with G722 algorithm.

        Parameters
        ----------
        arg : CommandAudioModeConfigG722V3
            Settings to be applied (Codec, EncoderMix, AuxData, G722Dither).

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode G722 V3 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G722_V3, 16,
                        arg.codec, arg.encoder_mix, arg.aux_data, arg.g722_dither),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_aptx_v2(arg: CommandAudioModeConfigAPTXV2) -> ProntonetCommand:
        """
        Set the audio configuration for a given codec with APTX algorithm.

        Parameters
        ----------
        arg : CommandAudioModeConfigAPTXV2
            Settings to be applied (Codec, APTXType, BitRate, AudioMode, EncoderMix, AuxData).

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode APTX V2 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii6i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_APTX_V2, 24,
                        arg.codec, arg.aptx_type, arg.bit_rate, arg.audio_mode, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_encoder_audio_mode_algorithm(arg: CommandGetAudioModeAlgorithm) -> ProntonetCommand:
        """
        Get the current audio algorithm family configured on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandGetAudioModeAlgorithm
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode algorithm message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_ALGORITHM, 4, arg.codec),
            "ii2i",
            CommandEncoderGetAudioModeAlgorithmResponse
        )

    @staticmethod
    def get_decoder_audio_mode_algorithm(arg: CommandGetAudioModeAlgorithm) -> ProntonetCommand:
        """
        Get the current audio algorithm family configured on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandGetAudioModeAlgorithm
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode algorithm message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_ALGORITHM, 4, arg.codec),
            "ii3i",
            CommandDecoderGetAudioModeAlgorithmResponse
        )

    @staticmethod
    def get_encoder_audio_mode_auto(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current AUTO configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode auto message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_AUTO, 4, arg.codec),
            "ii2i",
            CommandEncoderGetAudioModeAutoResponse
        )

    @staticmethod
    def get_encoder_audio_mode_pcm(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current PCM configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode PCM message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_PCM, 4, arg.codec),
            "ii5i",
            CommandEncoderGetAudioModePCMResponse
        )

    @staticmethod
    def get_encoder_audio_mode_g711(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current G711 configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode G711 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_G711, 4, arg.codec),
            "ii4i",
            CommandEncoderGetAudioModeG711Response
        )

    @staticmethod
    def get_encoder_audio_mode_g722(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current G722 configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode G722 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_G722, 4, arg.codec),
            "ii4i",
            CommandEncoderGetAudioModeG722Response
        )

    @staticmethod
    def get_encoder_audio_mode_mpeg(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current MPEG configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode MPEG message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_MPEG, 4, arg.codec),
            "ii10i",
            CommandEncoderGetAudioModeMPEGResponse
        )

    @staticmethod
    def get_encoder_audio_mode_acc(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current AAC configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode AAC message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_AAC, 4, arg.codec),
            "ii9i",
            CommandEncoderGetAudioModeAACResponse
        )

    @staticmethod
    def get_encoder_audio_mode_aptx(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current APTX configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode APTX message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_APTX, 4, arg.codec),
            "ii6i",
            CommandEncoderGetAudioModeAPTXResponse
        )

    @staticmethod
    def get_decoder_audio_mode_pcm(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current PCM configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode PCM message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_PCM, 4, arg.codec),
            "ii5i",
            CommandDecoderGetAudioModePCMResponse
        )

    @staticmethod
    def get_decoder_audio_mode_g711(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current G711 configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode G711 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_G711, 4, arg.codec),
            "ii4i",
            CommandDecoderGetAudioModeG711Response
        )

    @staticmethod
    def get_decoder_audio_mode_g722(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current G722 configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode G722 message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_G722, 4, arg.codec),
            "ii4i",
            CommandDecoderGetAudioModeG722Response
        )

    @staticmethod
    def get_decoder_audio_mode_mpeg(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current MPEG configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode MPEG message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_MPEG, 4, arg.codec),
            "ii10i",
            CommandDecoderGetAudioModeMPEGResponse
        )

    @staticmethod
    def get_decoder_audio_mode_aac(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current AAC configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode AAC message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_AAC, 4, arg.codec),
            "ii9i",
            CommandDecoderGetAudioModeAACResponse
        )

    @staticmethod
    def get_decoder_audio_mode_aptx(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current APTX configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode APTX message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_APTX, 4, arg.codec),
            "ii6i",
            CommandDecoderGetAudioModeAPTXResponse
        )

    @staticmethod
    def set_encoder_audio_mode_opus(arg: CommandAudioModeOPUS) -> ProntonetCommand:
        """
        Set the audio configuration for a given codec with an OPUS algorithm.

        Parameters
        ----------
        arg : CommandAudioModeOPUS
            Command parameter (Codec, BitRate, EncoderMix, AuxData).

        Returns
        -------
        ProntonetCommand
            Dataclass with set encoder audio mode OPUS message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_OPUS, 16,
                        arg.codec, arg.bit_rate, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_encoder_audio_mode_opus(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current OPUS configuration details on the encoder for a given codec.

        Parameters
        ----------
        arg : CommandEncoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get encoder audio mode OPUS message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_OPUS, 4, arg.codec),
            "ii4i",
            CommandAudioModeOPUS
        )

    @staticmethod
    def get_decoder_audio_mode_opus(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        """
        Get the current OPUS configuration details on the decoder for a given codec.

        Parameters
        ----------
        arg : CommandDecoderGetAudioMode
            Command parameter (Codec).

        Returns
        -------
        ProntonetCommand
            Dataclass with get decoder audio mode OPUS message,
            struct.unpack() pattern for response and response type.
        """

        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_OPUS, 4, arg.codec),
            "ii4i",
            CommandAudioModeOPUS
        )
