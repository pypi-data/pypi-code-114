from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sgamma:
	"""Sgamma commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sgamma", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:POWer:SGAMma:STATe \n
		Snippet: value: bool = driver.source.correction.cset.data.power.sgamma.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:CSET:DATA:POWer:SGAMma:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:POWer:SGAMma:STATe \n
		Snippet: driver.source.correction.cset.data.power.sgamma.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:CSET:DATA:POWer:SGAMma:STATe {param}')
