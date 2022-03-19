from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 10 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def ip(self):
		"""ip commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ip'):
			from .Ip import Ip
			self._ip = Ip(self._core, self._cmd_group)
		return self._ip

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.CodingInputFormat:
		"""SCPI: [SOURce<HW>]:BB:INPut:FORMat \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.inputPy.get_format_py() \n
		No command help available \n
			:return: input_format: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)

	def set_format_py(self, input_format: enums.CodingInputFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:FORMat \n
		Snippet: driver.source.bb.inputPy.set_format_py(input_format = enums.CodingInputFormat.ASI) \n
		No command help available \n
			:param input_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(input_format, enums.CodingInputFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:FORMat {param}')

	# noinspection PyTypeChecker
	def get_ts_channel(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:INPut:TSCHannel \n
		Snippet: value: enums.NumberA = driver.source.bb.inputPy.get_ts_channel() \n
		No command help available \n
			:return: ts_channel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:INPut:TSCHannel?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_ts_channel(self, ts_channel: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:TSCHannel \n
		Snippet: driver.source.bb.inputPy.set_ts_channel(ts_channel = enums.NumberA._1) \n
		No command help available \n
			:param ts_channel: No help available
		"""
		param = Conversions.enum_scalar_to_str(ts_channel, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:TSCHannel {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.CodingInputSignalInputA:
		"""SCPI: [SOURce<HW>]:BB:INPut \n
		Snippet: value: enums.CodingInputSignalInputA = driver.source.bb.inputPy.get_value() \n
		No command help available \n
			:return: input_py: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputA)

	def set_value(self, input_py: enums.CodingInputSignalInputA) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut \n
		Snippet: driver.source.bb.inputPy.set_value(input_py = enums.CodingInputSignalInputA.ASI1) \n
		No command help available \n
			:param input_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.CodingInputSignalInputA)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut {param}')

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
