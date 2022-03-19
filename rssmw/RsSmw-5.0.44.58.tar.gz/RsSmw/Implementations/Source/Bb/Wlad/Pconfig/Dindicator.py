from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dindicator:
	"""Dindicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dindicator", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DINDicator:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.dindicator.get_state() \n
		No command help available \n
			:return: dind: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:DINDicator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, dind: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DINDicator:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.dindicator.set_state(dind = False) \n
		No command help available \n
			:param dind: No help available
		"""
		param = Conversions.bool_to_str(dind)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:DINDicator:STATe {param}')
