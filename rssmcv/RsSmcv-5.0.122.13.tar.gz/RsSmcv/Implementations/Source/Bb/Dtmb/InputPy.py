from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.CodingInputFormat:
		"""SCPI: [SOURce<HW>]:BB:DTMB:INPut:FORMat \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.dtmb.inputPy.get_format_py() \n
		Sets the format of the input signal. \n
			:return: dtmb_format: ASI| SMPTE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)

	def set_format_py(self, dtmb_format: enums.CodingInputFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:INPut:FORMat \n
		Snippet: driver.source.bb.dtmb.inputPy.set_format_py(dtmb_format = enums.CodingInputFormat.ASI) \n
		Sets the format of the input signal. \n
			:param dtmb_format: ASI| SMPTE
		"""
		param = Conversions.enum_scalar_to_str(dtmb_format, enums.CodingInputFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:INPut:FORMat {param}')

	# noinspection PyTypeChecker
	def get_ts_channel(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:DTMB:INPut:TSCHannel \n
		Snippet: value: enums.NumberA = driver.source.bb.dtmb.inputPy.get_ts_channel() \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'.
			INTRO_CMD_HELP: For configuring IP channel settings and local IP data network parameters, see: \n
			- 'IP subsystem'
			- 'BCIP subsystem' \n
			:return: dtmb_ip_ts_channel: 1| 2| 3| 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:INPut:TSCHannel?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_ts_channel(self, dtmb_ip_ts_channel: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:INPut:TSCHannel \n
		Snippet: driver.source.bb.dtmb.inputPy.set_ts_channel(dtmb_ip_ts_channel = enums.NumberA._1) \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'.
			INTRO_CMD_HELP: For configuring IP channel settings and local IP data network parameters, see: \n
			- 'IP subsystem'
			- 'BCIP subsystem' \n
			:param dtmb_ip_ts_channel: 1| 2| 3| 4
		"""
		param = Conversions.enum_scalar_to_str(dtmb_ip_ts_channel, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:INPut:TSCHannel {param}')

	def get_data_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DTMB:[INPut]:DATarate \n
		Snippet: value: float = driver.source.bb.dtmb.inputPy.get_data_rate() \n
			INTRO_CMD_HELP: Queries the measured value of the data rate of one of the following: \n
			- External transport stream including null packets input at 'User 1' connector
			- External transport stream including null packets input at 'IP Data/LAN' connector (TSoverIP)
		The value equals the sum of useful data rate rmeas and the rate of null packets r0: rmeas = rmeas + r0 \n
			:return: dtmb_meas: float Range: 0 to 999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:INPut:DATarate?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.CodingInputSignalInputA:
		"""SCPI: [SOURce<HW>]:BB:DTMB:INPut \n
		Snippet: value: enums.CodingInputSignalInputA = driver.source.bb.dtmb.inputPy.get_value() \n
		Sets the external input interface. \n
			:return: dtmb_source: TS| IP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputA)

	def set_value(self, dtmb_source: enums.CodingInputSignalInputA) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:INPut \n
		Snippet: driver.source.bb.dtmb.inputPy.set_value(dtmb_source = enums.CodingInputSignalInputA.ASI1) \n
		Sets the external input interface. \n
			:param dtmb_source: TS| IP
		"""
		param = Conversions.enum_scalar_to_str(dtmb_source, enums.CodingInputSignalInputA)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:INPut {param}')
