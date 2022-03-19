from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bband:
	"""Bband commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bband", core, parent)

	def get_sensitivity(self) -> float:
		"""SCPI: [SOURce<HW>]:AM:BBANd:SENSitivity \n
		Snippet: value: float = driver.source.am.bband.get_sensitivity() \n
		No command help available \n
			:return: sensitivity: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:BBANd:SENSitivity?')
		return Conversions.str_to_float(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:AM:BBANd:[STATe] \n
		Snippet: value: bool = driver.source.am.bband.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:BBANd:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:AM:BBANd:[STATe] \n
		Snippet: driver.source.am.bband.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:AM:BBANd:STATe {param}')
