from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:NOISe:BWIDth:STATe \n
		Snippet: value: bool = driver.source.noise.bandwidth.get_state() \n
		Activates noise bandwidth limitation. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:BWIDth:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:BWIDth:STATe \n
		Snippet: driver.source.noise.bandwidth.set_state(state = False) \n
		Activates noise bandwidth limitation. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:BWIDth:STATe {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:BANDwidth \n
		Snippet: value: float = driver.source.noise.bandwidth.get_value() \n
		Sets the noise level in the system bandwidth when bandwidth limitation is enabled. \n
			:return: bwidth: float Range: 100E3 to 10E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:BANDwidth?')
		return Conversions.str_to_float(response)

	def set_value(self, bwidth: float) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:BANDwidth \n
		Snippet: driver.source.noise.bandwidth.set_value(bwidth = 1.0) \n
		Sets the noise level in the system bandwidth when bandwidth limitation is enabled. \n
			:param bwidth: float Range: 100E3 to 10E6
		"""
		param = Conversions.decimal_value_to_str(bwidth)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:BANDwidth {param}')
