from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 8 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def tsChannel(self):
		"""tsChannel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tsChannel'):
			from .TsChannel import TsChannel
			self._tsChannel = TsChannel(self._core, self._cmd_group)
		return self._tsChannel

	@property
	def dataRate(self):
		"""dataRate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dataRate'):
			from .DataRate import DataRate
			self._dataRate = DataRate(self._core, self._cmd_group)
		return self._dataRate

	# noinspection PyTypeChecker
	def get_low(self) -> enums.CodingInputSignalInputB:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:LOW \n
		Snippet: value: enums.CodingInputSignalInputB = driver.source.bb.dvbt.inputPy.get_low() \n
		Sets the external input interface. \n
			:return: input_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputB)

	def set_low(self, input_lp: enums.CodingInputSignalInputB) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:LOW \n
		Snippet: driver.source.bb.dvbt.inputPy.set_low(input_lp = enums.CodingInputSignalInputB.ASIFront) \n
		Sets the external input interface. \n
			:param input_lp: IP| TS TS Input for serial transport stream data. The signal is input at the 'User 1/2' connectors. IP Supported for high priority path (HP) only, i.e. setting requires non-hierarchical coding. Input for IP transport stream data. The signal is input at the 'IP Data' connector.
		"""
		param = Conversions.enum_scalar_to_str(input_lp, enums.CodingInputSignalInputB)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:INPut:LOW {param}')

	# noinspection PyTypeChecker
	def get_high(self) -> enums.CodingInputSignalInputB:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:[HIGH] \n
		Snippet: value: enums.CodingInputSignalInputB = driver.source.bb.dvbt.inputPy.get_high() \n
		Sets the external input interface. \n
			:return: input_py: IP| TS TS Input for serial transport stream data. The signal is input at the 'User 1/2' connectors. IP Supported for high priority path (HP) only, i.e. setting requires non-hierarchical coding. Input for IP transport stream data. The signal is input at the 'IP Data' connector.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputB)

	def set_high(self, input_py: enums.CodingInputSignalInputB) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:[HIGH] \n
		Snippet: driver.source.bb.dvbt.inputPy.set_high(input_py = enums.CodingInputSignalInputB.ASIFront) \n
		Sets the external input interface. \n
			:param input_py: IP| TS TS Input for serial transport stream data. The signal is input at the 'User 1/2' connectors. IP Supported for high priority path (HP) only, i.e. setting requires non-hierarchical coding. Input for IP transport stream data. The signal is input at the 'IP Data' connector.
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.CodingInputSignalInputB)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:INPut:HIGH {param}')

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
