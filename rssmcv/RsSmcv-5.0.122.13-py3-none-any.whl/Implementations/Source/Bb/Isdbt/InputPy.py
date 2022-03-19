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
		"""SCPI: [SOURce<HW>]:BB:ISDBt:INPut:FORMat \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.isdbt.inputPy.get_format_py() \n
		Sets the format of the input signal. \n
			:return: input_format: ASI| SMPTE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)

	def set_format_py(self, input_format: enums.CodingInputFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:INPut:FORMat \n
		Snippet: driver.source.bb.isdbt.inputPy.set_format_py(input_format = enums.CodingInputFormat.ASI) \n
		Sets the format of the input signal. \n
			:param input_format: ASI| SMPTE
		"""
		param = Conversions.enum_scalar_to_str(input_format, enums.CodingInputFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:INPut:FORMat {param}')

	# noinspection PyTypeChecker
	def get_ts_channel(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:INPut:TSCHannel \n
		Snippet: value: enums.NumberA = driver.source.bb.isdbt.inputPy.get_ts_channel() \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:return: ts_channel: 1| 2| 3| 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:INPut:TSCHannel?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_ts_channel(self, ts_channel: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:INPut:TSCHannel \n
		Snippet: driver.source.bb.isdbt.inputPy.set_ts_channel(ts_channel = enums.NumberA._1) \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:param ts_channel: 1| 2| 3| 4
		"""
		param = Conversions.enum_scalar_to_str(ts_channel, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:INPut:TSCHannel {param}')

	def get_data_rate(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[INPut]:DATarate \n
		Snippet: value: int = driver.source.bb.isdbt.inputPy.get_data_rate() \n
			INTRO_CMD_HELP: Queries the measured value of the data rate of one of the following: \n
			- External transport stream including null packets input at 'User 1' connector
			- External transport stream including null packets input at 'IP Data/LAN' connector (TSoverIP)
		The value equals the sum of useful data rate rmeas and the rate of null packets r0: rmeas = rmeas + r0 \n
			:return: meas_drate: integer Range: 0 to 9999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:INPut:DATarate?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.CodingInputSignalInputB:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:INPut \n
		Snippet: value: enums.CodingInputSignalInputB = driver.source.bb.isdbt.inputPy.get_value() \n
		Sets the external input interface. \n
			:return: input_py: TS| ASIFront| ASIRear| SPIFront| SPIRear| IP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputB)

	def set_value(self, input_py: enums.CodingInputSignalInputB) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:INPut \n
		Snippet: driver.source.bb.isdbt.inputPy.set_value(input_py = enums.CodingInputSignalInputB.ASIFront) \n
		Sets the external input interface. \n
			:param input_py: TS| ASIFront| ASIRear| SPIFront| SPIRear| IP
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.CodingInputSignalInputB)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:INPut {param}')
