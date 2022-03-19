from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hfb:
	"""Hfb commands group definition. 12 total commands, 0 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hfb", core, parent)

	def get_adj_cmd(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:ADJCmd \n
		Snippet: value: int = driver.source.bb.nr5G.hfb.get_adj_cmd() \n
		No command help available \n
			:return: init_timing_adj_cm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:ADJCmd?')
		return Conversions.str_to_int(response)

	def set_adj_cmd(self, init_timing_adj_cm: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:ADJCmd \n
		Snippet: driver.source.bb.nr5G.hfb.set_adj_cmd(init_timing_adj_cm = 1) \n
		No command help available \n
			:param init_timing_adj_cm: No help available
		"""
		param = Conversions.decimal_value_to_str(init_timing_adj_cm)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:ADJCmd {param}')

	def get_baseband(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:BASeband \n
		Snippet: value: int = driver.source.bb.nr5G.hfb.get_baseband() \n
		In serial mode, required for multiplexing serial commands for different basebands to one feedback line. See also Example
		'Configuring the 'Baseband Selector' for the 2 Tx antenna ports test cases'. \n
			:return: fb_baseband: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:BASeband?')
		return Conversions.str_to_int(response)

	def set_baseband(self, fb_baseband: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:BASeband \n
		Snippet: driver.source.bb.nr5G.hfb.set_baseband(fb_baseband = 1) \n
		In serial mode, required for multiplexing serial commands for different basebands to one feedback line. See also Example
		'Configuring the 'Baseband Selector' for the 2 Tx antenna ports test cases'. \n
			:param fb_baseband: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(fb_baseband)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:BASeband {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnectorAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:CONNector \n
		Snippet: value: enums.FeedbackConnectorAll = driver.source.bb.nr5G.hfb.get_connector() \n
		Sets the feedback line connector. \n
			:return: fb_connector: LOCal| GLOBal LOCal T/M 3 connector GLOBal (reserved for future use) USER 6 connector
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnectorAll)

	def set_connector(self, fb_connector: enums.FeedbackConnectorAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:CONNector \n
		Snippet: driver.source.bb.nr5G.hfb.set_connector(fb_connector = enums.FeedbackConnectorAll.LOCal) \n
		Sets the feedback line connector. \n
			:param fb_connector: LOCal| GLOBal LOCal T/M 3 connector GLOBal (reserved for future use) USER 6 connector
		"""
		param = Conversions.enum_scalar_to_str(fb_connector, enums.FeedbackConnectorAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:CONNector {param}')

	def get_cs_rate(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:CSRate \n
		Snippet: value: int = driver.source.bb.nr5G.hfb.get_cs_rate() \n
		No command help available \n
			:return: custom_ser_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:CSRate?')
		return Conversions.str_to_int(response)

	def set_cs_rate(self, custom_ser_rate: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:CSRate \n
		Snippet: driver.source.bb.nr5G.hfb.set_cs_rate(custom_ser_rate = 1) \n
		No command help available \n
			:param custom_ser_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(custom_ser_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:CSRate {param}')

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:DELay \n
		Snippet: value: float = driver.source.bb.nr5G.hfb.get_delay() \n
		Sets the point in time when the feedback can be sent to the instrument. \n
			:return: fb_user_delay: float Range: -20 to -1.0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, fb_user_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:DELay \n
		Snippet: driver.source.bb.nr5G.hfb.set_delay(fb_user_delay = 1.0) \n
		Sets the point in time when the feedback can be sent to the instrument. \n
			:param fb_user_delay: float Range: -20 to -1.0
		"""
		param = Conversions.decimal_value_to_str(fb_user_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:DELay {param}')

	def get_hpn_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:HPNMode \n
		Snippet: value: bool = driver.source.bb.nr5G.hfb.get_hpn_mode() \n
		Enables or disables the HARQ process number (HPN) mode. When the 'HPN Mode' is set to active, the additional user delay
		is set to -1.00 Slots and made unchangeable. An additional 'HARQ Process Number'parameter is accessible in the PUSCH
		settings ('PDSCH/PUSCH commands') . \n
			:return: hpn_mode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:HPNMode?')
		return Conversions.str_to_bool(response)

	def set_hpn_mode(self, hpn_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:HPNMode \n
		Snippet: driver.source.bb.nr5G.hfb.set_hpn_mode(hpn_mode = False) \n
		Enables or disables the HARQ process number (HPN) mode. When the 'HPN Mode' is set to active, the additional user delay
		is set to -1.00 Slots and made unchangeable. An additional 'HARQ Process Number'parameter is accessible in the PUSCH
		settings ('PDSCH/PUSCH commands') . \n
			:param hpn_mode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(hpn_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:HPNMode {param}')

	def get_log_path(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGPath \n
		Snippet: value: str = driver.source.bb.nr5G.hfb.get_log_path() \n
		Defines the output folder on the device for the log files. \n
			:return: log_gen_output_path: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:LOGPath?')
		return trim_str_response(response)

	def set_log_path(self, log_gen_output_path: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGPath \n
		Snippet: driver.source.bb.nr5G.hfb.set_log_path(log_gen_output_path = '1') \n
		Defines the output folder on the device for the log files. \n
			:param log_gen_output_path: string
		"""
		param = Conversions.value_to_quoted_str(log_gen_output_path)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:LOGPath {param}')

	def get_log_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGState \n
		Snippet: value: bool = driver.source.bb.nr5G.hfb.get_log_state() \n
		Enables the R&S SMW to create and store debug reports, i.e. log files with detailed information on the real-time feedback.
			INTRO_CMD_HELP: The instrument generates two types of reports: \n
			- Transmission report
			Table Header:  \n
			- This file contains information about what is sent (e.g. redundancy versions) during the first 100 slots after triggering.
			- File is created after the 100 slots are sent.
			- Reception report
			Table Header:  \n
			- This file contains information about the first 100 received serial commands.
			- File is created after 100 commands are successfully received.
		Use these debug files for troubleshooting of complex real-time feedback tests. \n
			:return: log_gen_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:LOGState?')
		return Conversions.str_to_bool(response)

	def set_log_state(self, log_gen_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGState \n
		Snippet: driver.source.bb.nr5G.hfb.set_log_state(log_gen_state = False) \n
		Enables the R&S SMW to create and store debug reports, i.e. log files with detailed information on the real-time feedback.
			INTRO_CMD_HELP: The instrument generates two types of reports: \n
			- Transmission report
			Table Header:  \n
			- This file contains information about what is sent (e.g. redundancy versions) during the first 100 slots after triggering.
			- File is created after the 100 slots are sent.
			- Reception report
			Table Header:  \n
			- This file contains information about the first 100 received serial commands.
			- File is created after 100 commands are successfully received.
		Use these debug files for troubleshooting of complex real-time feedback tests. \n
			:param log_gen_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(log_gen_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:LOGState {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FeedbackModeWithEthernet:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:MODE \n
		Snippet: value: enums.FeedbackModeWithEthernet = driver.source.bb.nr5G.hfb.get_mode() \n
		Enables real-time feedback and determines the mode of the feedback line. \n
			:return: fb_mode: OFF| SERial| S3X8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackModeWithEthernet)

	def set_mode(self, fb_mode: enums.FeedbackModeWithEthernet) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:MODE \n
		Snippet: driver.source.bb.nr5G.hfb.set_mode(fb_mode = enums.FeedbackModeWithEthernet.ETH) \n
		Enables real-time feedback and determines the mode of the feedback line. \n
			:param fb_mode: OFF| SERial| S3X8
		"""
		param = Conversions.enum_scalar_to_str(fb_mode, enums.FeedbackModeWithEthernet)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:MODE {param}')

	def get_pdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:PDELay \n
		Snippet: value: float = driver.source.bb.nr5G.hfb.get_pdelay() \n
		Sets a delay to the slot to which the timing adjustment command (TA) is applied. For example, if 'Processing Delay' is
		set to -2.00 and the TA is received in slot number 6, after processing, the TA is transmitted in slot number 8. If 'TA
		State' > 'Off', the value set for 'Feedback Delay' is used for 'Processing Delay'. \n
			:return: processing_delay: float Range: -20 to -1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:PDELay?')
		return Conversions.str_to_float(response)

	def set_pdelay(self, processing_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:PDELay \n
		Snippet: driver.source.bb.nr5G.hfb.set_pdelay(processing_delay = 1.0) \n
		Sets a delay to the slot to which the timing adjustment command (TA) is applied. For example, if 'Processing Delay' is
		set to -2.00 and the TA is received in slot number 6, after processing, the TA is transmitted in slot number 8. If 'TA
		State' > 'Off', the value set for 'Feedback Delay' is used for 'Processing Delay'. \n
			:param processing_delay: float Range: -20 to -1
		"""
		param = Conversions.decimal_value_to_str(processing_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:PDELay {param}')

	# noinspection PyTypeChecker
	def get_symbol_rate(self) -> enums.FeedbackRateAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:SRATe \n
		Snippet: value: enums.FeedbackRateAll = driver.source.bb.nr5G.hfb.get_symbol_rate() \n
		Sets the bit rate of the serial transmission. For test cases with high subcarrier spacing (SCS) and short slot duration,
		a serial rate of 115.2 kbps is insufficient. We recommend that you use higher serial rate so that at least one feedback
		command per slot is received. \n
			:return: fb_serial_rate: R1M6| R115| R1M9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackRateAll)

	def set_symbol_rate(self, fb_serial_rate: enums.FeedbackRateAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:SRATe \n
		Snippet: driver.source.bb.nr5G.hfb.set_symbol_rate(fb_serial_rate = enums.FeedbackRateAll.CUST) \n
		Sets the bit rate of the serial transmission. For test cases with high subcarrier spacing (SCS) and short slot duration,
		a serial rate of 115.2 kbps is insufficient. We recommend that you use higher serial rate so that at least one feedback
		command per slot is received. \n
			:param fb_serial_rate: R1M6| R115| R1M9
		"""
		param = Conversions.enum_scalar_to_str(fb_serial_rate, enums.FeedbackRateAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:SRATe {param}')

	def get_ta_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:TAMode \n
		Snippet: value: bool = driver.source.bb.nr5G.hfb.get_ta_mode() \n
		Enables timing advance (TA) adjustment for the selected feedback mode. The TA adjustment uses the 'Processing Delay' to
		define a new timing advance value for advancing or delaying the UL transmission. \n
			:return: ta_mode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:TAMode?')
		return Conversions.str_to_bool(response)

	def set_ta_mode(self, ta_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:TAMode \n
		Snippet: driver.source.bb.nr5G.hfb.set_ta_mode(ta_mode = False) \n
		Enables timing advance (TA) adjustment for the selected feedback mode. The TA adjustment uses the 'Processing Delay' to
		define a new timing advance value for advancing or delaying the UL transmission. \n
			:param ta_mode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ta_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:TAMode {param}')
