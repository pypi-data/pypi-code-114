from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sanity:
	"""Sanity commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sanity", core, parent)

	def get_cvalues(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SANity:CVALues \n
		Snippet: value: str = driver.source.bb.nr5G.sanity.get_cvalues() \n
		No command help available \n
			:return: current_values: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SANity:CVALues?')
		return trim_str_response(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:NR5G:SANity:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.sanity.get_state() \n
		No command help available \n
			:return: sanity_state: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:NR5G:SANity:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, sanity_state: bool) -> None:
		"""SCPI: [SOURce]:BB:NR5G:SANity:STATe \n
		Snippet: driver.source.bb.nr5G.sanity.set_state(sanity_state = False) \n
		No command help available \n
			:param sanity_state: No help available
		"""
		param = Conversions.bool_to_str(sanity_state)
		self._core.io.write(f'SOURce:BB:NR5G:SANity:STATe {param}')
