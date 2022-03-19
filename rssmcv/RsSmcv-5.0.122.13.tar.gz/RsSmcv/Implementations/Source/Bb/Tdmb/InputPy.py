from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	# noinspection PyTypeChecker
	def get_eti_channel(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:TDMB:INPut:ETIChannel \n
		Snippet: value: enums.NumberA = driver.source.bb.tdmb.inputPy.get_eti_channel() \n
		Selects the channel that is received over the IP interface. \n
			:return: ts_channel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:INPut:ETIChannel?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_eti_channel(self, ts_channel: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:INPut:ETIChannel \n
		Snippet: driver.source.bb.tdmb.inputPy.set_eti_channel(ts_channel = enums.NumberA._1) \n
		Selects the channel that is received over the IP interface. \n
			:param ts_channel: 1| 2
		"""
		param = Conversions.enum_scalar_to_str(ts_channel, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:INPut:ETIChannel {param}')

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.TdmbInputSignalInputFormat:
		"""SCPI: [SOURce<HW>]:BB:TDMB:INPut:FORMat \n
		Snippet: value: enums.TdmbInputSignalInputFormat = driver.source.bb.tdmb.inputPy.get_format_py() \n
		Sets the format of the input signal. \n
			:return: tdmb_format: ETI
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.TdmbInputSignalInputFormat)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Atsc30InputType:
		"""SCPI: [SOURce<HW>]:BB:TDMB:INPut \n
		Snippet: value: enums.Atsc30InputType = driver.source.bb.tdmb.inputPy.get_value() \n
		Sets the external input interface. \n
			:return: tdmb_input: IP| TS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30InputType)

	def set_value(self, tdmb_input: enums.Atsc30InputType) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:INPut \n
		Snippet: driver.source.bb.tdmb.inputPy.set_value(tdmb_input = enums.Atsc30InputType.IP) \n
		Sets the external input interface. \n
			:param tdmb_input: IP| TS
		"""
		param = Conversions.enum_scalar_to_str(tdmb_input, enums.Atsc30InputType)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:INPut {param}')
