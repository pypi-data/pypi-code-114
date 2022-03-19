from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtf:
	"""Rtf commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtf", core, parent)

	@property
	def sue(self):
		"""sue commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sue'):
			from .Sue import Sue
			self._sue = Sue(self._core, self._cmd_group)
		return self._sue

	def get_aus_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:AUSDelay \n
		Snippet: value: float = driver.source.bb.nr5G.tcw.rtf.get_aus_delay() \n
		Defines the delay added to the real-time feedback. \n
			:return: add_user_delay: float Range: -20 to -1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:AUSDelay?')
		return Conversions.str_to_float(response)

	def set_aus_delay(self, add_user_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:AUSDelay \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_aus_delay(add_user_delay = 1.0) \n
		Defines the delay added to the real-time feedback. \n
			:param add_user_delay: float Range: -20 to -1
		"""
		param = Conversions.decimal_value_to_str(add_user_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:AUSDelay {param}')

	def get_bb_selector(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:BBSelector \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.rtf.get_bb_selector() \n
		Defines which baseband selector index is used in the serial messages to address the baseband. For some test case that
		test a moving UE, the command sets the connector of the moving UE. \n
			:return: bb_selector: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:BBSelector?')
		return Conversions.str_to_int(response)

	def set_bb_selector(self, bb_selector: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:BBSelector \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_bb_selector(bb_selector = 1) \n
		Defines which baseband selector index is used in the serial messages to address the baseband. For some test case that
		test a moving UE, the command sets the connector of the moving UE. \n
			:param bb_selector: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(bb_selector)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:BBSelector {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnectorAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:CONNector \n
		Snippet: value: enums.FeedbackConnectorAll = driver.source.bb.nr5G.tcw.rtf.get_connector() \n
		Sets the connector used for the real-time feedback. For some test case that test a moving UE, the command sets the
		connector of the moving UE. \n
			:return: connector: LOCal| GLOBal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnectorAll)

	def set_connector(self, connector: enums.FeedbackConnectorAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:CONNector \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_connector(connector = enums.FeedbackConnectorAll.LOCal) \n
		Sets the connector used for the real-time feedback. For some test case that test a moving UE, the command sets the
		connector of the moving UE. \n
			:param connector: LOCal| GLOBal
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnectorAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:CONNector {param}')

	def get_cs_rate(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:CSRate \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.rtf.get_cs_rate() \n
		No command help available \n
			:return: custom_ser_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:CSRate?')
		return Conversions.str_to_int(response)

	def set_cs_rate(self, custom_ser_rate: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:CSRate \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_cs_rate(custom_ser_rate = 1) \n
		No command help available \n
			:param custom_ser_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(custom_ser_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:CSRate {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.TcwfEedbackMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:MODE \n
		Snippet: value: enums.TcwfEedbackMode = driver.source.bb.nr5G.tcw.rtf.get_mode() \n
		Defines the serial line mode used for the real-time feedback.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Serial Sets the serial line to 16 bits width.
			- Serial 3x8 Sets the serial line to an array with 3 times 8 bits width (24 bits) . \n
			:return: rtf_mode: SERial| S3X8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TcwfEedbackMode)

	def set_mode(self, rtf_mode: enums.TcwfEedbackMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:MODE \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_mode(rtf_mode = enums.TcwfEedbackMode.S3X8) \n
		Defines the serial line mode used for the real-time feedback.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Serial Sets the serial line to 16 bits width.
			- Serial 3x8 Sets the serial line to an array with 3 times 8 bits width (24 bits) . \n
			:param rtf_mode: SERial| S3X8
		"""
		param = Conversions.enum_scalar_to_str(rtf_mode, enums.TcwfEedbackMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:MODE {param}')

	# noinspection PyTypeChecker
	def get_ser_rate(self) -> enums.FeedbackRateAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SERRate \n
		Snippet: value: enums.FeedbackRateAll = driver.source.bb.nr5G.tcw.rtf.get_ser_rate() \n
		Sets the data rate of serial connection used. \n
			:return: serial_rate: R1M6| R115| R1M9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:SERRate?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackRateAll)

	def set_ser_rate(self, serial_rate: enums.FeedbackRateAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SERRate \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_ser_rate(serial_rate = enums.FeedbackRateAll.CUST) \n
		Sets the data rate of serial connection used. \n
			:param serial_rate: R1M6| R115| R1M9
		"""
		param = Conversions.enum_scalar_to_str(serial_rate, enums.FeedbackRateAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:SERRate {param}')

	def clone(self) -> 'Rtf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rtf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
