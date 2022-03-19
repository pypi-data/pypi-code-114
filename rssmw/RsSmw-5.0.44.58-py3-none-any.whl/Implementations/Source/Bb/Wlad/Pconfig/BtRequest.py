from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BtRequest:
	"""BtRequest commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btRequest", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:BTRequest:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.btRequest.get_state() \n
		Activates/deativates the beam tracking request. \n
			:return: btr: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:BTRequest:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, btr: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:BTRequest:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.btRequest.set_state(btr = False) \n
		Activates/deativates the beam tracking request. \n
			:param btr: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(btr)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:BTRequest:STATe {param}')
