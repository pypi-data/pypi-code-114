from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Double:
	"""Double commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("double", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:PULM:DOUBle:STATe \n
		Snippet: value: bool = driver.source.pulm.double.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:DOUBle:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:PULM:DOUBle:STATe \n
		Snippet: driver.source.pulm.double.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:PULM:DOUBle:STATe {param}')

	def get_width(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:DOUBle:WIDTh \n
		Snippet: value: float = driver.source.pulm.double.get_width() \n
		No command help available \n
			:return: width: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:DOUBle:WIDTh?')
		return Conversions.str_to_float(response)

	def set_width(self, width: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:DOUBle:WIDTh \n
		Snippet: driver.source.pulm.double.set_width(width = 1.0) \n
		No command help available \n
			:param width: No help available
		"""
		param = Conversions.decimal_value_to_str(width)
		self._core.io.write(f'SOURce<HwInstance>:PULM:DOUBle:WIDTh {param}')
