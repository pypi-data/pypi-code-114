from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Concurrent:
	"""Concurrent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("concurrent", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:EFRontend:CONCurrent:[STATe] \n
		Snippet: value: bool = driver.source.efrontend.concurrent.get_state() \n
		No command help available \n
			:return: fec_on_current_sta: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:CONCurrent:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, fec_on_current_sta: bool) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:CONCurrent:[STATe] \n
		Snippet: driver.source.efrontend.concurrent.set_state(fec_on_current_sta = False) \n
		No command help available \n
			:param fec_on_current_sta: No help available
		"""
		param = Conversions.bool_to_str(fec_on_current_sta)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:CONCurrent:STATe {param}')
