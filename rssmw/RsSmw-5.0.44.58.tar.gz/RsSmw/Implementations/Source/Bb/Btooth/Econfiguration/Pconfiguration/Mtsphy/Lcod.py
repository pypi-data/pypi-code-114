from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lcod:
	"""Lcod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcod", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MTSPhy:LCOD:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.mtsphy.lcod.get_state() \n
		Specifies the physical layers in Central-to-Peripheral (..:MTSPhy:..) or Peripheral-to-Central (..:STMPhy:..) direction.
		Information is signaled via LL_PHY_UPDATE_IND.
			INTRO_CMD_HELP: You can enable one or more PHYs: \n
			- L1M for LE uncoded 1 Msymbol/s PHY.
			- L2M for LE uncoded 2 Msymbol/s PHY.
			- LCOD for LE coded 1 Msymbol/s PHY. \n
			:return: mtsp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MTSPhy:LCOD:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, mtsp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MTSPhy:LCOD:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.mtsphy.lcod.set_state(mtsp = False) \n
		Specifies the physical layers in Central-to-Peripheral (..:MTSPhy:..) or Peripheral-to-Central (..:STMPhy:..) direction.
		Information is signaled via LL_PHY_UPDATE_IND.
			INTRO_CMD_HELP: You can enable one or more PHYs: \n
			- L1M for LE uncoded 1 Msymbol/s PHY.
			- L2M for LE uncoded 2 Msymbol/s PHY.
			- LCOD for LE coded 1 Msymbol/s PHY. \n
			:param mtsp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(mtsp)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MTSPhy:LCOD:STATe {param}')
