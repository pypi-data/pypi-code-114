from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DefSetting:
	"""DefSetting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("defSetting", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FILTer:DEFSetting:STATe \n
		Snippet: value: bool = driver.source.bb.wlnn.filterPy.defSetting.get_state() \n
		Activates the WLAN default filter settings. \n
			:return: use_default_filter: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:FILTer:DEFSetting:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, use_default_filter: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FILTer:DEFSetting:STATe \n
		Snippet: driver.source.bb.wlnn.filterPy.defSetting.set_state(use_default_filter = False) \n
		Activates the WLAN default filter settings. \n
			:param use_default_filter: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(use_default_filter)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FILTer:DEFSetting:STATe {param}')
