from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtfb:
	"""Rtfb commands group definition. 16 total commands, 0 Subgroups, 16 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtfb", core, parent)

	def get_aack(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:AACK \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.rtfb.get_aack() \n
		If enabled, the signal generator will not use any external HARQ feedback from the DUT for its HARQ processes until an ACK
		command is received the first time. \n
			:return: assume_ack: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:AACK?')
		return Conversions.str_to_bool(response)

	def set_aack(self, assume_ack: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:AACK \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_aack(assume_ack = False) \n
		If enabled, the signal generator will not use any external HARQ feedback from the DUT for its HARQ processes until an ACK
		command is received the first time. \n
			:param assume_ack: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(assume_ack)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:AACK {param}')

	# noinspection PyTypeChecker
	def get_ack_definition(self) -> enums.LowHigh:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ACKDefinition \n
		Snippet: value: enums.LowHigh = driver.source.bb.eutra.uplink.rtfb.get_ack_definition() \n
		(Binary ACK/NACK mode only) Determines whether a high or a low binary level on the feedback line connector represents an
		ACK. \n
			:return: ack_definition: HIGH| LOW
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ACKDefinition?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_ack_definition(self, ack_definition: enums.LowHigh) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ACKDefinition \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_ack_definition(ack_definition = enums.LowHigh.HIGH) \n
		(Binary ACK/NACK mode only) Determines whether a high or a low binary level on the feedback line connector represents an
		ACK. \n
			:param ack_definition: HIGH| LOW
		"""
		param = Conversions.enum_scalar_to_str(ack_definition, enums.LowHigh)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ACKDefinition {param}')

	def get_adu_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ADUDelay \n
		Snippet: value: float = driver.source.bb.eutra.uplink.rtfb.get_adu_delay() \n
		Determines the point in time when the feedback can be sent to the instrument.
			Table Header: Mode / Value Range \n
			- Binary / 3GPP Distance Mode: -1 to 2.99 subframes
			- Direct Response Distance Mode: +1 to 6.99 subframes
			- Serial and Serial 3x8 / 'UE x > Config > 3GPP Release = Release 8/9 or LTE-Advanced': -1 to 1.99 subframes 'UE x > Config > 3GPP Release = eMTC/NB-IoT': -18 to -0.3 subframes \n
			:return: add_user_delay: float Range: depends on the feedback mode and the installed options , Unit: Subframes
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ADUDelay?')
		return Conversions.str_to_float(response)

	def set_adu_delay(self, add_user_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ADUDelay \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_adu_delay(add_user_delay = 1.0) \n
		Determines the point in time when the feedback can be sent to the instrument.
			Table Header: Mode / Value Range \n
			- Binary / 3GPP Distance Mode: -1 to 2.99 subframes
			- Direct Response Distance Mode: +1 to 6.99 subframes
			- Serial and Serial 3x8 / 'UE x > Config > 3GPP Release = Release 8/9 or LTE-Advanced': -1 to 1.99 subframes 'UE x > Config > 3GPP Release = eMTC/NB-IoT': -18 to -0.3 subframes \n
			:param add_user_delay: float Range: depends on the feedback mode and the installed options , Unit: Subframes
		"""
		param = Conversions.decimal_value_to_str(add_user_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ADUDelay {param}')

	def get_bb_selector(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BBSelector \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_bb_selector() \n
		In serial mode, required for multiplexing serial commands for different basebands to one feedback line. \n
			:return: baseband_select: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BBSelector?')
		return Conversions.str_to_int(response)

	def set_bb_selector(self, baseband_select: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BBSelector \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_bb_selector(baseband_select = 1) \n
		In serial mode, required for multiplexing serial commands for different basebands to one feedback line. \n
			:param baseband_select: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(baseband_select)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BBSelector {param}')

	# noinspection PyTypeChecker
	def get_be_insertion(self) -> enums.FeedbackBlerMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BEINsertion \n
		Snippet: value: enums.FeedbackBlerMode = driver.source.bb.eutra.uplink.rtfb.get_be_insertion() \n
		Enables/disables the statistical insertion of block errors into PUSCH packets. The block error insertion can be enabled
		for a single HARQ process or for all processes. In the single HARQ process case, the used process is always the one that
		corresponds to the first activated PUSCH. \n
			:return: block_err_insert: OFF| FPRocess| APRocesses
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BEINsertion?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackBlerMode)

	def set_be_insertion(self, block_err_insert: enums.FeedbackBlerMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BEINsertion \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_be_insertion(block_err_insert = enums.FeedbackBlerMode.APRocesses) \n
		Enables/disables the statistical insertion of block errors into PUSCH packets. The block error insertion can be enabled
		for a single HARQ process or for all processes. In the single HARQ process case, the used process is always the one that
		corresponds to the first activated PUSCH. \n
			:param block_err_insert: OFF| FPRocess| APRocesses
		"""
		param = Conversions.enum_scalar_to_str(block_err_insert, enums.FeedbackBlerMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BEINsertion {param}')

	def get_bit_error_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BERate \n
		Snippet: value: float = driver.source.bb.eutra.uplink.rtfb.get_bit_error_rate() \n
		Block error rate for the statistical insertion of block errors. \n
			:return: block_err_rate: float Range: 0.0001 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BERate?')
		return Conversions.str_to_float(response)

	def set_bit_error_rate(self, block_err_rate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BERate \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_bit_error_rate(block_err_rate = 1.0) \n
		Block error rate for the statistical insertion of block errors. \n
			:param block_err_rate: float Range: 0.0001 to 1
		"""
		param = Conversions.decimal_value_to_str(block_err_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BERate {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnector:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:CONNector \n
		Snippet: value: enums.FeedbackConnector = driver.source.bb.eutra.uplink.rtfb.get_connector() \n
		Determines the feedback line connector. \n
			:return: connector: LOCal| GLOBal LOCal T/M 3 connector for R&S SMW-B10 T/M 2 connector for R&S SMW-B9 GLOBal (reserved for future use) USER 6 connector
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnector)

	def set_connector(self, connector: enums.FeedbackConnector) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:CONNector \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_connector(connector = enums.FeedbackConnector.GLOBal) \n
		Determines the feedback line connector. \n
			:param connector: LOCal| GLOBal LOCal T/M 3 connector for R&S SMW-B10 T/M 2 connector for R&S SMW-B9 GLOBal (reserved for future use) USER 6 connector
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnector)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:CONNector {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.FeedbackDistMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:DMODe \n
		Snippet: value: enums.FeedbackDistMode = driver.source.bb.eutra.uplink.rtfb.get_dmode() \n
		Determines how the number of the uplink subframe is calculated, in which the signaled feedback has the desired effect. \n
			:return: distance_mode: STD| DIRect
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackDistMode)

	def set_dmode(self, distance_mode: enums.FeedbackDistMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:DMODe \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_dmode(distance_mode = enums.FeedbackDistMode.DIRect) \n
		Determines how the number of the uplink subframe is calculated, in which the signaled feedback has the desired effect. \n
			:param distance_mode: STD| DIRect
		"""
		param = Conversions.enum_scalar_to_str(distance_mode, enums.FeedbackDistMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:DMODe {param}')

	def get_gen_reports(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:GENReports \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.rtfb.get_gen_reports() \n
		Triggers the instrument to create and store transmission and/or reception realtime feedback debug reports. \n
			:return: gen_debug_reports: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:GENReports?')
		return Conversions.str_to_bool(response)

	def set_gen_reports(self, gen_debug_reports: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:GENReports \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_gen_reports(gen_debug_reports = False) \n
		Triggers the instrument to create and store transmission and/or reception realtime feedback debug reports. \n
			:param gen_debug_reports: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(gen_debug_reports)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:GENReports {param}')

	def get_it_advance(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITADvance \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_it_advance() \n
		The initial timing advance of the uplink signal (at the output of the instrument's baseband unit) in units of 16 TS. \n
			:return: init_tim_advance: integer Range: 0 to 1282
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITADvance?')
		return Conversions.str_to_int(response)

	def set_it_advance(self, init_tim_advance: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITADvance \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_it_advance(init_tim_advance = 1) \n
		The initial timing advance of the uplink signal (at the output of the instrument's baseband unit) in units of 16 TS. \n
			:param init_tim_advance: integer Range: 0 to 1282
		"""
		param = Conversions.decimal_value_to_str(init_tim_advance)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITADvance {param}')

	def get_ita_feedback(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITAFeedback \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.rtfb.get_ita_feedback() \n
		If enabled the instrument ignores timing adjustment feedback. For missing feedback, no error message is indicated.
		If disabled, the instrument indicates error for missing TA adjustment command from the base station. \n
			:return: ignore_timing_adj: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITAFeedback?')
		return Conversions.str_to_bool(response)

	def set_ita_feedback(self, ignore_timing_adj: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITAFeedback \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_ita_feedback(ignore_timing_adj = False) \n
		If enabled the instrument ignores timing adjustment feedback. For missing feedback, no error message is indicated.
		If disabled, the instrument indicates error for missing TA adjustment command from the base station. \n
			:param ignore_timing_adj: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ignore_timing_adj)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITAFeedback {param}')

	def get_loffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:LOFFset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_loffset() \n
		Delays the start time for generation of the debug report files. \n
			:return: logging_offset: integer Range: 0 to 100000000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:LOFFset?')
		return Conversions.str_to_int(response)

	def set_loffset(self, logging_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:LOFFset \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_loffset(logging_offset = 1) \n
		Delays the start time for generation of the debug report files. \n
			:param logging_offset: integer Range: 0 to 100000000
		"""
		param = Conversions.decimal_value_to_str(logging_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:LOFFset {param}')

	def get_max_trans(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MAXTrans \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_max_trans() \n
		After this maximum number of transmissions (incl. first transmission) , the first redundancy version of the redundancy
		version sequence is used even in case of NACK. \n
			:return: max_transmission: integer Range: 1 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MAXTrans?')
		return Conversions.str_to_int(response)

	def set_max_trans(self, max_transmission: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MAXTrans \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_max_trans(max_transmission = 1) \n
		After this maximum number of transmissions (incl. first transmission) , the first redundancy version of the redundancy
		version sequence is used even in case of NACK. \n
			:param max_transmission: integer Range: 1 to 20
		"""
		param = Conversions.decimal_value_to_str(max_transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MAXTrans {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FeedbackMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MODE \n
		Snippet: value: enums.FeedbackMode = driver.source.bb.eutra.uplink.rtfb.get_mode() \n
		Enables realtime feedback and determines the mode (binary or serial) . \n
			:return: mode: OFF| SERial| S3X8 | BAN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackMode)

	def set_mode(self, mode: enums.FeedbackMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MODE \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_mode(mode = enums.FeedbackMode.BAN) \n
		Enables realtime feedback and determines the mode (binary or serial) . \n
			:param mode: OFF| SERial| S3X8 | BAN
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FeedbackMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MODE {param}')

	def get_rv_sequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:RVSequence \n
		Snippet: value: str = driver.source.bb.eutra.uplink.rtfb.get_rv_sequence() \n
		Determines the sequence of redundancy versions for the individual HARQ processes. Unless otherwise requested by serial
		feedback commands, the first value in the sequence of redundancy versions is used each time an ACK is received or for the
		very first transmission of a process. The sequence of redundancy versions is read out cyclically, i.e. whenever a NACK is
		received and a retransmission is requested, the next redundancy version in the sequence is used. The first value in the
		sequence is used again even in case a NACK is received, if the maximum number of transmissions (BB:EUTR:UL:RTFB:MAXT) in
		a process was reached. \n
			:return: red_vers_sequence: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:RVSequence?')
		return trim_str_response(response)

	def set_rv_sequence(self, red_vers_sequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:RVSequence \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_rv_sequence(red_vers_sequence = '1') \n
		Determines the sequence of redundancy versions for the individual HARQ processes. Unless otherwise requested by serial
		feedback commands, the first value in the sequence of redundancy versions is used each time an ACK is received or for the
		very first transmission of a process. The sequence of redundancy versions is read out cyclically, i.e. whenever a NACK is
		received and a retransmission is requested, the next redundancy version in the sequence is used. The first value in the
		sequence is used again even in case a NACK is received, if the maximum number of transmissions (BB:EUTR:UL:RTFB:MAXT) in
		a process was reached. \n
			:param red_vers_sequence: string
		"""
		param = Conversions.value_to_quoted_str(red_vers_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:RVSequence {param}')

	# noinspection PyTypeChecker
	def get_ser_rte(self) -> enums.EutraSerialRate:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:SERate \n
		Snippet: value: enums.EutraSerialRate = driver.source.bb.eutra.uplink.rtfb.get_ser_rte() \n
		(Serial mode only) Determines the bit rate of the serial transmission. \n
			:return: serial_rate: SR115_2K| SR1_92M| SR1_6M
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:SERate?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSerialRate)

	def set_ser_rte(self, serial_rate: enums.EutraSerialRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:SERate \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_ser_rte(serial_rate = enums.EutraSerialRate.SR1_6M) \n
		(Serial mode only) Determines the bit rate of the serial transmission. \n
			:param serial_rate: SR115_2K| SR1_92M| SR1_6M
		"""
		param = Conversions.enum_scalar_to_str(serial_rate, enums.EutraSerialRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:SERate {param}')
